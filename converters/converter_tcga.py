#! /usr/bin/python
'''
Author: Malisa Smith smimal@ohsu.edu 03-29-2016
This program converts TCGA pan cancer maf files and patient summary information into
JSON-encoded protobuf data based on the simple_schema.proto schema.
'''

import simple_schema_pb2 as schema
from google.protobuf import json_format
import json, sys, argparse, os
import csv #for convert_tcga_patients
import uuid

def parse_args(args):
    # We don't need the first argument, which is the program name
    args = args[1:]

    # Construct the parser
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Now add all the options to it
    parser.add_argument("--maf", type=str, default=os.path.join(os.getcwd(), 'pancan12_cleaned.maf'),
                        help="Path to the maf you want to import")
    parser.add_argument("--tsv", type=str, default=os.path.join(os.getcwd(), 'pancan12_cleaned.tsv'),
                        help="Path to the tsv you want to import")
    parser.add_argument("--outfile", type=str, default=os.path.join(os.getcwd(), 'pancan12_cleaned_pb.json'),
                        help="Path to output json file")
    return parser.parse_args(args)

def group_by(f, l):
    d = {}
    for item in l:
        k = f(item)
        if d.get(k) is None:
            d[k] = []
        d[k].append(item)

    return d

def find_individual(state, source, individual_name):
    individual = state["individuals"].get(individual_name)
    if individual is None:
        individual = schema.Individual()
        individual.id = str(uuid.uuid1())
        individual.name = individual_name
        individual.source = source
        state["individuals"][individual_name] = individual

    return individual

def process_line(state, source, line_raw):
    line = line_raw.rstrip().split("\t")

    # Information indices for VariantCall, BioSample, and Individual
    hugo_symbol = 0
    ncbi_build = 3
    reference_name = 4
    start = 5
    end = 6
    strand = 7
    variant_classification = 8
    variant_type = 9
    reference_allele = 10
    tumor_seq_allele1 = 11
    tumor_seq_allele2 = 12
    tumor_sample_barcode = 15
    matched_norm_sample_barcode = 16
    match_norm_seq_allele1 = 17
    match_norm_seq_allele2 = 18
    mutation_status = 25
    sequencing_phase = 26
    sequence_source = 27
    bam_file = 30

    # Information indices for VariantCallEffect and Feature
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

    # Construct the sample and individual names
    biosample_name = line[tumor_sample_barcode] + " " + line[matched_norm_sample_barcode] #biosample name: "TCGA-A1-A0SB-01A-11D-A142-09 TCGA-A1-A0SB-10B-01D-A142-09"
    biosample_id = "TCGA:" + biosample_name
    individual_name = biosample_name[0:12]

    # Find or create the Individual
    individual = find_individual(state, source, individual_name)

    # Find or create the BioSample
    biosample = state["biosamples"].get(biosample_name)
    if biosample is None:
        biosample = schema.BioSample()
        biosample.id = str(uuid.uuid1())
        biosample.name = biosample_name
        biosample.source = source
        biosample.individualId = individual.id
        biosample.individualName = individual.name
        state["biosamples"][biosample_name] = biosample

    # Create a VariantCall
    variant_call = schema.VariantCall()
    variant_call.id = str(uuid.uuid1())
    variant_call.source = source
    variant_call.bioSampleId = biosample.id
    variant_call.position.referenceName = line[reference_name] # e.g. 10
    variant_call.position.start = int(line[start]) # e.g. 116247760
    variant_call.position.end = int(line[end]) # e.g. 116247760

    # assign variant_call.position.strand
    if line[strand] == "+":
        variant_call.position.strand = 2 # Strand.POS_STRAND
    elif line[strand] == "-":
        variant_call.position.strand = 1 # Strand.NEG_STRAND
    else:
        variant_call.position.strand = 0 # Strand.STRAND_UNSPECIFIED

    variant_call.referenceBases = line[reference_allele] # Reference_Allele, e.g. "T"
    variant_call.genotype.append(line[tumor_seq_allele1]) # Tumor_Seq_Allele1, e.g. "T"
    variant_call.genotype.append(line[tumor_seq_allele2]) # Tumor_Seq_Allele2, e.g. "C"

    variant_call.info["NCBIBuild"] = line[ncbi_build] # e.g. "37"
    variant_call.info["VariantClassification"] = line[variant_classification] # e.g. "Missense_Mutation"
    variant_call.info["MatchNormSeqAllele1"] = line[match_norm_seq_allele1] # e.g. "T"
    variant_call.info["MatchNormSeqAllele2"] = line[match_norm_seq_allele2] # e.g. "T"
    variant_call.info["MutationStatus"] = line[mutation_status] # e.g. "Somatic"
    variant_call.info["SequencingPhase"] = line[sequencing_phase] # e.g. "Phase_IV"
    variant_call.info["SequenceSource"] = line[sequence_source] # e.g. "Capture"
    variant_call.info["BAMFile"] = line[bam_file] # e.g. "dbGAP"

    # Now create a VariantCallEffect
    variant_call_effect = schema.VariantCallEffect()
    variant_call_effect.id = str(uuid.uuid1())
    variant_call_effect.source = source
    variant_call_effect.variantCallId = variant_call.id
    variant_call_effect.feature = line[hugo_symbol]
    variant_call_effect.info["transcriptName"] = line[transcript_name]
    variant_call_effect.info["transcriptSpecies"] = line[transcript_species]
    variant_call_effect.info["transcriptSource"] = line[transcript_source]
    variant_call_effect.info["transcriptVersion"] = line[transcript_version]
    variant_call_effect.info["strand"] = line[vce_strand] #not sure what this means... has to do with sequencing process perhaps?
    variant_call_effect.info["transcriptStatus"] = line[transcript_status]
    variant_call_effect.info["trvType"] = line[trv_type]
    variant_call_effect.info["cPosition"] = line[c_position]
    variant_call_effect.info["aminoAcidChange"] = line[amino_acid_change]
    variant_call_effect.info["ucscCons"] = line[ucsc_cons]
    variant_call_effect.info["domain"] = line[domain]
    variant_call_effect.info["VariantType"] = line[variant_type] #e.g. "SNP"

    variant_call.variantCallEffects.extend([variant_call_effect])
    biosample.variantCalls.extend([variant_call])

    return state

