import 'dart:io';

void main() {
  stdout.write("Ingrese el 1er número: ");
  int num1 = int.parse(stdin.readLineSync()!);

  stdout.write("Ingrese el 2do número: ");
  int num2 = int.parse(stdin.readLineSync()!);

  bool esDivisible = num1 % num2 == 0;
  if (esDivisible) {
    print("$num1 es divisible por $num2");
  } else {
    print("$num1 no es divisible por $num2");
  }
}
