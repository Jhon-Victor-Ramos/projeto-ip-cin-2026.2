import pygame

def teclado_esquerda(keys:pygame.key.ScancodeWrapper) -> bool: #Função para checar se A ou < foram pressionados, sem D ou >. Útil para movimento do jogador

    result:bool = False

    if (keys[pygame.K_a] or keys[pygame.K_LEFT]) and not (keys[pygame.K_d] or keys[pygame.K_RIGHT]):

        result = True

    return result

def teclado_direita(keys:pygame.key.ScancodeWrapper) -> bool: #Mesma coisa, mas para a direita

    result:bool = False

    if (keys[pygame.K_d] or keys[pygame.K_RIGHT]) and not (keys[pygame.K_a] or keys[pygame.K_LEFT]):

        result = True

    return result

def teclado_cima(keys:pygame.key.ScancodeWrapper) -> bool:

    result:bool = False

    if (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]) and not (keys[pygame.K_DOWN] or keys[pygame.K_s]):

        result = True

    return result

def teclado_baixo(keys:pygame.key.ScancodeWrapper) -> bool:

    result:bool = False

    if (keys[pygame.K_DOWN] or keys[pygame.K_s]) and not (keys[pygame.K_w] or keys[pygame.K_UP] or keys[pygame.K_SPACE]):

        result = True

    return result