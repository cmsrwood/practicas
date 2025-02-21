import 'dart:io';

void main() {
  stdout.write("Ingrese su edad: ");
  int edad = int.parse(stdin.readLineSync()!);
  while (edad < 0) {
    print("La edad no puede ser negativa");
    stdout.write("Ingrese su edad: ");
    edad = int.parse(stdin.readLineSync()!);
  }

  String clasificacion = "";

  if (edad <= 12) {
    clasificacion = "Niño";
  } else if (edad >= 13 && edad <= 17) {
    clasificacion = "Adolescente";
  } else if (edad >= 18 || edad <= 64) {
    clasificacion = "Adulto";
  } else {
    clasificacion = "Anciano";
  }

  print("Su clasificación es: $clasificacion");
}
