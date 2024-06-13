
package figuras;

import javax.swing.JOptionPane;

public class Triangulo {
    int base,altura;

    public Triangulo(int base, int altura) {
        this.base = base;
        this.altura = altura;
    }
    double calcularArea(){
        return (base * altura / 2);
    }
    double calcularPerimetro(){
        return (base + altura + calcularHipotenusa());
   
    }
        double calcularHipotenusa(){
         return Math.pow(base* base + altura*altura , 0.5);
    }
    void determinarTipotriangulo(){
        if ((base==altura)&&(base==calcularHipotenusa()) && (altura==calcularHipotenusa())){
        JOptionPane.showMessageDialog(null, "Esto es un triangulo equilatero"); 
        } 
        else if ((base==altura)&&(base==calcularHipotenusa()) && (altura==calcularHipotenusa())){
            JOptionPane.showMessageDialog(null, "Esto es un triangulo escaleno"); 
        }
        else {
            JOptionPane.showMessageDialog(null, "Esto es un triangulo isoceles"); 
        }
    }
}

