#! /usr/bin/python
'''
Authors: Malisa Smith smimal@ohsu.edu 03-29-2016, Ryan Spangler spanglry@ohsu.edu
This program converts TCGA pan cancer maf files and patient summary information into
JSON-encoded protobuf data based on the simple_schema.proto schema.
'''

import sample_pb2 as schema
from google.protobuf import json_format
import json, sys, argparse, os
import csv #for convert_tcga_patients
import uuid
import string
import re

def parse_args(args):
    # We don't need the first argument, which is the program name
    args = args[1:]

    # Construct the parser
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Now add all the options to it
    parser.add_argument('--maf', type=str, help='Path to the maf you want to import')
    parser.add_argument('--tsv', type=str, help='Path to the tsv you want to import')
    parser.add_argument('--out', type=str, help='Path to output json file')
    parser.add_argument('--format', type=str, default='json', help='Format of output: json or pbf (binary)')
    return parser.parse_args(args)

def group_by(f, l):
    d = {}
    for item in l:
        k = f(item)
        if d.get(k) is None:
            d[k] = []
        d[k].append(item)

    return d

def partition(l, n):
    return [l[i:i+n] for i in xrange(0, len(l), n)]

def find_individual(state, source, individual_name):
    individual = state['Individual'].get(individual_name)
    if individual is None:
        individual = schema.Individual()
        individual.name = individual_name
        individual.source = source
        state['Individual'][individual_name] = individual

    return individual

def find_biosample(state, source, barcode, sample_type):
    sample_name = barcode[:16]
    biosample = state['Biosample'].get(sample_name)
    if biosample is None:
        biosample = schema.Biosample()
        biosample.name = sample_name
        biosample.source = source
        biosample.barcode = barcode
        biosample.sampleType = sample_type
        state['Biosample'][sample_name] = biosample

    return biosample

def find_position(state, chromosome, start, end, strand):
    position_name = chromosome + start + end + strand
    position = state['Position'].get(position_name)
    if position is None:
        position = schema.Position()
        position.name = position_name
        position.chromosome = chromosome
        position.start = int(start)
        position.end = int(end)
        position.strand = strand
        state['Position'][position_name] = position

    return position

def find_domain(state, name):
    domain = state['Domain'].get(name)
    if domain is None:
        domain = schema.Domain()
        domain.name = name
        state['Domain'][name] = domain

    return domain

def find_feature(state, name):
    feature = state['Feature'].get(name)
    if feature is None:
        feature = schema.Feature()
        feature.name = name
        state['Feature'][name] = feature

    return feature

def find_variant_call(state, source, position_name, reference_allele, normal_allele1, normal_allele2, tumor_allele1, tumor_allele2, variant_type, ncbi_build, mutation_status, sequencing_phase, sequence_source, bam_file):
    variant_name = source + position_name + variant_type + mutation_status
    variant_call = state['VariantCall'].get(variant_name)
    if variant_call is None:
        variant_call = schema.VariantCall()
        variant_call.name = variant_name
        variant_call.source = source
        
        variant_call.referenceAllele = reference_allele # Reference_Allele, e.g. 'T'
        variant_call.normalAllele1 = normal_allele1
        variant_call.normalAllele2 = normal_allele2
        variant_call.tumorAllele1 = tumor_allele1
        variant_call.tumorAllele2 = tumor_allele2
        variant_call.variantType = variant_type # e.g. 'SNP'
    
        variant_call.info['ncbiBuild'] = ncbi_build # e.g. '37'
        variant_call.info['mutationStatus'] = mutation_status # e.g. 'Somatic'
        variant_call.info['sequencingPhase'] = sequencing_phase # e.g. 'Phase_IV'
        variant_call.info['sequenceSource'] = sequence_source # e.g. 'Capture'
        variant_call.info['bamFile'] = bam_file # e.g. 'dbGAP'
        state['VariantCall'][variant_name] = variant_call

    return variant_call

def find_variant_call_effect(state, source, effect_name, classification, line):
    transcript_name = 39
    transcript_species = 40
    transcript_source = 41
    transcript_version = 42
    vce_strand = 43
    transcript_status = 44
    trv_type = 45
    c_position = 46
    amino_acid_change = 47
    ucsc_cons = 48
    domain = 49

    variant_call_effect = state['VariantCallEffect'].get(effect_name)
    if variant_call_effect is None:
        variant_call_effect = schema.VariantCallEffect()
        variant_call_effect.name = effect_name
        variant_call_effect.source = source
        variant_call_effect.variantClassification = classification # e.g. 'Missense_Mutation'
        try:
            variant_call_effect.info['transcriptSpecies'] = line[transcript_species]
            variant_call_effect.info['transcriptName'] = line[transcript_name]
            variant_call_effect.info['transcriptSource'] = line[transcript_source]
            variant_call_effect.info['transcriptStatus'] = line[transcript_status]
            variant_call_effect.info['transcriptVersion'] = line[transcript_version]
            variant_call_effect.info['cPosition'] = line[c_position]
            variant_call_effect.info['aminoAcidChange'] = line[amino_acid_change]
            variant_call_effect.info['strand'] = line[vce_strand] #not sure what this means... has to do with sequencing process perhaps?
            variant_call_effect.info['trvType'] = line[trv_type]
            variant_call_effect.info['ucscCons'] = line[ucsc_cons]

            if line[domain] == 'NULL' or line[domain] == '-':
                domains = []
            else:
                domains = line[domain].split(',')
            for domain_name in domains:
                find_domain(state, domain_name)
            variant_call_effect.inDomainEdges.extend(domains)

        except Exception as ex:
            None

        state['VariantCallEffect'][effect_name] = variant_call_effect

    return variant_call_effect
    
