#include <iostream>
#include <conio.h>
#include <string>
using namespace std;

//class declaration and definition
class Cars
{
	private:
		//data members
		string company_name;
		string model_name;
		string fuel_type;
		float mileage;
		double price;
	
	public:
        //Parameterized Constructor
		Cars(string cname,string mname,string ftype,float m,double p)
		{
			cout<<"\n\nParameterized Constructor called\n";
			company_name = cname;
			model_name = mname;
			fuel_type = ftype;
			mileage = m;
			price = p;
		}
		
                                 //member function
		void setData(string cname,string mname,string ftype,float m,double p) 
		{
			company_name = cname;
			model_name = mname;
			fuel_type = ftype;
			mileage = m;
			price = p;
		}	
		
		void displayData()
		{
			cout<<"\n\nCar Properties";
			cout<<"\nCar Company Name - "<<company_name;
			cout<<"\nCar Model -  "<<model_name;
			cout<<"\nCar Fuel Type - "<<fuel_type;
			cout<<"\nCar Mileage - "<<mileage;
			cout<<"\nCar Price - "<<price;
		}
};
int main()
{
	Cars car2("Toyota","Fortuner","Diesel",18,3500000);
	car2.displayData();
	return 0;
}

