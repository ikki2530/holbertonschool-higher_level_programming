#include <stdio.h>
#include "lists.h"

/**
 * check_cycle - Checks if exist a cycle in listint_t list
 * @list: list to check
 * Return: 1 if there is a cycle, 0 if there is no cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *list_one, *list_two;

	list_one = list;
	list_two = list;

	while (list_one && list_two && list_two->next)
	{
		list_one = list_one->next;
		list_two = list_two->next;
		list_two = list_two->next;
		if (list_one == list_two)
			return (1);
	}
	return (0);
}
