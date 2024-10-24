/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe para implementar todos os métodos da interface Eletrodomésticos
 * @author 2830482311024
 */
public class Tv implements Eletrodomestico{
    String marca;   
    int polegadas;
    
    @Override
    public void ligar() {
        System.out.println("A tv foi ligada!");
    }

    @Override
    public void desligar() {
        System.out.println("A tv foi desligada!");
    }
    
    //Método para desligar a tv quando um período de tempo definido pelo usuário passar
    public void ativarSoneca(int min) throws InterruptedException {
        System.out.println("A tv será desligada em tantos minutos");
        
        for (min=min; min>0; min--) {
            Thread.sleep(1000);
        }
        desligar();
    }
    
}
