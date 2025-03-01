/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author PEG
 */
public class Direcionador { 
    public static Midia definir(String arquivo, Midia myMidia){     
        switch (arquivo) {
            case "video" -> myMidia = new Video();
            case "musica" -> myMidia = new Musica();
            case "audio" -> myMidia = new Audio();
            default -> myMidia = null;
        }
        return myMidia;
    }
    
} // Fim da classe
