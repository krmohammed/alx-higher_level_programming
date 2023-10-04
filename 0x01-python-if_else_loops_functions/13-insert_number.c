#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * insert_node - inserts a new node a the specified index
 * @head: pointer to the pointer of the head node
 * @number: node data
 *
 * Return: pointer to head node on success, NULL otherwise
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *ptr, *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	if (*head == NULL)
	{
		*head = new;
		return (*head);
	}
	temp = *head;
	if (temp->n > number)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}

	while (temp->n < number)
	{
		ptr = temp;

		if (temp->next == NULL)
		{
			temp->next = new;
			new->next = NULL;
			return (*head);
		}
		temp = temp->next;
	}

	new->next = ptr->next;
	ptr->next = new;
	return (*head);
}
