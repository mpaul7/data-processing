"""
Date: 2025-01-26
Author: TW
"""

import os
import sys
import glob
import click
import pandas as pd
import numpy as np
import socket
from pathlib import Path
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from dataprocessing.utils.common import read_file, save_file
from dataprocessing.utils.constants import stat_features_nfs
import time
@click.group()
def cli():
    """Data processing CLI tool"""
    pass

data_path = [
    '/media/solana/Backup Plus/Data/dvc_data/2020a_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/2020c_Mobile_Wifi',
    '/media/solana/Backup Plus/Data/dvc_data/2021a_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/2021c_Mobile_LTE',
    '/media/solana/Backup Plus/Data/dvc_data/2022a_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/2023a_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/2023c_Mobile_LTE',    
    '/media/solana/Backup Plus/Data/dvc_data/2023e_MacOS_Wifi',
    '/media/solana/Backup Plus/Data/dvc_data/2024ag_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/2024a_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/2024cg_Mobile_LTE',
    '/media/solana/Backup Plus/Data/dvc_data/2024c_Mobile_LTE',
    '/media/solana/Backup Plus/Data/dvc_data/2024e_MacOS_Wifi',    
    '/media/solana/Backup Plus/Data/dvc_data/Homeoffice2024ag_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/Homeoffice2024a_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/Homeoffice2024c_Mobile_LTE',
    '/media/solana/Backup Plus/Data/dvc_data/Homeoffice2024e_MacOS_WiFi',
    '/media/solana/Backup Plus/Data/dvc_data/Homeoffice2025cg_Mobile_LTE',
    '/media/solana/Backup Plus/Data/dvc_data/Test2023a_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/Test2023c_Mobile_LTE',
    '/media/solana/Backup Plus/Data/dvc_data/Test2023e_MacOS_Wifi',
    '/media/solana/Backup Plus/Data/dvc_data/Test2024ag_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/Test2024a_Wireline_Ethernet',
    '/media/solana/Backup Plus/Data/dvc_data/Test2024cg_Mobile_LTE',
    '/media/solana/Backup Plus/Data/dvc_data/Test2024c_Mobile_LTE',
    '/media/solana/Backup Plus/Data/dvc_data/Test2024e_MacOS_Wifi'   
    ]

@cli.command(name="merge_all_dirs")
@click.argument('output_file', type=click.Path())
def merge_all_dirs(output_file):
    """Merge data from multiple files in a directory and save results  
    
    Args:
        output_file: Path to save merged output
    """
    start_time = time.time()
    all_df = []
    for i, input_file_path in enumerate(data_path):
        # try:
        data_source = input_file_path.split('/')[-1]
        click.echo(f'[{i+1}/{len(data_path)}] Processing {data_source}')
        
        features_path = Path(input_file_path)
        # if not features_path.exists():
        #     click.echo(f"Warning: Path does not exist: {features_path}", err=True)
        #     continue
            
        files = list(features_path.glob('**/data_beta.orc'))
        if not files:
            click.echo(f"Warning: No CSV files found in {features_path}", err=True)
            continue
        inner_df = []    
        for i, file in enumerate(files):
            # click.echo(f"[{i+1}/{len(files)}] Processing -> {file}")
            df = pd.read_orc(file)
        #     drop_col = ['sslCertSerial_fwd', 'sslCertSerial_bwd', 'quicDCID', 'quicSCID', 'quicODCID', 'numHdrs', 'natPass', 'voipType', 'srcIPCC',
        #                 'dstIPCC', 'dnsAType', 'dnsAClass', 'dnsATTL', 'dnsMXpref', 'dnsSRVprio', 'dnsSRVwgt', 'dnsSRVprt', 'ftpRC', 'httpRSCode', 'tcpOptions']
        #     change_col = {'srcIP': 'sip', 'srcPort': 'sport', 'dstIP': 'dip', 'dstPort': 'dport', 'l4Proto': 'proto'}
        #     df.rename(columns=change_col, inplace=True)
        #     existing_final_cols = [col for col in drop_col if col in df.columns]
        #     df.drop(columns=existing_final_cols, inplace=True)
        #     df = ip_swap(df)
        #     inner_df.append(df)
            
        # df = pd.concat(inner_df, ignore_index=True)
        # # click.echo(f"Merged -> {data_source}")
        # # print(df.head())
        
        # # Create intermediate directory if it doesn't exist
        # inter_dir = Path('/media/solana/Backup Plus/Data/dvc_data/merged_tr_files')
        # inter_dir.mkdir(parents=True, exist_ok=True)
        
        # inter_file_name = inter_dir / f'{data_source}_merged.parquet'
        # df.to_parquet(str(inter_file_name), index=False)
        # click.echo(f"saved -> {inter_file_name}")
        all_df.append(df)
        
        # click.echo(f"appended -> {data_source}")
        # except Exception as e:
        #     click.echo(f"Error processing ==============================================={input_file_path}: {str(e)}", err=True)
        #     continue  # Continue with next directory instead of exiting
    
    if not all_df:
        click.echo("Error: No data was successfully processed", err=True)
        sys.exit(1)
        
    df_all = pd.concat(all_df, ignore_index=True)
    df_all.to_parquet(output_file, index=False)
    click.echo(f"\nProcessed data saved to {output_file}")
    end_time = time.time()
    click.echo(f"Time taken: {end_time - start_time:.2f} seconds")

