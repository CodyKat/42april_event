#include <stdio.h>

int main(int argc, char **argv)
{
	int	scoreSum = 0;
	int aceCount = 0;
	char *handCards = argv[1];

	if (argc != 2)
		printf("Wrong number of arguments");
	else
	{
		while (*handCards != 0)
		{
			if (*handCards == 'A')
			{
				aceCount++;
				scoreSum += 11;
			}
			else if (*handCards >= '2' && *handCards <= '9')
				scoreSum += *handCards - '0';
			else if (*handCards == 'T' || *handCards == 'J' || *handCards == 'D' || *handCards == 'K')
				scoreSum += 10;
			else
			{
				dprintf(2, "Wrong card name: %c", *handCards);
				return 1;
			}
			handCards++;
		}
		while (aceCount > 0 && scoreSum > 21)
		{
			scoreSum -= 10;
			aceCount--;
		}
		if (scoreSum == 21)
			printf("Blackjack!");
		else
			printf("%d", scoreSum);
	}
	return scoreSum;
}
