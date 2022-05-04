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
	/* 1. allocate node */
	listint_t *new_node = (listint_t *)malloc(sizeof(listint_t));

	listint_t *last = *head; /* used in step 5*/

	/* 2. put in the data  */
	new_node->n = number;

	/* 3. This new node is going to be the last node, so make next of it as NULL*/
	new_node->next = NULL;

	/* 4. If the Linked List is empty, then make the new node as head */
	if (*head == NULL)
	{
		*head = new_node;
		return (new_node);
	}

	/* 5. Else traverse till the last node */
	while (last && last->next && last->next->n < number)
		last = last->next;

	/* 6. Change the next of last node */
	new_node->next = new_node->next
	last->next = new_node;
	return (new_node);
}
