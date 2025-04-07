
## Labirinto
Implementar os métodos de busca em largura e profundidade para uma ambiente de "labirinto".
Habilidade desenvolvida: compreender como utilizar os métodos de busca na resolução de um problema.

O método deve executar em um ambiente composto por uma matriz quadrada de ordem n (até 10). Células com valor "1" representarão lugares que o agente não poderá percorrer. A célula com valor 2 representa o local de onde o agente iniciará e a célula de valor 3 o lugar onde ele precisa chegar.

Considere o custo de passo com valor igual para qualquer movimentação e que será permitida a movimentação em quadro direções (cima, baixo, esquerda e direita). A implementação deve ter uma função sucessor e uma função de teste de objetivo.
Para mais informações veja:
[como resolver](http://www.galirows.com.br/meublog/blog/proposta-de-trabalho-metodos-de-busca-para-resolver-um-labirinto/)
Para o envio, compacte em um arquivo o que for necessário para a execução do código, instruções sobre dependências para rodar o código e possíveis instruções para execução (caso a interface não seja intuitiva).

O trabalho deve ser implementado em dupla ou individualmente. Indique no fórum o nome da dupla ou se você fará sozinho (pode ser alterado posteriormente, desde que uma semana antes da entrega da atividade).

Habilidade desenvolvida: compreender como utilizar os métodos de busca na resolução de um problema.

Caso esteja com dificuldade em representar o mapa em uma árvore para busca, segue uma breve explicação abaixo:
[explicação](https://www.youtube.com/watch?v=C8otuQJB60c&t=7s)

# Pacman
Este repositório é dedicado ao desenvolvimento do clássico jogo Pacman, com o objetivo de explorar conceitos de programação de jogos e interação com bibliotecas gráficas.

## Bibliotecas Utilizadas
Pygame: Biblioteca principal utilizada para criar e gerenciar a interface gráfica, eventos, e animações do jogo.
Classes Implementadas

## Cenario
Responsável por gerenciar o layout do labirinto, incluindo o desenho das paredes e o controle das regras do jogo.

### Métodos Principais:
#### pintar_coluna
Desenha as colunas do labirinto na tela principal com base no número de linhas especificado.

#### processar_eventos
Controla a movimentação do personagem, utilizando os eventos capturados pela biblioteca Pygame.

#### maze
Gera labirintos com paredes aleatórias, proporcionando novos desafios a cada execução.

#### calcular
Determina se o personagem atingiu uma parede do labirinto, impedindo movimentos inválidos.

## Pacman
Classe responsável por gerenciar as ações e comportamentos do personagem principal.

#### calcular
*determinar os movimentos possiveis que o personagem pode realizar*
