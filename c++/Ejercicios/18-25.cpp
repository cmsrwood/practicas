
#include<iostream>
#include <math.h>
using namespace std;

int main(){

    int edad;

    cout<<"Escriba su edad: ";
    cin>>edad;

    if (edad<1){
    cout<<"Su edad no es valida ";
    }
    else if (edad>= 18 && edad<=25)
    cout<<"Su edad se encuentra dentro del rango :D ";
    else
    cout<<"Su edad NO se encuentra dentro del rango ";
}
