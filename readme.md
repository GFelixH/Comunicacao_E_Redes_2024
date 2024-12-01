# **Trabalho de Comunicação e Redes**
* **UFABC 2024**

## Requisitos

Este projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas:

- `pandas`: Manipulação e análise de dados.
- `networkx`: Criação e manipulação de grafos.
- `matplotlib`: Geração de gráficos e visualizações.
- `python-louvain`: Detecção de comunidades no grafo usando o algoritmo Louvain.
- `requests`: Realização de requisições HTTP para acessar a API do OpenAlex.

## Descrição das Métricas

O código calcula várias métricas de rede, como:  

1. Centralidade de Grau: Mede a importância de um nó com base no número de conexões diretas que ele possui.
2. Centralidade de Proximidade: Avalia a proximidade de um nó com todos os outros nós da rede.
3. Centralidade de Intermediação: Mede a quantidade de vezes que um nó aparece como intermediário entre outros nós na rede.
4. Coeficiente de Clusterização: Indica a tendência de um nó formar clusters com seus vizinhos.
5. Assortatividade de Grau: Mede a tendência de nós com graus semelhantes se conectarem entre si.

##Licença

Este projeto está licenciado sob a Licença MIT.