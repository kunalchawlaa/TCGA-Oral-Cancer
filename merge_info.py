# Script to combine TCGA clinical data with TCGA RNA values 


# Imports:


import plotly.express as px
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile
import argparse

# Read arguments:

parser = argparse.ArgumentParser(description='Path to files containing clinical and RNA data, and desired output file')
parser.add_argument("--clinical_data", help = 'Path to excel sheet containing clinical data', default = "clinical.xlsx")
parser.add_argument("--RNA_data", help = 'Path to excel sheet containing RNA data', default = "SampleFiles.xlsx")
parser.add_argument("--output_file", help = 'Desired path to excel sheet containing merged data', default = "output.xlsx")
args = parser.parse_args()

# Read TCGA Excel Sheet:

values = pd.read_excel(args.RNA_data, engine='openpyxl')
values = values.loc[values['File Name'].str.contains("FPKM")]
#values.head()


# Read clinical data:


attributes = pd.read_excel(args.clinical_data,engine='openpyxl')
attr = attributes.drop_duplicates(subset = 'case_submitter_id')
columns = ['case_submitter_id','ajcc_clinical_m','ajcc_clinical_n','ajcc_clinical_stage','ajcc_clinical_t','ajcc_pathologic_m','ajcc_pathologic_n','ajcc_pathologic_stage','ajcc_pathologic_t','site_of_resection_or_biopsy','tissue_or_organ_of_origin','tumor_stage']
attr = attr[columns]


# Join TCGA and clinical data with Case ID as the key:


final = values.set_index('Case ID').join(attr.set_index("case_submitter_id"), how = "inner")


# Separate Primary Tumor with others:


fpkm1 = final.loc[final['Sample Type']=="Primary Tumor"]
fpkm2 = final.loc[final['Sample Type']!="Primary Tumor"]


# Write to excel file:


writer = pd.ExcelWriter(args.output_file, engine='openpyxl')
fpkm1.to_excel(writer, sheet_name = "tumor")
fpkm2.to_excel(writer, sheet_name = "normal")
final.to_excel(writer, sheet_name = "all")
writer.save()




