#include "lists.h"
#include <stdio.h>
/**
 * listint_len - number of elements in a linked listint_t list.
 * @h: head of the linked list
 * Return: number of elements in a linked list
 */
size_t listint_len(const listint_t *h)
{
	const listint_t *current;
	int cont = 0;

	if (h == NULL)
		return (cont);
	current = h;
	while (current)
	{
		cont++;
		current = current->next;
	}
	return (cont);
}
/**
 * reverse - reverse a linked list
 * @head: head of the linked list
 * Return: Nothing
 */
void reverse(listint_t **head)
{

	listint_t *next = NULL, *current = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = current;
		current = *head;
		*head = next;
	}
	*head = current;
}
/**
 * is_palindrome - checks if a singly linked list is a palindrome.
 * @head: head of the single linked list
 * Return: 0 if it is not a palindrome, 1 if it is a palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *node;
	int len = 0, index = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);
	len = listint_len(*head);
	node = *head;
	if (len % 2 == 0)
	{
		len = len / 2;
		len -= 1;
	}
	else
		len = len / 2;

	while (index <= len)
	{
		index++;
		node = node->next;
	}
	reverse(&node);
	while (node)
	{
		if (node->n != (*head)->n)
			return (0);
		(*head) = (*head)->next;
		node = node->next;
	}

	return (1);

}
