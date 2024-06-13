package Libros;
public class Libro {
    protected String titulo,autor;
    protected double precio;

    public Libro(String titulo, String autor, double precio) {
        this.titulo = titulo;
        this.autor = autor;
        this.precio = precio;
    }

    public String getTitulo() {
        return titulo;
    }

    public void setTitulo(String titulo) {
        this.titulo = titulo;
    }

    public String getAutor() {
        return autor;
    }

    public void setAutor(String autor) {
        this.autor = autor;
    }

    public double getPrecio() {
        return precio;
    }

    public void setPrecio(double precio) {
        this.precio = precio;
    }
    public void imprimir(){
        System.out.println("\nTitulo: "+this.titulo+"\nAutor: "+this.autor+"\nPrecio: "+this.precio);
    }
}
