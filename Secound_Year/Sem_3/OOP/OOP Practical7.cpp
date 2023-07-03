#include<iostream>
#include<iterator>
#include<map>
#include<ctype.h>
#include<algorithm>
using namespace std;

int main()
{
	typedef map<string, float> mapType;
	mapType populationMap;

	populationMap.insert(pair<string, float>("MAHARASHTRA", 125));
	populationMap.insert(pair<string, float>("UTTAR PRADESH", 225));
	populationMap.insert(mapType::value_type("BIHAR", 120)); 
	populationMap.insert(mapType::value_type("WEST BENGAL", 100)); 
	populationMap.insert(make_pair("MADHYA PRADESH", 90)); 
	populationMap.insert(make_pair("TAMIL NADU", 80)); 
	populationMap.insert(make_pair("RAJASTHAN", 78));
	populationMap.insert(make_pair("ANDHRA PRADESH", 53));
	populationMap.insert(make_pair("ODISHA", 47));
	populationMap.insert(make_pair("KERALA", 38));
	populationMap.insert(make_pair("TELANGANA", 37));
	populationMap.insert(make_pair("ASSAM", 35));
	populationMap.insert(make_pair("JHARKHAND", 38));
	populationMap.insert(make_pair("KARNATAKA", 68));
	populationMap.insert(make_pair("GUJARAT", 70));
	populationMap.insert(make_pair("PUNJAB", 31));
	populationMap.insert(make_pair("CHHATTISGARH", 30));
	populationMap.insert(make_pair("HARYANA", 29));
	populationMap.insert(make_pair("UT DELHI", 19));
	populationMap.insert(make_pair("UT JAMMU AND KASHMIR", 14));
	populationMap.insert(make_pair("UTTARAKHAND", 12));
	populationMap.insert(make_pair("HIMACHAL PRADESH", 8));
	populationMap.insert(make_pair("TRIPURA", 04));
	populationMap.insert(make_pair("MEGHALAYA", 4));
	populationMap.insert(make_pair("MANIPUR", 3));
	populationMap.insert(make_pair("NAGALAND", 2));
	populationMap.insert(make_pair("GOA", 2));
	populationMap.insert(make_pair("ARUNACHAL PRADESH", 2));
	populationMap.insert(make_pair("UT PUDUCHERRY", 2));
	populationMap.insert(make_pair("MIZORAM", 1));
	populationMap.insert(make_pair("UT CHANDIGARH", 1));
	populationMap.insert(make_pair("SIKKIM", 1));
	populationMap.insert(make_pair("UT DADRA AND NAGAR HAVELI AND DAMAN AND DIU", 1));
	populationMap.insert(make_pair("UT ANDAMAN AND NICOBAR ISLANDS", 1));
	populationMap.insert(make_pair("UT LAKSHADWEEP", 0.0003));
	populationMap.insert(make_pair("UT LADAKH", 0.00006));
// Erase the end element using the erase function
// Because it's ordered map (by key), 
// map elements are not in the order of the entry 
// In this map it's India since it's  not ordered alphabetically.
char ch = 'n';
do{
	mapType::iterator iter = --populationMap.end();  //populationMap.erase(iter);

// output the size of the map
	cout<<"Total state and UT of India with Size of populationMap: "<<populationMap.size()<<'\n';


	
// find will return an iterator to the matching element if it is found
// or to the end of the map if the key is not found
	string state;
	cout<<"\nEnter that state you known the population or \nEnter 'all' for all information:-> ";
	cin>>state;
	transform(state.begin(), state.end(), state.begin(), ::toupper); 
	if(state == "ALL")
	{
		for (iter = populationMap.begin(); iter != populationMap.end(); ++iter)
		{
			cout<<iter->first<<": "<<iter->second<<" million\n";
		}
	}
	else{
	iter = populationMap.find(state);
	if(iter != populationMap.end()) 
    cout<<state<<"'s populations is "<<iter->second<< " million\n";
	else
    cout<<"Key is not in populationMap"<<'\n';
	}
	
	cout<<"\nDo you want to search more...(y/n)";
	cin>>ch;
	}while(toupper(ch) == 'Y');

	populationMap.clear();
	} 			// clear the entries in the map

