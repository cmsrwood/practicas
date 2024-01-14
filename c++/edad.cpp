#include<iostream>
#include <math.h>
using namespace std;

int main(){

    char nombre [100];
    int edad, resultado;

    cout<<"Digite su nombre: ";
    cin>>nombre;
    cout<<"Digite su año de nacimiento: ";
    cin>>edad;
    
    resultado=2023-edad;
    cout<<"Hola "<<nombre<<" tu edad es: "<<resultado;
}