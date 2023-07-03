#include <fstream>
#include <iostream>
#include <conio.h>
using namespace std;
class Student
{
private:
	string name;
	int rollno;
public:
	void add_info()
	{
		fstream fs;      //Creating object of fstream class
		fs.open("F:\\3rd Sem\\OOP\\Practical4.txt",ios::app);      //Opening file in append
		if(!fs)      //Checking whethere file exist 
		   cout<<"File Creation Failed.......";
		else
		{
			//cout<<"New File Created.......";
			cout<<"\n Enter Name :";
			cin>>name;
			cout<<"\n Enter Rollno. :";
			cin>>rollno;
			fs<<name<< "\n";        //Write name to file
			fs<<rollno<< "\n";      //Write rollno to file
			fs.close();             //Closing file 
		}
	}     //End of add_info
	void display_info()
	{
		fstream fs;      //Creating object of fstream class
		fs.open("F:\\3rd Sem\\OOP\\Practical4.txt",ios::in);    //Opening file in input mode
		if(!fs)          //Checking whether file exist
		   cout<<"No such file.......";
		else
		{
			while (!fs.eof())    //Read till end of the file
			{
				fs>>name;        //Reading name from file
				fs>>rollno;      //Reading rollno. from file
				if(!fs.eof())    //Checking whether reached eof
				{
					cout<<name<<" ";
					cout<<rollno;
					cout<< "\n";    //Message Read from file
				} //End of if
			}//End of while
			fs.close();  //Closing file
		}
	}
};

int main()
{
	int ch;
	Student s;
	fstream fs;      //Creating object of fstream class
	
	do
	{
		cout<<"\n * * * Student Information System * * *";
		cout<<"\n * * * * * * * Menu * * * * * * *";
		cout<<"\n 1.Add Information ";
		cout<<"\n 2. Display Information ";
		cout<<"\n 3. Exit";
		cout<<"\n Enter Choice :  ";
		cin>>ch;
		 
		switch (ch)
		{
			case 1:     //Add Information
			    s.add_info();
			    break;
			case 2:     //Display Information
			    s.display_info();
			    break;
			case 3:
				exit(0);   //Successful exit of program
		} //End of Switch statement
	}while (ch !=3);    // end of while
	
return 0;
}
