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

def parse_args(args):

    # We don't need the first argument, which is the program name
    args = args[1:]

    # Construct the parser
    parser = argparse.ArgumentParser(description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)

    # Now add all the options to it
    parser.add_argument("--datatype", type=str, default="TCGA_maf", choices=['TCGA_maf', 'TCGA_patients'])
    parser.add_argument("--data", type=str, default=os.path.join(os.getcwd(), 'pancan12_cleaned.maf'),
    			help="Path to data you want to import")
    parser.add_argument("--outfile", type=str, default=os.path.join(os.getcwd(), 'pancan12_cleaned_pb.json'),
    			help="Path to output json file")
    return parser.parse_args(args)

# Converts the input tcga maf file into protobuf-schema-informed JSON-serialization of the data. Stores it in outfile.
# All arguments are file paths.
def convert_tcga_maf(inpath, outpath):

    variantcall_json = '"VariantCall": '
    feature_json = '"Feature": '
    variantcalleffect_json = '"VariantCallEffect": '
    biosample_json = '"BioSample": '
    individual_json = '"Individual": '
     
    def process_line(line, vc_e_id):
	line_list = line.rstrip().split("\t")

	# Information indices for VariantCall, BioSample, and Individual
	Tumor_Sample_Barcode = 15
	Matched_Norm_Sample_Barcode = 16
	reference_name = 4
	start = 5
	end = 6
	strand = 7
	Reference_Allele = 10
	Tumor_Seq_Allele1 = 11
	Tumor_Seq_Allele2 = 12
	NCBI_Build = 2
	Variant_Classification = 7
	Variant_Type = 8
	Match_Norm_Seq_Allele1 = 17
	Match_Norm_Seq_Allele2 = 18
	Mutation_Status = 25
	Sequencing_Phase = 26
	Sequence_Source = 27
	BAM_File = 30

	# Create a VariantCall
	vc = schema.VariantCall()
	vc.id = "TCGA:VC:" + str(current_id)
	# and assign vc.bioSampleId field 
	bioSampleName = line_list[Tumor_Sample_Barcode] + " " + line_list[Matched_Norm_Sample_Barcode] #biosample name: "TCGA-A1-A0SB-01A-11D-A142-09 TCGA-A1-A0SB-10B-01D-A142-09"
	new_bioSampleId = "TCGA:" + bioSampleName
	# Assign it to the VariantCall.bioSampleId field
	vc.bioSampleId = new_bioSampleId
	vc.position.reference_name = line_list[reference_name] #e.g. 10
	vc.position.start = int(line_list[start]) #e.g. 116247760
	vc.position.end = int(line_list[end]) #e.g. 116247760
	# assign vc.position.strand
	if line_list[strand] == "+":
	    vc.position.strand = 2 #Strand.POS_STRAND
	elif line_list[strand] == "-":
	    vc.position.strand = 1 #Strand.NEG_STRAND
	else:
	    vc.position.strand = 0 #Strand.STRAND_UNSPECIFIED
	vc.reference_bases = line_list[Reference_Allele] #Reference_Allele, e.g. "T"
	vc.genotype.append(line_list[Tumor_Seq_Allele1]) #Tumor_Seq_Allele1, e.g. "T"
	vc.genotype.append(line_list[Tumor_Seq_Allele2]) #Tumor_Seq_Allele2, e.g. "C"
	vc.info["NCBI_Build"] = line_list[NCBI_Build] #e.g. "37"
	vc.info["Variant_Classification"] = line_list[Variant_Classification] #e.g. "Missense_Mutation"
	vc.info["Variant_Type"] = line_list[Variant_Type] #e.g. "SNP"
	vc.info["Match_Norm_Seq_Allele1"] = line_list[Match_Norm_Seq_Allele1] #e.g. "T"
	vc.info["Match_Norm_Seq_Allele2"] = line_list[Match_Norm_Seq_Allele2] #e.g. "T"
	vc.info["Mutation_Status"] = line_list[Mutation_Status] #e.g. "Somatic"
	vc.info["Sequencing_Phase"] = line_list[Sequencing_Phase] #e.g. "Phase_IV"
	vc.info["Sequence_Source"] = line_list[Sequence_Source] #e.g. "Capture"
	vc.info["BAM_File"] = line_list[BAM_File] #e.g. "dbGAP"

	# Create new BioSample object
	bs = schema.BioSample()
	bs.id = new_bioSampleId
	bs.name = bioSampleName

	# Create Individual
	individualName = bioSampleName[0:12]
	ind = schema.Individual()
	ind.id = "TCGA:" + individualName


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
	hugo_symbol = 0


	# Now create a VariantCallEffect
	vce = schema.VariantCallEffect()
	vce.id = "TCGA:VCE:" + str(current_id)
	vce.variantCallId = str(current_id) #should be the same
	vce.info["transcript_name"] = line_list[transcript_name]
	vce.info["transcript_species"] = line_list[transcript_species]
	vce.info["transcript_source"] = line_list[transcript_source]
	vce.info["transcript_version"] = line_list[transcript_version]
	vce.info["strand"] = line_list[vce_strand] #not sure what this means... has to do with sequencing process perhaps?
	vce.info["transcript_status"] = line_list[transcript_status]
	vce.info["trv_type"] = line_list[trv_type]
	vce.info["c_position"] = line_list[c_position]
	vce.info["amino_acid_change"] = line_list[amino_acid_change]
	vce.info["ucsc_cons"] = line_list[ucsc_cons]
	vce.info["domain"] = line_list[domain]

	# Now create a Feature
	feat = schema.Feature()
	feat.featureType = "gene" #for now
	feat.attributes["Hugo_Symbol"] = line_list[hugo_symbol]
	feat.id = "TCGA:" + line_list[hugo_symbol] #not sure if this should be TCGA-specific

        jsons_dict = {}
	jsons_dict["VariantCall"] = json_format.MessageToJson(vc)
	jsons_dict["BioSample"] = json_format.MessageToJson(bs)
	jsons_dict["Individual"] = json_format.MessageToJson(ind)
	jsons_dict["VariantCallEffect"] = json_format.MessageToJson(vce)
	jsons_dict["Feature"] = json_format.MessageToJson(feat)

	return jsons_dict


    inhandle = open(inpath)
    outhandle = open(outpath, "w")
    outhandle.write("{\n")
    current_id = 1
    for line in inhandle:
        if not line.startswith("Hugo_Symbol") and not line.startswith("#"):
            line_jsons_dict = process_line(line, current_id)
	    if "VariantCall" in line_jsons_dict:
	        variantcall_json_tmp = variantcall_json + line_jsons_dict["VariantCall"] + ",\n"
		outhandle.write(variantcall_json_tmp)
	    if "BioSample" in line_jsons_dict:
	        biosample_json_tmp = biosample_json + line_jsons_dict["BioSample"] + ",\n"
		outhandle.write(biosample_json_tmp)
	    if "Individual" in line_jsons_dict:
	        individual_json_tmp = individual_json + line_jsons_dict["Individual"] + ",\n"
		outhandle.write(individual_json_tmp)
	    if "VariantCallEffect" in line_jsons_dict:
	        variantcalleffect_json_tmp = variantcalleffect_json + line_jsons_dict["VariantCallEffect"] + ",\n"
		outhandle.write(variantcalleffect_json_tmp)
	    if "Feature" in line_jsons_dict:
	        feature_json_tmp = feature_json + line_jsons_dict["Feature"] + ",\n"
		outhandle.write(feature_json_tmp)
	    current_id+=1
    inhandle.close()

    outhandle.write("{}\n}")
    outhandle.close()


