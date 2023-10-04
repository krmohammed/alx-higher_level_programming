#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *temp, *ptr, *new;

	if (*head == NULL)
		return (NULL);
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

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
		temp->next = temp;
	}

	new->next = ptr->next;
	ptr->next = new;
	return (*head);
}
