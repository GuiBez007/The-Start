/*
	Name: Recursive Functions Training
	Author: GUilherme Bezerra
	Date: 17/03/24 16:02
	Description: I'm trying to apply the Recursive Functions Concept in a factorial training
*/

// Libraries
#include <stdio.h>

// Prototopation
int Factorial(int, int);



int Factorial(int number, int initial_number)
{
	initial_number--;
	if (initial_number == 0)
		return number; // 01 - the line below, in the end, will return the original number to the next line
	return initial_number * Factorial(number, initial_number); 
	// 02 - The number returned * the previous initial_number will be returned to this same line until the first initial_number value 
	// EX: user_input = 4 -> (return initial_number... = return 3...)
}


int main()
{
	int number;
	scanf("%d", &number);
	printf("%d", Factorial(number, number));
	return 0;
}
