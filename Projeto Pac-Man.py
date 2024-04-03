import pygame
import random
import time

# Inicialização do pygame
pygame.init()

# Dimensões da tela
largura_tela = 800
altura_tela = 600

# Cores
cor_fundo = (0, 0, 0)
cor_personagem = (255, 255, 0)
cor_item = (0, 255, 0)
cor_texto = (255, 255, 255)

# Tamanho do personagem e do item
tamanho_personagem = 30
tamanho_item = 10

# Posição inicial do personagem
posicao_personagem = [largura_tela // 2, altura_tela // 2]

# Velocidade do personagem
velocidade_personagem = 1
velocidade_horizontal = 0
velocidade_vertical = 0

# Pontuação
pontuacao = 0

# Número de itens
numero_itens = 3


def criar_item():
    x = random.randint(0, largura_tela - tamanho_item)
    y = random.randint(0, altura_tela - tamanho_item)
    return [x, y]


# Lista de itens
itens = []
for _ in range(numero_itens):
    item = criar_item()
    item.append(time.time() + random.uniform(0, 2))  # Adiciona tempo limite aleatório
    itens.append(item)

# Função para criar um novo item em uma posição aleatória

# Criação da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo Parecido com Pac-Man")

# Loop principal do jogo
while True:
    # Verificação de eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_LEFT:
                velocidade_horizontal = -velocidade_personagem
            elif evento.key == pygame.K_RIGHT:
                velocidade_horizontal = velocidade_personagem
            elif evento.key == pygame.K_UP:
                velocidade_vertical = -velocidade_personagem
            elif evento.key == pygame.K_DOWN:
                velocidade_vertical = velocidade_personagem
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                velocidade_horizontal = 0
            elif evento.key == pygame.K_UP or evento.key == pygame.K_DOWN:
                velocidade_vertical = 0

    # Atualização da posição do personagem
    posicao_personagem[0] += velocidade_horizontal
    posicao_personagem[1] += velocidade_vertical

    # Verificação de colisão entre o personagem e os itens
    for item in itens:
        if posicao_personagem[0] < item[0] + tamanho_item and \
           posicao_personagem[0] + tamanho_personagem > item[0] and \
           posicao_personagem[1] < item[1] + tamanho_item and \
           posicao_personagem[1] + tamanho_personagem > item[1]:
            pontuacao += 1
            item[0], item[1] = criar_item()
            item[2] = time.time() + random.uniform(0, 2)  # Tempo limite aleatório

    # Verificação de tempo limite dos itens
    for item in itens:
        if time.time() > item[2]:
            item[0], item[1] = criar_item()
            item[2] = time.time() + random.uniform(0, 2)  # Tempo limite aleatório

    # Verificação de colisão com as bordas da tela
    if posicao_personagem[0] < 0 or \
       posicao_personagem[0] + tamanho_personagem > largura_tela or \
       posicao_personagem[1] < 0 or \
       posicao_personagem[1] + tamanho_personagem > altura_tela:
        pontuacao = 0
        for item in itens:
            item[2] = time.time() + random.uniform(0, 2)  # Reinicia o tempo limite de todos os itens

    # Preenchimento da tela
    tela.fill(cor_fundo)

    # Desenho do personagem
    pygame.draw.rect(tela, cor_personagem, (posicao_personagem[0],
                                            posicao_personagem[1], tamanho_personagem, tamanho_personagem))

    # Desenho dos itens
    for item in itens:
        pygame.draw.rect(tela, cor_item, (item[0], item[1], tamanho_item, tamanho_item))

    # Renderização da pontuação na tela
    fonte = pygame.font.Font(None, 36)
    texto_pontuacao = fonte.render("Pontuação: " + str(pontuacao), True, cor_texto)
    tela.blit(texto_pontuacao, (10, 10))

    # Atualização da tela
    pygame.display.flip()
