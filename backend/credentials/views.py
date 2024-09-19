from django.http import JsonResponse
from .utils import store_data_in_ipfs, get_data_from_ipfs
from web3 import Web3

# Connect to Ganache
w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:7545'))
contract_address = '0xf15481003A7517CAAc27e1053463c3BB2A15308e'
contract_abi ='[{"inputs":[{"internalType":"string","name":"studentID","type":"string"}],"name":"getCID","outputs":[{"internalType":"string","name":"","type":"string"}],"stateMutability":"view","type":"function"},{"inputs":[{"internalType":"string","name":"studentID","type":"string"},{"internalType":"string","name":"cid","type":"string"}],"name":"storeCID","outputs":[],"stateMutability":"nonpayable","type":"function"}]'
private_key = 'YOUR_GANACHE_PRIVATE_KEY'
acct = w3.eth.account.privateKeyToAccount(private_key)

# Load the contract
contract = w3.eth.contract(address=contract_address, abi=contract_abi)

def store_credential(request):
    """Store credential in IPFS and blockchain."""
    student_id = request.POST['student_id']
    name = request.POST['name']
    degree = request.POST['degree']

    # Prepare data for IPFS
    data = {'name': name, 'degree': degree}
    cid = store_data_in_ipfs(data)

    # Store CID in blockchain
    tx = contract.functions.storeCID(student_id, cid).buildTransaction({
        'from': acct.address,
        'nonce': w3.eth.getTransactionCount(acct.address),
    })
    signed_tx = w3.eth.account.signTransaction(tx, private_key)
    w3.eth.sendRawTransaction(signed_tx.rawTransaction)

    return JsonResponse({'status': 'success', 'cid': cid})

def verify_credential(request):
    """Verify credential by fetching CID from blockchain and data from IPFS."""
    student_id = request.GET['student_id']

    # Get CID from blockchain
    cid = contract.functions.getCID(student_id).call()

    # Retrieve data from IPFS
    data = get_data_from_ipfs(cid)

    return JsonResponse({'student_data': data})
