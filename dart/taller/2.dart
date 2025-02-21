import 'dart:io';

void main() {
  stdout.write("Ingrese el número: ");
  int num = int.parse(stdin.readLineSync()!);

  if (num >0 ) {
    print("El número es positivo");
  } else if (num < 0) {
    print("El número es negativo");
  } else {
    print("El número es cero");
  }
}