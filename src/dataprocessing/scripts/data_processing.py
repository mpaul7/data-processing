import click
import pandas as pd
import numpy as np
import os
import sys
import glob

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

if __name__ == '__main__':
    cli()
