from .jogador import Jogador
from .objeto_jogo import ObjetoDeJogo

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

    def empurrar_horizontal(self, outro_objeto:Jogador) -> None: 

        '''Método de empurrar, mas apenas com as direções horizontais. 
        Por isso, é possível utilizar apenas a direção da velocidade para saber
        para que direção o jogador deve ser empurrado'''

        outro_pos:tuple[float,float] = outro_objeto.get_pos()

        distancias:dict = {'esquerda': abs(outro_objeto.retangulo().right - self.retangulo().left),
                            'direita': abs(outro_objeto.retangulo().left - self.retangulo().right),}
        
        if outro_objeto._velocidade_horizontal > 0:

            outro_objeto.atualizar_pos((outro_pos[0] - distancias['esquerda'], outro_pos[1]))

        elif outro_objeto._velocidade_horizontal < 0:

            outro_objeto.atualizar_pos((outro_pos[0] + distancias['direita'], outro_pos[1]))

    def empurrar_vertical(self, outro_objeto:Jogador) -> None: #Mesma coisa só que verticalmente

        outro_pos:tuple[float,float] = outro_objeto.get_pos()

        distancias:dict = {'cima': abs(outro_objeto.retangulo().bottom - self.retangulo().top), 
                           'baixo': abs(outro_objeto.retangulo().top - self.retangulo().bottom)}

        if outro_objeto._velocidade_vertical > 0:

            outro_objeto.atualizar_pos((outro_pos[0], outro_pos[1] - distancias['cima']))

        elif outro_objeto._velocidade_vertical < 0:

            outro_objeto.atualizar_pos((outro_pos[0], outro_pos[1] + distancias['baixo']))