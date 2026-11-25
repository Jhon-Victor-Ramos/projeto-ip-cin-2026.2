import pygame

from classes import *

def checar_chao(objeto:ObjetoDeJogo, lista_blocos:list) -> bool:

    #Esta função checa se um objeto está acima de um bloco com colisão. Útil para aplicar gravidade e controlar pulos

    result:bool = False

    copia:pygame.Rect = objeto.retangulo().copy() #É feita uma cópia do retângulo do objeto, e ele é movido uma unidade abaixo

    copia.centery += 1

    for piso in lista_blocos: #Para cada piso, é checada a colisão entre o retângulo rebaixado e o piso. Se houver alguma colisão, o resultado é True

        if piso.checar_colisao(copia):

            result = True

    return result

def checar_empurrar_horizontal(jogador:Jogador, lista_blocos:list[Bloco]) -> None:

    #Função para checar se o jogador colide com algum bloco na lista, e se sim, empurrá-lo horizontalmente

    for g in lista_blocos:
        
        if g.checar_colisao(jogador.retangulo()):
        
            g.empurrar_horizontal(jogador)

def checar_empurrar_vertical(jogador:Jogador, lista_blocos:list[Bloco], tem_gravidade:bool) -> None:

    #Função para checar se o jogador colide com algum bloco na lista, e se sim, empurrá-lo verticalmente

    #Se tem_gravidade for verdadeiro, a velocidade vertical do jogador é zerada

    for g in lista_blocos:
        
        if g.checar_colisao(jogador.retangulo()):
        
            g.empurrar_vertical(jogador)

            if tem_gravidade:

                jogador._velocidade_vertical = 0

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

def add_blits(obj:ObjetoDeJogo, sequencia:list, cor:str | None = None) -> None:

    #Esta função adiciona um objeto de jogo ou superfície a uma lista de tuplas com superfícies e retângulos para
    #desenhá-los na tela. Atente-se com a ordem que os objetos são adicionados à lista, pois isso irá definir 
    #quais vão aparecer em frente de quais outras superfícies. 

    if cor != None: #Se uma cor for fornecida, a superfície é preenchida com essa cor. De qualquer forma, checa se é um objeto de jogo ou uma superfície para saber como acessar a superfície

        if isinstance(obj, ObjetoDeJogo):

            obj.fill_surface(cor)

            sequencia.append((obj.get_surface(), obj.retangulo()))

        else:

            obj.fill(cor)

            sequencia.append((obj, obj.get_bounding_rect()))

    else:

        if isinstance(obj, ObjetoDeJogo):

            sequencia.append((obj.get_surface(), obj.retangulo()))

        else:

            sequencia.append((obj, obj.get_bounding_rect()))