import 'dart:io';

void main() {
  stdout.write("Ingrese el precio: ");
  double precio = double.parse(stdin.readLineSync()!);

  stdout.write("Ingrese el descuento: ");
  double descuento = double.parse(stdin.readLineSync()!);

  double valorDescuento = descuento / 100;

  double precioFinal = precio - (precio * valorDescuento);

  print("El precio final es: $precioFinal");
  print("El valor del descuento es: $descuento");
}
