#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - displays information about a PyFloatObject
 * @p: the PyObject to examine
 */
void print_python_float(PyObject *p)
{
    double value = 0;
    char *string = NULL;

    fflush(stdout);
    printf("[.] float object info\n");

    // Check if the PyObject is a PyFloatObject
    if (!PyFloat_CheckExact(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    // Retrieve the value of the float object
    value = ((PyFloatObject *)p)->ob_fval;

    // Convert the float value to a string
    string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);

    // Print the value of the float object
    printf("  value: %s\n", string);
}

/**
 * print_python_bytes - prints information about a PyBytesObject
 * @p: the PyObject to examine
 */
void print_python_bytes(PyObject *p)
{
    Py_ssize_t size = 0, i = 0;
    char *string = NULL;

    fflush(stdout);
    printf("[.] bytes object info\n");

    // Check if the PyObject is a PyBytesObject
    if (!PyBytes_CheckExact(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    // Get the size of the bytes object
    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);

    // Get the string representation of the bytes object
    string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
    printf("  trying string: %s\n", string);

    // Print the first 10 bytes of the bytes object
    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
    while (i < size + 1 && i < 10)
    {
        printf(" %02hhx", string[i]);
        i++;
    }
    printf("\n");
}

/**
 * print_python_list - prints information about a PyListObject
 * @p: the PyObject to examine
 */
void print_python_list(PyObject *p)
{
    Py_ssize_t size = 0;
    PyObject *item;
    int i = 0;

    fflush(stdout);
    printf("[*] Python list info\n");

    // Check if the PyObject is a PyListObject
    if (PyList_CheckExact(p))
    {
        // Get the size of the list
        size = PyList_GET_SIZE(p);
        printf("[*] Size of the Python List = %zd\n", size);
        printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

        // Iterate over the elements of the list
        while (i < size)
        {
            // Get the i-th item from the list
            item = PyList_GET_ITEM(p, i);
            printf("Element %d: %s\n", i, item->ob_type->tp_name);

            // Print information about the item based on its type
            if (PyBytes_Check(item))
                print_python_bytes(item);
            else if (PyFloat_Check(item))
                print_python_float(item);

            i++;
        }
    }
    else
    {
        printf("  [ERROR] Invalid List Object\n");
    }
}

