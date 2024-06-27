/*
	Name: ListaLigada.cpp
	Author: GUilherme Bezerra
	Date: 16/04/24 18:34
	Description: Algoritmo de testes e aprendizado de Listas Ligadas
*/

// Libraries
#include <stdio.h>
#include <locale.h>

// Prototipation
void AdicionarFim(int);
void AdicionarInicio(int);
void MostrarTudo();
int isFull(int);
int isEmpty(int);



struct No
{
	int valor;
	struct No *prox;
};

struct Lista
{
	No *inicio, *fim;
	int tamanho;
};



main()
{
	Lista numeros;
	numeros.inicio = NULL;
	numeros.fim = NULL;
	numeros.tamanho = -1;
	
	AdicionarInicio(56);
	printf("");
}


void AdicionarFim(int)
{
	return;
}

void AdicionarInicio(Lista *numeros, int vlr)
{
	No *novo = (No*) malloc(sizeof(No));
	novo->valor = vlr;
	
	if (numeros->inicio == NULL)
	{
		novo->prox = NULL;
		numeros->fim = novo;
		numeros->inicio = novo;
	}
	else
	{
		novo->prox = numeros->inicio;
		numeros->inicio = novo;
	}
	
	numeros->tamanho++;
}

void MostrarTudo(Lista *numeros)
{
	
}
