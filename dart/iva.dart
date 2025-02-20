import 'dart:io';

void main() {
  const valorIva = 19;
  var iva = valorIva / 100;

  stdout.write("Ingrese su nombre: ");
  String? nombre = stdin.readLineSync();

  stdout.write("Ingrese su numero de documento: ");
  int documento = int.parse(stdin.readLineSync()!);

  stdout.write("Ingrese el precio del producto: ");
  double precio = double.parse(stdin.readLineSync()!);

  double precioConIva = precio + (precio * iva);

  double precioIva = precioConIva - precio;

  const valorDescuento = 10;

  var descuento = valorDescuento / 100;

  double precioFinal = precioConIva - (precioConIva * descuento);

  double precioDescuento = precioConIva * descuento;

  print("\nBienvenido $nombre\n");

  print("Número de documento: $documento");

  print("El precio del producto sin IVA es: $precio");

  print("El precio del producto con IVA es: $precioConIva");

  print("El valor del IVA es: $precioIva");

  print("El valor del descuento es: $precioDescuento");

  print("El total a pagar es: $precioFinal");
}
