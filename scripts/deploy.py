# scripts/deploy.py
from brownie import accounts, CredentialStorage

def main():
    # Use one of Ganache's private keys
    acct = accounts.add('0x69d589555bca81f9e7644a2d2735d2df197c2f57b72667dac6462021d518bc07')
    contract = CredentialStorage.deploy({'from': acct})
    print(f"Contract deployed at: {contract.address}")
