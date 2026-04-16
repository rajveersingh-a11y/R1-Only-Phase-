import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler

def extract_and_align_time_series(meters_df, transformers_df, ground_truth_df):
    meter_id_col = next((col for col in meters_df.columns if 'meter' in col or 'consumer' in col), meters_df.columns[0])
    m_ts_col = 'timestamp' if 'timestamp' in meters_df.columns else next((col for col in meters_df.columns if 'time' in col or 'date' in col), meters_df.columns[1])
    m_volt_col = 'voltage' if 'voltage' in meters_df.columns else next((col for col in meters_df.columns if 'volt' in col), meters_df.columns[2])
    
    tf_id_col = next((col for col in transformers_df.columns if 'transformer' in col or 'meter' in col), transformers_df.columns[0])
    t_ts_col = 'timestamp' if 'timestamp' in transformers_df.columns else next((col for col in transformers_df.columns if 'time' in col or 'date' in col), transformers_df.columns[1])
    
    gt_meter_col = next((col for col in ground_truth_df.columns if 'meter' in col or 'consumer' in col), ground_truth_df.columns[0])
    gt_tf_col = next((col for col in ground_truth_df.columns if 'transformer' in col), ground_truth_df.columns[1])
    
    m_pivot = meters_df.pivot(index=meter_id_col, columns=m_ts_col, values=m_volt_col)
    common_ts = m_pivot.columns.tolist()
    m_ts = m_pivot.reset_index()
    m_ts.dropna(subset=common_ts, how='all', inplace=True)
    m_ts.loc[:, common_ts] = m_ts[common_ts].apply(lambda row: row.fillna(row.mean()), axis=1)
    
    m_ts = m_ts.merge(ground_truth_df[[gt_meter_col, gt_tf_col]], left_on=meter_id_col, right_on=gt_meter_col, how='left')
    
    v_a_col = next((col for col in transformers_df.columns if 'voltage_a' in col), None)
    v_b_col = next((col for col in transformers_df.columns if 'voltage_b' in col), None)
    v_c_col = next((col for col in transformers_df.columns if 'voltage_c' in col), None)
    
    corr_a, corr_b, corr_c = [], [], []
    for _, row in m_ts.iterrows():
        tf_id = row[gt_tf_col]
        meter_volts = row[common_ts].astype(float).values
        
        # Explicit type conversion string->datetime is mostly handled if types match, assuming direct == works
        tf_data = transformers_df[(transformers_df[tf_id_col] == tf_id) & (transformers_df[t_ts_col].isin(common_ts))]
        
        if not tf_data.empty and len(tf_data) == len(common_ts) and v_a_col and v_b_col and v_c_col:
            # Sort chronologically to align exactly with common_ts which is sorted by columns usually, but to be truly safe, match indices exactly
            tf_data_dict = tf_data.set_index(t_ts_col).to_dict(orient='index')
            a_v = [tf_data_dict[ts][v_a_col] if ts in tf_data_dict else meter_volts[i] for i, ts in enumerate(common_ts)]
            b_v = [tf_data_dict[ts][v_b_col] if ts in tf_data_dict else meter_volts[i] for i, ts in enumerate(common_ts)]
            c_v = [tf_data_dict[ts][v_c_col] if ts in tf_data_dict else meter_volts[i] for i, ts in enumerate(common_ts)]
            
            ca = float(np.corrcoef(meter_volts, a_v)[0,1]) if np.std(a_v) > 0 and np.std(meter_volts) > 0 else 0.0
            cb = float(np.corrcoef(meter_volts, b_v)[0,1]) if np.std(b_v) > 0 and np.std(meter_volts) > 0 else 0.0
            cc = float(np.corrcoef(meter_volts, c_v)[0,1]) if np.std(c_v) > 0 and np.std(meter_volts) > 0 else 0.0
        else:
            ca, cb, cc = 0.0, 0.0, 0.0
            
        # fill nan
        if np.isnan(ca): ca = 0.0
        if np.isnan(cb): cb = 0.0
        if np.isnan(cc): cc = 0.0
            
        corr_a.append(ca)
        corr_b.append(cb)
        corr_c.append(cc)
        
    m_ts['corr_A'] = corr_a
    m_ts['corr_B'] = corr_b
    m_ts['corr_C'] = corr_c
    
    t_ts = transformers_df
    return m_ts, t_ts, meter_id_col, tf_id_col, common_ts

def standardize_data(df, ts_cols):
    data = df[ts_cols].values
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data.T).T
    
    if 'corr_A' in df.columns:
        corrs = df[['corr_A', 'corr_B', 'corr_C']].values
        # Weight them aggressively relative to scaled voltages
        corrs_scaled = StandardScaler().fit_transform(corrs) * 10.0
        return np.hstack((scaled_data, corrs_scaled))
        
    return scaled_data