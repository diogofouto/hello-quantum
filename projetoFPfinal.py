# Feito por: Diogo Fouto

def cria_celula(v):
    """cria_celula: gera uma lista que contem o valor da celula"""
    if v not in (-1, 0, 1):
        raise ValueError("cria_celula: argumento invalido.")
    #A representacao escolhida para as celulas foi a lista
    return [v]


def obter_valor(c):
    """obter_valor: retorna o valor da celula"""
    return c[0]


def inverte_estado(c):
    """inverte_estado: inverte o valor da celula (se era -1 fica igual)"""
    if c[0] == -1:
        return c

    c[0] = abs(c[0]-1)

    return c


def eh_celula(arg):
    """eh_celula: verifica se o argumento e celula"""
    return (
            isinstance(arg, list) and len(arg) == 1
            and isinstance(arg[0], int)
            and arg[0] in (-1, 0, 1)
            )


def celulas_iguais(c1, c2):
    """celulas_iguais: verifica se as celulas sao iguais"""
    if not(eh_celula(c1) and eh_celula(c2)):
        return False

    return c1 == c2


def celula_para_str(c):
    """celula_para_str: retorna a string que contem o valor da celula"""
    return "x" if c[0] == -1 else str(c[0])


def cria_coordenada(l, c):
    """
    cria_coordenada: gera uma lista em que as entradas sao a linha e coluna
    da coordenada, respetivamente
    """
    #A representacao escolhida foi uma lista que contem a linha e coluna
    #da coordenada, respetivamente

    if not(l in (0, 1, 2) and c in (0, 1, 2)):
        raise ValueError("cria_coordenada: argumentos invalidos.")
    return [l, c]


def coordenada_linha(c):
    """coordenada_linha: devolve a linha da coordenada"""
    return c[0]


def coordenada_coluna(c):
    """coordenada_coluna: devolve a coluna da coordenada"""
    return c[1]


def eh_coordenada(arg):
    """eh_coordenada: verifica se o argumento e coordenada"""
    return (
            isinstance(arg, list) and len(arg) == 2
            and isinstance(arg[0], int) and isinstance(arg[1], int)
            and arg[0] in (0, 1, 2) and arg[1] in (0, 1, 2)
            )


def coordenadas_iguais(c1, c2):
    """coordenadas_iguais: verifica se as coordenadas sao iguais"""
    if not(eh_coordenada(c1) and eh_coordenada(c2)):
        return False
    return c1 == c2


def coordenada_para_str(c):
    """coordenada_para_str: devolve a string que representa a coordenada"""
    return str((c[0], c[1]))


def tabuleiro_inicial():
    """
    tabuleiro_inicial: devolve o dicionario que representa o tabuleiro
    inicial
    """
    #A representacao escolhida para os tabuleiros foi o dicionario,
    #em que as chaves sao as coordenadas convertidas em str e os valores
    #sao
    return {
            coordenada_para_str(cria_coordenada(0, 0)): cria_celula(-1),
            coordenada_para_str(cria_coordenada(0, 1)): cria_celula(-1),
            coordenada_para_str(cria_coordenada(0, 2)): cria_celula(-1),
            coordenada_para_str(cria_coordenada(1, 0)): cria_celula(0),
            coordenada_para_str(cria_coordenada(1, 1)): cria_celula(0),
            coordenada_para_str(cria_coordenada(1, 2)): cria_celula(-1),
            coordenada_para_str(cria_coordenada(2, 1)): cria_celula(0),
            coordenada_para_str(cria_coordenada(2, 2)): cria_celula(-1)
            }


def tabuleiro_celula(t, coor):
    """tabuleiro_celula: devolve a celula do tabuleiro t na coordenada coor"""
    return t[coordenada_para_str(coor)]


def eh_str_possivel(s):
    """
    eh_str_tabuleiro: verifica se o argumento e uma string valida para
    ser transformada em tabuleiro
    """
    return isinstance(s, str)


