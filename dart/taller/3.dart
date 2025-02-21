import 'dart:io';

void main() {
  stdout.write("Ingrese el hemisferio: ");
  String hemisferio = stdin.readLineSync()!;
  while (hemisferio.toLowerCase() != "norte" && hemisferio.toLowerCase() != "sur") {
    print("Hemisferio no valido");
    stdout.write("Ingrese el hemisferio: ");
    hemisferio = stdin.readLineSync()!;
  }
  print("Ingrese la fecha");
  stdout.write("Ingrese el mes: ");
  int mes = int.parse(stdin.readLineSync()!);
  while (mes < 1 || mes > 12) {
    print("Mes no valido");
    stdout.write("Ingrese el mes: ");
    mes = int.parse(stdin.readLineSync()!);
  }
  stdout.write("Ingrese el dia: ");
  int dia = int.parse(stdin.readLineSync()!);
  while (dia < 1 || dia > 31) {
    print("Dia no valido");
    stdout.write("Ingrese el dia: ");
    dia = int.parse(stdin.readLineSync()!);
  }

  String estacion = "";

  if (hemisferio.toLowerCase() == "norte") {
    if ((mes == 3 && dia >= 20) || (mes == 4) || (mes == 5) || (mes == 6 && dia <= 20)) {
      estacion = "Primavera";
    }
    else if ((mes == 6 && dia >= 20) || (mes == 7) || (mes == 8) || (mes == 9 && dia <= 20)) {
      estacion = "Verano";
    }
    else if ((mes == 9 && dia >= 20) || (mes == 10) || (mes == 11) || (mes == 12 && dia <= 20)) {
      estacion = "Otonio";
    }
    else {
      estacion = "Invierno";
    }
  }
  else if (hemisferio.toLowerCase() == "sur") {
    if ((mes == 3 && dia >= 20) || (mes == 4) || (mes == 5) || (mes == 6 && dia <= 20)) {
      estacion = "Otonio";
    }
    else if ((mes == 6 && dia >= 20) || (mes == 7) || (mes == 8) || (mes == 9 && dia <= 20)) {
      estacion = "Invierno";
    }
    else if ((mes == 9 && dia >= 20) || (mes == 10) || (mes == 11) || (mes == 12 && dia <= 20)) {
      estacion = "Primavera";
    }
    else {
      estacion = "Verano";
    }
  }
  print("La estacion es: $estacion");
}