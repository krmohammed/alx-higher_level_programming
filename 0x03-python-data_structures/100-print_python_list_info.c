#include <Python.h>
#include <stdio.h>

/**
 * print_python_list_info - prints basic info about python lists
 * @p: pointer to python object
 *
 */

void print_python_list_info(PyObject *p)
{
	int size, allocated, k;
	PyObject *item;

	if (!PyList_Check(p))
		return;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n",  allocated);

	for (k = 0; k < PyList_Size(p); k++)
	{
		item = PyList_GetItem(p, k);
		printf("Element %d: %s\n", k, Py_TYPE(item)->tp_name);
	}
}
