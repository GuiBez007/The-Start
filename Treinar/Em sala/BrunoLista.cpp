//programa para implementar as funcionalidades da lista encadeada
#include <stdio.h>
#include <conio.h>
#include<stdlib.h>

typedef struct No 
{
	int valor;
	struct No *prox;
};

typedef struct Lista
{
	No *inicio, *fim;
	int tamanho;
};



//função para inserir u nó na lista
void inseririnicio(Lista *lista, int valor)
{
	No *novo = (No*) malloc(sizeof(No));
	novo->valor = valor;
	if(lista->inicio == NULL)
	{
		novo->prox = NULL;
		lista->inicio = novo;
		lista->fim = novo;
	}
	else //quando a lista nao esta vazia
	{
		novo->prox = lista->inicio;
		lista->inicio = novo;
 
	}
lista ->tamanho++;	
}



void inserirfim(Lista *lista, int valor)
{
	No *novo = (No*) malloc(sizeof(No));
	novo->valor= valor;
	novo->prox = NULL;
	if(lista->inicio == NULL)//se a lista
	{
		lista->inicio=novo;
		lista->fim=novo;
	}
	else{
		lista->fim->prox = novo;
		lista->fim=novo;
	}
	lista ->tamanho++;
}



void removerNoLista(Lista *lista, int valor)
{
    No *inicio = lista->inicio; //ponteiro para incio da lista
    No *noARemover = NULL;
    if(inicio != NULL && lista->inicio->valor == valor)
    {
        noARemover = lista->inicio;
        lista->inicio = noARemover->prox;
    }
    else//remover Nos do meio ou fim da lista
    {
        while(inicio != NULL && inicio->prox != NULL && inicio->prox->valor != valor)
        {
            inicio = inicio->prox;
        }
        if(inicio != NULL && inicio->prox != NULL)
        {
            noARemover = inicio->prox;
            inicio->prox = noARemover->prox;
            if(inicio->prox == NULL)//se o ultimo elemento for removido, 
                lista->fim = inicio;
        }
    }
    if(noARemover) //testa se ele é NULL
    {
    	free(noARemover);
    	lista->tamanho--;
	}
}



//função que exibe os numeros da lista
void exibirlista(Lista*lista)
{
	No *inicio =lista->inicio;
	printf("Tamanho da lista: %d\n", lista->tamanho);
	//laço para percorrer todos os nós da lista
	while(inicio != NULL)
	{
		printf("%d|", inicio->valor);
		inicio = inicio->prox ;
	}
}



int main()
{
  Lista numeros;
  int opc;
  int valor;//inicialização da lista 
  numeros.inicio = NULL;
  numeros.fim = NULL;
  numeros.tamanho = 0;	
 
  while(1)
{
	system("cls");
	printf("1 - Inserir no Inicio\n2 - Inserir no Fim\n3 - Exibir Lista\n4 - remover\n5 - sair\n");
	printf("Escolha sua opcao: ");
	scanf("%d", &opc);
	switch(opc)
	{
		case 1:
			printf("Digite um valor a ser inserido no inicio da lista: ");
			scanf("%d", &valor);
			inseririnicio(&numeros,valor);
			break;
		case 2:
			printf("Digite um valor a ser inserido no fim da lista: ");
			scanf("%d", &valor);
			inserirfim(&numeros,valor);
			break;
		case 3:
			puts("Conteudo da lista: \n");
			exibirlista(&numeros);
			break;
		case 4:
			printf("Digite um valor a ser removido da lista: ");
			scanf("%d", &valor);
			removerNoLista(&numeros,valor);
		case 5:
			puts("\n\nFinalizando...");
			exit(0);
		default:
			puts("Opcao invalida!!");
	}
	puts("\n\n\n\nPressione qualquer tecla para continuar....\n\n");
	getche();
} // fim do while
}
