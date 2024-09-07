import json
import argparse
import csv

def extract_fids(json_data):
    # Parse the JSON data
    data = json.loads(json_data)
    
    # Find the "Network School v1" conversation
    network_school_conversation = None
    for conversation in data['result']['conversations']:
        if conversation['name'] == "Network School v1":
            network_school_conversation = conversation
            break
    
    if not network_school_conversation:
        print("Network School v1 conversation not found.")
        return []
    
    # Extract fids from participants
    fids = [participant['fid'] for participant in network_school_conversation['participants']]
    
    return fids

def save_fids_to_csv(fids, output_file):
    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['FID'])  # Header
        for fid in fids:
            writer.writerow([fid])

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Extract FIDs from Farcaster group chat JSON")
    parser.add_argument("-i", "--input", required=True, help="Path to the input group chat JSON file")
    parser.add_argument("-o", "--output", required=True, help="Path to the output CSV file")
    args = parser.parse_args()

    try:
        with open(args.input, 'r') as file:
            json_data = file.read()
        
        fids = extract_fids(json_data)
        save_fids_to_csv(fids, args.output)
        print(f"Extracted FIDs saved to {args.output}")
    except FileNotFoundError:
        print(f"Error: File '{args.input}' not found.")
    except json.JSONDecodeError:
        print("Error: Invalid JSON data in the file.")
    except IOError:
        print(f"Error: Unable to write to file '{args.output}'.")