def convert_maf(state, mafpath, source):
    inhandle = open(mafpath)
    for line in inhandle:
        if not line.startswith("Hugo_Symbol") and not line.startswith("#"):
            state = process_line(state, source, line)
    inhandle.close()

    return state

def convert_tcga_patients(state, tcgapath, source):
    with open(tcgapath) as patient_file:
        reader = csv.DictReader(patient_file, delimiter='\t')
        for row in reader:
            individual = find_individual(state, source, row["barcode"])
            for key, value in row.iteritems():
                if value == "":
                    continue
                else:
                    individual.observations[key] = value

    return state

def write_individual_list(state, outpath):
    individual_list = schema.IndividualList()
    biosample_groups = group_by(lambda i: i.individualName, state["biosamples"].values())

    for individual_name in state["individuals"]:
        individual = state["individuals"][individual_name]
        biosamples = biosample_groups.get(individual_name)
        if biosamples is not None:
            individual.bioSamples.extend(biosamples)
        individual_list.individuals.extend([individual])

    outhandle = open(outpath, "w")
    outhandle.write(json_format.MessageToJson(individual_list))
    outhandle.close()

def convert_maf_and_tsv_to_profobuf(mafpath, tsvpath, outpath):
    state = {"individuals": {}, "biosamples": {}}
    source = "TCGA"

    if mafpath:
        convert_maf(state, mafpath, source)
    if tsvpath:
        convert_tcga_patients(state, tsvpath, source)

    write_individual_list(state, outpath)

if __name__ == "__main__":
    options = parse_args(sys.argv)
    convert_maf_and_tsv_to_profobuf(options.maf, options.tsv, options.outfile)
