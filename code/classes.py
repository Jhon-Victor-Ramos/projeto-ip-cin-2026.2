from __future__ import annotations #Módulo de anotações importado para usar type annotation de uma classe dentro dela mesma

import pygame

class ObjetoDeJogo:

    #Classe mais genérica. Possui posição, dimensões e modo. 
    #O modo se refere a como o retângulo é posicionado: center, topright, topleft, midtop, bottomright, bottomleft, midbottom, midright, midleft.
    #Os métodos e atributos possibilitam movimento, alterar a superfície e retângulo, e checar colisões com outros retângulos ou pontos

    def __init__(self, pos_inicial:tuple[float,float], comprimento:float, altura:float, modo:str): #Os atributos não são privados, mas tomem cuidado ao mexer com eles

        self._pos_inicial:tuple[float,float] = pos_inicial

        self._pos_atual:tuple[float,float] = pos_inicial

        self._comprimento:float = comprimento

        self._altura:float = altura

        self._modo:str = modo

        self._surface:pygame.Surface = pygame.Surface((comprimento, altura))

    def get_surface(self) -> pygame.Surface: #Retorna a superfície para evitar alterá-la

        return self._surface

    def fill_surface(self, cor:str) -> None: #Preenche a superfície com uma cor sólida

        self._surface.fill(cor)

    def atualizar_pos(self, coordenadas:tuple[float,float]) -> None: #Altera as coordendas do objeto para as coordenadas fornecidas

        self._pos_atual = coordenadas

    def get_pos(self) -> tuple[float,float]: #Retorna as coordenadas atuais para evitar alterá-las

        return self._pos_atual

    def retangulo(self) -> pygame.Rect: #Cria um retângulo envolto na superfície. O modo determina qual ponto do retângulo serve de âncora

        result:pygame.Rect = pygame.Rect((0,0), (0,0))

        if self._modo == 'topleft':

            result = self._surface.get_rect(topleft = self._pos_atual)

        elif self._modo == 'topright':

            result = self._surface.get_rect(topright = self._pos_atual)

        elif self._modo == 'midtop':

            result = self._surface.get_rect(midtop = self._pos_atual)

        elif self._modo == 'bottomleft':

            result = self._surface.get_rect(bottomleft = self._pos_atual)

        elif self._modo == 'bottomright':

            result = self._surface.get_rect(bottomright = self._pos_atual)

        elif self._modo == 'midbottom':

            result = self._surface.get_rect(midbottom = self._pos_atual)

        elif self._modo == 'midleft':

            result = self._surface.get_rect(midleft = self._pos_atual)

        elif self._modo == 'midright':

            result = self._surface.get_rect(midright = self._pos_atual)

        elif self._modo == 'center':

            result = self._surface.get_rect(center = self._pos_atual)

        return result

    def mudar_modo(self,novo_modo:str) -> None: #Altera o modo para os retângulos

        self._modo = novo_modo

    def checar_colisao(self, outro:ObjetoDeJogo | tuple[float, float]) -> bool: #Recebe outro objeto de jogo ou uma coordenada, e checa se há colisão com este retângulo ou ponto

        if isinstance(outro, ObjetoDeJogo):

            return bool(self.retangulo().colliderect(outro.retangulo()))

        elif isinstance(outro, tuple):

            return bool(self.retangulo().collidepoint(outro[0], outro[1]))

class Jogador(ObjetoDeJogo): #Classe filha de Objeto de Jogo. Possui velocidades e um método para movimentação

    def __init__(self, pos_inicial:tuple[float,float], comprimento:float, altura:float, modo:str, velocidade_andar:float, velocidade_pulo:float):
        
        super().__init__(pos_inicial, comprimento, altura, modo)

        self._velocidade_andar:float = velocidade_andar

        self._velocidade_horizontal:float = 0

        self._velocidade_pulo:float = (-1) * velocidade_pulo

        self._velocidade_vertical:float = 0

    def mover(self) -> None:

        self._pos_atual = (self._pos_atual[0] + self._velocidade_horizontal, self._pos_atual[1] + self._velocidade_vertical)

class Bloco(ObjetoDeJogo): #Classe filha de Objeto de Jogo. Possui um método para empurrar outros objetos que colidem consigo, servindo como chãos e paredes

    def __init__(self, pos_inicial:tuple[float,float], comprimento:float, altura:float, modo:str):

        super().__init__(pos_inicial, comprimento, altura, modo)

    def empurrar(self, outro_objeto:ObjetoDeJogo) -> None: 

        #Este método verifica a distância que outro objeto de jogo teria que ser movido para parar de colidir com este bloco, e decide baseado na menor distância. Sempre verifique que uma colisão está ocorrendo antes de chamar este método

        outro_pos:tuple[float,float] = outro_objeto.get_pos()

        distancias:dict = {'esquerda': abs(outro_objeto.retangulo().right - self.retangulo().left),
                            'direita': abs(outro_objeto.retangulo().left - self.retangulo().right),
                            'cima': abs(outro_objeto.retangulo().bottom - self.retangulo().top),
                            'baixo': abs(outro_objeto.retangulo().top - self.retangulo().bottom)}

        distancia_minima:str = min(distancias.items(), key = lambda x: x[1])[0]

        if distancia_minima == 'esquerda':

            outro_objeto.atualizar_pos((outro_pos[0] - distancias['esquerda'], outro_pos[1]))

        elif distancia_minima == 'direita':

            outro_objeto.atualizar_pos((outro_pos[0] + distancias['direita'], outro_pos[1]))

        elif distancia_minima == 'cima':

            outro_objeto.atualizar_pos((outro_pos[0], outro_pos[1] - distancias['cima']))

        elif distancia_minima == 'baixo':

            outro_objeto.atualizar_pos((outro_pos[0], outro_pos[1] + distancias['baixo']))