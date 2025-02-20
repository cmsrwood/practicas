import 'dart:io';

int menu() {
  print(
    "Opciones:\n1. Sumar\n2. Multiplicar\n3. Dividir\n4. Restar\n5. Salir\nTu opción es: ",
  );
  int? opcion = int.parse(stdin.readLineSync()!);
  return opcion;
}

void main() {
  print("Bienvenido a la calculadora\n");
  int opcion = menu();
  //Solicitar datos al usuario
  while (opcion != 5) {
    switch (opcion) {
      case 1:
        print("-----------Sumar-----------");
        print("Ingrese el primer número: ");
        int? num1 = int.parse(stdin.readLineSync()!);
        print("Ingrese el segundo número: ");
        int? num2 = int.parse(stdin.readLineSync()!);
        int? suma = num1 + num2;
        print("La suma de $num1 y $num2 es: $suma");
        print("¿Desea continuar? (Y/N): ");
        String? continuar = stdin.readLineSync();
        while (continuar != "N" &&
            continuar != "n" &&
            continuar != "Y" &&
            continuar != "y") {
          print("Opción inválida. Por favor, ingrese 'Y' o 'N': ");
          continuar = stdin.readLineSync();
        }
        if (continuar == "N" || continuar == "n") {
          opcion = 5;
          print("Gracias por usar la calculadora");
          break;
        } else if (continuar == "Y" || continuar == "y") {
          opcion = menu();
          break;
        }
      case 2:
        print("-----------Multiplicar-----------");
        print("Ingrese el primer número: ");
        int? num1 = int.parse(stdin.readLineSync()!);
        print("Ingrese el segundo número: ");
        int? num2 = int.parse(stdin.readLineSync()!);
        int? multiplicar = num1 * num2;
        print("La multiplicación de $num1 y $num2 es: $multiplicar");
        print("¿Desea continuar? (Y/N): ");
        String? continuar = stdin.readLineSync();
        while (continuar != "N" &&
            continuar != "n" &&
            continuar != "Y" &&
            continuar != "y") {
          print("Opción inválida. Por favor, ingrese 'Y' o 'N': ");
          continuar = stdin.readLineSync();
        }
        if (continuar == "N" || continuar == "n") {
          opcion = 5;
          print("Gracias por usar la calculadora");
          break;
        } else if (continuar == "Y" || continuar == "y") {
          opcion = menu();
          break;
        }
      case 3:
        print("-----------Dividir-----------");
        print("Ingrese el primer número: ");
        int? num1 = int.parse(stdin.readLineSync()!);
        print("Ingrese el segundo número: ");
        int? num2 = int.parse(stdin.readLineSync()!);
        double? dividir = num1 / num2;
        print("La división de $num1 y $num2 es: $dividir");
        print("¿Desea continuar? (Y/N): ");
        String? continuar = stdin.readLineSync();
        while (continuar != "N" &&
            continuar != "n" &&
            continuar != "Y" &&
            continuar != "y") {
          print("Opción inválida. Por favor, ingrese 'Y' o 'N': ");
          continuar = stdin.readLineSync();
        }
        if (continuar == "N" || continuar == "n") {
          opcion = 5;
          print ("Gracias por usar la calculadora");
          break;
        } else if (continuar == "Y" || continuar == "y") {
          opcion = menu();
          break;
        }
      case 4:
        print("-----------Restar-----------");
        print("Ingrese el primer número: ");
        int? num1 = int.parse(stdin.readLineSync()!);
        print("Ingrese el segundo número: ");
        int? num2 = int.parse(stdin.readLineSync()!);
        int? restar = num1 - num2;
        print("La resta de $num1 y $num2 es: $restar");
        print("¿Desea continuar? (Y/N): ");
        String? continuar = stdin.readLineSync();
        while (continuar != "N" &&
            continuar != "n" &&
            continuar != "Y" &&
            continuar != "y") {
          print("Opción inválida. Por favor, ingrese 'Y' o 'N': ");
          continuar = stdin.readLineSync();
        }
        if (continuar == "N" || continuar == "n") {
          opcion = 5;
          print("Gracias por usar la calculadora");
          break;
        } else if (continuar == "Y" || continuar == "y") {
          opcion = menu();
          break;
        }
      default:
        print("Opción inválida");
    }
  }
}
