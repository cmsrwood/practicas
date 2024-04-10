package ejercicio2;

public class Contratista extends Empleado{
    int totalHoras,valorHora;

    public Contratista(int totalHoras, int valorHora, String cargo, String nombre, int identficacion, float salario) {
        super(cargo, nombre, identficacion, salario);
        this.totalHoras = totalHoras;
        this.valorHora = valorHora;
    }

    public int getTotalHoras() {
        return totalHoras;
    }

    public void setTotalHoras(int totalHoras) {
        this.totalHoras = totalHoras;
    }

    public int getValorHora() {
        return valorHora;
    }

    public void setValorHora(int valorHora) {
        this.valorHora = valorHora;
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
        this.salario+=this.valorHora*this.totalHoras;
        System.out.println("Salario: "+this.salario);
    }
}
