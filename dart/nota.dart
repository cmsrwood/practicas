import 'dart:io';

void main() {
  stdout.write("Ingrese su nota: ");
  double? nota = double.parse(stdin.readLineSync()!);

  var mensaje = "";
  if (nota >= 0 && nota <= 20) {
    mensaje = "${nota}:Deficiente";
  }
  else if (nota >= 21 && nota <= 29) {
    mensaje = "${nota}:Bajo";
  }
  else if (nota >= 30 && nota <= 38) {
    mensaje = "${nota}: Bueno";
  }
  else if (nota >= 39 && nota <= 50) {
    mensaje = "${nota}: Superior";
  }
  else {
    mensaje = "Error, el valor de la nota debe estar entre 0 y 50\nValor registrado: $nota";
  }
  print(mensaje);
}
