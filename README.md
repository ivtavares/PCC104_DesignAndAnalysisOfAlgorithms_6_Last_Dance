# Universidade Federal de Ouro Preto PCC104
## Projeto e Análise de Algoritmos 
### Diminuir e Conquistar Prof. Rodrigo Silva 
### November 25, 2024
## Instruções 
- Para cada conjunto de algoritmos o aluno deve escolher um.
- O aluno deve criar um repositório público no github com todos os códigos desenvolvidos. 
- Em cada implementação o aluno deve: 
  - Apresentar 3 casos de teste 
  - Estar preparado para desenvolver a análise de custo 
  - Estar preparado para responder perguntas sobre o seu próprio código, sobre o algoritmo e sobre o problema que o algoritmo resolve
## Requisitos
Será necessário o pacote pytest ([link](https://docs.pytest.org/en/stable/index.html)) para executar os testes
## Conjunto 1 - Dividir e Conquistar
1. Implemente o algoritmo MergeSort ([link](./conjuntos/conjunto1.py)).
## Conjunto 2 - Programação Dinâmica
1. Implemente os dois algoritmos baseados em programação dinâmica para o problem da mochila ([link](./conjuntos/conjunto2.py)).
## Conjunto 3 - Algoritmos Gulosos
2. Implemente o algorimo de Kruskall ([link](./conjuntos/conjunto3.py)).
### Caso 0
```mermaid
graph LR
    0 ---|10| 1
    0 ---|6| 2
    0 ---|5| 3
    1 ---|15| 3
    2 ---|4| 3

```
### Caso 1
```mermaid
graph LR
    0 ---|1| 1
    1 ---|2| 2
    0 ---|3| 2

```
### Caso 2
```mermaid
graph LR
    0 ---|2| 1
    1 ---|3| 2
    2 ---|4| 3
    3 ---|5| 4

```
### Caso 3
```mermaid
graph LR
    7 ---|1| 6
    8 ---|2| 2
    6 ---|2| 5
    0 ---|4| 1
    2 ---|4| 5
    8 ---|6| 6
    2 ---|7| 3
    7 ---|7| 8
    0 ---|8| 7
    1 ---|8| 2
    3 ---|9| 4
    5 ---|10| 4
    1 ---|11| 7
    3 ---|14| 5
```