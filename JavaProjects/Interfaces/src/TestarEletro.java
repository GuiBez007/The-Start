/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */

/**
 * Classe principal para instanciar 
 * @author 2830482311024
 */
public class TestarEletro {
    public static void main(String [] args) throws InterruptedException {
        Tv tv = new Tv();
        Microondas micro = new Microondas();
        
        tv.ligar();
        tv.ativarSoneca(10);
        
        micro.ligar(10);
    }
}
