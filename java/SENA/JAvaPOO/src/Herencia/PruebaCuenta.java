package Herencia;
import java.util.Scanner;
public class PruebaCuenta {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
      Scanner input = new Scanner(System.in);
        System.out.println(" Con Cuenta de Ahorros ");
        System.out.println("Ingrese un saldo Inicial ");
        float saldoInicialAhorros = input.nextFloat();
        System.out.println("Ingrese una tasa de Interes ");
        float tasaAhorros = input.nextFloat();
        CuentaAhorros cuenta1 = new CuentaAhorros( saldoInicialAhorros, tasaAhorros);
        System.out.println("Ingrese el valor a consignar ");
        float cantidadConsignar = input.nextFloat();
        cuenta1.consignar(cantidadConsignar);
        System.out.println("Ingrese el valor a retirar ");
        float cantidadRetirar = input.nextFloat();
        cuenta1.retirar(cantidadRetirar);
        cuenta1.extractoMensual();
        cuenta1.imprimir();
    
      
    }
    
}
