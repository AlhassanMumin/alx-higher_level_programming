#include "lists.h"

/**
 * is_palindrome - it checks if a singly linkded list is palindrome
 * @head: the head pointer
 * Return: 1 if palindrome or 0 if not a palindrome
 */

int is_palindrome(listint_t **head)
{
	int indx = 0, len = 0, len_half = 0, i, *strlit = '\0';
	listint_t *tmp = *head;
	
	strlit = malloc(sizeof(listint_t));
	if (strlit == NULL)
		exit (1);


	while (tmp)
	{
		strlit[indx] = tmp->n;
		indx++;
		len++;
		tmp = tmp->next;
	}
	len_half = len / 2;
	if (len == 0)
		return (1);

	len -= 1;
	for (i = 0; i < len_half; i++, len--)
	{
		if (strlit[i] != strlit[len])
			return (0);
	}

	return (1);
}
