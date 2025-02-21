import 'dart:io';

void main() {
  stdout.write("Ingrese la temperatura del agua en °C: ");

  double temperatura = double.parse(stdin.readLineSync()!);

  if (temperatura < 0) {
    print("El estado del agua es liquido");
  } else if (temperatura > 100) {
    print("El estado del agua es gas");
  } else {
    print("El estado del agua es sólido");
  }
}