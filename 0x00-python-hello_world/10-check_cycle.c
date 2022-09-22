#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle - it checks whether or not a list has a cycle
 * @list: the list to check
 * Return: 1 if list has a cycle or 0 if it doesnt hace a cycle
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
        listint_t *fast = list;

	while (fast != NULL && fast->next != NULL)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}
	return (0);
}
