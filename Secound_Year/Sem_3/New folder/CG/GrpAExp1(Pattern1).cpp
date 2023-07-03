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
    float x,y,i,dx,dy,l;
    if(x1==x2 && y1==y2)
    {
	putpixel(x1,y1,3);
    }
    else
    {
	dx=abs(x2-x1);
	dy=abs(y2-y1);
	if(dx>dy)
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
	    putpixel(x,y,3);
	    x=x+dx;
	    y=y+dy;
	    i++;
	}
    }
}

void show(int x1,int y1,int x,int y)
{
	putpixel(x1+x,y1+y,4);
	putpixel(x1-x,y1+y,4);
	putpixel(x1+x,y1-y,4);
	putpixel(x1-x,y1-y,4);
	putpixel(x1+y,y1+x,4);
	putpixel(x1-y,y1+x,4);
	putpixel(x1+y,y1-x,4);
	putpixel(x1-y,y1-x,4);
}

void b_circle(int x1,int y1,int r)
{
    int d;
    d=3-2*r;
    int x=0,y=r;

    show(x1,y1,x,y);
    while(y>=x)
    {
	x++;
	if(d>0)
	{
	    y--;
	    d=d+4*(x-y)+10;
	}
	else
	{
	    d=d+4*x+6;
	}
	show(x1,y1,x,y);
    }
}


void main()
{
    clrscr();
    int x1,x2,y1,y2,col;
    int gd=DETECT,gm;
    initgraph(&gd,&gm,"C:\\turboc3\\bgi");

    b_circle(300,250,100);
    b_circle(300,250,50);

    dda(300,150,385,300);
    dda(300,150,215,300);
    dda(385,300,215,300);


    getch();
    closegraph();
}
