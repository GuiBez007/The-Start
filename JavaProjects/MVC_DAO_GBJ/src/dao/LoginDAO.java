/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dao;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import utilitarios.Conexao;

/**
 *
 * @author PEG
 */
public class LoginDAO {
    
    public static boolean verificar(String nome, String senha) {
        Connection conexao = Conexao.obterConexao();
        try {
            String sql = "SELECT 'true' as 'estado' FROM cliente WHERE nome=? and senha=?";
            PreparedStatement pst = conexao.prepareStatement(sql);
            pst.setString(1, nome);
            pst.setString(2, senha);
            ResultSet rs = pst.executeQuery();
            
            while (rs.next()) {
                if (rs.getString("estado").equals("true")) {
                    return true;
                }
            }
            pst.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return false;
    } // fim listar
}
