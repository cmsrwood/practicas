
package banco;
import javax.swing.*;
import banco.cuenta.tipoDeCuenta;
public class BancoMain {

    public static void main(String[] args) {
        String nombre=JOptionPane.showInputDialog("Ingresa tus nombres");
        String apellidos=JOptionPane.showInputDialog("Ingresa tus apellidos");
        cuenta cuenta1=new cuenta(nombre,apellidos,tipoDeCuenta.CORRIENTE,45390185,0);
        int menu=1;
        while (menu==1){
            int opcion=Integer.parseInt(JOptionPane.showInputDialog("Elija una de las siguientes opciones\n1.Mostrar atributos\n2.Consultar saldo\n3.Consignar\n4.Retirar"));
            switch (opcion){
                case 1:
                    cuenta1.mostrarAtributos();
                    menu=Integer.parseInt(JOptionPane.showInputDialog("¿Desea realizar otra transaccion?\n1.Si\n2.Salir"));
                    break;
                case 2:
                    cuenta1.consultarSaldo();
                    menu=Integer.parseInt(JOptionPane.showInputDialog("¿Desea realizar otra transaccion?\n1.Si\n2.Salir"));
                    break;
                case 3:
                    cuenta1.consignar();
                    menu=Integer.parseInt(JOptionPane.showInputDialog("¿Desea realizar otra transaccion?\n1.Si\n2.Salir"));
                    break;
                case 4:
                    cuenta1.retirar();
                    menu=Integer.parseInt(JOptionPane.showInputDialog("¿Desea realizar otra transaccion?\n1.Si\n2.Salir"));
                    break;
                default:
                    JOptionPane.showMessageDialog(null,"La opcion no es valida");
            }
        }
    }
    
}
