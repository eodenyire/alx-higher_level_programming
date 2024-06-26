#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * String information printer.
 * print_python_string - Prints string information.
 *
 * This function prints information about a Python string object.
 *
 * @p: Python Object - The string object to print information about.
 * Return: No return value.
 */
void print_python_string(PyObject *p)
{

	PyObject *str, *repr;

	(void)repr;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");

	repr = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(str));
}

