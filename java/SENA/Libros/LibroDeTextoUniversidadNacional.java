package Libros;
import javax.swing.*;

public class LibroDeTextoUniversidadNacional extends LibroDeTexto{
    String facultad;

    public LibroDeTextoUniversidadNacional(String facultad, String curso, String titulo, String autor, double precio) {
        super(curso, titulo, autor, precio);
        this.facultad = facultad;
    }
    @Override
    public void imprimir(){
        super.imprimir();
        System.out.println("Facultad: "+this.facultad);
    }
}
