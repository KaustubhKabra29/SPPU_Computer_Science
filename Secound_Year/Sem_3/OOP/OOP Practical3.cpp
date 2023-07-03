#include<iostream>
#include<conio.h>
using namespace std;

// Base class
class publication
{
	// Base class variables
	public:
		string title;
		float price;
		
		// Constructor
		publication()
		{
			title="";
			price=0.0;
		}
};

// Derived class for books
class book:public publication
{
	public:
		int page_count;
		
		// Constructor
		book()
		{
			page_count=0;
		}
		
		void set_info()
		{
			// Try block
			try
			{
				cout<<"Enter title of the book: ";
				cin.ignore();
				getline(cin,title);
				cout<<"Enter number of pages in the book: ";
				cin>>page_count;
				if(page_count<0)
				{
					throw page_count;
				}
				cout<<"Enter price of the book: ";
				cin>>price;
				if(price<0)
				{
					throw price;
				}
			}
			// Catch block
			catch(int p)
			{
					cout<<"Page count cannot be negative"<<endl;
					page_count=0;
					title="0";
					price=0.0;
			}
			catch(float p)
			{
					cout<<"Price cannot be negative";
					page_count=0;
					title="0";
					price=0;
			}
	}
		
		void display_info()
		{
			cout<<"Title-"<<endl<<title<<endl;
			cout<<"Number of pages: "<<endl<<page_count<<endl;
			cout<<"Price: "<<endl<<price<<endl;
		}
};

// Derived class for cassettes
class tape:public publication
{
	public:
		float time;
		
		tape()
		{
			time=0.0;
		}
		
		void set_info()
		{
			try
			{
				cout<<"Enter title of the cassette: ";
				cin.ignore();
				getline(cin,title);
				cout<<"Enter the running time of the cassete in minutes: ";
				cin>>time;
				if(time<0)
				{
					throw time;
				}
				cout<<"Enter price of the cassette: ";
				cin>>price;
				if(price<0)
				{
					throw price;
				}
			}
			catch(float t)
			{
					cout<<"Time cannot be negative"<<endl;
					time=0.0;
					title="0";
					price=0.0;
			}
			catch(float p)
			{
					cout<<"Price cannot be negative"<<endl;
					time=0.0;
					title="0";
					price=0.0;
			}
		}
		
		void display_info()
		{
			cout<<"Title:"<<endl<<title<<endl;
			cout<<"Running time: "<<endl<<time<<endl;
			cout<<"Price: "<<endl<<price<<endl;
		}
};

int main()
{
	int n1,n2,ch;
	char c;
	cout<<"Enter number of books: ";
	cin>>n1;
	cout<<"Enter number of cassettes: ";
	cin>>n2;
	// Dynamically memory allocation
	book *b=new book[n1];
	tape *t=new tape[n2];
	
	do
	{
		cout<<"Enter 1 to add books"<<endl;
		cout<<"Enter 2 to add cassettes"<<endl;
		cout<<"Enter 3 to display available books"<<endl;
		cout<<"Enter 4 to display available cassettes"<<endl;
		cout<<"Enter your choice: "<<endl;
		cin>>ch;
		
		// Switch case
		switch(ch)
		{
			case 1:
			{
				// Enter books details
				for(int i=0;i<n1;i++)
				{
					cout<<endl<<"Enter details of book "<<i+1<<endl;
					b[i].set_info();
				}
			}
			break;
			
			case 2:
			{
				for(int i=0;i<n2;i++)
				{
					// Enter cassette details
					cout<<endl<<"Enter details of cassette "<<i+1<<endl;
					t[i].set_info();
				}
			}
			break;
			
			case 3:
			{
				// Display book details
				for(int i=0;i<n1;i++)
				{
					cout<<endl<<"Details of Book "<<i+1<<"- "<<endl;
					b[i].display_info();
				}
			}
			break;
			
			case 4:
			{
				// Display cassette details
				for(int i=0;i<n2;i++)
				{
					cout<<endl<<"Details of cassette "<<i+1<<"- "<<endl;
					t[i].display_info();
				}
			}
			break;
			
			default:
				cout<<"Wrong choice";
		}
		cout<<endl<<"Do you want to continue?(Y/N)"<<endl;
		cin>>c;
	}while(c=='Y' || c=='y');
	return 0;
	getch();
}