def process_line(state, source, line_raw):
    # Information indices for VariantCall, Biosample, and Individual
    ncbi_build = 3
    chromosome = 4
    start = 5
    end = 6
    strand = 7
    variant_type = 9
    reference_allele = 10
    tumor_allele1 = 11
    tumor_allele2 = 12
    tumor_sample_barcode = 15
    normal_sample_barcode = 16
    normal_allele1 = 17
    normal_allele2 = 18
    verification_status = 23
    validation_status = 24
    mutation_status = 25
    sequencing_phase = 26
    sequence_source = 27
    bam_file = 30
    sequencer = 31
    tumor_sample_uuid = 32
    matched_norm_sample_uuid = 33

    # Information indices for VariantCallEffect and Feature
    hugo_symbol = 0
    variant_classification = 8
    dbsnp_rs = 13
    dbsnp_val_status = 14

    # --------------------------------------------
    line = line_raw.rstrip().split('\t')

    # example normal name: 'TCGA-A1-A0SB-01A-11D-A142-09'
    # example tumor name:  'TCGA-A1-A0SB-10B-01D-A142-09'

    # create nodes
    individual_name = line[tumor_sample_barcode][0:12]
    individual = find_individual(state, source, individual_name)

    tumor_sample = find_biosample(state, source, line[tumor_sample_barcode], "tumor")
    normal_sample = find_biosample(state, source, line[normal_sample_barcode], "normal")

    position = find_position(state, line[chromosome], line[start], line[end], line[strand])

    feature = find_feature(state, line[hugo_symbol])

    variant_call = find_variant_call(state, source, position.name, line[reference_allele], line[normal_allele1], line[normal_allele2], line[tumor_allele1], line[tumor_allele2], line[variant_type], line[ncbi_build], line[mutation_status], line[sequencing_phase], line[sequence_source], line[bam_file])

    effect_name = source + individual.name + line[variant_classification] + position.name
    variant_call_effect = find_variant_call_effect(state, source, effect_name, line[variant_classification], line)

    # make edges
    tumor_sample.sampleOfEdgesIndividual.extend([individual.name])
    normal_sample.sampleOfEdgesIndividual.extend([individual.name])

    # individual.hasSampleEdges.extend([tumor_sample.name, normal_sample.name])
    # feature.atPositionEdges.extend([position.name])
    # feature.hasEffectEdges.extend([variant_call_effect.name])
    # variant_call.hasEffectEdges.extend([variant_call_effect.name])

    variant_call.atPositionEdgesPosition.extend([position.name])
    variant_call.tumorSampleEdgesBiosample.extend([tumor_sample.name])
    variant_call.normalSampleEdgesBiosample.extend([normal_sample.name])

    variant_call_effect.inFeatureEdgesFeature.extend([feature.name])
    variant_call_effect.effectOfEdgesVariantCall.extend([variant_call.name])

    return state

def convert_maf(state, mafpath, source):
    print("converting maf: " + mafpath)

    inhandle = open(mafpath)
    for line in inhandle:
        if not line.startswith('Hugo_Symbol') and not line.startswith('#'):
            state = process_line(state, source, line)
    inhandle.close()

    return state

def convert_tcga_patients(state, tcgapath, source):
    print("converting tsv: " + tcgapath)
    with open(tcgapath) as patient_file:
        reader = csv.DictReader(patient_file, delimiter='\t')
        for row in reader:
            individual = find_individual(state, source, row['bcr_patient_barcode'])
            for key, value in row.iteritems():
                if value == '':
                    continue
                else:
                    individual.observations[key] = value

    return state

def convert_expression(state, exppath, source):
    5

def splice_path(path, s):
    path_split = path.split(".")
    suffix = path_split[-1]
    path_parts = path_split[:-1]
    path_parts.extend([s, suffix])
    return string.join(path_parts, ".")

def message_to_json(message):
    json = json_format.MessageToJson(message)
    return re.sub(r" +", " ", json.replace("\n", ""))

def write_messages(state, outpath, format):
    if format == 'json':
        for message in state:
            outmessage = splice_path(outpath, message)
            messages = map(message_to_json, state[message].values())
            if len(messages) > 0:
                out = string.join(messages, "\n")
                outhandle = open(outmessage, 'w')
                outhandle.write(out)
                outhandle.close()
    else:
        for message in state:
            outmessage = splice_path(outpath, message)
            messages = map(lambda m: m.SerializeToString(), state[message].values())
            if len(messages) > 0:
                out = string.join(messages, "\n")
                outhandle = open(outmessage, 'wb')
                outhandle.write(out)
                outhandle.close()

def convert_maf_and_tsv_to_profobuf(mafpath, tsvpath, outpath, format):
    state = {'Individual': {},
             'Biosample': {},
             'Position': {},
             'Feature': {},
             'Domain': {},
             'VariantCall': {},
             'VariantCallEffect': {}}
    source = 'TCGA'

    if mafpath:
        convert_maf(state, mafpath, source)
    if tsvpath:
        convert_tcga_patients(state, tsvpath, source)

    write_messages(state, outpath, format)

if __name__ == '__main__':
    options = parse_args(sys.argv)
    convert_maf_and_tsv_to_profobuf(options.maf, options.tsv, options.out, options.format)
