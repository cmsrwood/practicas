package ejercicio2;

import javax.swing.*;

public class Triangulo {
    double base,altura,area;

    public Triangulo(double base, double altura) {
        this.base = base;
        this.altura = altura;
        this.area= (base*altura)/2;
    }
    void info(){
        JOptionPane.showMessageDialog(null,"[Trinagulo]:\nBase: "+base+"\nAltura: "+altura+"\n"+"Area: "+area);        
    }
}


