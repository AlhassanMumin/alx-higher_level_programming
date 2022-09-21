#include "lists.h"
#include <stdlib.h>
/**
 * insert_node - the function to insert a number at a positon
 *
 * @head: the pointer to the first node in the list
 * @number: the number that is to be inserted
 *
 * Return: the address of the newly created node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *cur = *head, *temp = NULL;

	temp = malloc(sizeof(listint_t));
	if (temp == NULL)
		return (NULL);
	temp->n = number;
	if (*head == NULL)
	{
		temp->next = *head;
		*head = temp;
	}
	else
	{
		while (cur->next != NULL)
		{
			if (cur->n == 4)
			{
				temp->next = cur->next;
				cur->next = temp;
				return (temp);
			}
			cur = cur->next;
		}
	}
	temp->next = NULL;
	cur->next = temp;
	return (temp);
}
