import 'dart:io';

void main() {
  print("Ingrese el nombre: ");
  String nombre = stdin.readLineSync()!;

  String nombre_mayuscula = nombre.toUpperCase();
  String nombre_minuscula = nombre.toLowerCase();

  int? tamano_de_cadena = nombre.length;
  if (tamano_de_cadena < 1) {
    print("El nombre está vacío");
  }
  print("Ingrese la posición: ");
  int? posicion = int.parse(stdin.readLineSync()!);
  if (posicion > tamano_de_cadena) {
    print("La posición ingresada es mayor al tamaño de la cadena");
  }
  if (posicion < 1) {
    print("La posición ingresada es menor a 1");
  }
  String letra_cadena = nombre[posicion - 1].toUpperCase();
  print("El nombre en mayúsculas es: $nombre_mayuscula");
  print("El nombre en minúsculas es: $nombre_minuscula");
  print(
    "La letra en la posición $posicion del nombre ${nombre} es: $letra_cadena",
  );
}
