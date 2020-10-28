import sys, pygame

global tela
global tamanhoTela
global largura
global altura
global matrizQuadrados
global matrizPesos
global matrizPosicoes
global matrizObjetos
global minhoca
global minhocaX
global minhocaY
global tartaruga
global tartarugaX
global tartarugaY

pygame.init()

tamanhoTela = largura, altura = 700, 500

tela = pygame.display.set_mode(tamanhoTela)

matrizQuadrados=[
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,1,1,0],
    [0,0,0,1,0,0]
]

matrizPesos=[
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
    [1,1,1,1,1,1],
]

matrizPosicoes=[
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,0]
]

matrizObjetos=[
    [0,0,0,0,0,0],
    [0,1,0,0,0,0],
    [0,0,0,0,0,0],
    [0,0,0,0,0,2]
]

tartarugaX = 0
tartarugaY = 0

def retorna_posicao(matriz,valor):

    posicoes = []

    for i in range(4):
        for j in range(6):

            if(matriz[i][j]==valor):
                posicoes.append([i,j])

    return posicoes

def desenha_grade():

    global tela
    global matrizQuadrados
    global matrizPesos
    global matrizPosicoes
    global matrizObjetos

    # posicoes
    x = 0
    y = 0

    # iteradores
    i = 0
    j = 0

    while (y < 400):

        while (x < 600):

            if(matrizQuadrados[i][j]==0):
                pygame.draw.rect(tela, (0, 0, 0), (x, y, 100, 100), 2)

            else:
                pygame.draw.rect(tela, (0, 0, 255), (x, y, 100, 100))

            matrizPosicoes[i][j] = [x+5,y+5]

            x += 100
            j += 1

        y += 100
        i += 1

        x = 0
        j = 0

def desenha_objetos():

    global tela
    global matrizPosicoes
    global matrizObjetos
    global minhoca
    global tartaruga
    global tartarugaX
    global tartarugaY
    global minhocaX
    global minhocaY

    tartaruga = pygame.image.load('tartaruga.png')
    minhoca = pygame.image.load('minhoca.png')

    tartaruga = pygame.transform.scale(tartaruga, (90, 90))
    minhoca = pygame.transform.scale(minhoca, (90, 90))

    for i in range(4):
        for j in range(6):

            x = matrizPosicoes[i][j][0]
            y = matrizPosicoes[i][j][1]

            if(matrizObjetos[i][j]==1):
                tela.blit(tartaruga, (x, y))
                tartarugaX = x
                tartarugaY = y

            elif (matrizObjetos[i][j]==2):
                tela.blit(minhoca, (x, y))
                minhocaX = x
                minhocaY = y

def faz_animacao():

    global tartaruga
    global tela
    global matrizPosicoes
    global matrizObjetos
    global tartarugaX
    global tartarugaY
    global minhocaX
    global minhocaY

    velocidade= 5

    if(tartarugaX<minhocaX):

        tartarugaX = tartarugaX + velocidade

    elif(tartarugaY<minhocaY):

        tartarugaY = tartarugaY + velocidade

    else:

        tartarugaX = 105
        tartarugaY = 105

    tela.blit (minhoca, ( minhocaX,minhocaY ) )
    tela.blit(tartaruga, (tartarugaX, tartarugaY))


def principal():

    global tela
    global tartaruga
    a = 0

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()


        tela.fill((255, 255, 255))
        desenha_grade()

        if(a==0):
            desenha_objetos()
            a = 1

        faz_animacao()

        pygame.display.update()
        pygame.time.Clock().tick(30)

principal()