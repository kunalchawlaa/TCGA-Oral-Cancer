# Code for processing TCGA Data

This is the code to merge TCGA Clinical Data of patients with RNA values for the patient. Note that this can be extended to other data in similar format, such as TCGA gene data.

## Getting Started
Following are the instructions to get started with the code.

### Requirements
* Python 3.6 or higher
* Linux (code can also be modified easily for Windows/ Mac)

All required packages can be installed by:

	pip install -r requirements.txt

## Dataset
Use TCGA to extract the desired files of selected cases, by selecting and adding the desired file from transcriptome profiling to cart. The clinical data, cart, manifest, metadata and sample sheets can be downloaded from [here](https://portal.gdc.cancer.gov/exploration?filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.primary_site%22%2C%22value%22%3A%5B%22accessory%20sinuses%22%2C%22base%20of%20tongue%22%2C%22floor%20of%20mouth%22%2C%22gum%22%2C%22hypopharynx%22%2C%22larynx%22%2C%22lip%22%2C%22nasal%20cavity%20and%20middle%20ear%22%2C%22nasopharynx%22%2C%22oropharynx%22%2C%22other%20and%20ill-defined%20sites%20in%20lip%2C%20oral%20cavity%20and%20pharynx%22%2C%22other%20and%20ill-defined%20sites%22%2C%22other%20and%20unspecified%20major%20salivary%20glands%22%2C%22other%20and%20unspecified%20parts%20of%20mouth%22%2C%22other%20and%20unspecified%20parts%20of%20tongue%22%2C%22palate%22%2C%22parotid%20gland%22%2C%22pyriform%20sinus%22%2C%22tonsil%22%2C%22trachea%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22cases.diagnoses.tissue_or_organ_of_origin%22%2C%22value%22%3A%5B%22accessory%20sinus%2C%20nos%22%2C%22anterior%202%2F3%20of%20tongue%2C%20nos%22%2C%22anterior%20floor%20of%20mouth%22%2C%22anterior%20surface%20of%20epiglottis%22%2C%22anterior%20wall%20of%20nasopharynx%22%2C%22base%20of%20tongue%2C%20nos%22%2C%22border%20of%20tongue%22%2C%22branchial%20cleft%22%2C%22cheek%20mucosa%22%2C%22commissure%20of%20lip%22%2C%22dorsal%20surface%20of%20tongue%2C%20nos%22%2C%22ethmoid%20sinus%22%2C%22external%20lip%2C%20nos%22%2C%22external%20lower%20lip%22%2C%22external%20upper%20lip%22%2C%22floor%20of%20mouth%2C%20nos%22%2C%22frontal%20sinus%22%2C%22glottis%22%2C%22gum%2C%20nos%22%2C%22hard%20palate%22%2C%22head%2C%20face%20or%20neck%2C%20nos%22%2C%22hypopharyngeal%20aspect%20of%20aryepiglottic%20fold%22%2C%22hypopharynx%2C%20nos%22%2C%22laryngeal%20cartilage%22%2C%22larynx%2C%20nos%22%2C%22lateral%20floor%20of%20mouth%22%2C%22lateral%20wall%20of%20nasopharynx%22%2C%22lateral%20wall%20of%20oropharynx%22%2C%22lingual%20tonsil%22%2C%22lip%2C%20nos%22%2C%22lower%20gum%22%2C%22major%20salivary%20gland%2C%20nos%22%2C%22maxillary%20sinus%22%2C%22middle%20ear%22%2C%22mouth%2C%20nos%22%2C%22mucosa%20of%20lip%2C%20nos%22%2C%22mucosa%20of%20lower%20lip%22%2C%22mucosa%20of%20upper%20lip%22%2C%22nasal%20cavity%22%2C%22nasopharynx%2C%20nos%22%2C%22oropharynx%2C%20nos%22%2C%22overlapping%20lesion%20of%20accessory%20sinuses%22%2C%22overlapping%20lesion%20of%20floor%20of%20mouth%22%2C%22overlapping%20lesion%20of%20hypopharynx%22%2C%22overlapping%20lesion%20of%20larynx%22%2C%22overlapping%20lesion%20of%20lip%2C%20oral%20cavity%20and%20pharynx%22%2C%22overlapping%20lesion%20of%20lip%22%2C%22overlapping%20lesion%20of%20major%20salivary%20glands%22%2C%22overlapping%20lesion%20of%20nasopharynx%22%2C%22overlapping%20lesion%20of%20other%20and%20unspecified%20parts%20of%20mouth%22%2C%22overlapping%20lesion%20of%20palate%22%2C%22overlapping%20lesion%20of%20tongue%22%2C%22overlapping%20lesion%20of%20tonsil%22%2C%22overlapping%20lesions%20of%20oropharynx%22%2C%22palate%2C%20nos%22%2C%22parotid%20gland%22%2C%22pharynx%2C%20nos%22%2C%22postcricoid%20region%22%2C%22posterior%20wall%20of%20hypopharynx%22%2C%22posterior%20wall%20of%20nasopharynx%22%2C%22posterior%20wall%20of%20oropharynx%22%2C%22pyriform%20sinus%22%2C%22retromolar%20area%22%2C%22soft%20palate%2C%20nos%22%2C%22sphenoid%20sinus%22%2C%22subglottis%22%2C%22sublingual%20gland%22%2C%22submandibular%20gland%22%2C%22superior%20wall%20of%20nasopharynx%22%2C%22supraglottis%22%2C%22tongue%2C%20nos%22%2C%22tonsil%2C%20nos%22%2C%22tonsillar%20fossa%22%2C%22tonsillar%20pillar%22%2C%22trachea%22%2C%22upper%20gum%22%2C%22uvula%22%2C%22vallecula%22%2C%22ventral%20surface%20of%20tongue%2C%20nos%22%2C%22vestibule%20of%20mouth%22%2C%22waldeyer%20ring%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D).

### Clinical Data

The clinical data has information about the patients. It is indexed by Case ID, and has information about cancer type, severity, area as well as age, death date, and smoking and drinking habits of patients. It can be downlaoded from [here](https://portal.gdc.cancer.gov/repository?filters=%7B%22content%22%3A%5B%7B%22content%22%3A%7B%22field%22%3A%22cases.case_id%22%2C%22value%22%3A%5B%2246e51eb2-0c5e-457b-af1a-8bac1b8a8bea%22%5D%7D%2C%22op%22%3A%22in%22%7D%2C%7B%22content%22%3A%7B%22field%22%3A%22files.data_category%22%2C%22value%22%3A%5B%22Transcriptome%20Profiling%22%5D%7D%2C%22op%22%3A%22in%22%7D%5D%2C%22op%22%3A%22and%22%7D&searchTableTab=files).

### RNA Data

The RNA values for all genes for each patient are given in a file. The files can be downloaded from [here](https://portal.gdc.cancer.gov/files/c56b8970-ab89-432e-9125-79ab04daeff5).

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