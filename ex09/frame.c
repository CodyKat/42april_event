#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct s_string
{
	char *string;
	struct s_string *next;
}	t_string;

t_string *lst_add_last(t_string **lst, t_string *new)
{
	t_string *tmp;

	if (*lst == 0)
		*lst = new;
	else
	{
		tmp = *lst;
		while (tmp->next)
			tmp = tmp->next;
		tmp->next = new;
	}
	return new;
}

t_string *new_lstnode(char *str)
{
	t_string *new;

	new = (t_string *)malloc(sizeof(t_string));
	new->string = str;
	new->next = NULL;
	return (new);
}

int	main(int argc, char **argv)
{
	int max_length = 0;
	int length;
	t_string *lst_string = 0;
	t_string *tmp_lst_string;
	char *cur_str;

	if (argc == 1)
		return 0;
	for (int i = 0; i < argc - 1; i++)
	{
		cur_str = strtok(argv[i + 1], " ");
		while (1)
		{
			if (cur_str == 0)
			{
				break;
			}
			if (lst_add_last(&lst_string, new_lstnode(cur_str)) == 0)
			{
				dprintf(2, "Error: malloc failed");
				exit(1);
			}
			cur_str = strtok(0, " ");
		}
	};
	tmp_lst_string = lst_string;
	while (tmp_lst_string)
	{
		length = strlen(tmp_lst_string->string);
		if (length > max_length)
			max_length = length;
		tmp_lst_string = tmp_lst_string->next;
	}

	for (int i = 0; i < max_length + 4; i++)
		printf("*");
	printf("\n");

	tmp_lst_string = lst_string;
	while (tmp_lst_string)
	{
		printf("* %s", tmp_lst_string->string);
		for (int i = 0; i < max_length - strlen(tmp_lst_string->string); i++)
			printf(" ");
		printf(" *\n");
		tmp_lst_string = tmp_lst_string->next;
	}

	for (int i = 0; i < max_length + 4; i++)
		printf("*");
	printf("\n");
}
