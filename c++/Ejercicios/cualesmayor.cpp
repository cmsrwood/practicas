#include<iostream>

using namespace std;

int main(){

    int a,b;
    cout<<"Ingrese el valor de a: ";
    cin>>a;
    cout<<"Ingrese el valor de b: ";
    cin>>b;

    if (a == b) {
        cout<<"Es el mismo numero ._.";
    }
    else if (a>b) {
        cout<<a<<" es el numero mayor";
    }
    else{
        cout<<b<<" es el numero mayor";
    }

    return 0;
}
