/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe principal do projeto de banco
 * @author GUIlherme Bezerra
 * @since 17/10/2024 08:20h
 */
public class Banco {
    public static void main(String[] args) {
        Conta pessoa1 = new Conta("Gui",1000f,123);
        
        while (true)
            pessoa1.exibirMenu();
    }
    
} //Fim da classe