#include <iostream>
#include <iomanip> // Input-output-manipulation

using namespace std;

int main() {
	// Tipos de datos en C++
	
	// Tipo entero
	int entero = 10;
	cout << "Entero: " << entero << endl;
	// Tipo flotante
	float flotante = 8.9;
	cout << fixed << setprecision(2);
	cout << "Flotante: " << flotante << endl;
	// Tipo double
	double doble = 9.9999;
	cout << "Doble: " << doble << endl;
	// Tipo char
	char caracter = 'A';
	cout << "Caracter: " << caracter << endl;
	char caracterDecimal = 65; // A - Ascii
	cout << "Caracter en Decimal: " << caracterDecimal << endl;
	// Tipo bool
	bool boleano = false; //true - 1, false - 0
	cout << "Boleano: " << boleano << endl;
	
	return 0;
}

