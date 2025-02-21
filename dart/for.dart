import 'dart:io';

void main() {
  var I = 0;
  var NI = 0;
  for (int i = 0; i < 10; i++) {
    if (i >= 5 && i <= 6) {
      print("$i");
      I++;
    }
    else {
      NI++;
    }
  }
  print("Total de impresos: $I");
  print("Total de no impresos: $NI");
}
