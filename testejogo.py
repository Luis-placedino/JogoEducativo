import pygame
import random
import time
pygame.init() 


icone = pygame.image.load("assets/doce.png")
pygame.display.set_caption("")
pygame.display.set_icon(icone)
largura = 770
altura = 635
display = pygame.display.set_mode((largura, altura))
fps = pygame.time.Clock()
fundo = pygame.image.load("assets/dentes.png")
crianca = pygame.image.load("assets/cria.png")
bolo = pygame.image.load("assets/doce.png")
preto = (0, 0, 0)
branco = (255, 255, 255)

def text_objects(texto, fonte):
    textSurface = fonte.render(texto, True, preto)
    return textSurface, textSurface.get_rect()
def message_display(text):
    fonte = pygame.font.Font("freesansbold.ttf",50)
    TextSurf, TextRect = text_objects(text, fonte)
    TextRect.center = ((largura/2), (altura/2))
    display.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(3)
    jogo()
def dead(desvios):
  
    message_display("você desviou da cárie "+str(desvios)+" vezes")

def escrevendoPlacar(desvios):
    font = pygame.font.SysFont(None, 25)
    texto = font.render("desvios:"+str(desvios), True, preto)
    display.blit(texto, (0, 0))
    
def jogo():
    pygame.mixer.music.load('assets/baby.WAV')
    pygame.mixer.music.play(-1) # -1 é loopig infinito
    criancaPosicaoX = largura * 0.45
    criancaPosicaoY = altura * 0.8
    criancaLargura = 80 
    movimentoX = 0
    boloPosicaoX = largura * 0.45
    boloPosicaoY = -220
    boloLargura = 30
    boloAltura = 36
    boloVelocidade = 5

    desvios = 0

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                quit() 
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoX = -10
                elif evento.key == pygame.K_RIGHT:
                    movimentoX = 10
            if evento.type == pygame.KEYUP:
                movimentoX = 0

        
        display.fill(branco)  
        display.blit(fundo, (0, 0))  
        criancaPosicaoX = criancaPosicaoX + movimentoX
        if criancaPosicaoX < 0:
            criancaPosicaoX = 0
        elif criancaPosicaoX > 680:
            criancaPosicaoX = 680
        display.blit(crianca, (criancaPosicaoX, criancaPosicaoY))
        display.blit(bolo, (boloPosicaoX, boloPosicaoY))
        boloPosicaoY = boloPosicaoY + boloVelocidade
        
        if boloPosicaoY > altura:
           
            boloPosicaoY = -220
            boloVelocidade += 1
            boloPosicaoX = random.randrange(0, largura-50)
            desvios = desvios + 1
        escrevendoPlacar(desvios)
        if criancaPosicaoY < boloPosicaoY + boloAltura:
            if criancaPosicaoX < criancaPosicaoX and criancaPosicaoX+criancaLargura > boloPosicaoX or boloPosicaoX+boloLargura > criancaPosicaoX and boloPosicaoX+boloLargura < criancaPosicaoX+criancaLargura:
                dead(desvios)
        # [fim]análise de colisão:
        pygame.display.update()
        fps.tick(60)
jogo()
print("Volte sempre....")
