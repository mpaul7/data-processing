import os
import pandas as pd

def read_file(input_file)->pd.DataFrame:
    file_ext = os.path.splitext(input_file)[1].lower()
    if file_ext == '.csv':
        df = pd.read_csv(input_file)
    elif file_ext == '.parquet':
            df = pd.read_parquet(input_file)
    elif file_ext == '.orc':
        df = pd.read_orc(input_file)
    else:
        raise ValueError(f"Unsupported file format: {file_ext}. Supported formats are: .csv, .parquet, .orc")
    return df


def save_file(df, output_file):
    _, ext = os.path.splitext(output_file)
    if ext == '.csv':
        df.to_csv(output_file, index=False)
    elif ext == '.parquet':
        df.to_parquet(output_file, index=False)
    elif ext == '.orc':
        df.to_orc(output_file, index=False)