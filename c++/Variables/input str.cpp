#include <iostream>

using namespace std;

int main() {
	// Introducir datos desde la consola
	
	// 1. Declarar variable
	int entero;
	// 2. Solicitar el valor de entrada
	cout << "Proporciona un numero: ";
	cin >> entero;
	// 3. Desplegamos el valor
	cout << "Valor proporcionado: " << entero << endl;
	
	// Introducir una cadena
	string nombre;
	// solicitamos el valor de la consola
	cout << "Proporciona tu nombre: " << endl;
	//cin >> nombre; // No lee la linea completa, sino hasta un espacio
	cin.ignore();// limpiar caracteres del buffer de la consola
	getline(cin, nombre);
	cout << "Nombre proporcionado: " << nombre;
	
	return 0;
}

