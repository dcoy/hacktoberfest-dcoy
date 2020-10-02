#include<bits/stdc++.h> 
#include<iostream>
#include<conio.h>
using namespace std; 
  
// Function to find the nth root of a number
void findNthRoot(double x, int n) 
{ 
  
// Initialize boundary values  
double low, high; 
if (x >= 0 and x <= 1) 
{ 
    low = x; 
    high = 1; 
} 
else
{ 
    low = 1; 
    high = x;  
}  
  
// Used for taking approximations of the answer  

double epsilon = 0.00000001; 
  
// Do binary search  
double guess = (low + high) / 2; 
while (abs((pow(guess, n)) - x) >= epsilon) 
{ 
    if (pow(guess, n) > x) 
    { 
        high = guess ; 
    }  
    else
    { 
        low = guess ; 
    } 
    guess = (low + high) / 2; 
} 
  
cout
cout << fixed << setprecision(16)  
     << guess; 
}      
  
// Main code  
int main() 
{ 
    double x; 
    int n;
	cout << "Enter the number whose root has to be find: ";
	cin>>x;
	cout << "\n"; 
	cout << "Enter which root has to be find: ";
	cin >> n;
    findNthRoot(x, n) ; 
    
    getch();
} 
