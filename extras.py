import pygame
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SPACE:
       return(" ")
    else:
        return("")

def dibujar(screen, letraPrincipal, letrasEnPantalla, candidata, puntos, segundos):
    fondo=pygame.image.load('sol.jpg')  #carga una imagen de fondo
    screen.blit(fondo,(0,0))

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 20)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), 80)

    #Linea del piso
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    ren1 = defaultFont.render("Escribe una Palabra: " + candidata, 1, COLOR_TEXTO)
    ren2 = defaultFont.render("Puntos: " + str(puntos).zfill(3), 1, COLOR_TEXTO)  #zfill(3) para que aparezca tres 0(puntos=000)
    if(segundos<15):
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren3 = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    #escribe grande la palabra (letra por letra) y la letra principal de otro color
    pos = 130
    for i in range(len(letrasEnPantalla)):
        if letrasEnPantalla[i] == letraPrincipal:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, (255, 0, 0)), (pos, 200))
        else:
            screen.blit(defaultFontGrande.render(letrasEnPantalla[i], 1, COLOR_LETRAS), (pos, 200))
        pos = pos + TAMANNO_LETRA_GRANDE

    screen.blit(ren1, (100, 560))
    screen.blit(ren2, (680, 10))
    screen.blit(ren3, (10, 10))

def correctaRepetida(palabrasAcertadas,candidata):
    for palabra in palabrasAcertadas:
        if palabra == candidata:
            return True  #la palabra candidata ya esta en la lista palabrasAcertadas
    return False

def reproducir_musica(musica):
    pygame.mixer.init()
    pygame.mixer.music.load(musica) #carga la pista de sonido
    pygame.mixer.music.play() #reproduce la pista de sonido

def dibujarPalabrasAcertadas(screen, palabrasAcertadas): #pantalla final que muestra las palabras acertadas por el usuario
    fondo=pygame.image.load('sol1.jpg')
    screen.blit(fondo,(0,0))

    defaultFont= pygame.font.Font( pygame.font.get_default_font(), 30)
    defaultFontGrande= pygame.font.Font( pygame.font.get_default_font(), 60)

    ren1 = defaultFontGrande.render("Tus Palabras Correctas", 1, COLOR_TEXTO)

    pos=160 #distancia de largo de apariciones de las palabras
    for i in range(len(palabrasAcertadas)):
        text = defaultFont.render(palabrasAcertadas[i], 1, COLOR_LETRAS)
        text_rect = text.get_rect(center=(ANCHO/2, pos)) #centra el texto solo a lo ancho, el largo esta definido por variable pos
        screen.blit(text, text_rect)
        pos += 30 #hace que aparesca las palabras uno abajo del otra


    text_rect = ren1.get_rect(center=(ANCHO/2, 100)) #centra el texto solo el ancho de la pantalla
    screen.blit(ren1, text_rect)
