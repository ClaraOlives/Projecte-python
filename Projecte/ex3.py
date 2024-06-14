import pygame
from pygame.locals import *
import random
def pex3():
    pygame.init()

    # crear la pestanya
    ancho = 1300
    altura = 1100
    screen_size = (ancho, altura)
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption('Car Game')

    # colors
    gris = (100, 100, 100)
    verde = (76, 208, 56)
    rojo = (200, 0, 0)
    blanco = (255, 255, 255)
    amarillo = (255, 232, 0)

    #fondo
    fondo_imagen = pygame.image.load("images/editarfondo.png").convert()
    fondo_rect = fondo_imagen.get_rect()

    # tamany carretera i voreres
    road_width = 765
    marker_width = 10
    marker_height = 50

    # cordenades linies blanques
    left_lane = 400
    center_lane = 660
    right_lane = 930
    lanes = [left_lane, center_lane, right_lane]

    #posició carretera i voreres
    road = (265, 0, road_width, altura)
    left_edge_marker = (265, 0, marker_width, altura)
    right_edge_marker = (1030, 0, marker_width, altura)

    #animació linies blanques
    lane_marker_move_y = 0

    #coordenades on comença el jugador
    player_x = 680
    player_y = 700

    #configuració FPS
    clock = pygame.time.Clock()
    fps = 120

    #Configuració joc
    gameover = False
    speed = 2
    score = 0

    class Vehicle(pygame.sprite.Sprite):
        
        def __init__(self, image, x, y):
            pygame.sprite.Sprite.__init__(self)
            
            #escala de les imatges
            image_scale = 100 / image.get_rect().width
            new_width = image.get_rect().width * image_scale
            new_height = image.get_rect().height * image_scale
            self.image = pygame.transform.scale(image, (new_width, new_height))
            
            self.rect = self.image.get_rect()
            self.rect.center = [x, y]
            
    class PlayerVehicle(Vehicle):
        #dibuixar el cotxe
        def __init__(self, x, y):
            image = pygame.image.load('images/coche_principal.png')
            super().__init__(image, x, y)
            
    #grups de sprites
    player_group = pygame.sprite.Group()
    vehicle_group = pygame.sprite.Group()

    #cream el cotxu principal i li deim on aparèixer
    player = PlayerVehicle(player_x, player_y)
    player_group.add(player)

    #carregem les imatges dels enemics
    image_filenames = ['coche_lila.png', 'coche_rojo.png', 'coche_verde.png']
    vehicle_images = []
    #afegim les imatges a la llista buida
    for image_filename in image_filenames:
        image = pygame.image.load('images/' + image_filename)
        vehicle_images.append(image)
        
    #carregem la imatge de colisió
    crash = pygame.image.load('images/boom.png')
    crash_rect = crash.get_rect()


    #bucle del joc
    running = True
    while running:
        
        clock.tick(fps)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            #establim el fons
            screen.blit(fondo_imagen, fondo_rect)
            #moviment cotxe principal
            if event.type == KEYDOWN:
                
                if event.key == K_LEFT and player.rect.center[0] > left_lane:
                    player.rect.x -= 250
                elif event.key == K_RIGHT and player.rect.center[0] < right_lane:
                    player.rect.x += 250
                    
                #per detectar si hi ha una colisió
                for vehicle in vehicle_group:
                    if pygame.sprite.collide_rect(player, vehicle):
                        
                        gameover = True
                        
                        #per saber en quin lloc ha estat la colisió
                        if event.key == K_LEFT:
                            player.rect.left = vehicle.rect.right
                            crash_rect.center = [player.rect.left, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                        elif event.key == K_RIGHT:
                            player.rect.right = vehicle.rect.left
                            crash_rect.center = [player.rect.right, (player.rect.center[1] + vehicle.rect.center[1]) / 2]
                
                
        
        
        #dibuixar la carretera
        pygame.draw.rect(screen, gris, road)
        
        #dibuixar les voreres
        pygame.draw.rect(screen, amarillo, left_edge_marker)
        pygame.draw.rect(screen, amarillo, right_edge_marker)
        
        #dibuixar les linies blanques
        lane_marker_move_y += speed * 2
        if lane_marker_move_y >= marker_height * 2 :
            lane_marker_move_y = 0
        for y in range(marker_height * -2, altura, marker_height * 2):
            pygame.draw.rect(screen,blanco, (left_lane + 400, y + lane_marker_move_y, marker_width, marker_height))
            pygame.draw.rect(screen,blanco, (center_lane + -140, y + lane_marker_move_y, marker_width, marker_height))
            
        #dibuixar el cotxe principal
        player_group.draw(screen)
        
        #afegir un cotxe
        if len(vehicle_group) < 2:
            
            #mirar que hi hagi prou espai entre cotxe i cotxe
            add_vehicle = True
            for vehicle in vehicle_group:
                if vehicle.rect.top < vehicle.rect.height * 1.5:
                    add_vehicle = False
                    
            if add_vehicle:
                
                #seleccionar un carril aleatori
                lane = random.choice(lanes)
                
                #eligeix spawnetjar un coxtu aleatori
                image = random.choice(vehicle_images)
                vehicle = Vehicle(image, lane, altura / -2)
                vehicle_group.add(vehicle)
        
        #velocitat del cotxe
        for vehicle in vehicle_group:
            vehicle.rect.y += speed
            
            #quan es cotxu surti de sa pantalla que desapareixi
            if vehicle.rect.top >= altura:
                vehicle.kill()
                
                #i sumar 1 punt a la puntuació
                score += 1
                
                #quan es passin 5 cotxus aumentar la velocitat
                if score > 0 and score % 5 == 0:
                    speed += 1
        
        #dibuixar cotxus
        vehicle_group.draw(screen)
        
        #escriure la puntuació
        font = pygame.font.Font(pygame.font.get_default_font(), 16)
        text = font.render('Puntuación: ' + str(score), True, blanco)
        text_rect = text.get_rect()
        text_rect.center = (60, 30)
        screen.blit(text, text_rect)
        
        #vigilar quan hi hagi una colisió
        if pygame.sprite.spritecollide(player, vehicle_group, True):
            gameover = True
            crash_rect.center = [player.rect.center[0], player.rect.top]
                
        #cartell game over
        if gameover:
            screen.blit(crash, crash_rect)
            
            pygame.draw.rect(screen, rojo, (0, 50, ancho, 100))
            
            font = pygame.font.Font(pygame.font.get_default_font(), 16)
            text = font.render('Game over. Jugar otra vez? (Presione S o N)', True, blanco)
            text_rect = text.get_rect()
            text_rect.center = (ancho / 2, 100)
            screen.blit(text, text_rect)
                
        pygame.display.update()

        #esperar a q el jugador eligeixi entre tornar a jugar o tancar la pestanya
        while gameover:
            
            clock.tick(fps)
            
            for event in pygame.event.get():
                
                if event.type == QUIT:
                    gameover = False
                    running = False
                    
                #si es "s" restablir tot 
                if event.type == KEYDOWN:
                    if event.key == K_s:
                        gameover = False
                        speed = 2
                        score = 0
                        vehicle_group.empty()
                        player.rect.center = [player_x, player_y]
                    elif event.key == K_n:
                        #sinos sortir
                        gameover = False
                        running = False

    pygame.quit()

