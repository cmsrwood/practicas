#include <iostream>
#include <iomanip> // Input-output-manipulation

using namespace std;

int main() {
	// Direccion Memoria de una Variable en C++
	
	// Tipo entero
	int entero = 10;
	cout << "Entero: " << entero << endl;
	// Direccion memoria de la variable
	cout << "Dir. memoria: " << &entero;
	
	return 0;
}

