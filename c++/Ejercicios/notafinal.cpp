#include<iostream>

using namespace std;

int main(){

	float nota1;
	float nota2;
	float nota3;
	float nota4;
    float resultado;
    cout<<"Digite la 1ra nota: ";
    cin>>nota1;
    cout<<"Digite la 2da nota: ";
    cin>>nota2;
    cout<<"Digite la 3ra nota: ";
    cin>>nota3;
    cout<<"Digite la 4ta nota: ";
    cin>>nota4;
    resultado =(nota1+nota2+nota3+nota4)/4;
    cout<<"El promedio es de: "<<resultado;
    return 0;
}
