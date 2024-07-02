import pandas as pd


def import_cancer_data():
    """
    Imports cancer data from a CSV file and performs data filtering and transformation.

    Returns:
        pandas.DataFrame: The filtered and transformed cancer data in wide format.
    """
    cancer_data = pd.read_csv('sciviz/sciviz/src/data/data-raw/cancer_proteomics/cancer_synthetic_data.csv')
    unique_assays = cancer_data['Assay'].unique()[:500]  # keep only the first 500 Assays
    data_filtered = cancer_data[cancer_data['Assay'].isin(unique_assays)]
    data_wide = data_filtered.pivot(index='Sample', columns='Assay', values='NPX').reset_index()
    return data_wide


def import_cancer_metadata():
    """
    Imports cancer metadata from a CSV file.

    Returns:
        pandas.DataFrame: The imported cancer metadata.
    """
    cancer_metadata = pd.read_csv('sciviz/sciviz/src/data/data-raw/cancer_proteomics/cancer_synthetic_metadata.csv')
    return(cancer_metadata)
    

def main():
    """
    Main function to import cancer data, merge it with cancer metadata, filter the merged data,
    and save the filtered data to a CSV file.

    Returns:
        None
    """
    cancer_data = import_cancer_data() 
    cancer_metadata = import_cancer_metadata()
    merged_data = pd.merge(cancer_metadata, cancer_data, on='Sample', how='left')
    merged_filtered = merged_data[merged_data['GROUP'].isin(['AML', 'CLL', 'CRC', 'GLIOM', 'LUNGC', 'LYMPH', 'MYEL'])]  # keep only non gender specific cancers
    merged_filtered.to_csv("sciviz/sciviz/src/data/cancer.csv", index=False)


if __name__ == "__main__":
    main()