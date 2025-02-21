import 'dart:io';

void main() {
  stdout.write("Ingrese la nota del examen: ");

  int nota = int.parse(stdin.readLineSync()!);

  if (nota >= 30) {
    print("El alumno aprobó con $nota");
  } else {
    print("El alumno reprobó con $nota");
  }
}
