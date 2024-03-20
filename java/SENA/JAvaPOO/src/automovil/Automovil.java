
package automovil;

public class Automovil {
    String marca;
    int modelo,motor,puertas,velocidadMaxima,velocidadActual;
    public enum tipoDeCombustible{GASOLINA,BIOETANOL,DIESEL,BIODESEL,GASNATURAL};
    tipoDeCombustible tipoCombustible;
    public enum tipoDeAutomovil{CIUDAD,SUBCOMPACTO,COMPACTO,FAMILIAR,EJECTUVIO,SUV};
    tipoDeAutomovil tipoAutomovil;
    public enum Color{BLANCO,NEGRO,ROJO,NARANJA,AMARILLO,VERDE,AZUL,VIOLETA};
    Color color;
    boolean automatico;
    int multa;

    public Automovil(String marca, int modelo, int motor,int puertas, int velocidadMaxima, int velocidadActual, tipoDeCombustible tipoCombustible, tipoDeAutomovil tipoAutomovil, Color color,boolean automatico,int multa) {
        this.marca = marca;
        this.modelo = modelo;
        this.motor=motor;
        this.puertas = puertas;
        this.velocidadMaxima = velocidadMaxima;
        this.velocidadActual = velocidadActual;
        this.tipoCombustible = tipoCombustible;
        this.tipoAutomovil = tipoAutomovil;
        this.color = color;
        this.automatico=automatico;
        this.multa=multa;
    }

    public String getMarca() {
        return marca;
    }

    public int getModelo() {
        return modelo;
    }

    public int getPuertas() {
        return puertas;
    }

    public int getMotor() {
        return motor;
    }

    public boolean isAutomatico() {
        return automatico;
    }
    

    public int getVelocidadMaxima() {
        return velocidadMaxima;
    }

    public int getVelocidadActual() {
        return velocidadActual;
    }

    public tipoDeCombustible getTipoCombustible() {
        return tipoCombustible;
    }

    public tipoDeAutomovil getTipoAutomovil() {
        return tipoAutomovil;
    }

    public Color getColor() {
        return color;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    public void setModelo(int modelo) {
        this.modelo = modelo;
    }

    public void setPuertas(int puertas) {
        this.puertas = puertas;
    }

    public void setMotor(int motor) {
        this.motor = motor;
    }

    public void setAutomatico(boolean automatico) {
        this.automatico = automatico;
    }
    
    public void setVelocidadMaxima(int velocidadMaxima) {
        this.velocidadMaxima = velocidadMaxima;
    }

    public void setVelocidadActual(int velocidadActual) {
        this.velocidadActual = velocidadActual;
    }

    public void setTipoCombustible(tipoDeCombustible tipoCombustible) {
        this.tipoCombustible = tipoCombustible;
    }

    public void setTipoAutomovil(tipoDeAutomovil tipoAutomovil) {
        this.tipoAutomovil = tipoAutomovil;
    }

    public void setColor(Color color) {
        this.color = color;
    }
    public void acelerar(int velocidadAcelerar){
        if (velocidadAcelerar>this.velocidadMaxima){
            this.multa+=1;
            System.out.println("USTED HA SIDO MULTADO\nNumero de multas: "+this.multa);
        }
        else {
            System.out.println("Acelerando...");
            for (int i=0;i<velocidadAcelerar;i++){
                this.velocidadActual+=1;
                System.out.println("Velocidad actual: "+this.velocidadActual);
            }
                
        }
    }
    public void desacelerar(int velocidadDesacelerar){
        if (velocidadDesacelerar>this.velocidadMaxima){
            
        }
        else {
            System.out.println("Desacelerando...");
            for (int i=0;i<velocidadDesacelerar;i++){
                this.velocidadActual-=1;
                System.out.println("Velocidad actual: "+this.velocidadActual);
            }
                
        }
    }
    public void frenar(){
        System.out.println("Frenando...");
        for (int i=0;this.velocidadActual>0;i++){
                this.velocidadActual-=1;
                System.out.println("Velocidad actual: "+this.velocidadActual);
            }
    }
    float calcularDistancia(float distancia){
        return distancia/this.velocidadActual;
    }
    public void mostrarAtributos(){
        System.out.println("Marca: "+this.marca);
        System.out.println("Modelo: "+this.modelo);
        System.out.println("Motor: "+this.motor);
        System.out.println("Número de puertas: "+this.puertas);
        System.out.println("Velocidad maxima: "+this.velocidadMaxima);
        System.out.println("Tipo de combustible: "+this.tipoCombustible);
        System.out.println("Tipo de automovil: "+this.tipoAutomovil);
        System.out.println("Color: "+this.color);
    }
}
