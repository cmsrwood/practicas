package avion;

public class Avion {
    String nombreFabricante;
    int numeroMotores;

    public Avion(String nombreFabricante, int numeroMotores) {
        this.nombreFabricante = nombreFabricante;
        this.numeroMotores = numeroMotores;
    }

    public String getNombreFabricante() {
        return nombreFabricante;
    }

    public void setNombreFabricante(String nombreFabricante) {
        this.nombreFabricante = nombreFabricante;
    }

    public int getNumeroMotores() {
        return numeroMotores;
    }

    public void setNumeroMotores(int numeroMotores) {
        this.numeroMotores = numeroMotores;
    }
    public void cambiarFabricante(Avion a){
        a.setNombreFabricante("Loockhead");
    }
    public void imprimir(){
        System.out.println("Fabricante: "+this.nombreFabricante);
        System.out.println("Número de motores: "+this.numeroMotores);
    }
}
