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

    def get_pos(self) -> tuple[float,float]: #Retorna as coordenadas atuais para evitar alterá-las. Depende do modo

        return self._pos_atual

    def get_center_pos(self) ->tuple[float,float]: #Retorna as coordenadas atuais do centro

        return self.retangulo().center

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

    def checar_colisao(self, rect_point:pygame.Rect | tuple[float, float]) -> bool: #Recebe outro objeto de jogo ou uma coordenada, e checa se há colisão com este retângulo ou ponto

        if isinstance(rect_point, pygame.Rect):

            return bool(self.retangulo().colliderect(rect_point))

        elif isinstance(rect_point, tuple):

            return bool(self.retangulo().collidepoint(rect_point))

