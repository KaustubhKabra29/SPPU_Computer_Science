// graphics.h library 
#include <conio.h> 
#include <graphics.h> 
#include <stdio.h> 

// Driver Code 
int main() 
{ 
              // Initialize of gdriver with 
              // DETECT macros 
              int gdriver = DETECT, gmode; 

              // Initialize structure of 
              // the house 
              initgraph( &gdriver, &gmode, " " ); 

              // Create lines for structure 
              // of the House 
              line(100, 100, 150, 50); 

              line(150, 50, 200, 100); 

              line(150, 50, 350, 50); 
              line(350, 50, 400, 100); 

              // Draw rectangle to give proper 
              // shape to the house 
              rectangle(100, 100, 200, 200); 
              rectangle(200, 100, 400, 200); 
              rectangle(130, 130, 170, 200); 
              rectangle(250, 120, 350, 180); 

              // Set color using setfillstyle() 
              // which take style and color as 
              // an argument 
              setfillstyle(2, 3); 

              // Fill the shapes with colors
              floodfill(131, 131, RED); 
              floodfill(201, 101, RED); 

              // Change the filling color 
              setfillstyle(11, 7); 

              // Fill the shapes with changed colors 
              floodfill(101, 101, BLUE); 
              floodfill(150, 52, BLUE); 
              floodfill(163, 55, BLUE); 
              floodfill(251, 121, BLUE); 

              // Close the initialized gdriver
              getch(); 
              closegraph(); 
}

