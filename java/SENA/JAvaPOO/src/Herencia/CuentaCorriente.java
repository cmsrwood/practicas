package Herencia;
public class CuentaCorriente extends Cuenta{
    float sobregiro; 

    public CuentaCorriente(float sobregiro, float saldo, float tasaAnual) {
        super(saldo, tasaAnual);
        sobregiro = 0;
    }
    @Override
    public void retirar(float cantidad){
        float resultado = saldo -cantidad;
        if(resultado <0){
            sobregiro = sobregiro - resultado; 
            saldo = 0; 
        }else{
            super.retirar(cantidad);
        }
    }
    
    @Override
    public void consignar (float cantidad){
        float residuo = sobregiro -cantidad; 
        
        if(sobregiro>0){
            if(residuo>0){
                sobregiro = 0; 
                saldo = 0; 
            }
        }else{
            super.consignar(cantidad);
        }
    }
    @Override
    public void extractoMensual(){
        super.extractoMensual();
    }
    
        public void imprimir(){
        System.out.println("Saldo " +saldo);
        System.out.println("Comision Mensual" +comisionMensual);
        System.out.println(" numero de Transacciones" +(numeroConsignaciones +numeroRetiros));
            System.out.println("Valor del sobregiro" +(numeroConsignaciones +numeroRetiros));
    }
}