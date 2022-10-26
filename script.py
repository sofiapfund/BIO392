
##############################################################################
################# BIO392 - Survival Analysis Project (HS22) ##################
################# Dataset: lymphoma tumor                   ##################
################# Author: Sofia Pfund                       ##################
##############################################################################


####################### Step 1: load required packages ########################

# data manipulation
import pandas as pd
import numpy as np

# data visualization
import kaplanmeier as km
import matplotlib.pyplot as plt
import seaborn as sns

####################### Step 2: import the data ###############################

# gene data
tp_53_group_info = pd.read_csv("data/biosample-tp53.tsv", sep="\t")
cdkn2a_group_info = pd.read_csv("data/biosample-CDKN2A.tsv", sep="\t")
myc_group_info = pd.read_csv("data/biosample-myc.tsv", sep="\t")
erbb2_group_info = pd.read_csv("data/biosample-ERBB2.tsv", sep="\t")

# tumor data
lymphoma = pd.read_csv("data/lymphoma.csv")

####################### Step 3: data pre-processing ###########################

### 1. match lymphoma samples to CNV samples that exhibit mutations in the 4 genes of interest:

# match "sample_id" column from lymphoma with "id" column from group_info:
tp53_df = pd.merge(lymphoma, tp_53_group_info, left_on = "id", right_on = "biosample_id")
cdkn2a_df = pd.merge(lymphoma, cdkn2a_group_info, left_on = "id", right_on = "biosample_id")
myc_df = pd.merge(lymphoma, myc_group_info, left_on = "id", right_on = "biosample_id")
erbb2_df = pd.merge(lymphoma, erbb2_group_info, left_on = "id", right_on = "biosample_id")

# add column with label for later grouping:
tp53_df["group"] = "tp53" # lymphoma tumor samples that have mutations in the tp53 gene
cdkn2a_df["group"] = "cdkn2a"
myc_df["group"] = "myc"
erbb2_df["group"] = "erbb2"

# merge everything into the same dataset:
whole_df = pd.concat([tp53_df, cdkn2a_df, myc_df, erbb2_df])
  
### 2. select features of interest:
whole_df = whole_df[['info.followupMonths',             # how much time has passed since the sample was collected 
                     'info.death',                      # is dead or alive at time of sample collection? (0, 1)
                     'group',                           # which gene mutation in the tumor sample? (tp53, myc, ...)
                     'sex',                             # sex of the patient (male, female)
                     'histologicalDiagnosis.id',        # name of the tumor type
                     'pathologicalStage.label'          # cancer stage of the sample
                     'info.cnvstatistics.cnvfraction'   # CNV fraction in the whole genome of the sample
                    ]]

### 3. select rows (tumors) of interest:
ncit_codes = ["NCIT:C80280", "NCIT:C4340", "NCIT:C3246", "NCIT:C4337", "NCIT:C27753", "NCIT:C8851"]
filtered_df = whole_df[whole_df['histologicalDiagnosis.id'].isin(ncit_codes)]

### 4. replace NCIT tumor codes with human-readable tumor names:
def my_func(row):
    if row['histologicalDiagnosis.id'] == "NCIT:C80280":
        val = 'Diffuse Large B-Cell Lymphoma'
    elif row['histologicalDiagnosis.id']  == "NCIT:C4340":
        val = 'Peripheral T-Cell Lymphoma'
    elif row['histologicalDiagnosis.id']  == "NCIT:C3246":
        val = 'Mycosis Fungoides'
    elif row['histologicalDiagnosis.id']  == "NCIT:C4337":
        val = 'Mantle Cell Lymphoma'
    elif row['histologicalDiagnosis.id']  == "NCIT:C27753":
        val = 'Acute Myeloid Leukemia'
    elif row['histologicalDiagnosis.id']  == "NCIT:C8851":
        val = 'Diffuse Large B-Cell Lymphoma'
    return val

filtered_df['name'] = filtered_df.apply(my_func, axis=1)

### 5. remove missing values:
filtered_df = filtered_df.dropna()

### 6. visually inspect data: frequencies of CNVs samples for each gene of interest
plt.figure(figsize=(8,5))
sns.countplot(x='group', data=filtered_df, palette='rainbow')
plt.title("Nr of CNVs Samples by Gene in the `lymphoma.cvs` dataset")
plt.xlabel("Gene")
plt.ylabel("Count")
plt.show()

####################### Step 4: survival analysis ##############################

# compute survival based on gene mutation:
time = filtered_df["info.followupMonths"]
event = filtered_df["info.death"]
group = filtered_df["group"]
results = km.fit(time, event, group)
km.plot(results) # visualize Kaplan-Meier plot
plt.show()

# compute survival based on sex:
time = filtered_df["info.followupMonths"]
event = filtered_df["info.death"]
sex = filtered_df["sex"]
results_2 = km.fit(time, event, sex)
km.plot(results_2) # visualize Kaplan-Meier plot
plt.show()

# compute survival based on tumor type:
time = filtered_df["info.followupMonths"]
event = filtered_df["info.death"]
tumor = filtered_df["name"]
results_3 = km.fit(time, event, tumor) # visualize Kaplan-Meier plot
km.plot(results_3)
plt.show()

####################### Step 5: exploratory analysis #########################

### Q1: Does CNV fraction change depending on tumor stage?

# sort the dataset by stage
filtered_df = filtered_df.sort_values(['pathologicalStage.label'])

# plot
plt.figure(figsize=(20,6))
sns.violinplot(x='pathologicalStage.label', y="info.cnvstatistics.cnvfraction", data=filtered_df)
plt.title("Violin Plot of CNV fraction based on Tumor Stage")
plt.xlabel("Tumor stage")
plt.ylabel("CNV fraction")
plt.show()

### Q2: Does CNV fraction change depending on tumor type?
plt.figure(figsize=(15,6))
sns.violinplot(x='name',y="info.cnvstatistics.cnvfraction", data=filtered_data, palette='rainbow')
plt.title("Violin Plot of CNV fraction by Tumor Type")
plt.xlabel("Tumor Type")
plt.ylabel("CNV fraction")
plt.show()

## Q3: Does CNV fraction change depending on mutated gene? 
plt.figure(figsize=(10,6))
sns.violinplot(x='group',y="info.cnvstatistics.cnvfraction", data=filtered_data, palette='rainbow')
plt.title("Violin Plot of CNV fraction vs. Mutated Gene")
plt.xlabel("Mutated Gene")
plt.ylabel("CNV fraction")
plt.show()

#############################################################################
#############################################################################
#############################################################################
