#include<stdio.h>
#include<conio.h>
#include<graphics.h>
#include<dos.h>
int main(void)
{
int a=DETECT,gmode;
int i,p,c,b,k;
initgraph(&a,&gmode,"C://TurboC3//BGI");
for(i=1;i<=1000;i++)
{
delay(0);
cleardevice();
if(i<440)
{
if(i<220)
p=0;
else
p=(i-220)/5;
}
else
{
if(i<660)
p=88-(i-220)/5;
else
p=0;
}
setfillstyle(1,14);
fillellipse(40,40,30,30);             //sun
circle(90,250,15);
circle(95,243,3);
line(96,254,100,256);
line(87,264,87,271);
line(93,264,93,271);
setfillstyle(1,12);
bar3d(65,271,105,320,10,1);
line(65,271,55,285);
line(55,285,50,295);
line(105,271,60,295);
line(75,320,75,350);
line(95,320,95,350);                    //BATSMAN
line(40+p,360-p,50,295);
line(50+p,360-p,60,295);
line(40+p,360-p,50+p,360-p);                 //bat
line(40,330,542,330);                  //creetch
line(20,305,20,370);
line(25,300,25,365);
line(30,295,30,360);                       //RIGHT stamp
line(520,305,520,370);
line(525,300,525,365);
line(530,295,530,360);		       //left stamp
line(10,390,510,390);
line(10,390,40,330);
line(510,390,542,330);
line(105,330,75,390);
line(477,330,445,390);
if(i<430)
{
delay(5);
if(i<250)
b=i/5;
else
b=100-(i/5);
k=0;
c=i;
}
else
{
k=(i-430)/2;
c=430-(i-430);
b=-5;
}
setfillstyle(1,10);
fillellipse(530-c,290-k+b,7,7);
}
getch();
return 0;
}