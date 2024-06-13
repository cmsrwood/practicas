package figuras;

public class Cuadrado {
    int lados;

    public Cuadrado(int lados) {
        this.lados = lados;
    }
    double calcularArea(){
        return lados*lados;
    }
    double calcularPerimetro(){
        return lados*4;
    }
}
