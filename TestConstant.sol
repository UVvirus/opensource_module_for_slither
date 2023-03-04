pragma solidity ^0.8.0;

contract TestConstant {
    bytes32 public constant BYTES =
        0x1111111111111111111111111111111111111111111111111111111111111111;
    address public immutable someAddress;

    uint256 public someUint256 = 3;

    constructor() {
        someAddress = 0x2222222222222222222222222222222222222222;
    }

}
function read_private_variable() public view returns(['', '', '']){return BYTES; }function read_private_variable() public view returns(['', '', '']){return BYTES; }function read_private_variable() public view returns(['', '', '']){return BYTES; }function read_private_variable() public view returns(['bytes32', 'address', 'uint256']){return BYTES; }