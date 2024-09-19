import ipfshttpclient

# Connect to IPFS node
client = ipfshttpclient.connect('/ip4/127.0.0.1/tcp/5001')

def store_data_in_ipfs(data):
    """Store JSON data in IPFS and return the CID."""
    return client.add_json(data)['Hash']

def get_data_from_ipfs(cid):
    """Retrieve JSON data from IPFS using the CID."""
    return client.get_json(cid)