def str_para_tabuleiro(s):
    """str_para_tabuleiro: devolve o tabuleiro que representa o argumento"""

    #Testamos se s e string:
    if not eh_str_possivel(s):
        raise ValueError(
                         "str_para_tabuleiro: argumento invalido."
                         )
    #Se for, ja e seguro usar eval(s)
    tuplo = eval(s)
    tabuleiro = {}

    #Testamos o eval(s):
    if not(
           isinstance(eval(s), tuple)
           and len(eval(s)) == 3 and len(eval(s)[0]) == 3
           and len(eval(s)[1]) == 3 and len(eval(s)[2]) == 2
            ):
        raise ValueError(
                         "str_para_tabuleiro: argumento invalido."
                         )

    for i in range(len(tuplo)):
        for e in range(len(tuplo[i])):
            if not(isinstance((tuplo[i])[e], int) and (tuplo[i])[e] in (-1, 0, 1)):
                raise ValueError("str_para_tabuleiro: argumento invalido.")

    #Vamos colocando no tabuleiro as entradas de acordo com o eval(s)

    #As entradas do terceiro tuplo de eval(s) passam a ser nas coordenadas
    #(2,1) e (2,2), respetivamente, no dicionario
            if i == 2:
                tabuleiro[coordenada_para_str(cria_coordenada(i, e + 1))] = \
                cria_celula((tuplo[i])[e])

    #As restantes, ficam nas coordenadas normais
            else:
                tabuleiro[coordenada_para_str(cria_coordenada(i, e))] = \
                cria_celula((tuplo[i])[e])

    return tabuleiro


def tabuleiro_dimensao(t):
    """
    tabuleiro_dimensao: devolve o inteiro que representa a dimensao do
    tabuleiro
    """
    return 3


def eh_tabuleiro(arg):
    """eh_tabuleiro: verifica se o argumento e um tabuleiro"""

    #Condicoes para ser dicionario:
    if not(
           isinstance(arg, dict) and len(arg) == 8
           and (coordenada_para_str(cria_coordenada(2, 0)) not in arg)
           ):
        return False

    for i in arg:
        #Aqui testamos cada chave do dicionario
        if not(
               isinstance(i, str) and isinstance(eval(i), tuple)
               and len(eval(i)) == 2
               ):
            return False

        if not eh_celula(arg[i]):
            #Testamos as celulas do dicionario
            return False

        for e in eval(i):
            if not(isinstance(e, int) and e in (0, 1, 2)):
                return False

    return True


def tabuleiro_substitui_celula(t, cel, coor):
    """
    tabuleiro_substitui_celula: substitui a celula do tabuleiro t
    na coordenada coor pela celula cel
    """
    if not(eh_tabuleiro(t) and eh_celula(cel) and eh_coordenada(coor)):
        raise ValueError("tabuleiro_substitui_celula: argumentos invalidos.")
    # Substituir a celula
    t[coordenada_para_str(coor)] = cel

    return t


def tabuleiro_inverte_estado(t, coor):
    """
    tabuleiro_inverte_estado: inverte a celula presente na coordenada coor
    do tabuleiro t
    """
    if not(eh_tabuleiro(t) and eh_coordenada(coor)):
        raise ValueError("tabuleiro_inverte_estado: argumentos invalidos.")

    #Faz o recurso a funcoes já definidas para inverter o estado da celula
    tabuleiro_substitui_celula(t, inverte_estado(tabuleiro_celula(t, coor)), coor)
    return t


def tabuleiros_iguais(t1, t2):
    """tabuleiros_iguais: verifica se os tabuleiros sao iguais"""

    if not(eh_tabuleiro(t1) and eh_tabuleiro(t2)):
        return False

    return t1 == t2


def tabuleiro_para_str(t):
    """tabuleiro_para_str: devolve a string que representa o tabuleiro t"""

    return (
            '+-------+\n|...'
            + celula_para_str(tabuleiro_celula(t, cria_coordenada(0, 2)))
            + '...|\n|..'
            + celula_para_str(tabuleiro_celula(t, cria_coordenada(0, 1)))
            + '.'
            + celula_para_str(tabuleiro_celula(t, cria_coordenada(1, 2)))
            + '..|\n|.'
            + celula_para_str(tabuleiro_celula(t, cria_coordenada(0, 0)))
            + '.'
            + celula_para_str(tabuleiro_celula(t, cria_coordenada(1, 1)))
            + '.'
            + celula_para_str(tabuleiro_celula(t, cria_coordenada(2, 2)))
            + '.|\n|..'
            + celula_para_str(tabuleiro_celula(t, cria_coordenada(1, 0)))
            + '.'
            + celula_para_str(tabuleiro_celula(t, cria_coordenada(2, 1)))
            + '..|\n+-------+'
            )


