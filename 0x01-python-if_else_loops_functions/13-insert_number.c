#include "lists.h"
/**
 * insert_node - inserts a number into a sorted singly linked list.
 * @head: head of the list
 * @number: value to insert in the new node
 * Return: address of the new node
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_n = *head;
	listint_t *ret;
	unsigned int cont = 0;

	if (head == NULL)
		return (NULL);
	while (new_n)
	{
		if (new_n->n >= number)
		{
			ret = insert_nodeint_at_index(head, cont, number);
			if (ret == NULL)
				return (NULL);
			return (ret);
		}
		else if (new_n->next == NULL)
		{
			cont++;
			ret = insert_nodeint_at_index(head, cont, number);
			if (ret == NULL)
				return (NULL);
			return (ret);
		}
		cont++;
		new_n = new_n->next;
	}
	return (NULL);
}
/**
  * insert_nodeint_at_index - insert a new node at a given position
  * @head: head of the list
  * @idx: index of the list where the new node should be added
  * @n: data for the newn node
  * Return: the address of the new node
  */
listint_t *insert_nodeint_at_index(listint_t **head, unsigned int idx, int n)
{
	listint_t *new, *current;
	unsigned int cont = 0;

	current = *head;
	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = n;
	if (idx == 0)
	{
		new->next = *head;
		*head = new;
		return (*head);
	}
	while (current)
	{
		if (cont == (idx - 1))
		{
			new->next = current->next;
			current->next = new;
			return (new);
		}
		cont++;
		current = current->next;
	}
	return (NULL);
}
