# include<iostream>
# include<conio.h>
# include<string.h>
using namespace std;
class students				// Class created
{
	public:
		string name,cls,dob;
		int rollno,marks;
		float per;
		char div;
	static int c;			// Static variable declared
	
	// Personal Information variables declared
	private:		
		long long telno;
		string bg,address,divl;
		
	friend class personal_info;			// Friend class declared
	
	// Default constructor to initialise default values	
	public:
		students()
		{
			name="";
			dob="DD/MM/YYYY";
			cls="";
			bg="";
			address="";
			divl="";
			rollno=0;
			telno=0;
			marks=0;
			div=' ';
		}
	
	// Copy constructor
	public:
		students(students &obj)
		{
			this->name=obj.name;
			this->rollno=obj.rollno;
			this->cls=obj.cls;
			this->dob=obj.dob;
			this->div=obj.div;
			this->telno=obj.telno;
			this->address=obj.address;
			this->bg=obj.bg;
			this->divl=obj.divl;
			this->marks=obj.marks;
			this->per=obj.per;
		}
	
	// Destructor
	public:
		~students()
		{
		}
	
	// Get details of student
	public:
		void getdetails()
		{
			cout<<"Enter name: ";
			cin.ignore();
			getline(cin,name);
			cout<<"Enter class: ";
			getline(cin,cls);
			cout<<"Enter date of birth: ";
			cin>>dob;
			cout<<"Enter Roll no.: ";
			cin>>rollno;
			cout<<"Enter division: ";
			cin>>div;
		}
	
	// Print all the details of student
	public:
		void printdetails()
		{
			cout<<endl<<"Name:"<<name<<endl;
			cout<<"Roll No.: "<<rollno<<endl;
			cout<<"Class: "<<cls<<endl;
			cout<<"Date of birth: "<<dob<<endl;
			cout<<"Division: "<<div<<endl;
		}
	
	// Inline function to calculate percentage of student
	inline float getmarks()
	{
		cout<<"Enter marks out of 500: ";
		cin>>marks;
		per=((marks*100)/500);
	}
	
	inline void displaymarks()
	{
		cout<<"Marks out of 500: "<<marks<<endl;
		cout<<"Percentage: "<<per<<endl;
	}
	
	// Static function to count number of students in database
	static void count()
	{
		c++;
	}
	
	// Static function to display number of students in database
	static void showcount()
	{
		cout<<endl<<"Number of students are: "<<c;
	}
};		// Class ends
int students::c;			// Definition of static member


class personal_info			// Friend Class
{
	public:
		personal_info()
		{}
		
	public:
		personal_info(personal_info &obj)
		{}
	
	// Get personal details of students
	public:
		void getperdetails(students& obj)
		{
			cout<<"Enter Telephone number: ";
			cin>>obj.telno;
			cout<<"Enter address: ";
			cin.ignore();
			getline(cin,obj.address);
			cout<<"Enter Blood Group: ";
			getline(cin,obj.bg);
			cout<<"Enter driving Liscence number: ";
			getline(cin,obj.divl);
		}
		
	// Display personal details of student
	public:
		void showperdetails(students& obj)
		{
			cout<<"Telephone number: "<<obj.telno<<endl;
			cout<<"Address: "<<obj.address<<endl;
			cout<<"Blood Group: "<<obj.bg<<endl;
			cout<<"Driving Liscence: "<<obj.divl<<endl;
		}
		
	// Destructor
	public:
		~personal_info()
		{
		}
};		// Friend class ends


// Main function
int main()
{
	int ch,n;
	char c;
	cout<<"Enter the total number of students: ";
	cin>>n;
	// Array of pointers of student class
	students *std=new students[n];					
	// Array of pointers of friend class
	personal_info *pinfo=new personal_info[n];		
	do					// Do-while loop
	{
		cout<<endl<<"********MENU********"<<endl;
		cout<<"Enter 1 to add new entry to student database"<<endl;
		cout<<"Enter 2 to display database"<<endl;
		cout<<"Enter 3 to call copy constructor"<<endl;
		cout<<"Enter 4 to call default constructor"<<endl;
		cout<<"Enter 5 to delete records"<<endl;
		cout<<"Enter your choice: ";
		cin>>ch;
		switch(ch)					// Switch Case
		{
			case 1:				
			{
				for(int i=0;i<n;i++)
				{
					// Enter details
					cout<<endl<<"Enter details of student "<<i+1<<endl;
					std[i].getdetails();
					pinfo[i].getperdetails(std[i]);
					std[i].count();
					std[i].getmarks();
				}
			}
			break;
			
			case 2:
			{
				// Display database
				int i;
				personal_info obj1;
				std[i].showcount();
				for(int i=0;i<n;i++)
				{	
					cout<<endl<<endl<<"STUDENT DETAILS-";
					std[i].printdetails();
					obj1.showperdetails(std[i]);
					std[i].displaymarks();
				}	
			
			}
			break;
			
			case 3:
			{
				// Copy constructor
				students s1,s3;
				personal_info obj1,obj3;
				cout<<endl<<"DEFAULT VALUES-";
				s3.printdetails();
				obj3.showperdetails(s3);
				
				cout<<endl<<"Enter Details-"<<endl;
				s1.getdetails();
				obj1.getperdetails(s1);
				s1.getmarks();
				
				cout<<endl<<"COPY CONSTRUCTOR CALLED."<<endl;
				
				students s2(s1);
				personal_info obj2(obj1);
				
				cout<<endl<<"***************"<<endl;
				cout<<"COPIED DATA IS-"<<endl;
				s2.printdetails();
				obj2.showperdetails(s2);
				s2.displaymarks();
			}
			break;
			
			case 4:
			{
				// Default constructor
				cout<<endl<<"DEFAULT VALUES-"<<endl;
				students s1;
				personal_info obj1;
				s1.printdetails();
				obj1.showperdetails(s1);
				s1.displaymarks();
			}
			break;
			
			case 5:
			{
				// Destructor
				cout<<endl<<"!!!!!!!!!!!!!!!!!!!!"<<endl;
				cout<<"DATA DESTROYED"<<endl<<"THANK YOU"<<endl;
				delete [] std;
				delete [] pinfo;
			}
			break;
			
			default:
			{
				cout<<"WRONG INPUT";
			}
		}
	cout<<endl<<"Want to continue(y/n)"<<endl;
	cin>>c;
	}while(c=='y' || c=='Y');
	return 0;
	getch();
}

