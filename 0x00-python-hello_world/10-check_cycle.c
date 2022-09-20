#include "lists.h"
#include <stdlib.h>
/**
 * check_cycle - it checks whether or not a list has a cycle
 * @list: the list to check
 * Return: 1 if list has a cycle or 0 if it doesnt hace a cycle
 */
int check_cycle(listint_t *list)                                              
{                                                                                                     
	int ret;                   

	while (list)                                                           
	{                                                                     
		if (list->n == 1)                                             
			ret = 1;                                               
		else if (list->n == 0)                                       
			ret = 0;                                              
		list = list->next;                                 
	}                                                                                                 
	return (ret);
}
