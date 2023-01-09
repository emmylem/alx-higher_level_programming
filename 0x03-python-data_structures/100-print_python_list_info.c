#include <Python.h>

/**
 * print_python_list_info - prints info about python lists
 * @p: PyObject list
 */
void print_python_list_info(PyObject *p)
{
	int first, sec, x;
	PyObject *obj;

	first = Py_SIZE(p);
	sec = ((PyListObject *)p)->allocated;

	printf("[*] Size of Python List = %d\n", first);
	printf("[*] Allocated = %d\n", sec);

	for (x = 0; x < first; x++)
	{
		printf("Element %d:", x);

		obj = PyList_GetItem(p, x);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
