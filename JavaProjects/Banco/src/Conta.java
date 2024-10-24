import javax.swing.JOptionPane;


/**
 *  Classe para demonstrar o princípio do encapsulamento
 *  @author GUIlherme Bezerra
 *  @since 17/10/2024 08:35h
 */
public class Conta {
    
    private String cliente;
    private float saldo;
    private int senha;
    private boolean bloqueado;
    private int tentativas;

    
    //Construtor da Classe
    public Conta(String cliente, float saldo, int senha) {
        this.cliente = cliente;
        this.saldo = saldo;
        this.senha = senha;
        this.bloqueado = false;
        this.tentativas = 1;
    }

    
    //Métodos da classe//
    
    //Método que cria uma linha no console
    private static void putLine() {
        System.out.println("");
    }
    
    
    //Método responsável pela exibição do menu inicial
    public void exibirMenu() {
        putLine();
        System.out.println("       ===== BANCO 24H =====      ");
        System.out.println("[01] - exibir dados da conta;     ");
        System.out.println("[02] - realizar saque;            ");
        System.out.println("[03] - depositar em outra conta;  ");
        System.out.println("[04] - trocar a senha;            ");
        System.out.println("[05] - sair.                      ");
        validarEscolhaUsuario();
    }
    
    
    //Método que valida a escolha do usuário
    private void validarEscolhaUsuario() {
        int opcao = Integer.parseInt(JOptionPane.showInputDialog("Informe uma opçao "));
        putLine();
        switch (opcao) {
            case 01 -> exibirDadosConta();
            case 02 -> realizarSaque();
            case 03 -> depositarDinheiro();
            case 04 -> trocarSenha(getSenha());
            case 05 -> System.exit(0);            
        }
    }
    
    
    //Método que exibe os dados do usuário da conta
    private void exibirDadosConta(){
        System.out.println("Nome do Cliente: " + cliente);
        System.out.println("Saldo da Conta: " + saldo);
        System.out.println("Conta " + (isBloqueado() == true ? "Ativa!" : "Bloqueada!"));
    }
    
    
    //Metodo para realizar saque na conta do cliente
    public void realizarSaque(){
        int pwd = 0;
        if (isBloqueado())
            JOptionPane.showMessageDialog(null, "Conta bloqueada!", "Acesso Negado", 0);
        else {
            pwd = Integer.parseInt(JOptionPane.showInputDialog(null, "Informe a senha da conta", "Tentativa ("+String.valueOf(tentativas)+"/3)", 1));
        
            if(!verificarSenha(pwd)){
                if (!isBloqueado()) {                   
                    JOptionPane.showMessageDialog(null, "A senha esta incorreta!", "Erro!", 2);
                    realizarSaque();
                }
            }else{
                float vlrSaque = 0;
                vlrSaque = Float.parseFloat(JOptionPane.showInputDialog("Digite o valor a sacar"));

                if (getSaldo()-vlrSaque < 0)
                    JOptionPane.showMessageDialog(null, "O valor do saldo é insuficiente para o saque");
                else
                    setSaldo(getSaldo()-vlrSaque);
            }            
        }
    }
    
    
    //Método para depositar dinheiro em outras contas
    private void depositarDinheiro() {
        String conta = JOptionPane.showInputDialog(null, "Informe o numero da conta de destino", "Conta", 1);
        float valor = Float.parseFloat(JOptionPane.showInputDialog(null, "Informe o valor a ser transferido", "Valor", 1));
        
        if (!conta.equals(""))
            JOptionPane.showMessageDialog(null, "Dinheiro depositado com sucesso!", "Warning", 2);
        else
            JOptionPane.showMessageDialog(null, "Dinheiro não depositado! Tente novamente", "Error", 0);
    }
    
    //Método para trocar a senha
    private void trocarSenha(int pwd) {
        int senhaAtual = Integer.parseInt(JOptionPane.showInputDialog(null, "Informe sua senha atual", "Input", 1));
        if (senhaAtual == pwd) {
            String npwd1 = JOptionPane.showInputDialog(null, "Informe a nova senha", "Input", 1);
            String npwd2 = JOptionPane.showInputDialog(null, "Confirme a nova senha", "Input", 1);

            if (npwd1.equals(npwd2)) {
                JOptionPane.showMessageDialog(null, "Nova senha criada com sucesso!", "Warning", 2);
                setSenha(Integer.parseInt(npwd1));
            }else
                JOptionPane.showMessageDialog(null, "As senhas não são iguais!", "Warning", 0);
        }else
            JOptionPane.showMessageDialog(null, "Senha incorreta!", "Warning", 0);
    }
    
    
    //Método para verificar a senha
    private boolean verificarSenha(int pwd){
       if(pwd == getSenha()){
           tentativas = 1;
           return true;
       }else{
           if(tentativas == 3){
               JOptionPane.showMessageDialog(null, "Conta bloqueada!", "Acesso Negado", 0);
               setBloqueado(true);
           }else
               tentativas++;  
           
        return false; 
       }
    }
    
    
    //Métodos assessores//
    public String getCliente() {
        return cliente;
    }

    public void setCliente(String cliente) {
        this.cliente = cliente;
    }

    private float getSaldo() {
        return saldo;
    }

    private void setSaldo(float saldo) {
        this.saldo = saldo;
    }

    public int getSenha() {
        return senha;
    }

    public void setSenha(int senha) {
        this.senha = senha;
    }

    public boolean isBloqueado() {
        return bloqueado;
    }

    public void setBloqueado(boolean bloqueado) {
        this.bloqueado = bloqueado;
    }
    
} //Fim da Classe