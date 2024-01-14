import java.util.Scanner;
public class mayorque {

    public static void main(String[] args) {
        
        int num1,num2,suma;
        Scanner teclado = new Scanner(System.in);
        System.out.println("Ingrese el 1er numero: ");
        num1 = teclado.nextInt();
        System.out.println("Ingrese el 2do numero: ");
        num2 = teclado.nextInt();
        if (num1>num2){
            System.out.println(num1+" es mayor");
        }
        else if (num1==num2){
            System.out.println("Los numeros son iguales");
        }
        else {
            System.out.println(num2+" es mayor");
        }
    }
}