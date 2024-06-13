
package banco;
import javax.swing.*;
public class cuenta {
    String nombre,apellidos;
    int numeroDeCuenta;
    public enum tipoDeCuenta{CORRIENTE,AHORROS};
    tipoDeCuenta tipo;
    double saldo=0;

    public cuenta(String nombre, String apellidos,tipoDeCuenta tipo, int numeroDeCuenta,int saldo) {
        this.nombre = nombre;
        this.apellidos = apellidos;
        this.tipo=tipo;
        this.numeroDeCuenta = numeroDeCuenta;
        this.saldo = saldo;
    }
    void mostrarAtributos(){
        JOptionPane.showMessageDialog(null,"Nombre completo: "+ this.nombre+" "+this.apellidos+"\nNumero de cuenta: "+this.numeroDeCuenta+"\nTipo de cuenta: "+this.tipo+"\nSaldo: "+this.saldo);
    }
    void consultarSaldo(){
        JOptionPane.showMessageDialog(null,"Saldo: " +this.saldo);
    }
    void consignar(){
        
        int consigna=Integer.parseInt(JOptionPane.showInputDialog("Ingrese la cantidad a consignar"));
        this.saldo+=consigna;
        JOptionPane.showMessageDialog(null,"Saldo actual: " +this.saldo);
    }   
    void retirar(){
        double retiro=Double.parseDouble(JOptionPane.showInputDialog("Ingrese la cantidad a retirar"));
        if (retiro>this.saldo){
            JOptionPane.showMessageDialog(null, "No puedes retirar "+retiro+" tu saldo no es suficiente\nSaldo actual: " +this.saldo);
        }
        else {
            this.saldo-=retiro;
            JOptionPane.showMessageDialog(null,"Saldo actual: " +this.saldo);
        }
    }   
}
