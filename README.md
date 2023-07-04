# Sumário

Esse algoritmo busca encontrar uma solução para um problema comum em **Teoria dos Grafos** que envolve a busca encontrar articulações e blocos em um grafo G. 

1. ***Introdução*:** 
Será apresentado o **problema** motivador do algoritmo.

2. ***Definições*:** 
Será introduzidos conceitos básicos utilizados para a desenvolvimento do algoritmo. 

3. ***Algoritmos*:**
Será finalmente abordado as funções e estruturas de dados utilizados na elaboração do algoritmo.

# 1. Introdução

## Problema 
> Dado um grafo G determine as **articulações** e **blocos** de G.

Esse problema é de suma importância nas aplicações de modelagem de grafos, uma vez que a natureza das articulações e blocos nos permite conseguir identificar os pontos e conexões críticas, isso é, pontos regiões de conexão entre duas componentes conexas de um grafo sem alternativas de outras conexões. 

### Aplicações

Modelagem de redes de computadores, mapa de vôo, planejamento de plantas e salas e referenciamento geoespacial.

# 2. Definições

Conceitos e definições básicas de algoritmo de grafos. 

## Articulações

Em um dado grafo $G$, uma **articulação**, ou ***nó crítico***, é um vértice $v$ que sua remoção desconecta $G$. Dessa forma, se $v$ é articulação $G$ então $w(G - v) > w(G)$, ou seja o número de componentes conexas de $G - v$ é maior do que de $G$.   

## Bloco  

Um **bloco** de um grafo $G$ é um subgrafo maximal $H$ em ser conexo e não possuir nenhuma articulação na sua composição. 

## Ponte 

Uma **ponte**, ou ***conexão crítica***, poder ser descrita como um bloco que é composto por uma única aresta (dois vértices conexos). 

# 3. Algoritmos

Para que seja possível definir as articulações e blocos (ou pontes) de um grafo dado G é necessário que seja efetuado o algoritmo de **busca em profundidade** e assim, durante a execução do algoritmo serão definido as articulações do grafo G.

## Estrutura 

Assim como na busca em profundidade, será usado as mesmas estruturas de dados utilizadas para formar a árvore geradora de profundidade, sendo elas: 

1. **`PE(v)`: Profundidade de Entrada de $v$**
2. **`PS(v)`: Profundidade de Saída de $v$**
3. **`pai(v)`: Vértice pai do vértice $v$**

E além dessas estruturas já conhecidas da busca de profundidade será introduzida outro vetor `back(v)`, que irá representar a profundidade de entrada do descendente mais antigo na busca, a partir de $v$.

* ### back(v)

    A estrutura auxiliar que servirá na definição de articulações do grafo $G$.

    **`back(v)`: Profundidade de Entrada do descendente mais antigo na árvore a partir de $v$.**

## Pseudocódigo

Para isso basta implementar algumas linhas adicionais que irá inserir o valor à nova estrutura de dados `back(v)`.
```
Procedimento profundidade(v):
    t <- t + 1;
    PE(v) <- t;
    back(v) <- PE(v);
    para todo vértice w em N(v):
        se PE(w) = 0 então: 
            visitar vw;
            pai(w) <- v;
            executar profundidade(w);
            back(v) <- min(back(v), back(w));
        senão se PS(w) = 0 e w != pai(v) então:
            visitar vw;
            back(v) <- min(back(v), PE(w));
    fim_para
    t <- t + 1;
    PS(v) <- t;
fim_procedimento

```