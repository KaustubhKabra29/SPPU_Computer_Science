# include<iostream>
# include<conio.h>
using namespace std;

class complex	// class created
{
	public:
		float a,b;	
	public:
		complex()	// constructor 
		{
			a=0.0;
			b=0.0;
		}

complex operator+(complex obj) // '+' operator overloaded
{
	complex temp;
	temp.a=a+obj.a;
	temp.b=b+obj.b;
	return temp;
};

complex operator-(complex obj)	// '-' operator overloaded
{
	complex temp;
	temp.a=a-obj.a;
	temp.b=b-obj.b;
	return temp;
};

complex operator*(complex obj)	// '*' operator overloaded
{
	complex temp;
	temp.a=(a*obj.a)-(b*obj.b);
	temp.b=(a*obj.a)+(b*obj.b);
	return temp;
};

complex operator/(complex obj)	// '/' operator overloaded
{
	complex temp;
	temp.a=(a*obj.a)-(b*(-obj.b));
	temp.b=(a*(-obj.a))+(b*obj.b);
	temp.a=temp.a/((obj.a*obj.a)+(obj.b*obj.b));
	temp.b=temp.b/((obj.a*obj.a)+(obj.b*obj.b));
	return temp;
};

// Friend classes declared
friend ostream &operator<<(ostream &out,complex &c);
friend istream &operator>>(istream &in,complex &c);

};

// '<<' operator overloaded
ostream &operator<<(ostream &out,complex &c)
{
	out<<c.a<<" + i("<<c.b<<")";
	return out;
}

// '>>' operator overloaded
istream &operator>>(istream &in,complex &c)
{
	cin>>c.a>>c.b;
	return in;
}

// Driver function
int main()
{
	char out,cont;
	out='N',cont='N';
	int op;
	complex c1,c2,c3;	// Objects initialized
	
	do
	{
		// Accept real and imaginary part of two complex numbers
		cout<<"Enter real and imaginary parts of first complex number: \n";
		cin>>c1;
		
		cout<<"Enter real and imaginary parts of second complex number: \n";
		cin>>c2;
		
		do
		{
			// Menu
			cout<<"\nSelect operation:\n";
			cout<<"1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n";
			cout<<"Enter choice: ";
			cin>>op;
			
			switch(op)
			{
				case 1:
					{
						// Add two complex numbers
						c3=c1+c2;
						cout<<c3<<endl;	  //Display result
						break;
					}
				case 2:
					{
						// Subtract two complex numbers
						c3=c1-c2;
						cout<<c3<<endl;	  //Display result
						break;
					}
				case 3:
					{
						// Multiply two complex numbers
						c3=c1*c2;
						cout<<c3<<endl;	  //Display result
						break;
					}
				case 4:
					{
						// Divide two complex numbers
						c3=c1/c2;
						cout<<c3<<endl;	  //Display result
						break;
					}
				cout<<"Select another operation?(Y/N)\n";
				cin>>cont;
			}
		}while(cont=='Y' || cont=='y');
		
		cout<<"Input different complex numbers?(Y/N)\n";
		cin>>out;
	}while(true);
}

