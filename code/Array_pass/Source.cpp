// #include <iostream>
using namespace std;
__declspec(dllexport) double _stdcall
cp(double * x, int size) {

	double sum = 0.0;

	for (int i = 0; i < size; i++) {
		sum += x[i];
	}

	// cout << sum << " done!" << endl;

	return sum;
}