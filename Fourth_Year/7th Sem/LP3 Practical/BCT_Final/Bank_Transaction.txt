//SPDX-License-Identifier: Unlicensed
pragma solidity ^0.8.0;

contract Bank{
    mapping(address=>uint) public balances;

    function deposit(uint _amount) public payable{
        balances[msg.sender] += _amount;
    }

    function withdraw(uint _amount) public{
        require(balances[msg.sender]>= _amount, "Not enough ether");
        balances[msg.sender] -= _amount;
    }

    function getBal() public view returns(uint){
        return balances[msg.sender];
    }

}