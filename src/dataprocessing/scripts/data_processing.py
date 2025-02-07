import os
import sys
import glob
import click
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from dataprocessing.utils.common import read_file, save_file
from dataprocessing.utils.constants import stat_features_nfs

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
        files = glob.glob(os.path.join(input_dir, "*.csv"))
        # Read input data
        df = pd.concat([pd.read_csv(file) for file in files], ignore_index=True)
        
        
        # Save processed data
        df.to_csv(output_file, index=False)
        click.echo(f"Processed data saved to {output_file}")
        
    except Exception as e:
        click.echo(f"Error processing data: {str(e)}", err=True)
        sys.exit(1)

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

if __name__ == '__main__':
    cli()


