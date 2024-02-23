import java.util.Scanner;
public class suma {

    public static void main(String[] args) {
        
        int num1,num2,suma;
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingrese el 1er numero: ");
        num1 = teclado.nextInt();
        System.out.println("Ingrese el 2do numero: ");
        num2 = teclado.nextInt();
        suma=num1+num2;
        System.out.println("El resultado es: "+suma);
        
    }
}