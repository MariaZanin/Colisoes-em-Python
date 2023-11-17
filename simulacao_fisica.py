import pygame
import sys

# Inicializar o Pygame
pygame.init()

# Configurações da tela
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Simulação Física em Python")

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Parâmetros do objeto
posicao = [largura // 2, 50]
velocidade = [0, 0]
aceleracao = [0, 0.1]

# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar posição e velocidade do objeto
    velocidade[0] += aceleracao[0]
    velocidade[1] += aceleracao[1]
    posicao[0] += velocidade[0]
    posicao[1] += velocidade[1]

    # Limpar a tela
    tela.fill(branco)

    # Desenhar o objeto
    pygame.draw.circle(tela, preto, (int(posicao[0]), int(posicao[1])), 20)

    # Atualizar a tela
    pygame.display.flip()

    # Limitar a taxa de atualização
    pygame.time.Clock().tick(60)