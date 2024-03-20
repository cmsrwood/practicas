
package automovil;
import automovil.Automovil.Color;
import automovil.Automovil.tipoDeAutomovil;
import automovil.Automovil.tipoDeCombustible;

public class AutomovilMain {

    public static void main(String[] args) {
        Automovil tesla= new Automovil("Marca",2018,200,4,180,100,Automovil.tipoDeCombustible.GASOLINA,Automovil.tipoDeAutomovil.CIUDAD,Automovil.Color.ROJO,true,0);
        tesla.acelerar(90);
        System.out.println("Tiempo estimado de llegada: "+tesla.calcularDistancia(500)+"h");
        tesla.desacelerar(50);
        tesla.frenar();
    }
    
}
