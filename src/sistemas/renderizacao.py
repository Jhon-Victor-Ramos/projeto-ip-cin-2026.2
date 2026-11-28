from ..entidades.objeto_jogo import ObjetoDeJogo

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