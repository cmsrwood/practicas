import 'dart:io';

void main() {
  stdout.write("Ingrese el 1er número: ");
  int num1 = int.parse(stdin.readLineSync()!);
  stdout.write("Ingrese el 2do número: ");
  int num2 = int.parse(stdin.readLineSync()!);

  int resultado = 0;

  for (int i = 1; i <= num1; i++) {
    resultado += num2;
    print("$num2 x $i = ${resultado}");
  }
  print ("El resultado es: $resultado");
}
