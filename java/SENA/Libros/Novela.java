package Libros;
public class Novela extends Libro{
    public enum Tipo{Historica,Romantica,Policiaca,Realista,CienciaFiccion,Aventuras};
    Tipo tipo;

    public Novela(Tipo tipo, String titulo, String autor, double precio) {
        super(titulo, autor, precio);
        this.tipo = tipo;
    }
    @Override
    public void imprimir(){
        super.imprimir();
        System.out.println("Tipo: "+this.tipo);
    }
}
