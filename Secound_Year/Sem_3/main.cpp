#include<iostream>                  
using namespace std;               

class complex                     
{
 public:
 float real,img;          


        complex()              
{
}
        complex operator+ (complex);
        complex operator* (complex);
        friend ostream &operator<<(ostream &,complex&);
        friend istream &operator<<(istream &,complex&);
};

 complex complex:: operator + (complex obj)
{
 complex temp;
 temp.real=real+obj.real;
 temp.img=img+obj.img;
 return (temp);
}
 istream &operator >> (istream &is,complex &obj)
{
 is>>obj.real;
 is>>obj.img;
 return is;
}
 ostream &operator<<(ostream &outt,complex &obj)
{
 outt<<""<<obj.real;
 outt<<"+"<<obj.img<<"i";
 return outt;
}
 complex complex :: operator * (complex obj)
{
   complex temp;
        temp.real=real*obj.real-img*obj.img;
        temp.img=real*obj.img+img*obj.real;
        return (temp);
}


int main()
{
 complex a,b,c,d;
 cout<<"\nEnter first complex number\n";
 cout<<"\nEnter real and imaginary: ";
 cin>>a;
 cout<<"Enter second complex number \n";
 cout<<"\nEnter real and imaginary: ";
 cin>>b;
 cout<<"\n\tArithmetic operations";
 c=a+b;
 cout<<"\n\tAddition =";
 cout<<c;
 d=a*b;
 cout<<"\n\tMultiplication=";
 cout<<d;
 cout<<endl;
 return 0;
}


