#include<iostream>

using namespace std;

int main(){

	char nombre[100];
	char apellido[300];
	int numero;
	cin>>numero;
	cout<<numero;
    cout<<"Digite su nombre: ";
    cin>>nombre;
    cout<<"Digite su apellido: ";
    cin>>apellido;
    cout<<"Digite un numero: ";
    cout<<"Bienvenido "<< nombre<<' '<< apellido<<endl;
    return 0;
}
