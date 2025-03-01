/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author PEG
 */
public class VentiladorTipoA implements Ventilador{
    int botoes;
    
    public VentiladorTipoA(int botoes) {
        this.botoes = botoes;
    }
    
    
    @Override
    public void girar() {
        System.out.println("girando");
    }
    
    @Override
    public void parar() {
        System.out.println("parando");
    }
    
}
