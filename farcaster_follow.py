import requests
import argparse
import csv
import os
import time

# Default CSV file path
DEFAULT_CSV_PATH = 'default_fids.csv'

def read_fids_from_csv(file_path):
    """Read targetFids from a CSV file"""
    target_fids = []
    try:
        with open(file_path, mode='r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header
            for row in csv_reader:
                for fid in row:
                    target_fids.append(int(fid.strip()))
    except Exception as e:
        print(f"Error reading file: {e}")
        exit(1)
    return target_fids

def follow_users(token, target_fids):
    """Send requests to follow users on Farcaster with throttling"""
    url = 'https://client.warpcast.com/v2/follows'
    headers = {
        'authorization': f'Bearer {token}',
        'content-type': 'application/json; charset=utf-8'
    }

    for fid in target_fids:
        data = {"targetFid": fid}
        try:
            response = requests.put(url, headers=headers, json=data)
            response.raise_for_status()
            print(f"Successfully followed user with FID: {fid}")
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred while following FID {fid}: {http_err}")
        except Exception as err:
            print(f"Error occurred while following FID {fid}: {err}")
        
        # Add a delay of 1 second between requests
        time.sleep(1)

def main():
    parser = argparse.ArgumentParser(description='Farcaster Follow CLI')
    parser.add_argument('-t', '--token', required=True, help='Bearer token for authentication')
    parser.add_argument('-f', '--file', help='CSV file with targetFid list (optional)')
    
    args = parser.parse_args()
    
    token = args.token
    
    # Use the provided CSV file or the default one
    csv_file = args.file if args.file else DEFAULT_CSV_PATH
    
    # Check if the CSV file exists
    if not os.path.exists(csv_file):
        print(f"Error: CSV file '{csv_file}' not found.")
        exit(1)
    
    target_fids = read_fids_from_csv(csv_file)

    # Call the function to follow users
    follow_users(token, target_fids)

if __name__ == '__main__':
    main()