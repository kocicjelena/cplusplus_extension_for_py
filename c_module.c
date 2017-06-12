#include <Python.h>
#include <stdio.h>


static PyObject* c_module_calc_stat(PyObject *self, PyObject *args)
{
	 int a;   int b;
   if (!PyArg_ParseTuple(args, "ii", &a, &b)) {      
   return NULL;   }   
   return Py_BuildValue("ii", a + b, a - b); 
}
static PyObject* c_module_module_func(PyObject *self, PyObject *args) {}   
static PyMethodDef c_module_methods[] = { 
    {   
        "calc_stat",
        c_module_calc_stat,
        METH_NOARGS,
        "calculation and returns in a C extension."
    },
 { "func", c_module_module_func, METH_VARARGS, NULL },	
    {NULL, NULL, 0, NULL}
};
static struct PyModuleDef c_module_definition = { 
    PyModuleDef_HEAD_INIT,
    "c_module",
    "implement getting return in C code",
    -1, 
    c_module_methods
};

PyMODINIT_FUNC PyInit_c_module(void){
    Py_Initialize();

    return PyModule_Create(&c_module_calc_stat);
}
