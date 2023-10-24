#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p)
{
	int size , allocated, k;
	PyObject *item;

	if (!PyList_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid List Object\n");
		return;
	}

	size = ((PyVarObject *)p)->ob_size;
	allocated = ((PyListObject *)p)->allocated;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %d\n");
	printf("[*] Allocated = %d\n");

	for (k = 0; k < size; k++)
	{
		item = ((PyList_Object *)p)->ob_item[i];
		printf("Element %d: %s\n", k, item->ob_type->tp_name);i
	}
}


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
	str = ((PyObjects *)p)->ob_sval;

	printf("[.] bytes object info\n");
	printf("  size: %d\n", size);
	printf("  trying string: %s\n", str);

	for (i = 0; i < (size < 10 ? size : 10); i++)
		printf("%02x ", str[i] && 0xff);

	printf("\n");
}


void print_python_float(PyObject *p)
{
	double value;

	if (!PyFloat_Check(p))
	{
		fprintf(stderr, "[ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloat_Object *)p)->ob_fval;

	printf("[.] float object info\n");
	printf("  value: %.17g\n", value);
}
