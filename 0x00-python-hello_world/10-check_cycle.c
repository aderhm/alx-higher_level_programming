#include "lists.h"

/**
 * check_cycle - checks if a singly linked list has a cycle in it.
 * @list: pointer to head of list
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
	const listint_t *list1;
	const listint_t *list2;

	list1 = list;
	list2 = list;
	while (list2 != NULL && list2->next != NULL)
	{
		list1 = list1->next;
		list2 = list2->next->next;

		if (list1 == list2)
			return (1);
	}

	return (0);
}
