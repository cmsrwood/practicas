
package figuras;

public class Rombo {
    int dMayor,dMenor,lados;

    public Rombo(int dmayor, int dmenor, int lados) {
        this.dMayor = dmayor;
        this.dMenor = dmenor;
        this.lados = lados;
    }
    double calcularArea(){
        return (dMenor*dMayor/2);
    }
    double calcularPerimetro(){
        return lados*4;
    }
}
