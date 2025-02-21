import 'dart:io';

void main() {
  stdout.write("Ingrese la contrasena: ");
  String contrasena = stdin.readLineSync()!;
  var errores = [];
  if (contrasena.length < 8) {
    errores.add("La contrasena debe tener al menos 8 caracteres");
  }

  if (!contrasena.contains("#") || !contrasena.contains("*") || !contrasena.contains("!")) {
    errores.add("La contrasena debe contener al menos un #, un * y un !");
  }

  if (!contrasena.contains(RegExp(r'[A-Z]'))) {
    errores.add("La contrasena debe contener al menos una letra mayuscula");
  }

  if (errores.isNotEmpty) {
    print("Errores en la contrasena:");
    for (var error in errores) {
      print("- $error");
    }
    return;
  }
  print("La contrasena es $contrasena");
}
