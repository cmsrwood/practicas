package avion;
public class AvionMain {
    public static void main(String[] args) {
        Avion a1=new Avion("Airbus",4);
        Avion a2=new Avion("Lookheed",7);
        a1.imprimir();
        a2.imprimir();
        a2.cambiarFabricante(a2);
        a1.imprimir();
        a2.imprimir();
    }
}
