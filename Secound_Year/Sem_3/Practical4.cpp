#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main(){
ofstream f;
string Name,st1;
char div,clas;
int Rollno;
long long Contact;

cout<<" *WELCOME* "<<endl;
cout<<"ENTER THE DATA TO BE STORED IN FILE "<<endl;
f.open("EXAMPLE.txt");
if(f.is_open()){

cout<<"///////////////"<<endl; 
cout<<"ENTER STUDENT NAME: "<<endl;  
// cin.ignore(100,'\n');
getline(cin,Name);
f<<"NAME :"<<Name<<endl;
cout<<"\nENTER YOUR ROLL NUMBER"<<endl;
cin>>Rollno;
f<<"ROLL NUMBER    :"<<Rollno<<endl;
cout<<"ENTER YOUR DIVISION"<<endl;
cin>>div;
f<<"DIVISION :"<<div<<endl;
cout<<"ENTER YOUR CLASS"<<endl;
cin>>clas;
f<<"CLASS :"<<clas<<endl;
cout<<"ENTER CONTACT NUMBER "<<endl;
cin>>Contact;
f<<"CONTACT:"<<Contact<<endl;
cout<<"///////////////"<<endl;
}
else{
cout<<"FILE NOT OPEN "<<endl;
}
f.close();


ifstream in;
in.open("EXAMPLE.txt",ios::in);
cout<<" DATA STRORED IN FILE :"<<endl;
cout<<"*********************"<<endl;
while(in.eof()==0){
getline(in,st1);
cout<<st1<<endl;
}
in.close();
return 0;
}