def aplicar_porta_x_ou_z(t, x, y, p):
    """
    aplicar_porta_x_ou_z: aplica a porta x ou z baseado nos argumentos:
    t = tabuleiro
    x = coluna onde inverter as celulas
    y = linha  onde inverter as celulas
    p = indica se a porta e aplicada a direita ou a esquerda
    """
    if p == "D":
        for i in (0, 1, 2):
            tabuleiro_inverte_estado(t, cria_coordenada(i, x))

    else:
        for i in (0, 1, 2):
            tabuleiro_inverte_estado(t, cria_coordenada(y, i))

    return t


def porta_entradas_validas(t, p):
    """porta_entradas_validas: verifica a validade dos argumentos t e p"""

    return (eh_tabuleiro(t) and p in ("D", "E"))


def porta_x(t, p):
    """porta_x: aplica a porta x ao tabuleiro t na posicao p"""

    if not porta_entradas_validas(t, p):
        raise ValueError("porta_x: argumentos invalidos.")
    #x indica a coluna onde as celulas vao ser invertidas
    #y indica a linha onde as celulas vao ser invertidas
    x, y = 1, 1

    return aplicar_porta_x_ou_z(t, x, y, p)


def porta_z(t, p):
    """porta_z: aplica a porta z ao tabuleiro t na posicao p"""

    if not porta_entradas_validas(t, p):
        raise ValueError('porta_z: argumentos invalidos.')
    #Mesmas instrucoes para x, y que a porta x
    x, y = 2, 0

    return aplicar_porta_x_ou_z(t, x, y, p)


def porta_h(t, p):
    """porta_h: aplica a porta h ao tabuleiro t na posicao p"""

    if not porta_entradas_validas(t, p):
        raise ValueError('porta_h: argumentos invalidos.')
    #Criamos um dicionario temporario que ira guardar os valores do tabuleiro
    #que serao perdidos ao inverter as colunas ou linhas
    dicionario_temporario = {}

    if p == "D":
        #Inverte a segunda coluna com a primeira
        for e in (0, 1, 2):
            dicionario_temporario[str(e)] = tabuleiro_celula(t, cria_coordenada(e, 2))

            #Trocamos os valores das coordenadas:
            tabuleiro_substitui_celula(t, \
            tabuleiro_celula(t, cria_coordenada(e, 1)), cria_coordenada(e, 2))
            #Recorremos ao dicionario temporario para restaurar os valores perdidos:
            tabuleiro_substitui_celula(t, dicionario_temporario[str(e)], cria_coordenada(e, 1))

    else:
        #Mesmo funcionamento do dicionario temporario e troca de valores que p == "D",
        #mas, neste caso, p == "E":
        for e in (0, 1, 2):
            dicionario_temporario[str(e)] = tabuleiro_celula(t, cria_coordenada(1, e))

            tabuleiro_substitui_celula(t, \
            tabuleiro_celula(t, cria_coordenada(0, e)), cria_coordenada(1, e))

            tabuleiro_substitui_celula(t, dicionario_temporario[str(e)], cria_coordenada(0, e))

    return t


def hello_quantum(s):
    """hello_quantum: funcao que permite jogar o jogo"""

    lista_dados = s.split(":")
    tab_final = str_para_tabuleiro(lista_dados[0])
    num_jogadas = int(lista_dados[1])

    #Comeca o jogo
    print(
          "Bem-vindo ao Hello Quantum!\n"
          "O seu objetivo e chegar ao tabuleiro:\n"
          + tabuleiro_para_str(tab_final)
          + "\nComecando com o tabuleiro que se segue:"
          )

    # O jogo e jogavel dentro do numero limite de jogadas estabelecido
    for i in range(num_jogadas):
        print(tabuleiro_para_str(tab_jogo))

        qual_porta = input("Escolha uma porta para aplicar (X, Z ou H): ")
        qual_qubit = input("Escolha um qubit para analisar (E ou D): ")

        #Executa a porta correta:
        if qual_porta == "X":
            porta_x(tab_jogo, qual_qubit)

        elif qual_porta == "Z":
            porta_z(tab_jogo, qual_qubit)

        elif qual_porta == "H":
            porta_h(tab_jogo, qual_qubit)

        #Se for completado dentro das condicoes:
        if tabuleiros_iguais(tab_jogo, tab_final):
            print("Parabens, conseguiu converter o tabuleiro em", i+1, "jogadas!")
            break
            
    #Retorna o resultado:
    return tabuleiros_iguais(tab_jogo, tab_final)
