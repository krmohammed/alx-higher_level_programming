#include "lists.h"

/**
 * check_cycle - checks if a singly linked list is circular
 * @list: node of list
 *
 * Return: 1 if circular, 0 otherwise
 *
 */

int check_cycle(listint_t *list)
{
	listint_t *temp = list;

	if (list == NULL)
		return (0);

	do {
		temp = temp->next;
		if (temp == list)
			return (1);
	} while (temp);

	return (0);
}
