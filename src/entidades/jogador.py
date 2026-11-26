import ObjetoDeJogo

class Jogador(ObjetoDeJogo): #Classe filha de Objeto de Jogo. Possui velocidades e um método para movimentação

    def __init__(self, pos_inicial:tuple[float,float], comprimento:float, altura:float, modo:str, velocidade_andar:float, velocidade_pulo:float):
        
        super().__init__(pos_inicial, comprimento, altura, modo)

        self._velocidade_andar:float = velocidade_andar

        self._velocidade_horizontal:float = 0

        self._velocidade_pulo:float = velocidade_pulo #Note que um pulo para cima tem que usar a negação deste valor

        self._velocidade_vertical:float = 0

    def mover(self) -> None:

        self._pos_atual = (self._pos_atual[0] + self._velocidade_horizontal, self._pos_atual[1] + self._velocidade_vertical)

    def mover_horizontal(self) -> None: #Método para movimentar apenas no eixo horizontal

        self._pos_atual = (self._pos_atual[0] + self._velocidade_horizontal, self._pos_atual[1])

    def mover_vertical(self) -> None: #Método para movimentar apenas no eixo vertical

        self._pos_atual = (self._pos_atual[0], self._pos_atual[1] + self._velocidade_vertical)

    #Separar a movimentação em dois instantes diferentes facilita muito checar e lidar com colisões
