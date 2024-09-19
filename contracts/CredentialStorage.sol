// contracts/CredentialStorage.sol
pragma solidity ^0.8.0;

contract CredentialStorage {
    mapping(string => string) private studentToCID;

    function storeCID(string memory studentID, string memory cid) public {
        studentToCID[studentID] = cid;
    }

    function getCID(string memory studentID) public view returns (string memory) {
        return studentToCID[studentID];
    }
}