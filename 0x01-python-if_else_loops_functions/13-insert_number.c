#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - Inserts a number into a sorted singly linked list.
 * @head: Double pointer to the head
 * @number: New data
 * Return: listint_t*
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));
	listint_t *last = *head;

	new_node->n = number;
	if (new_node == NULL)
		return (NULL);
	new_node->n = number;

	if (last == NULL || last->n >= number)
	{
		new_node->next = last;
		*head = new_node;
		return (new_node);
	}
	while (last && last->next && last->next->n < number)
		last = last->next;

	new_node->next = last->next;
	last->next = new_node;

	return (new_node);
}
