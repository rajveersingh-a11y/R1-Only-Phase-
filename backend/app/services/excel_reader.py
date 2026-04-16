import pandas as pd
from app.utils import clean_column_names

def read_excel_file(filepath: str):
    meters_df = pd.read_excel(filepath, sheet_name='Meters')
    transformers_df = pd.read_excel(filepath, sheet_name='Transformer_Voltages')
    ground_truth_df = pd.read_excel(filepath, sheet_name='GroundTruth')
    
    meters_df = clean_column_names(meters_df)
    transformers_df = clean_column_names(transformers_df)
    ground_truth_df = clean_column_names(ground_truth_df)
    
    return meters_df, transformers_df, ground_truth_df