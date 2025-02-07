import click
from scapy.all import IP, Ether, rdpcap, wrpcap
import glob
import os
import ipaddress

@click.group()
def cli():
    """A command line tool for modifying pcaps"""
    pass

@cli.command('ip_address')
@click.argument('input_dir', type=click.Path(exists=True))
def modify_ip_address_pcaps(input_dir):
    """Modify pcaps by replacing IP addresses with new ones
    
    Args:
        input_dir: Directory containing pcap files to process
        
    Returns:
        None. Modified pcaps are saved to a new directory
    """
    # Track any pcaps that fail processing
    failed_pcaps = []
    
    # Find all pcap files in input directory
    pcaps = glob.glob(os.path.join(input_dir, '*.pcap'), recursive=True)
    click.echo(f"Found {len(pcaps)} pcap files to process")
    
    cnt = 1

    output_dir = os.path.join(input_dir, 'modified_pcaps')
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for pcap in pcaps:
        try:
            head, tail  = os.path.split(pcap)
            click.echo(f'[{cnt}/{len(pcaps)}] - Processing -> {tail}')
            packets = rdpcap(pcap)
            new_ips = {}
            ip_pool = ipaddress.ip_network('192.168.240.0/20')
            ip_counter = 0
            modified_packets = []
            
            for packet in packets:
                if packet.haslayer(IP):
                    src_ip = packet[IP].src
                    dst_ip = packet[IP].dst
                    src_port = packet[IP].sport
                    dst_port = packet[IP].dport
                    proto = packet[IP].proto

                    flow_id_f = ((src_ip, src_port), (dst_ip, dst_port), proto)
                    flow_id_b = ((dst_ip, dst_port), (src_ip, src_port), proto)

                    if flow_id_f not in new_ips and flow_id_b not in new_ips:
                        if ip_counter < ip_pool.num_addresses:
                            new_ip_addr = str(list(ip_pool)[ip_counter])
                            new_ips[flow_id_f] = new_ip_addr
                            new_ips[flow_id_b] = new_ip_addr
                            ip_counter += 1
                        else:
                            print("Not enough IP addresses in the pool")
                            break

                    # Replace the source IP address in the packet
                    if src_ip.startswith('192.168.') or src_ip.startswith('10.'):
                        if flow_id_f in new_ips:
                            packet[IP].src = new_ips[flow_id_f]
                        elif flow_id_b in new_ips:
                            packet[IP].dst = new_ips[flow_id_b]

                    # Replace the destination IP address in the packet
                    if dst_ip.startswith('192.168.') or dst_ip.startswith('10.'):
                        if flow_id_f in new_ips:
                            packet[IP].dst = new_ips[flow_id_f]
                        elif flow_id_b in new_ips:
                            packet[IP].src = new_ips[flow_id_b]

                # Add the modified packet to the list
                modified_packets.append(packet)

            output_file = os.path.join(output_dir, tail)
            wrpcap(output_file, modified_packets)
            cnt +=1
        
        except Exception as e:
            click.echo(f"An error occurred: {e}")
            failed_pcaps.append(tail)

    click.echo(f'Total - {len(failed_pcaps)} - {failed_pcaps}')

if __name__ == '__main__':
    cli()