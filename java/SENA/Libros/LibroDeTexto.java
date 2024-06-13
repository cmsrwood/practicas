package Libros;

public class LibroDeTexto extends Libro{
    protected String curso;

    public LibroDeTexto(String curso, String titulo, String autor, double precio) {
        super(titulo, autor, precio);
        this.curso = curso;
    }
    @Override
    public void imprimir(){
        super.imprimir();
        System.out.println("Curso: "+this.curso);
    }
}
