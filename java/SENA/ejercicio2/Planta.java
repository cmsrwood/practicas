package ejercicio2;
public class Planta extends Empleado{
    float deduccion,sueldoBasico,valorExtras;

    public Planta(float deduccion, float sueldoBasico, float valorExtras, String cargo, String nombre, int identficacion, float salario) {
        super(cargo, nombre, identficacion, salario);
        this.deduccion = deduccion;
        this.sueldoBasico = sueldoBasico;
        this.valorExtras = valorExtras;
    }

    public float getDeduccion() {
        return deduccion;
    }

    public void setDeducccion(float deducccion) {
        this.deduccion = deducccion;
    }

    public float getSueldoBasico() {
        return sueldoBasico;
    }

    public void setSueldoBasico(float sueldoBasico) {
        this.sueldoBasico = sueldoBasico;
    }

    public float getValorExtras() {
        return valorExtras;
    }

    public void setValorExtras(float valorExtras) {
        this.valorExtras = valorExtras;
    }

    public String getCargo() {
        return cargo;
    }

    public void setCargo(String cargo) {
        this.cargo = cargo;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public int getIdentficacion() {
        return identficacion;
    }

    public void setIdentficacion(int identficacion) {
        this.identficacion = identficacion;
    }

    public float getSalario() {
        return salario;
    }

    public void setSalario(float salario) {
        this.salario = salario;
    }
    public void calcularSalario(){
        this.salario=this.sueldoBasico+valorExtras-(this.salario*this.deduccion/100);
        System.out.println("Salario: "+this.salario);
    }
}
