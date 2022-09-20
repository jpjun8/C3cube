#include <stdio.h>
int main()
{
	int i, num, sum = 0, min = 100;
	for(i = 0; i < 7; i++)
	{
		scanf("%d", &num);
		if(num % 2 == 1)
		{
			sum += num;
			if(num < min)
			{
				min = num;
			}
		}
	}

	printf("%d ", sum);
	printf("%d ", min);
}