/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author PEG
 */
public class Main {
    public static void main(String[] args) {
        VentiladorTipoA va = new VentiladorTipoA(2);
        va.girar();
        
        Ventilador vb = new VentiladorTipoB(3);
        vb.parar();
    }
}
