import pandas as pd


def import_cancer_data():
    cancer_data = pd.read_csv('sciviz/sciviz/src/data/data-raw/cancer_proteomics/cancer_synthetic_data.csv')
    unique_assays = cancer_data['Assay'].unique()[:500]  # keep only the first 500 Assays
    data_filtered = cancer_data[cancer_data['Assay'].isin(unique_assays)]
    data_wide = data_filtered.pivot(index='Sample', columns='Assay', values='NPX').reset_index()
    return (data_wide)


def import_cancer_metadata():
    cancer_metadata = pd.read_csv('sciviz/sciviz/src/data/data-raw/cancer_proteomics/cancer_synthetic_metadata.csv')
    return(cancer_metadata)
    

def main():
    cancer_data = import_cancer_data() 
    cancer_metadata = import_cancer_metadata()
    merged_data = pd.merge(cancer_metadata, cancer_data, on='Sample', how='left')
    merged_data.to_csv("sciviz/sciviz/src/data/data_cancer.csv")


if __name__ == "__main__":
    main()