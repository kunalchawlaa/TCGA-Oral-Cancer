# Code for processing TCGA Transcriptome Profiling Data

This is the code to merge TCGA Clinical Data of patients with RNA values for the patient. Note that this can be extended to other data in similar format, such as TCGA gene data.

Note that this code can only be used for single RNA profiling and should be avoided for differential expression analysis.

## Getting Started
Following are the instructions to get started with the code.

### Requirements
* Python 3.6 or higher
* Linux (code can also be modified easily for Windows/ Mac)

All required packages can be installed by:

	pip install -r requirements.txt

## Dataset
Use TCGA to extract the desired files of selected cases, by selecting and adding the desired file from transcriptome profiling to cart. The clinical data, cart, manifest, metadata and sample sheets can be downloaded from [here](https://portal.gdc.cancer.gov).

## How to use

### Making RNA Value Excel from all files

Go to the directory with downloaded RNA files. Find the gene TCGA code for the desired RNA from [here](http://asia.ensembl.org/index.html). On a linux subsystem, run:

    grep -ri gene_code "" >> rna_values.csv
    
This will give an excel sheet containing the patient case ID and associated RNA values. Note that the csv file might need to be converted to xslx depending on system.

### Merging RNA and patient clinical information

Run:

    python merge_info.py --clinical_data PATH_TO_CLINICAL_EXCEL --RNA_data PATH_TO_RNA_EXCEL --output_file DESIRED_PATH_TO_OUTPUT_FILE
    
This will combine the information from both sheets and write the output to excel file.


## Citation
*Neeti Swarup, Kyoung-Ok Hong1, Kunal Chawla, Su-Jung Choi, Ji-Ae Shin, Kyu-Young Oh, Hye-Jung Yoon, Jae-Il Lee, Sung-Dae Cho, Seong-Doo Hong*: Effect of PAIP1 on metastatic potential and its prognostic significance in oral squamous cell carcinoma.

If you would like to refer to it, please cite the paper mentioned above. Please contact the following persons for any questions:
* Neeti Swarup (neeti@snu.ac.kr)
* Kunal Chawla (kunalchawla@gatech.edu)
