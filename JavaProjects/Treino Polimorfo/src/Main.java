
import javax.swing.JOptionPane;

/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author PEG
 */
public class Main {
    public static void main(String [] args) {
        Jogador player;
        
        String classe = JOptionPane.showInputDialog(null, "- guerreiro\n- elfo\n\nDesejo jogar com a classe:", "Classes disponíveis", 2);
        switch (classe) {
            case "guerreiro" -> player = new Guerreiro();
            case "elfo" -> player = new Elfo();
            default -> player = null;
        }
        
        player.andar();
        player.falar();
        player.correr();
        
    }
}
