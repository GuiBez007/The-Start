/*
	Name: Fibonacci Sequence in a Recursive Function
	Author: GUilherme Bezerra
	Date: 18/03/24 22:23
	Description: Recursive Fibonacci
*/

// Libraries
#include <stdio.h>

// Prototipation
int Fibonacci(int, int, int);


int Fibonacci(int position_number, int previous, int actual)
{
	if (position_number == 1)
		return actual;
		
	int next = previous + actual;
	return Fibonacci(--position_number, actual, next);
	
}



int main()
{
	int position_number;
	scanf("%i", &position_number);
	
	if (position_number == 0)
		printf("\nFibonacci Number in the %i position is -> 0", position_number);
	else if (position_number == 1)
		printf("\nFibonacci Number in the %i position is -> 1", position_number);
	else
		printf("\nFibonacci Number in the %i position is -> %i", position_number, Fibonacci(position_number, 0, 1));	
}
