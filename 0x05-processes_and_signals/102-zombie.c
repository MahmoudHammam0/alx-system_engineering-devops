#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - infinite while loop
 * Return: 0 (Success)
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}

/**
 * main - Entry point
 * Description: create 5 zombie processes
 * Return: 0 (Success)
 */
int main(void)
{
	int i;
	pid_t z;

	for (i = 0; i < 5; i++)
	{
		z = fork();
		if (!z)
			return (0);
		printf("Zombie process created, PID: %d\n", z);
	}
	infinite_while();
	return (0);
}
