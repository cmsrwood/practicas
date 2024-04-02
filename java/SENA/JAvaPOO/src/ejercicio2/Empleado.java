package ejercicio2;
public class Empleado {
    protected String cargo,nombre;
    protected int identficacion;
    protected float salario;

    public Empleado(String cargo, String nombre, int identficacion, float salario) {
        this.cargo = cargo;
        this.nombre = nombre;
        this.identficacion = identficacion;
        this.salario = salario;
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
    
}
