/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author PEG
 */
public class VentiladorTipoB implements Ventilador {
    private int botoes;
    
    public VentiladorTipoB(int botoes) {
        this.botoes = botoes;
    }
    
    public void girar() {
        System.out.println("girando");
    }
    
    public void parar() {
        System.out.println("parando");        
    }
    
} //Fim da classe
