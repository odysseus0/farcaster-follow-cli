# Farcaster Follow CLI

A simple CLI tool to follow users on Farcaster using their `fid` (Farcaster ID).

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/odysseus0/farcaster-follow-cli.git
   cd farcaster-follow-cli
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Step 0: Obtain Bearer Token and Group Chat JSON

Before running the scripts, you need to obtain your bearer token and the group chat JSON:

1. Open Warpcast in your browser and log in.
2. Open the developer tools (usually F12 or right-click and select "Inspect").
3. Go to the "Network" tab.
4. Look for a request to `direct-cast-conversation-list?limit=15&category=default&filter=group`. You can filter by `group` to find the group chat.
5. In the request headers, find the "Authorization" header. The bearer token is the string after "Bearer".
6. In the response tab, you'll find the JSON containing the group chat information. Save this JSON to a file (e.g., `group_chat.json`).


### Step 1: Extract FIDs from group chat JSON

First, use the `extract_fids.py` script to extract FIDs from a Farcaster group chat JSON file:

```bash
python3 extract_fids.py --input <path-to-group-chat-json> --output fids.csv
```

- **Input JSON file (`--input`)**: Required. Path to the Farcaster group chat JSON file.
- **Output CSV file (`--output`)**: Required. Path to save the extracted FIDs as a CSV file.

### Step 3: Follow users using the extracted FIDs

Now use the `farcaster_follow.py` script to follow the users:

```bash
python3 farcaster_follow.py --token <your-bearer-token> --file fids.csv
```

- **Bearer token (`--token`)**: Required. Your Farcaster API token for authentication.
- **CSV file (`--file`)**: Optional. A CSV file containing a list of `targetFid`s. If not provided, the default list will be used.

The output of the script should look like this:

```
Successfully followed user with FID: 123456
Successfully followed user with FID: 7891011
Successfully followed user with FID: 1121314
```

There might be one 400 error in the output, which is fine. It is usually from you trying to follow yourself.

## You are done!

🎉 Hooray! You're all set to start following users on Farcaster! Enjoy connecting with your community! 🚀


## License

MIT License
