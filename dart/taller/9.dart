import 'dart:io';

void main() {
  stdout.write("Ingrese el numero: ");
  int numero = int.parse(stdin.readLineSync()!);

  if (numero % 2 == 0) {
    print("El número es par");
  } else {
    print("El número es impar");
  }
}
