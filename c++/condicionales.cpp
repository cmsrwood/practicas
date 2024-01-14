#include<iostream>

using namespace std;

int main(){

	int numero, dato = 5;
	
    cout<<"Digite el numero: ";
    cin>>numero;
    if (numero == dato){
    cout<<"Su numero es 5"<<endl;
    }
    else {
    cout<<"Su numero es diferente de 5, obviamente xd"<<endl;
    }
    if (numero < dato){
    cout<<"Su numero es menor que 5";
    }
    else {
    cout<<"Su numero es mayor que 5";
    }
    return 0;
}
