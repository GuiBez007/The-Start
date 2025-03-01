/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package raizesdaterra;

/**
 *
 * @author PEG
 */
public class Usuario {
    private String nome;
    private String celularEmail;
    private String senha;
    private String dataNascimento;
    private String genero;
    
    // Método Construtor
    public Usuario(String nome, String celularEmail, String senha, String dataNascimento, String genero) {
        this.nome = nome;
        this.celularEmail = celularEmail;
        this.dataNascimento = dataNascimento;
        this.senha = senha;
        this.genero = genero;
    }
    
    // Método que permite o usuário logar na plataforma
    public void logarUsuario() {
        Login login = new Login();
        login.setVisible(true);
    }
    
    // Método que permite o usuário se cadastrar na plataforma
    public void cadastrarUsuario() {
        Cadastrar cadastro = new Cadastrar();
        cadastro.setVisible(true);
    }
    
    // Método que permite o usuário a recuperar sua senha
    public void recuperarSenha() {
        EsqueciSenha recuperar = new EsqueciSenha();
        recuperar.setVisible(true);
    }
    
    // Método que permite o usuário alterar sua senha
    
    
    // Métodos assessores 
    public String getNome() {
        return nome;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public String getCelularEmail() {
        return celularEmail;
    }

    public void setCelularEmail(String celularEmail) {
        this.celularEmail = celularEmail;
    }

    public String getSenha() {
        return senha;
    }

    public void setSenha(String senha) {
        this.senha = senha;
    }

    public String getDataNascimento() {
        return dataNascimento;
    }

    public void setDataNascimento(String dataNascimento) {
        this.dataNascimento = dataNascimento;
    }
    
    public String getGenero() {
        return genero;
    }

    public void setGenero(String dataNascimento) {
        this.genero = genero;
    }

} // Fim da Classe