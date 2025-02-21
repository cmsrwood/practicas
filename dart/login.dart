import 'dart:io';

void main() {
  const user = "jose";
  const pass = "123456789";
  stdout.write("Ingrese su user: ");
  String? userin = stdin.readLineSync();
  stdout.write("Ingrese su contraseña: ");
  String? password = stdin.readLineSync();


  if (password!.length < 8) {
    print("La contraseña debe tener al menos 8 caracteres");
  }

  if (userin == user && password == pass) {
    print("Acceso concedido");
  } else {
    print("Acceso denegado");
  }
}