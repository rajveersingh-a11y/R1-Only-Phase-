import pandas as pd
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import os

def evaluate_predictions():
    # File paths
    ground_truth_path = "sample_grid_data_3phase.xlsx"
    predictions_path = "backend/backend/app/outputs/csv/final_phase_mapping.csv"
    
    if not os.path.exists(predictions_path):
        print("Predictions file not found! Please run the pipeline first via the dashboard.")
        return
        
    print("Loading Ground Truth and Predictions...\n")
    
    # Read outputs and truths
    ground_truth_df = pd.read_excel(ground_truth_path, sheet_name='GroundTruth')
    predictions_df = pd.read_csv(predictions_path)
    
    # Normalize column names for robust matching
    gt_cols = {c.strip().lower(): c for c in ground_truth_df.columns}
    
    # Identify key columns
    gt_meter_col = [gt_cols[k] for k in gt_cols if 'meter' in k or 'consumer' in k][0]
    gt_phase_col = [gt_cols[k] for k in gt_cols if 'phase' in k][0]
    
    # Merge datasets
    merged = predictions_df.merge(
        ground_truth_df[[gt_meter_col, gt_phase_col]], 
        left_on='consumer_id', 
        right_on=gt_meter_col, 
        how='inner'
    )
    
    y_true = merged[gt_phase_col].astype(str).str.upper()
    y_pred = merged['predicted_phase'].astype(str).str.upper()
    
    # Calculate metrics
    accuracy = accuracy_score(y_true, y_pred)
    conf_matrix = confusion_matrix(y_true, y_pred, labels=['A', 'B', 'C'])
    report = classification_report(y_true, y_pred, labels=['A', 'B', 'C'])
    
    # Terminal Output
    print("="*40)
    print(" PHASE MAPPING ACCURACY REPORT ")
    print("="*40)
    print(f"Total Consumers Evaluated: {len(y_true)}")
    print(f"Overall Accuracy:          {accuracy * 100:.2f}%\n")
    
    print(" Classification Report:")
    print("-" * 55)
    print(report)
    
    print(" Confusion Matrix:")
    print("-" * 25)
    print("    | Predicted")
    print("True|   A   B   C")
    print("----+------------")
    print(f"  A | {conf_matrix[0][0]:3} {conf_matrix[0][1]:3} {conf_matrix[0][2]:3}")
    print(f"  B | {conf_matrix[1][0]:3} {conf_matrix[1][1]:3} {conf_matrix[1][2]:3}")
    print(f"  C | {conf_matrix[2][0]:3} {conf_matrix[2][1]:3} {conf_matrix[2][2]:3}")
    print("="*40)

if __name__ == '__main__':
    evaluate_predictions()
