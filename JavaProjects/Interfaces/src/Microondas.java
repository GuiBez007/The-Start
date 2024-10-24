/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe para implementar todos os métodos da interface Eletrodomestico
 * @author GUIlherme Bezerra
 * @since 24/10/2024 12:14h
 */
public class Microondas implements Eletrodomestico{

    @Override
    public void ligar() {
        System.out.println("O microondas foi ligado!");
    }

    @Override
    public void desligar() {
        System.out.println("O microondas foi desligado!");
    }
    
    //Método para ligar o microondas com o tempo escolhido pelo usuário
    public void ligar(int tempo) throws InterruptedException {
        ligar();
        for (tempo=tempo; tempo>0; tempo--) {
            System.out.println(tempo);
            Thread.sleep(1000);
        }
        desligar();
    }
    
}
