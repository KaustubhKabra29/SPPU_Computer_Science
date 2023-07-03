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
	Cars car1;
	//car1.setData("Mercedes-Benz","AMG GT 4-Door Coupe","Petrol",10.2,7500000);
	car1.displayData();
	return 0;	
}
