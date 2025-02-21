import 'dart:io';

void main() {
  stdout.write("Ingrese la hora: ");
  int hora = int.parse(stdin.readLineSync()!);

  while (hora < 0 || hora > 24) {
    print("Hora no valida");
    stdout.write("Ingrese la hora: ");
    hora = int.parse(stdin.readLineSync()!);
  }

  int horaInicio = 8;
  int horaFin = 16;

  if (hora >= horaInicio && hora <= horaFin) {
    print("La hora corresponde al horario laboral");
  } else {
    print("La hora NO corresponde al horario laboral");
  }
}
