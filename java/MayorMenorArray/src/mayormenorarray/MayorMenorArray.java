package mayormenorarray;

import javax.swing.JOptionPane;

public class MayorMenorArray {

    public static void main(String[] args) {
        int tamaño = obtenerTamañoArray();
        int[] array = new int[tamaño];
        llenarArray(array);
        int mayor = encontrarMayor(array);
        int menor = encontrarMenor(array);
        mostrarResultado(mayor, menor);
    }
    public static int obtenerTamañoArray() {
        String input = JOptionPane.showInputDialog("Ingrese el tamaño del array:");
        return Integer.parseInt(input);
    }
    public static void llenarArray(int[] array) {
        for (int i = 0; i < array.length; i++) {
            String input = JOptionPane.showInputDialog("Ingrese el número en la posición " + (i+1) + ":");
            array[i] = Integer.parseInt(input);
        }
    }
    public static int encontrarMayor(int[] array) {
        int mayor = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] > mayor) {
                mayor = array[i];
            }
        }
        return mayor;
    }
    public static int encontrarMenor(int[] array) {
        int menor = array[0];
        for (int i = 1; i < array.length; i++) {
            if (array[i] < menor) {
                menor = array[i];
            }
        }
        return menor;
    }
    public static void mostrarResultado(int mayor, int menor) {
        JOptionPane.showMessageDialog(null, "El número mayor es: " + mayor + "\nEl número menor es: " + menor);
    }
}
