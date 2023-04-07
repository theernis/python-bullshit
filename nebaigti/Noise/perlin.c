#include <Python.h>
#include <Math.h>


//how detailed noise will be
//if set to 0 or negative number it will crash the program because of not stopping while loop
float detail = .125;

//how strong overlay be compared to previous layer overlay strength
//if set to 1 it will crash the program because of not stopping while loop
float overlay_strength = .875;

//how many times bigger scale will be compared to previous layer size
//recommended to keep it > 1 to make each layer smaller, but it doesnt crash if its = < 1
float overlay_size = 2;

static float changeVar(float var) {
    int a = (int)var;
    float b = var - a;

    return sinf(a + ((b != 0) ? 1 / b : 1));
}

static void setSeed(float x, float y, float z, float n) {
    float x1 = changeVar((x + n) / ((y * z != 0) ? y * z : detail));
    float y1 = changeVar((y + n) / ((z * x != 0) ? z * x : detail));
    float z1 = changeVar((z + n) / ((x * y != 0) ? x * y : detail));

    PyObject* tuple = Py_BuildValue("(i i i)", x1, y1, z1);
    srand(PyObject_Hash(tuple));
    Py_DECREF(tuple);
}

static PyObject*
getGrayscale(PyObject* self, PyObject* args) {
    float x, y, z;
    if (!PyArg_ParseTuple(args, "fff", &x, &y, &z)) {
        return NULL;
    }

    float final_n = 0;

    float strength = 1;
    float i = 0;
    while (1) {
        float n[8];
        for (int x1 = 0; x1 < 2; x1++) {
            for (int y1 = 0; y1 < 2; y1++) {
                for (int z1 = 0; z1 < 2; z1++) {
                    float x2 = floorf(x + x1);
                    float y2 = floorf(y + y1);
                    float z2 = floorf(z + z1);
                    setSeed(x2, y2, z2, strength);
                    n[z1 + y1 * 2 + x1 * 4] = ((float)rand() / RAND_MAX);
                }
            }
        }

        float n1[4];
        for (int x3 = 0; x3 < 4; x3++) {
            n1[x3] = ((1 - (x - (int)x)) * n[x3] + (x - (int)x) * n[x3 + 4]);
        }

        float n2[2];
        for (int y3 = 0; y3 < 2; y3++) {
            n2[y3] = ((1 - (y - (int)y)) * n1[y3] + (y - (int)y) * n1[y3 + 2]);
        }

        float n3 = (1 - (z - (int)z)) * n2[0] + (z - (int)z) * n2[1];

        final_n += n3 * strength;

        i += strength;
        strength *= overlay_strength;
        x *= overlay_size;
        y *= overlay_size;
        z *= overlay_size;

        if (min(detail, 1/detail) > min(strength, 1/strength)) {
            break;
        }
    }

    final_n /= i;
    return Py_BuildValue("(f f f)", final_n * 255, final_n * 255, final_n * 255);
}

static PyObject*
getColor(PyObject* self, PyObject* args) {
    float x, y, z;
    if (!PyArg_ParseTuple(args, "fff", &x, &y, &z)) {
        return NULL;
    }

    float final_r = 0;
    float final_g = 0;
    float final_b = 0;

    float strength = 1;
    float i = 0;
    while (1) {
        float r[8];
        float g[8];
        float b[8];
        for (int x1 = 0; x1 < 2; x1++) {
            for (int y1 = 0; y1 < 2; y1++) {
                for (int z1 = 0; z1 < 2; z1++) {
                    float x2 = floorf(x + x1);
                    float y2 = floorf(y + y1);
                    float z2 = floorf(z + z1);
                    setSeed(x2, y2, z2, strength);
                    r[z1 + y1 * 2 + x1 * 4] = ((float)rand() / RAND_MAX);
                    g[z1 + y1 * 2 + x1 * 4] = ((float)rand() / RAND_MAX);
                    b[z1 + y1 * 2 + x1 * 4] = ((float)rand() / RAND_MAX);
                }
            }
        }

        float r1[4];
        float g1[4];
        float b1[4];
        for (int x3 = 0; x3 < 4; x3++) {
            r1[x3] = ((1 - (x - (int)x))* r[x3] + (x - (int)x) * r[x3 + 4]);
            b1[x3] = ((1 - (x - (int)x))* g[x3] + (x - (int)x) * g[x3 + 4]);
            g1[x3] = ((1 - (x - (int)x))* b[x3] + (x - (int)x) * b[x3 + 4]);
        }
        
        float r2[2];
        float g2[2];
        float b2[2];
        for (int y3 = 0; y3 < 2; y3++) {
            r2[y3] = ((1 - (y - (int)y))* r1[y3] + (y - (int)y) * r1[y3 + 2]);
            g2[y3] = ((1 - (y - (int)y))* g1[y3] + (y - (int)y) * g1[y3 + 2]);
            b2[y3] = ((1 - (y - (int)y))* b1[y3] + (y - (int)y) * b1[y3 + 2]);
        }
        
        float r3 = (1 - (z - (int)z)) * r2[0] + (z - (int)z) * r2[1];
        float g3 = (1 - (z - (int)z)) * g2[0] + (z - (int)z) * g2[1];
        float b3 = (1 - (z - (int)z)) * b2[0] + (z - (int)z) * b2[1];
    
        final_r += r3 * strength;
        final_g += g3 * strength;
        final_b += b3 * strength;

        i += strength;
        strength *= overlay_strength;
        x *= overlay_size;
        y *= overlay_size;
        z *= overlay_size;

        if (min(detail, 1/detail) > min(strength, 1/strength)) {
            break;
        }
    }
        
    final_r /= i;
    final_g /= i;
    final_b /= i;

    return Py_BuildValue("(f f f)", final_r * 255, final_g * 255, final_b * 255);
}

static PyMethodDef SomeMethods[] = {
    {"getGrayscale", getGrayscale, METH_VARARGS, NULL},
    {"getColor", getColor, METH_VARARGS, NULL},
    {NULL, NULL, 0, NULL}
};


static struct PyModuleDef perlin = {
    PyModuleDef_HEAD_INIT,
    "perlin",
    "Some lib",
    -1,
    SomeMethods
};


PyMODINIT_FUNC PyInit_perlin(void) {
    return PyModule_Create(&perlin);
}