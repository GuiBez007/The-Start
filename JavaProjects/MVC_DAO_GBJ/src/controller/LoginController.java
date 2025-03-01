/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package controller;

import dao.LoginDAO;

/**
 *
 * @author PEG
 */
public class LoginController {
    
    public static boolean verificar(String nome, String senha) {
        return LoginDAO.verificar(nome, senha);
    }
}

