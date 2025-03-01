/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

import javax.swing.JOptionPane;

/**
 *
 * @author PEG
 */
public class Main {
    public static void main(String [] args) {
        String arquivo = JOptionPane.showInputDialog(null, "Informe o tipo de arquivo a ser executado");
        Midia myMidia = Direcionador.definir(arquivo, null);
        
        try {
            myMidia.executar();
            myMidia.pausar();
            myMidia.finalizar();
        }
        catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Não foi possível identificar o tipo de mídia!", "Tente novamente!", 0);
        }
    }
    
} // Fim da classe
