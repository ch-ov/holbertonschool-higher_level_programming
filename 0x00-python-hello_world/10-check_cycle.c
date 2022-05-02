#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it
 * @list: Pointer to list
 * Return: int
 */
int check_cycle(listint_t *list)
{
	listint_t *pointPlusOne = list, *pointPlusTwo = list;

	while (pointPlusOne && pointPlusTwo && pointPlusTwo->next)
	{
		pointPlusOne = pointPlusOne->next;
		pointPlusTwo = pointPlusTwo->next->next;
		if (pointPlusOne == pointPlusTwo)
			return (1);
	}
	return (0);
}
