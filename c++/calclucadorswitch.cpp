#include<iostream>
#include <math.h>
using namespace std;

int main(){

    int  opcion = 0;
    while (opcion == 0){
    cout<<"-================================= MENU ================================= "<<endl;
    cout<<"Escoja una de las siguientes opciones:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\n5.Exponente"<<endl<<"Su opcion: ";
    cin>>opcion;

    switch (opcion)
    {
    case 1:
        int num1,num2,resultado;
        cout<<"--------------------------SUMA------------------------------ "<<endl;
        cout<<"Digite el 1er numero: ";
        cin>>num1; 
        cout<<"Digite el 2do numero: ";
        cin>>num2;
        resultado=num1+num2;
        cout<<"El resultado es: "<<resultado<<endl;
        cout<<"Si desea realizar otra operacion digite Y, si desea salir digite N"<<endl<<"Su opcion: ";
        char pregunta;
        cin>>pregunta;
        if (pregunta == 'Y'){
            opcion = 0;
        }
        else {
            opcion = 10;
            cout<<"Gracias por usar mi calculadora :)"<<endl;
        }
        break;

    case 2:
        cout<<"--------------------------RESTA------------------------------ "<<endl;
        cout<<"Digite el 1er numero: ";
        cin>>num1; 
        cout<<"Digite el 2do numero: ";
        cin>>num2;
        resultado=num1-num2;
        cout<<"El resultado es: "<<resultado<<endl;
        cout<<"Si desea realizar otra operacion digite Y, si desea salir digite N"<<endl<<"Su opcion: ";
        cin>>pregunta;
        if (pregunta == 'Y'){
            opcion = 0;
        }
        else {
            opcion = 10;
            cout<<"Gracias por usar mi calculadora :)"<<endl;
        }
        break;

    case 3:
        cout<<"--------------------------MULTIPLICACION------------------------------ "<<endl;
        cout<<"Digite el 1er numero: ";
        cin>>num1; 
        cout<<"Digite el 2do numero: ";
        cin>>num2;
        resultado=num1*num2;
        cout<<"El resultado es: "<<resultado<<endl;
        cout<<"Si desea realizar otra operacion digite Y, si desea salir digite N"<<endl<<"Su opcion: ";
        cin>>pregunta;
        if (pregunta == 'Y'){
            opcion = 0;
        }
        else {
            opcion = 10;
            cout<<"Gracias por usar mi calculadora :)"<<endl;
        }
        break;

    case 4:
        cout<<"--------------------------DIVISION------------------------------ "<<endl;
        cout<<"Digite el 1er numero: ";
        cin>>num1; 
        cout<<"Digite el 2do numero: ";
        cin>>num2;
        resultado=num1/num2;
        cout<<"El resultado es: "<<resultado<<endl;
        cout<<"Si desea realizar otra operacion digite Y, si desea salir digite N"<<endl<<"Su opcion: ";
        cin>>pregunta;
        if (pregunta == 'Y'){
            opcion = 0;
        }
        else {
            opcion = 10;
            cout<<"Gracias por usar mi calculadora :)"<<endl;
        }
        break;

    case 5:
        cout<<"-------------------------POTENCIA------------------------------ "<<endl;
        cout<<"Digite el 1er numero: ";
        cin>>num1; 
        cout<<"Digite el 2do numero: ";
        cin>>num2;
        resultado=pow(num1,num2);
        cout<<"El resultado es: "<<resultado<<endl;    
        cout<<"Si desea realizar otra operacion digite Y, si desea salir digite N"<<endl<<"Su opcion: ";
        cin>>pregunta;
        if (pregunta == 'Y'){
            opcion = 0;
        }
        else {
            opcion = 10;
            cout<<"Gracias por usar mi calculadora :)"<<endl;
        }
        break;
}
    }
    
}
