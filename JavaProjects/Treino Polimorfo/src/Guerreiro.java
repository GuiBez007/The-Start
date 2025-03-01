/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author PEG
 */
public class Guerreiro implements Jogador{
    
    @Override
    public void andar() {
        System.out.println("Guerreiro anda raivoso!");
    }
    
    @Override
    public void falar() {
        System.out.println("Guerreiro fala alto!");
    }
    
    @Override
    public void correr() {
        System.out.println("Guerreiro corre como barbaro!");
    }
    
}
