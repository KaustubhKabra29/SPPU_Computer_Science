#include<graphics.h>
#include<iostream.h>
#include<conio.h>
#include<stdlib.h>
static int LEFT=1,RIGHT=2,BOTTOM=4,TOP=8,xmax,ymax,xmin,ymin;
int find_code(int x,int y)
{
 int code=0;
 if(y>ymax)
code|=TOP;
 if(y<ymin)
code|=BOTTOM;
 if(x>xmax)
code|=RIGHT;
 if(x<xmin)
code|=LEFT;
 return code;
}
void main()
{
 clrscr();
 int x1,y1,x2,y2;
 int gd=DETECT,gm;
 initgraph(&gd,&gm,"C:\\turboc3\\bgi");
 setcolor(CYAN);
 cout<<"Enter maximum and minimum value of window: ";
 cin>>xmin>>ymin>>xmax>>ymax;
 rectangle(xmin,ymin,xmax,ymax);
 cout<<"Enter start (x1,y1) and end points (x2,y2) of the line: ";
 cin>>x1>>y1>>x2>>y2;
 line(x1,y1,x2,y2);
 getch();
 int ocode1=find_code(x1,y1),ocode2=find_code(x2,y2);
 int accept=0;
 while(1)
 {
float m=(float)(y2-y1)/(x2-x1);
if(ocode1==0 && ocode2==0)
{
 accept=1;
 break;
}
else if((ocode1&ocode2)!=0)
{
 break;
}
else
{
 int x,y;
 int temp;
 if(ocode1==0)
 {
temp=ocode2;
 }
 else
 {
temp=ocode1;
 }
 if(temp&TOP)
 {
x=x1+(ymax-y1)/m;
y=ymax;
 }
 else if(temp&BOTTOM)
 {
x=x1+(ymin-y1)/m;
y=ymin;
 }
 else if(temp&LEFT)
 {
x=xmin;
y=y1+m*(xmin-x1);
 }
 else if(temp&RIGHT)
 {
x=xmax;
y=y1+m*(xmax-x1);
 }
 if(temp==ocode1)
 {
x1=x;
y1=y;
ocode1=find_code(x1,y1);
 }
 else
 {
x2=x;
y2=y;
ocode2=find_code(x2,y2);
 }
}
 }
 setcolor(RED);
 cout<<"After clipping";
 if(accept)
 {
line(x1,y1,x2,y2);
rectangle(xmin,ymin,xmax,ymax);
 }
 getch();
 closegraph();
}