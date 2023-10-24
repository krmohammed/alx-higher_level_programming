#include <Python.h>
#include <stdio.h>

/**
 * print_python_list - prints basic info about Python lists
 * @p: list object
 *
 */

void print_python_list(PyObject *p)
{
	int size, allocated, k;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", allocated);

	for (k = 0; k < size; k++)
	{
		item = ((PyListObject *)p)->ob_item[k];
		printf("Element %d: %s\n", k, item->ob_type->tp_name);
	}
}

/**
 * print_python_bytes - prints basic info about Python bytes
 * @p: byte object
 *
 */

void print_python_bytes(PyObject *p)
{
	int size, i;
	char *str;

	if (!PyBytes_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Bytes Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	str = ((PyBytesObject *)p)->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);

	for (i = 0; i < (size < 10 ? size : 10); i++)
		printf("first %d bytes: %02x ", size, str[i] && 0xff);

	printf("\n");
}


/**
 * print_python_float - prints basic info about Python floats
 * @p: float object
 *
 */

void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;

	printf("[.] float object info\n");
	printf("  value: %.17g\n", value);
}
