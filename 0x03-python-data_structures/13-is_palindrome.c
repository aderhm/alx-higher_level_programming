#include "lists.h"
#include <stdlib.h>

listint_t *reverseLinkedList(listint_t *head);

/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: pointer to pointer of first node of listint_t list.
 *
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *reachmdl, *reachend, *mdltracker, *second_half;
	int isPalindrome;

	if ((*head) == NULL || (*head)->next == NULL)
		return (1);

	reachmdl = reachend = mdltracker = *head;
	isPalindrome = 1;

	while (reachend != NULL && reachend->next != NULL)
	{
		reachend = reachend->next->next;
		mdltracker = reachmdl;
		reachmdl = reachmdl->next;
	}

	if (reachend != NULL)
		reachmdl = reachmdl->next;

	second_half = reverseLinkedList(reachmdl);

	while (second_half != NULL)
	{
		if ((*head)->n != second_half->n)
		{
			isPalindrome = 0;
			break;
		}
		(*head) = (*head)->next;
		second_half = second_half->next;
	}

	mdltracker->next = reverseLinkedList(second_half);

	return (isPalindrome);
}

/**
 * reverseLinkedList - reverse a sigly linked list.
 * @head: pointer to head of list.
 *
 * Return: the reversed list.
 */
listint_t *reverseLinkedList(listint_t *head)
{
	listint_t *prev;
	listint_t *current;
	listint_t *next;

	prev = NULL;
	current = head;
	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}

	return (prev);
}
