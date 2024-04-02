package Libros;
import Libros.Novela.Tipo;
public class Main {
    public static void main(String[] args) {
        Libro libro = new Libro("Satanás","Mario Mendoza",30000);
        LibroDeTexto librotxt = new LibroDeTexto("Física relativista","Relatividad","Cientifico loco",10000);
        LibroDeTextoUniversidadNacional libronacho=new LibroDeTextoUniversidadNacional("Facultad de ingenieria","Programacion en Python desde cero","Como programar en Python","Programador divorciado",30000);
        Novela novela= new Novela (Tipo.Romantica,"Love history","Eric Segan",30000);
        libro.imprimir();
        librotxt.imprimir();
        libronacho.imprimir();
        novela.imprimir();
    }
}