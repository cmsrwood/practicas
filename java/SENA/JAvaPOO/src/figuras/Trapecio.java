
package figuras;

public class Trapecio {
    int base,baseInferior,altura,lados;

    public Trapecio(int base, int baseInferior, int altura, int lados) {
        this.base = base;
        this.baseInferior = baseInferior;
        this.altura = altura;
        this.lados = lados;
    }
    double calcularArea(){
        return (base+baseInferior*altura/2);
    }
    double calcularPerimetro(){
        return (base+baseInferior+altura*2);
    }
}
