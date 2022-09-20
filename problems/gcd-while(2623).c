#include <stdio.h>
int main()
{
	int n1, n2;

	printf("Enter 2 integers: ");
	scanf("%d %d", &n1, &n2);

	while(n1 != n2)
	{
		if(n1 > n2)
			n1 -= n2;
		else
			n2 -= n1;
	}

	printf("GCD : %d\n", n1);

	retrun 0;
}