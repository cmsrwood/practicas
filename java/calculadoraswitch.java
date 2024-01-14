import java.util.Scanner;

public class calculadoraswitch {
    public static void main(String[] args) {
        int opcion=0,num1,num2,resultado,pregunta;
        String nombre;
        Scanner teclado = new Scanner(System.in);
        System.out.println("Hola, bienvenido a una increible calculadora en consola\nPara continuar por favor digite su nombre: ");
        nombre = teclado.nextLine();
        while (opcion==0){
        System.out.println("----------------------------------------------------MENU--------------------------------------------\n"+"Hola "+nombre+", bienvenido a la calculadora \n"+nombre+ " elija una de las siguientes opciones:\n1.Suma\n2.Resta\n3.Multiplicacion\n4.Division\nSu opción: ");
        opcion= teclado.nextInt();
        switch (opcion){
            case 1:
                System.out.println("---------------SUMA------------------");
                System.out.println("Digite el 1er numero: ");
                num1= teclado.nextInt();
                System.out.println("Digite el 2do numero: ");
                num2= teclado.nextInt();
                resultado=num1+num2;
                System.out.println("El resultado es: "+resultado);
                System.out.println("Si desea realizar una nueva operacion digite 1, si desea salir digite 2\nSu opción: ");
                pregunta= teclado.nextInt();
                if (pregunta==1){
                    opcion=0;
                }
                else if (pregunta==2){
                    opcion=10;
                    System.out.println("gracias por usar mi calculadora");
                }
                else {
                    System.out.println("Opcion invalida");
                }
                break;
            case 2:
                System.out.println("---------------RESTA------------------");
                System.out.println("Digite el 1er numero: ");
                num1= teclado.nextInt();
                System.out.println("Digite el 2do numero: ");
                num2= teclado.nextInt();
                resultado=num1-num2;
                System.out.println("El resultado es: "+resultado);
                System.out.println("Si desea realizar una nueva operacion digite 1, si desea salir digite 2\nSu opción: ");
                pregunta= teclado.nextInt();
                if (pregunta==1){
                    opcion=0;
                }
                else if (pregunta==2){
                    opcion=10;
                    System.out.println("gracias por usar mi calculadora");
                }
                else {
                    System.out.println("Opcion invalida");
                }
                break;
            case 3:
                System.out.println("---------------MULTIPLICACION------------------");
                System.out.println("Digite el 1er numero: ");
                num1= teclado.nextInt();
                System.out.println("Digite el 2do numero: ");
                num2= teclado.nextInt();
                resultado=num1*num2;
                System.out.println("El resultado es: "+resultado);
                System.out.println("Si desea realizar una nueva operacion digite 1, si desea salir digite 2\nSu opción: ");
                pregunta= teclado.nextInt();
                if (pregunta==1){
                    opcion=0;
                }
                else if (pregunta==2){
                    opcion=10;
                    System.out.println("gracias por usar mi calculadora");
                }
                else {
                    System.out.println("Opcion invalida");
                }
                break;
            case 4:
                System.out.println("---------------DIVISION------------------");
                System.out.println("Digite el 1er numero: ");
                num1= teclado.nextInt();
                System.out.println("Digite el 2do numero: ");
                num2= teclado.nextInt();
                resultado=num1/num2;
                System.out.println("El resultado es: "+resultado);
                System.out.println("Si desea realizar una nueva operacion digite 1, si desea salir digite 2\nSu opción: ");
                pregunta= teclado.nextInt();
                if (pregunta==1){
                    opcion=0;
                }
                else if (pregunta==2){
                    opcion=10;
                    System.out.println("gracias por usar mi calculadora");
                }
                else {
                    System.out.println("Opcion invalida");
                }
                break;
            default:
                System.out.println("Opcion invalida");
                break;
            }
        }
    }
}
