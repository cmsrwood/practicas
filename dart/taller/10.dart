import 'dart:io';

void main() {
  stdout.write("Ingrese su IMC: ");
  double? imc = double.parse(stdin.readLineSync()!);
  if (imc < 18.5) {
    print("Usted esta por debajo del peso ideal");
  } else if (imc > 18.5 && imc < 25) {
    print("Usted tiene un peso ideal");
  } else if (imc > 25 && imc < 30) {
    print("Usted tiene sobrepeso");
  } else if (imc > 30) {
    print("Usted tiene obesidad");
  }
}