def convert_tcga_patients(inpath, outpath):
    individual_json = '"Individual_list": ['

    with open(inpath) as patient_file:
	reader = csv.DictReader(patient_file, delimiter='\t')
	for row in reader:
	    # Create Individual
	    ind = schema.Individual()
	    #print(row)
            for key, value in row.iteritems():
		if key == "barcode":
		    ind.name = value
		    ind.id = "TCGA:" + value
		elif value == "":
		    continue
		else:
		    ind.observations[key] = value

	    individual_json = individual_json + json.dumps(json.loads(json_format.MessageToJson(ind))) + ", "

    final_json = "{ "

    if individual_json.endswith(", "): # data has been added to individual_json, so we add it to the object to be written to file
	individual_json = individual_json[0:-2] + "]"
	final_json = final_json + individual_json + ", "

    if final_json.endswith(", "):
	final_json = final_json[0:-2] + " }"

    # Finally, write the final JSON to the outpath file
    outhandle = open(outpath, "w")
    #outhandle.write(final_json)
    outhandle.write(json.dumps(json.loads(final_json), indent=4, separators=(',', ': ')))
    outhandle.close()

if __name__ == "__main__":
    options = parse_args(sys.argv)
    
    if options.datatype == "TCGA_maf":
	convert_tcga_maf(options.data, options.outfile)
    elif options.datatype == "TCGA_patients":
	convert_tcga_patients(options.data, options.outfile)
