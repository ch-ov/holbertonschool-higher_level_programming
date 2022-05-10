#include "lists.h"
/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Pointer to first element of the list.
 * Return: int
 */
int is_palindrome(listint_t **head)
{
	listint_t *copy;
	int arrayAux[2048], x = 0;
	int sizeList = 0, sizeDiv = 0;

	if (head == 0)
		return (1);
	copy = *head;

	while (copy)
	{
		arrayAux[sizeList] = copy->n;
		copy = copy->next;
		sizeList++;
	}

	sizeList--;
	sizeDiv = sizeList / 2;
	while (x <= sizeDiv)
	{
		if (arrayAux[x] != arrayAux[sizeList])
			return (0);
		x++;
		sizeList--;
	}
	return (1);
}
