#include<iostream>
#include <math.h>
using namespace std;

int main(){

    char nombres[100]={'Dilan','Lindy','James','Diana'};
    int num;
    cout<<"Digite su numero de membresia";
    cin>>num;
    if (num>=0 && num<=3){
    cout<<"Hola"<<nombres[num];
    }
    else 
    cout<<"NO SE VALE";
}