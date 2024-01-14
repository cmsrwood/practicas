#include<iostream>

using namespace std;

int main(){

    int a;
    cout<<"Digite el numero: ";
    cin>>a;
    if (a == 0){
        cout<<"El numero es cero .-.";
    }
    else if (a%2==0){
        cout<<"Su numero es par ";
    }
    else {
        cout<<"Su numero es impar ";
    }
    return 0;
}
