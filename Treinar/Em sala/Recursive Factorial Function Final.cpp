/*
	Name: Recursive Factorial Function in the Right Form
	Author: GUilherme Bezerra
	Date: 18/03/24 17:23
	Description: I'll write a code with a recursive function that returns the number 1 and has as parameter only one element
*/

// Libraries
#include <stdio.h>

// Prototipation Session
int User_input();
int Factorial(int);



int User_input()
{
	int number;
	scanf("%i", &number);
	return number;
}



int Factorial(int number)
{
	if (number == 0)
		return 1;
		
	return number * Factorial(number - 1);
}



int main()
{
	printf("%i", Factorial(User_input()));
	return 0;
}
