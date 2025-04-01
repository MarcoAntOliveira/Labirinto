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