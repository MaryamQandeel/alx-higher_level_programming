#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - print python list info
 *
 * @p: some description
 */

void print_python_list_info(PyObject *p)
{
	long int size = PyList_Size(p);
	int j;
	PyListObject *obj = (PyListObject *)p;

	printf("[*] Size of the Python List = %li\n", size);
	printf("[*] Allocated = %li\n", obj->allocated);
	for (j = 0; j < size; j++)
		printf("Element %d: %s\n", j, Py_TYPE(obj->ob_item[j])->tp_name);
}
