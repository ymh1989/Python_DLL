#define STRUC_API __declspec(dllexport)
 
typedef struct cor {
	double x, y;
}cor;


STRUC_API void _stdcall fill(cor *c, int num) {
	for (int i = 0; i < num; i++) {
		c[i].x = (double)i;
		c[i].y = (double)i + 1.2;
	}
}

STRUC_API void _stdcall sum(double * res, cor *c, int num) {
	for (int i = 0; i < num; i++) {
		res[i] = c[i].x + c[i].y;
	}
}