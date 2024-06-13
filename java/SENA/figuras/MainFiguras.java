package figuras;

import javax.swing.*;
public class MainFiguras {

    public static void main(String[] args) {
        int opcion=Integer.parseInt(JOptionPane.showInputDialog("Elija una de las siguientes opciones\n\n1.Circulo\n2.Cuadrado\n3.Rectangulo\n4.Rombo\n5.Trapecio\n6.Triangulo"));
        switch (opcion){
            case 1:
                Circulo circulo1=new Circulo(Integer.parseInt(JOptionPane.showInputDialog("Ingrese el radio")));
                JOptionPane.showMessageDialog(null, "El area es de: "+circulo1.calcularArea());
                JOptionPane.showMessageDialog(null, "El perimetro es de: "+circulo1.calcularPerimetro());
                break;
            case 2:
                Cuadrado cuadrado1=new Cuadrado(Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor de los lados")));
                JOptionPane.showMessageDialog(null, "El area es de: "+cuadrado1.calcularArea());
                JOptionPane.showMessageDialog(null, "El perimetro es de: "+cuadrado1.calcularPerimetro());
                break;
            case 3:
                Rectangulo rectangulo1=new Rectangulo(Integer.parseInt(JOptionPane.showInputDialog("Ingrese la base")),Integer.parseInt(JOptionPane.showInputDialog("Ingrese la altura")));
                JOptionPane.showMessageDialog(null, "El area es de: "+rectangulo1.calcularArea());
                JOptionPane.showMessageDialog(null, "El perimetro es de: "+rectangulo1.calcularPerimetro());
                break;
            case 4:
                Rombo rombo1=new Rombo(Integer.parseInt(JOptionPane.showInputDialog("Ingrese la diagonal mayor")),Integer.parseInt(JOptionPane.showInputDialog("Ingrese la digonal menor")),Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor de los lados")));
                JOptionPane.showMessageDialog(null, "El area es de: "+rombo1.calcularArea());
                JOptionPane.showMessageDialog(null, "El perimetro es de: "+rombo1.calcularPerimetro());
                break;
            case 5:
                Trapecio trapecio1=new Trapecio(Integer.parseInt(JOptionPane.showInputDialog("Ingrese la base")),Integer.parseInt(JOptionPane.showInputDialog("Ingrese la base inferior")),Integer.parseInt(JOptionPane.showInputDialog("Ingrese la altura")),Integer.parseInt(JOptionPane.showInputDialog("Ingrese el valor de los lados")));
                JOptionPane.showMessageDialog(null, "El area es de: "+trapecio1.calcularArea());
                JOptionPane.showMessageDialog(null, "El perimetro es de: "+trapecio1.calcularPerimetro());
                break;
            case 6:
                Triangulo triangulo1=new Triangulo(Integer.parseInt(JOptionPane.showInputDialog("Ingrese la base")),Integer.parseInt(JOptionPane.showInputDialog("Ingrese la altura")));
                JOptionPane.showMessageDialog(null, "El area es de: "+triangulo1.calcularArea());
                JOptionPane.showMessageDialog(null, "El perimetro es de: "+triangulo1.calcularPerimetro());
                JOptionPane.showMessageDialog(null, "El perimetro es de: "+triangulo1.calcularHipotenusa());
                triangulo1.determinarTipotriangulo();
                break;
            default:
                JOptionPane.showMessageDialog(null, "La opcion no es valida :(");
                break;
        }
    }
    
}
