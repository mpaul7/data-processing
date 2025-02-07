import re
import os
import json
import click
import subprocess
import pandas as pd
from collections import defaultdict
import logging
from dataprocessing.utils.mapping_asn import *

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

static_ip = defaultdict(list)
ip_not_found = defaultdict(list)

output_dir = '/data/Solana_datasets/mn-data/results/globall_ip'
prefix = 'twc_v1-5-4_20apps'
file_name = f'{prefix}_{pd.Timestamp.now().strftime("%Y-%m-%d_%H-%M-%S")}.csv'
output = os.path.join(output_dir, file_name)

@click.group()
def cli():
    """ Based on ASN, generate a CSV file containing 'net_address' and 'label' """

@cli.command(name='asn')
def run_whois():
    """ Run whois command to retrieve route information """
    
    def extract_route_info(whois_output):
        """ Extract route information from whois output """
        route_info = []
        pattern = r'route:\s+([\d./]+)'
        matches = re.findall(pattern, whois_output)
        route_info.extend(matches)
        return route_info

    try:
        for app, asn_list in new_apps.items():
            logging.info(f'Retrieving data for app -> [{app}]')
            for asn in asn_list:
                whois_cmd = ["whois", "-h", "whois.radb.net", "--", "-i", "origin", asn]
                process = subprocess.Popen(whois_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout, stderr = process.communicate()
                stdout = stdout.decode('utf-8')
                stderr = stderr.decode('utf-8')

                if stderr:
                    logging.warning(f'Error occurred while running whois command for ASN {asn}: {stderr}')
                    continue

                ips = extract_route_info(stdout)
                logging.info(f'ASN - [{asn}] -> IPs -[{len(ips)}]')
                
                if ips:
                    static_ip[app].extend(set(ips))
                else:
                    ip_not_found[app].append(asn)

            logging.info(f'IPs not found for app {app}: {ip_not_found[app]}')

        logging.info(f'IPs not found: {ip_not_found}')

        # Prepare data for CSV output
        tuples = [(subnet, k) for k, v in static_ip.items() for subnet in v]
        df = pd.DataFrame.from_records(tuples, columns=['net_address', 'label'])
        df.to_csv(output, index=False)

        logging.info('Generated network addresses')
        logging.info(df.groupby('label').size())

    except Exception as e:
        logging.error(f"An error occurred: {e}")

if __name__ == "__main__":
    cli()