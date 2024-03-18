package busquedanumero;

import javax.swing.JOptionPane;

public class BusquedaNumero {

    public static boolean buscarNumero(int[] array, int numero) {
        for (int i = 0; i < array.length; i++) {
            if (array[i] == numero) {
                return true;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        String sizeInput = JOptionPane.showInputDialog(null, "Ingrese el tamaño del array:");
        int tamañoArray = Integer.parseInt(sizeInput);

        int[] numeros = new int[tamañoArray];

        for (int i = 0; i < tamañoArray; i++) {
            String valorInput = JOptionPane.showInputDialog(null, "Ingrese el valor para el índice " + i + ":");
            numeros[i] = Integer.parseInt(valorInput);
        }

        String input = JOptionPane.showInputDialog(null, "Ingrese un número entero a buscar:");
        int numeroBuscado = Integer.parseInt(input);

        boolean encontrado = buscarNumero(numeros, numeroBuscado);

        if (encontrado) {
            JOptionPane.showMessageDialog(null, "El número " + numeroBuscado + " se encuentra en el array.");
        } else {
            JOptionPane.showMessageDialog(null, "El número " + numeroBuscado + " no se encuentra en el array.");
        }
    }
}
