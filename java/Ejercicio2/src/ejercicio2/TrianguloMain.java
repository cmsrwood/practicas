package ejercicio2;
import javax.swing.*;
public class TrianguloMain {
    public static void main(String[] args) {
        double base=Double.parseDouble(JOptionPane.showInputDialog("Ingrese la base"));
        double altura=Double.parseDouble(JOptionPane.showInputDialog("Ingrese la altura"));
        Triangulo triangulo=new Triangulo(base,altura);
        triangulo.info();
    }
}
