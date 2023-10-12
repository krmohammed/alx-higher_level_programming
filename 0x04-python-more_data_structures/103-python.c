#include <stdio.h>
#include <Python.h>

/**
 * print_python_list - prints some basic info about Python list object
 * @p: list object
 *
 */
void print_python_list(PyObject *p)
{
	int i, size, allocated;
	PyObject *item;

	if (!PyList_Check(p))
		return;

	size = PyList_Size(p);
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (i = 0; i < size; i++)
	{
		item = ((PyListObject *)p)->ob_item[i];
		printf("Element %d: %s\n", i, ((PyTypeObject *)item)->tp_name);
	}
}


/**
 * print_python_bytes - prints some basic info about Python byte object
 * @p: bytes object
 *
 */
void print_python_bytes(PyObject *p)
{
	int i, size;
	char *str_rep = NULL;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("[ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	str_rep = PyBytes_AsString(p);
	printf("  size: %d\n", size);
	prinf("  trying string: %s\n", str_rep);

	printf("  first %d bytes:", size > 10 ? 10 : size + 1);
	for (i = 0; i <= size && i < 10; i++)
		printf(" %02x", str_rep[i]);
	prinf("\n");
}
