package empresa;

public class trabajador {
    private int id,edad;
    private String nombre,area,correo;
    private boolean jefe;
    private double salario;
    public trabajador(int id, int edad, String nombre, String area, String correo, boolean jefe) {
        this.id = id;
        this.edad = edad;
        this.nombre = nombre;
        this.area = area;
        this.correo = correo;
        this.jefe = jefe;
    if (area=="desarrollo"){
        this.salario=4500000;
        if (jefe){
            this.salario+=2500000;
            }
        }
    else if(area=="administrativa"){
        this.salario=3500000;
        if (jefe){
            this.salario+=3000000;
            }
        }
    double descuentos=(this.salario*8/100);
    double solidaridad =0;
    if (this.salario>1300000*4){
        solidaridad=this.salario*1/100;
        }
    this.salario-=descuentos-solidaridad;
    }
    public void info(){
        System.out.println("Nombre: "+ this.nombre);
        System.out.println("Identificacion: "+this.id);
        System.out.println("Correo: "+this.correo);
        System.out.println("Edad: "+this.edad);
        System.out.println("Area: "+this.area);
        System.out.println("Salario es: "+this.salario);
    }
}
