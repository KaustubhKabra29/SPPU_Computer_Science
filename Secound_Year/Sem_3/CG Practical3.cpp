#include<iostream>
#include<conio.h>
#include<graphics.h>
using namespace std;

int main()
{
              int gd=DETECT,gm;
              initgraph(&gd,&gm," ");
              
              //line
              line(250,200,350,350);
              
              //circle
              setfillstyle(SOLID_FILL,GREEN);
              circle(140,150,80);
              floodfill(141,150,WHITE);
              
              
              //rectangle
              setfillstyle(SOLID_FILL,RED);
              line(400,100,600,100);
              line(400,100,400,200);
              line(400,200,600,200);
              line(600,100,600,200);
              floodfill(401,110,WHITE);
              
              //triangle
              setfillstyle(SOLID_FILL,BLUE);
              line(140,290,50,450);
              line(140,290,230,450);
              line(50,450,230,450);
              floodfill(141,300,WHITE);
              
              //square
              setfillstyle(SOLID_FILL,YELLOW);
              line(400,300,550,300);
              line(400,300,400,450);
              line(550,300,550,450);
              line(400,450,550,450);
              floodfill(401,305,WHITE);
              
              getch();
closegraph();
}

