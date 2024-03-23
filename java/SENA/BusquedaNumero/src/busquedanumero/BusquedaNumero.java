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
        String tamaño = JOptionPane.showInputDialog(null, "Ingrese el tamaño del array:");
        int tamañoArray = Integer.parseInt(tamaño);

        int[] numeros = new int[tamañoArray];

        for (int i = 0; i < tamañoArray; i++) {
            String valor = JOptionPane.showInputDialog(null, "Ingrese el valor #" + (i+1) + ":");
            numeros[i] = Integer.parseInt(valor);
        }

        String input = JOptionPane.showInputDialog(null, "Ingrese el número buscar:");
        int numeroBuscado = Integer.parseInt(input);

        boolean encontrado = buscarNumero(numeros, numeroBuscado);

        if (encontrado) {
            JOptionPane.showMessageDialog(null, "El número " + numeroBuscado + " se encuentra en el array.");
        } else {
            JOptionPane.showMessageDialog(null, "El número " + numeroBuscado + " no se encuentra en el array.");
        }
    }
}
