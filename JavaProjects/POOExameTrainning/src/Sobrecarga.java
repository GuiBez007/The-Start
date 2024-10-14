/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */

/**
 *
 * @author PEG
 */
public class Sobrecarga {
    private String name;
    private Integer age;
    private String phone;
    
    
    public Sobrecarga(String name, int age, String phone) {
        this.name = name;
        this.age = age;
        this.phone = phone;
    }
    
    
    public Sobrecarga(String name, int age) {
        this.name = name;
        this.age = age;
    }
    
    
    public void exibirDados() {
        if (phone == null)
            exibirDados('d');
        else
            exibirDados(4);
    }
    
    
    private void exibirDados(char f) {
        System.out.println("Nome> "+name+"\nIdade> "+age);
    }
    
    
    private void exibirDados(int f) {
        System.out.println("Nome> "+name+"\nIdade> "+age+"\nTelefone> "+phone);
    }
    
}
