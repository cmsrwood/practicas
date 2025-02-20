import 'dart:io';

void main() {
  stdout.write("Ingrese el nombre del estudiante: ");
  String? nombre_estudiante = stdin.readLineSync();

  stdout.write("Ingrese el titulo del libro: ");
  String? nombre_libro = stdin.readLineSync();

  stdout.write("Ingrese el numero de la pagina inicial: ");
  int pagina_inicial = int.parse(stdin.readLineSync()!);

  stdout.write("Ingrese el numero de la pagina final: ");
  int pagina_final = int.parse(stdin.readLineSync()!);

  int paginas = (pagina_final - pagina_inicial) + 1;

  int valor = 0;

  while (paginas <= 0) {
    print("Valor invalido de paginas. Digitelas de nuevo");
    stdout.write("Ingrese el numero de la pagina inicial: ");
    int pagina_inicial = int.parse(stdin.readLineSync()!);

    stdout.write("Ingrese el numero de la pagina final: ");
    int pagina_final = int.parse(stdin.readLineSync()!);

    paginas = (pagina_final - pagina_inicial) + 1;
  }

  if (paginas == 1) {
    valor = 100;
  }
  if (paginas > 1 && paginas <= 10) {
    valor = 80;
  }
  if (paginas > 10 && paginas <= 20) {
    valor = 50;
  }
  if (paginas > 20) {
    valor = 40;
  }

  int valor_final = paginas * valor;

  print(
    "${nombre_estudiante}, el valor de las fotocopias para el libro ${nombre_libro} de las paginas ${pagina_inicial}-${pagina_final} es de COP ${valor_final}, COP ${valor} por pagina (${paginas} paginas)",
  );
}
