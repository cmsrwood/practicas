import 'dart:io';
import 'dart:math';

void main() {

  int inicio = 1;
  int fin = 9;
  
  var rifa = Random().nextInt(fin) + 1;

  print ("Bienvenido al juego de la rifa");

  stdout.write("Adivine el número de la rifa: ");
  int respuesta = int.parse(stdin.readLineSync()!);

  while (respuesta < inicio || respuesta >= 9) {
    print("Por favor, ingresa un número válido.\nRecuerda que el número debe estar entre ${inicio} y ${fin}.");
    stdout.write("Adivine el número de la rifa: ");
    respuesta = int.parse(stdin.readLineSync()!);
  }

  if ((respuesta) == rifa) {
    print("¡Ganaste, el número ganador es ${rifa}!");
  } else if (respuesta > rifa) {
    print ("Numero ganador: ${rifa}");
    print("Perdiste el numero ganador es menor al jugado (${respuesta})");
  } else if (respuesta < rifa) {
    print("Numero ganador: ${rifa}");
    print("Perdiste el numero ganador es mayor al jugado (${respuesta})");
  }
}
