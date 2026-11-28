import pygame

from ..entidades.bloco import Bloco
from ..entidades.jogador import Jogador
from ..entidades.objeto_jogo import ObjetoDeJogo

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

