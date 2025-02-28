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

import time
@click.group()
def cli():
    """Data processing CLI tool"""
    pass

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



if __name__ == '__main__':
    cli()


