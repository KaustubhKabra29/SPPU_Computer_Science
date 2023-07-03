#include<iostream>
#include<stdio.h>
#include<graphics.h>
using namespace std;
int main()
{
int gd,gm;
char a[2];
int x,y;
detectgraph(&gd,&gm);
initgraph(&gd,&gm," ");
x=getmaxx()/2; //To get center of the x-axis
y=getmaxy()/2; //To get center of the y-axis
line(x,0,x,y); //Draw a verticle line from top to center
line(0,y,x,y); //Draw a horizontal line from left to center
line(x,y,getmaxx(),y);
line(x,y,x,getmaxy());
outtext("Circle");
circle(159,120,80);
outtextxy(320,0,"Rectangle");
rectangle(360,40,580,200);
outtextxy(0,241,"Ellipse");
ellipse(159,360,0,360,50,100);
outtextxy(321,241,"Half Ellipse");
ellipse(529,360,0,180,50,100);
 getch();
closegraph();
}