@cli.command(name="merge")
@click.argument('input_dir', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def merge_data(input_dir, output_file):
    """Merge data from multiple files in a directory and save results  
    
    Args:
        input_dir: Path to directory containing input data files
        output_file: Path to save merged output
    """
    
    try:


        files = glob.glob(os.path.join(input_dir, "*.parquet"))

        inner_df = []    
        for i, file in enumerate(files):
            # click.echo(f"[{i+1}/{len(files)}] Processing -> {file}")
            df = pd.read_csv(file, low_memory=False)
            drop_col = ['sslCertSerial_fwd', 'sslCertSerial_bwd', 'quicDCID', 'quicSCID', 'quicODCID', 'numHdrs', 'natPass', 'voipType', 'srcIPCC',
                        'dstIPCC', 'dnsAType', 'dnsAClass', 'dnsATTL', 'dnsMXpref', 'dnsSRVprio', 'dnsSRVwgt', 'dnsSRVprt', 'ftpRC', 'httpRSCode', 'tcpOptions', 'tcpMPTBF']
            change_col = {'srcIP': 'sip', 'srcPort': 'sport', 'dstIP': 'dip', 'dstPort': 'dport', 'l4Proto': 'proto'}
            df.rename(columns=change_col, inplace=True)
            existing_final_cols = [col for col in drop_col if col in df.columns]
            df.drop(columns=existing_final_cols, inplace=True)
            inner_df.append(df)
        # Read input data
        df = pd.concat([pd.read_parquet(file) for file in files], ignore_index=True)
        
        
        # Save processed data
        df.to_parquet(output_file, index=False)
        click.echo(f"Processed data saved to {output_file}")
        
    except Exception as e:
        click.echo(f"Error processing data: {str(e)}", err=True)
        sys.exit(1)
        
# @cli.command(name="ipswap")
# @click.argument('df', type=click.Path(exists=True))
# @click.argument('output_file', type=click.Path())
def ip_swap(df):
    """
    Swap if the sip is public and the dip is private,
    or if both addresses have the same privacy levels, swap if the sip is well known
    """
    def in_classA_private(ip):
        return ((ip & 0xFF000000) == 0x0A000000)

    def in_classB_private(ip):
        return ((ip & 0xFFF00000) == 0xAC100000)

    def in_classC_private(ip):
        return ((ip & 0xFFFF0000) == 0xC0A80000)

    def in_private(ip):
        return in_classA_private(ip) or in_classB_private(ip) or in_classC_private(ip)

    WELL_KNOWN_PORTS = [1311, 5986, 8243, 8333, 8531, 8888, 9443, 5985, 8000, 8008, 8080, 8243, 8403, 8530, 8887, 9080,
                        16080]

    # method to check if the port is wellknown
    def is_wellknown(port):
        return ((port < 1024) | (port in WELL_KNOWN_PORTS))

    # method to convert ip address to bytes then to int
    def convert_to_int(ip):
        try:
            ip_bin = socket.inet_pton(socket.AF_INET, ip)
            ip_int = int.from_bytes(ip_bin, byteorder='big')
            return ip_int
        except socket.error:
            return False  # Handle invalid IP addresses
    # df = read_file(input_file)
    # IP comparison columns
    df['sip_int'] = df.sip.apply(convert_to_int)
    df['dip_int'] = df.dip.apply(convert_to_int)

    # swap if the sip is public and the dip is private
    swap_ind = df.loc[(df['sip_int'].apply(in_private) == False) & (df['dip_int'].apply(in_private) == True)].index
    # or if both addresses have the same privacy levels, swap if the sip is well known
    swap_ind = swap_ind.append(df.loc[(df['sip_int'].apply(in_private) == df['dip_int'].apply(in_private)) & (
                df.sport.apply(is_wellknown) == True)].index)

    # swap the column name for the rows that meet the above criteria
    df_ip_swapped = df.loc[swap_ind].rename(columns={'sip': 'dip', 'sport': 'dport', 'dip': 'sip', 'dport': 'sport'})
    # replace the data needs to be updated with swapped ip
    df.loc[swap_ind] = df_ip_swapped

    df.drop(columns=['sip_int', 'dip_int'], inplace=True)
    
    return df
    
    # df.to_csv(output_file, index=False)
    # click.echo(f"Processed data saved to {output_file}")

@cli.command(name="split")
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_dir', type=click.Path())
@click.option('--test-size', '-t', default=0.2, help='Proportion of data to use for testing (default: 0.2)')
@click.option('--random-state', '-r', default=42, help='Random seed for reproducibility (default: 42)')
def split_data(input_file, output_dir, test_size, random_state):
    """Split data into train and test sets
    
    Args:
        input_file: Path to input CSV file
        output_dir: Directory to save train and test files
        test_size: Proportion of data to use for testing
        random_state: Random seed for reproducibility
    """
    try:
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
        
        # Read input data
        """accept input file in csv, parquet, orc format"""
        df = read_file(input_file)
        
        # Split the data
        train_df, test_df = train_test_split(
            df, 
            test_size=test_size,
            random_state=random_state
        )
        
        # Save train and test sets
        """save train and test sets in csv format"""
        _, tail = os.path.split(input_file)
        train_file = tail.split('.')[0] + '_train.csv'
        test_file = tail.split('.')[0] + '_test.csv'
        train_path = os.path.join(output_dir, train_file)
        test_path = os.path.join(output_dir, test_file)
        
        train_df.to_csv(train_path, index=False)
        test_df.to_csv(test_path, index=False)
        
        click.echo(f"Train data saved to: {train_path}")
        click.echo(f"Test data saved to: {test_path}")
        
    except Exception as e:
        click.echo(f"Error splitting data: {str(e)}", err=True)
        sys.exit(1)

@cli.command(name="scaler")
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--columns', '-c', multiple=True, help='Columns to scale (multiple allowed)')
def scale_data(input_file, output_file, columns):
    """Scale numeric columns using StandardScaler
    
    Args:
        input_file: Path to input file
        output_file: Path to save scaled data
        columns: List of columns to scale. If none provided, scales all numeric columns
    """
    try:
        # Read input data
        df = read_file(input_file)
        
        columns = stat_features_nfs
        
        # Create scaler and transform data
        scaler = StandardScaler()
        df_scaled = df.copy()
        df_scaled[list(columns)] = scaler.fit_transform(df[list(columns)])
        
        save_file(df_scaled, output_file)
            
        click.echo(f"Scaled data saved to: {output_file}")
        
    except Exception as e:
        click.echo(f"Error scaling data: {str(e)}", err=True)
        sys.exit(1)

@cli.command(name="format")
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
def format_data(input_file, output_file):
    """Format data into a standard format
    
    Args:
        input_file: Path to input file
        output_file: Path to save formatted data
    """
    try:
        # Read input data using common utility
        df = read_file(input_file)
        
        # Save in requested format using common utility 
        save_file(df, output_file)
        
        click.echo(f"Formatted data saved to: {output_file}")
        
    except Exception as e:
        click.echo(f"Error formatting data: {str(e)}", err=True)
        sys.exit(1)

@cli.command(name="pad")
@click.argument('input_file', type=click.Path(exists=True))
@click.argument('output_file', type=click.Path())
@click.option('--max_length', type=int, help='Maximum sequence length for padding')
def pad_sequences(input_file, output_file, max_length=None):
    """Pad sequences with zeros to a fixed length
    
    Args:
        input_file: Path to input file
        output_file: Path to save padded data
        max_length: Maximum sequence length for padding. If not provided, uses length of longest sequence
    """
    try:
        # Read input data
        df = read_file(input_file)
        
        # If max_length not provided, use longest sequence
        if not max_length:
            max_length = df.shape[1]
            
        # Pad sequences with zeros
        df_padded = df.copy()
        for col in df.columns:
            if len(df[col]) < max_length:
                padding_length = max_length - len(df[col])
                df_padded[col] = pd.concat([df[col], pd.Series([0] * padding_length)])
                
        save_file(df_padded, output_file)
        
        click.echo(f"Padded sequences saved to: {output_file}")
        
    except Exception as e:
        click.echo(f"Error padding sequences: {str(e)}", err=True)
        sys.exit(1)


if __name__ == '__main__':
    cli()


