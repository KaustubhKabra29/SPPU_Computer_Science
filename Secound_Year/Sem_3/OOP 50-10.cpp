#include <iostream>
#include <conio.h>
#include <string>
using namespace std;

//class declaration and definition
class Cars{
	private:
		//data members
		string company_name;
		string model_name;
		string fuel_type;
		float mileage;
		double price;
	
	public:
		//Default Constructor
		Cars(){
			cout<<"\nDefault Constructor called";
		}
		
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
		
		//Copy Constructor
		Cars(Cars &obj)
		{
			cout<<"\n\nCopy Constructor called\n";
			company_name = obj.company_name;
			model_name = obj.model_name;
			fuel_type = obj.fuel_type;
			mileage = obj.mileage;
			price = obj.price;
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
		//Destructor
		~Cars()
		{
			cout<<"\nDestructor called";
		}
};
int main()
{
	Cars car1,car2("Toyota","Fortuner","Diesel",18,3500000);
	car1.setData("Mercedes-Benz","AMG GT 4-Door Coupe","Petrol",10.2,7500000);
	car1.displayData();
	car2.displayData();
	Cars car3 = car1; // Copy Constructor called
	car3.displayData();
	return 0;
	
}

