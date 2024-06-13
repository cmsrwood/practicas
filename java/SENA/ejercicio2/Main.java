package ejercicio2;
public class Main {
    public static void main(String[] args) {
        Contratista c1= new Contratista(3,3000,"Profesor","Zaida",10,1300000);
        c1.calcularSalario();
        Planta p1=new Planta (8,1300000,5000,"Profesor","Vladimir",10,1300000);
        p1.calcularSalario();
    }
    
}
