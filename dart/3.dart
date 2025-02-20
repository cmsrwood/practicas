import 'dart:io';

void main() {
  String menu = "Seleccione una de las siguientes opciones\n1.String a Int\n2.Int a String\n3.Double a String\n4.String a Double\nSu opción es: ";
  print(menu);
  int? opcion = int.parse(stdin.readLineSync()!);

  if (opcion == 1) {
    int a = 10;
    String b = "20";
    String convertido = a.toString();
    String resultado = convertido + b;
    print("El resultado convirtiendo Int a String es: $resultado");
  } else if (opcion == 2) {
    int a = 10;
    String b = "20";
    int convertido = int.parse(b);
    int resultado = a + convertido;
    print("El resultado conviertiendo String a Int es: $resultado");
  } else if (opcion == 3) {
    String num3 = "5.9";
    double num4 = 3.5;
    String convertido = num4.toString();
    String resultado = num3 + convertido;
    print("El resultado convirtiendo double a String es: $resultado");
  } else if (opcion == 4) {
    String num3 = "5.9";
    double num4 = 3.5;
    double convertido = double.parse(num3);
    double resultado = convertido + num4;
    print("El resultado convirtiendo String a double es: $resultado");
  }
  while (opcion != 1 && opcion != 2 && opcion != 3 && opcion != 4) {
    print("Opción inválida");
    print(menu);
    opcion = int.parse(stdin.readLineSync()!);
  }
}