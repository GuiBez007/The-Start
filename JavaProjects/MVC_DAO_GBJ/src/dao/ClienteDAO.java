/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package dao;

import java.sql.PreparedStatement;
import java.sql.Connection;
import java.sql.ResultSet;
import javax.swing.JOptionPane;
import java.util.ArrayList;
import java.util.List;

import utilitarios.Conexao;
import model.Cliente;

/**
 *
 * @author PEG
 */
public class ClienteDAO {
    
    public void cadastrar(Cliente cliente) {
        Connection conexao = Conexao.obterConexao();
        try {
            String sql = "INSERT INTO cliente (nome, telefone, endereco, email) "
                    + "VALUES (?, ?, ?, ?)";
            PreparedStatement pst = conexao.prepareStatement(sql);
            pst.setString(1, cliente.getNome());
            pst.setString(2, cliente.getTelefone());
            pst.setString(3, cliente.getEndereco());
            pst.setString(4, cliente.getEmail());            
            pst.execute();
            pst.close();
            JOptionPane.showMessageDialog(null, "Cadastro realizado com sucesso!");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
    
    public List<Cliente> listar(String pesquisa) {
        Connection conexao = Conexao.obterConexao();
        List<Cliente> lista = new ArrayList<>();
        try {
            String sql = "SELECT codigo, nome, telefone, endereco, "
                    + "email FROM cliente WHERE nome like ?";
            PreparedStatement pst = conexao.prepareStatement(sql);
            pst.setString(1, pesquisa + "%");
            ResultSet rs = pst.executeQuery();
            
            while (rs.next()) {
                Cliente cliente = new Cliente();
                cliente.setCodigo(rs.getInt("codigo"));
                cliente.setNome(rs.getString("nome"));
                cliente.setTelefone(rs.getString("telefone"));
                cliente.setEndereco(rs.getString("endereco"));
                cliente.setEmail(rs.getString("email"));
                lista.add(cliente);
            }
            pst.close();
        } catch (Exception e) {
            e.printStackTrace();
        // fim catch
        }
        return lista;
    } // fim listar
    
    public void update(Cliente cliente) { 
        Connection conexao = Conexao.obterConexao();
        try {
            String sql = "UPDATE cliente SET nome=?, telefone=?, endereco=?, "
                    + "email=? WHERE codigo = ?";
            PreparedStatement pst = conexao.prepareStatement(sql);
            pst.setString(1, cliente.getNome());
            pst.setString(2, cliente.getTelefone());
            pst.setString(3, cliente.getEndereco());
            pst.setString(4, cliente.getEmail());   
            pst.setString(5, String.valueOf(cliente.getCodigo()));
            pst.execute();
            pst.close();
            //limpar();
        } catch (Exception e) {
            JOptionPane.showMessageDialog(null, "Não atualizado!");
            System.out.println(e.getMessage());
        }
    } // end update
    
    public void excluir(int codigo) {
        Connection conexao = Conexao.obterConexao();
        try {
            String url = "DELETE FROM cliente WHERE codigo=?";
            PreparedStatement pst = conexao.prepareStatement(url);
            pst.setInt(1, codigo);
            pst.execute();
            pst.close();
            JOptionPane.showMessageDialog(null, "Excluído com sucesso!");
        } catch(Exception e) {
            JOptionPane.showMessageDialog(null, "Erro ao excluir!");         
            System.out.println(e.getMessage());
        }
    }
    
}
