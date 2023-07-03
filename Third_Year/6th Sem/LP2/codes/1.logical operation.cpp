#include <iostream.h>
//using namespace std;
#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>
void main()
{
    //clrscr();
    char str[]="HELLOWORLD";
    char str1[11];
    char str2[11];
    int i,len;
    len = strlen(str);
    
    for(i=0;i<len;i++)
    {
        str1[i]=str[i] & 127;
        cout<<str1[i];
    }
    cout<<"\n";
    for(i=0;i<len;i++)
    {
        str2[i] = str[i] ^ 127;
        cout<<str2[i];
    }
    cout<<"\n";
    getch();
}
