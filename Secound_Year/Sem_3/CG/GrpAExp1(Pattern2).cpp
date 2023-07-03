#include<graphics.h>
#include<conio.h>
#include<math.h>
#include<iostream.h>
int sign(int x)
{
 if(x>0)
   return 1;
 else if(x<0)
    return -1;
 else
    return 0;
}
void dda(int x1,int y1,int x2,int y2)
{
 float x,y,l,i,dx,dy;
 if(x1==x2 && y1==y2)
 {
   putpixel(x1,y1,4);
 }
 else
 {
   dx=abs(x2-x1);
   dy=abs(y2-y1);
   if(dx>=dy)
     l=dx;
   else
      l=dy;
   dx=(x2-x1)/l;
   dy=(y2-y1)/l;
   x=x1+0.5*sign(dx);
   y=y1+0.5*sign(dy);
   i=1;
   while(i<l)
   {
     putpixel(x,y,4);
      x=x+dx;
      y=y+dy;
      i++;
    }
 }
}
void bla(int x1,int y1,int x2,int y2)
{
 float dx,dy,x,y,e,i;
 if(x1==x2 && y1==y2)
    putpixel(x1,y1,4);
 else
 {
    dx=abs(x2-x1);
    dy=abs(y2-y1);
    x=x1;
    y=y1;
    putpixel(x,y,4);
    e=2*dy-dx;
    i=1;
    while(i<=dx)
    {  
      while(e>=0)
      {
         y=y+1;
         e=e-2*dx;
       }
       x=x+1;
       e=e+2*dy;
       putpixel(x,y,4);
       i=i+1;
    }
 }
}

void main()
{
 clrscr();
 int gd=DETECT,gm;
 initgraph(&gd,&gm,"C:\\turboc3\\bgi");
 
 bla(200,300,400,300);
 dda(200,300,200,200);
 bla(200,200,400,200);
 dda(400,200,400,300);
 
 dda(200,250,300,200);
 dda(200,250,300,300);
 bla(300,200,400,250);
 dda(300,300,400,250);
 
 bla(250,225,150,225);
 dda(250,225,250,275);
 dda(350,275,250,275);
 dda(350,225,350,275);
 
 getch();
 closegraph();
}