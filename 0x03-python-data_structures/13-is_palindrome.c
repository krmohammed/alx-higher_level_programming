#include "lists.h"

/**
 * is_palindrome - checks is a singly linked list is a palindrome
 * head: pointer to head node
 *
 * Return: 1 if palindrome, 0 otherwise
 *
 */

int is_palindrome(listint_t **head)
{
	listint_t *faster = *head, *slower = *head;
	int first_half[1024], itr = 0;

	if (*head == NULL)
		return (1);

	while (faster && faster->next)
	{
		first_half[itr++] = slower->n;
		faster = faster->next->next;
		slower = slower->next;
	}

	if (faster)
		slower = slower->next;


	while (slower)
	{
		if (first_half[--itr] != slower->n)
			return (0);
		slower = slower->next;
	}

	return (1);
}
