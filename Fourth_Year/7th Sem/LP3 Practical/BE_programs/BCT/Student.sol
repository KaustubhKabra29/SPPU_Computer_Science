//SPDX-License-Identifier: Unlicensed
pragma solidity ^0.8.0;

contract Database{

    struct student{
        int ID;
        string _fname;
        string _lname;
    }

    int public Count = 0;

    mapping(int => student) public stdRecords;

    function addNew(int _id, string calldata _fname, string calldata _lname) public{
                        Count+=1;
                        stdRecords[Count] = student(_id, _fname, _lname);
                    }
    
    event received(address user, uint amount);

    receive() external payable{
        emit received(msg.sender, msg.value);
    }

}