import 'dart:io';

void main() {
  stdout.write("Ingrese el valor de la longitud: ");
  double longitud = double.parse(stdin.readLineSync()!);

  while (longitud <= 0) {
    print("La longitud debe ser mayor a 0");
    stdout.write("Ingrese el valor de la longitud: ");
    longitud = double.parse(stdin.readLineSync()!);
  }

  stdout.write("Ingrese la medida de la longitud: ");
  String medida = stdin.readLineSync()!;

  while (medida != "cm" && medida != "m" && medida != "km" && medida != "mm" && medida != "dm" ) {
    print("La medida debe ser:\n - mm\n - cm\n - dm\n - m\n - km");
    stdout.write("Ingrese la medida de la longitud: ");
    medida = stdin.readLineSync()!;
  }


  print("La longitud es: $longitud $medida");
}
