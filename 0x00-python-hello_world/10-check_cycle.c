#include <stdio.h>
#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - checks singly lists
 * @list: sinh=gly lists
 *
 * Return: 0
 */
int check_cycle(listint_t *list)
{
	listint_t *first, *second;

	if (list == NULL || list->next == NULL)
		return (0);

	first = list->next;
	second = list->next->next;

	while (first && second && second->next)
	{
		if (first == second)
			return (1);

		first = first->next;
		second = second->next->next;
	}
	return (0);
}
