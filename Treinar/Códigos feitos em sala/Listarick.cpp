/*
Name: Lista.cpp
Author: Erick Gomes Barbosa
Date: 13/03/24 09:57
Description: Programa para implementar as funcionalidade de uma lista encadeada
CRUD (Create, Read, Update e Delete): são operações básicas para um código, o Create cria/grava a informação em um Banco de
 Dados, o Read busca a informação do Banco de Dados, o Update atualiza um dado gravado no 
 Banco e o Delete apaga a informação do Banco.
Persistência de dados é a ação de gravar o dado no Banco de Dados
 
*/

#include <stdio.h>
#include <conio.h>
#include <stdlib.h>
#include <locale.h>

struct No
{
	int valor;
	struct No *prox;//
};

struct Lista
{
	No *inicio, *fim;
	int tamanho;
};



//Função para inserir um nó no início da Lista
void inserirInicio(Lista *lista, int vlr)
{
	No *novo = (No*) malloc(sizeof(No));
	novo->valor = vlr;


	if(lista->inicio == NULL) //Se a lista estiver vazia
	{
		novo->prox = NULL;
		lista->inicio = novo;
		lista->fim = novo;
	}
	else //Quando a lista não está vazia
	{
		novo->prox = lista->inicio;
		lista->inicio = novo;
	}
	lista->tamanho++;
}



//Função para inserir um nó no fim da Lista
void inserirFim(Lista *lista, int vlr)
{
	No *novo = (No*) malloc(sizeof(No)); //Cria um novo nó
	novo->valor = vlr;
	novo->prox = NULL;
	
	
	if(lista->inicio == NULL) //Se a lista estiver vazia
	{
		lista->inicio = novo;
		lista->fim = novo;
	}
	else //Se a lista não estiver vazia
	{
		lista->fim->prox = novo;
		lista->fim = novo;
	}
	lista->tamanho++;
}



//Função para excluir um elemento da Lista
void removerNoLista(Lista *lista, int vlr)
{
	No *inicio = lista->inicio; //Ponteiro para o início da Lista
	No *noARemover = NULL; //Ponterio para um nó a ser removido
	
	
	if(inicio != NULL && lista->inicio->valor == vlr) //Remove o primeiro nó da Lista
	{
		noARemover = lista->inicio;
		lista->inicio = noARemover->prox; //Aqui atribuímos ao inicio da lista o valor do segundo item da lista, pois a função apagará o primeiro nó, assim o segundo se torna o primeiro
	}
	else //Remover nós do meio ou do fim da Lista
	{
		while(inicio != NULL && inicio->prox != NULL && inicio->prox->valor != vlr)
		{
			inicio = inicio->prox;
		}
		if(inicio != NULL && inicio->prox != NULL)
		{
			noARemover = inicio->prox;
			inicio->prox = noARemover->prox;
			
			if(inicio->prox == NULL)//Se o ultimo elemento for removido
				lista->fim = inicio;
		}
	}//fim do else
	
	if(noARemover)//Testa se ele é NULL
	{
		free(noARemover);
		lista->tamanho--;
	}
}



//Função que exibe os números (elementos) presentres na Lista
void exibirLista(Lista *lista)
{
	No *inicio = lista->inicio;
	printf("\nTamanho da Lista: %d\n", lista->tamanho);
	
	//Laço pra percorrer todos os Nós da lista
	while(inicio != NULL) //Testa se ele é NULL
	{
		printf("%d|", inicio->valor);//Libera a memória do nó
		inicio = inicio->prox;//Decrementa o tamanho da lista
	}
}

main()
{
	setlocale(LC_ALL, "Portuguese");
	
	Lista numeros;
	int vlr;
	int opc; //opção de escolha
	
	
	//Inicialização da Lista
	numeros.inicio = NULL;
	numeros.fim = NULL;
	numeros.tamanho = 0;
	
	
	while(1)//Enquanto verdadeiro
	{
		system("cls");
		puts("LISTA LIGADA ou ENCADEADA");
		puts("===================================");
		printf("1- Inserir no Inicio\n2- Inserir no Fim\n3- Exibir Lista\n4- Remover da Lista\n5- Sair");
		printf("\n\nEscolha a sua opção: ");
		scanf("%d", &opc);
		
		
		switch(opc)
		{
			case 1: 
				printf("\nDigite um valor a ser inserido no INICIO da Lista: ");
				scanf("%d", &vlr);
				inserirInicio(&numeros, vlr);
				break;
			case 2:
				printf("\nDigite um valor a ser inserido no FINAL da Lista: ");
				scanf("%d", &vlr);
				inserirFim(&numeros, vlr);
				break;
			case 3:
				puts("\nConteúdo da Lista:\n");
				exibirLista(&numeros);
				break;
			case 4:
				printf("\nDigite um valor a ser REMOVIDO da Lista: ");
				scanf("%d", &vlr);
				removerNoLista(&numeros, vlr);
				break;
			case 5:
				puts("\n\nFinalizando...");
				exit(0);
			default:
				puts("\n=========Opção Inválida=========");
		}//fim do switch
		
		puts("\nPressione qualquer tecla para continuar.");
		getch();
	}//fim do while
}
