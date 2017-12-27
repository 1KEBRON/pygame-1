# MADE BY KEBRON SOLOMON ZERIE
import pygame
import time
import random


pygame.init()



screen_width = 800
screen_height =600

GameScreen = pygame.display.set_mode( (screen_width, screen_height) )
pygame.display.set_caption( "LITTY" )


#colors

white = (255, 255, 255)
black= (0,0,0)
grey=(213,213,213)
dark_grey=(128, 128, 128)
dark_red=(128,0,0)
light_red=(227,0,0)
fresh_green=(61,201,117)
fresh_blue=(13,255,248)
dark_orange=(255,69,0)
light_orange=(255, 98, 0)
gold=(255,215,0)

all_fonts=pygame.font.get_fonts()
#print (all_fonts)


clock = pygame.time.Clock()

#images
bg  = pygame.image.load("pygame/img/cosmos.jpg").convert()
intro_bg  = pygame.image.load("pygame/img/intro_bg.jpg").convert()
lvl30  = pygame.image.load("pygame/img/lvl30_bg.png").convert()
lvl55  = pygame.image.load("pygame/img/lvl55.jpg").convert()
lvl70  = pygame.image.load("pygame/img/lvl70.png").convert()
the_player = pygame.image.load( 'pygame/img/rocket.png' )
o_fireball  = pygame.image.load("pygame/img/fireball.png")
b_fireball  = pygame.image.load("pygame/img/enmy_lvl70.png")
icon_img= pygame.image.load("pygame/img/icon.png")
pygame.display.set_icon(icon_img)

#sounds
explod_sound=pygame.mixer.Sound("pygame/sound_effect/exploding.wav")
swoosh_sound=pygame.mixer.Sound("pygame/sound_effect/meteor_sound.wav")
takeoff_sound=pygame.mixer.Sound("pygame/sound_effect/takeoff.wav")
pause=False

# .convert.alpha()

player_width=74
player_height=100

enemy_width = 85
enemy_heigth = 200


bg = pygame.transform.scale(bg, (screen_width, screen_height))
lvl70 = pygame.transform.scale(lvl70, (screen_width, screen_height))
intro_bg = pygame.transform.scale(intro_bg,(screen_width, screen_height))
the_player = pygame.transform.scale(the_player, (player_width, player_height))
o_fireball = pygame.transform.scale(o_fireball, (enemy_width, enemy_heigth))
b_fireball = pygame.transform.scale(b_fireball, (enemy_width, enemy_heigth))




def play_button(msg,x,y,w,h,inact_color,act_color,txt_color,txtx,txty,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(GameScreen, act_color, (x, y, w, h))
        if click[0]==1 and action !=None:
            action()

    else:
        pygame.draw.rect(GameScreen, inact_color, (x, y, w, h))

    button_labelP = pygame.font.SysFont("impact", 25)
    GameScreen.blit(button_labelP.render(msg, True, (txt_color)), ((txtx + (w / 2)), y + (txty / 2)))

def quit_button(msge,x,y,w,h,inact_color,act_color,txt_color,txtx,txty,action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(GameScreen, act_color, (x, y, w, h))
        if click[0] == 1 and action != None:
            action()

    else:
        pygame.draw.rect(GameScreen, inact_color, (x, y, w, h))

    button_labelQ = pygame.font.SysFont("Impact", 25)
    GameScreen.blit(button_labelQ.render(msge+"!", True, (txt_color)), (( txtx+ (w / 2)), y + (txty / 2)))


def enemy_avoided(count):
    font = pygame.font.SysFont(None,25,True)
    text= font.render("SCORE: "+str(count),True,fresh_green)
    GameScreen.blit(text,(0,0))

def enemy(the_image,enemy_x, enemy_y):
    GameScreen.blit(the_image, (enemy_x, enemy_y))

def b_enemy(the_image,b_enemy_x, enemy_y):
    GameScreen.blit(the_image, (b_enemy_x, enemy_y))

def player(player_x, player_y):
    # blit_alpha(screen, happy, (100, 100), 128)
    GameScreen.blit( the_player, (player_x, player_y))

def massage_display(text):
    txtfont = pygame.font.SysFont("colibri", 84)
    GameScreen.blit(txtfont.render(text,True,(light_red)),((screen_width/2)-len(text)*15,
                                                           (screen_height/2)))

    pygame.display.update()
    time.sleep(2)

    game_loop()




def info_pause():
    font = pygame.font.SysFont("colibri", 20)
    info_text = "PRESS p to pause"
    GameScreen.blit(font.render(info_text, True, (fresh_blue)), (0,20))


def Quit():
    pygame.quit()
    quit()

def unpause():
    global pause
    pygame.mixer.unpause()
    pause=False

def game_paused():
    pygame.mixer.pause()
    while pause:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        #GameScreen.fill(white)
        font = pygame.font.SysFont("georgia", 82)
        pause_text="PAUSED"
        GameScreen.blit(font.render(pause_text, True, (grey)), ((screen_height / 3), screen_height / 3))
        # play/Quit_button(msg, x, y, w, h, inact_color, act_color, txt_color, txtx, txty, action=None):
        play_button("Resume",150, 350, 100, 30,fresh_green,fresh_blue,black,110,5,unpause)
        quit_button("QUIT",550, 350, 100, 30, dark_red, light_red,grey,510,5,Quit)


        pygame.display.update()
        clock.tick(15)

def game_intro():
    intro=False

    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                quit()
        GameScreen.blit(intro_bg,(0,0))
        intro_text = pygame.font.SysFont("georgia", 82)
        GameScreen.blit(intro_text.render("LITTY", True, (dark_grey)),
                        (345,8))

        # play_button(msg, x, y, w, h, inact_color, act_color, txt_color, txtx, txty, action=None):
        play_button("TAKEOFF",150, 350, 100, 50,fresh_green,fresh_blue,white,110,25,game_loop)
        quit_button("QUIT",550, 350, 100, 50, dark_red,light_red,black,510,25,Quit)


        pygame.display.update()
        clock.tick(15)

def game_over():
    pygame.mixer.Sound.play(explod_sound)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
       
        font = pygame.font.SysFont("georgia", 82)
        the_text="GAMEOVER"
       
        GameScreen.blit(font.render(the_text, True, (grey)), ((screen_height / 3), screen_height / 3))

        # play_button(msg, x, y, w, h, inact_color, act_color, txt_color, txtx, txty, action=None):
        play_button("play again", 162, 325, 110,30, grey, white, black,110,7, game_loop)
        quit_button("QUIT",  550, 325, 80,35, dark_red, light_red,black,518,7, Quit)

        pygame.display.update()
        clock.tick(15)

def game_loop():
    pygame.mixer.Sound.play(takeoff_sound, 1)
    global pause
    player_x = (screen_width * 0.45)
    player_y = (screen_height * 0.8)
    x_change = 0
    enemy_x = random.randrange(0, screen_width)
    enemy_y = -600
    b_enemy_x=random.randrange(0,screen_width)
    enemy_count=1
    enemy_speed=2
    score= 0



    gameExit = False
    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change += -5

                if event.key == pygame.K_RIGHT:
                    x_change += 5
                    
                 #pause button
                if event.key ==pygame.K_p:
                    pause=True
                    game_paused()


              
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    x_change += 5
                if event.key == pygame.K_RIGHT:
                    x_change += -5


             # If the rocket toches the boundries
        if  (player_x + player_width) > screen_width or player_x < 0:
                game_over()

         # Touched Block
        if player_y < enemy_y + enemy_heigth:
                if enemy_x < player_x < enemy_x + enemy_width or enemy_x < player_x + \
                        player_width < enemy_x + enemy_width:
                    game_over()

        # repeat blocks
        if enemy_y > screen_height:
            enemy_y = 0-enemy_heigth
            enemy_x = random.randrange(0,screen_width)
            b_enemy_x=random.randrange(0,screen_width)
            pygame.mixer.Sound.play(swoosh_sound,1)
            pygame.mixer.Sound.set_volume(swoosh_sound,4)
            score += 1
            if score%10==0:
                enemy_speed += 2


        player_x += x_change
        GameScreen.blit(bg,(0,0))
        enemy_y += enemy_speed

        if score>30:
                GameScreen.blit(lvl30, (0, 0))
        if score>55:
            GameScreen.blit(lvl55,(0,0))
        if score>70:
            GameScreen.blit(lvl70, (0, 0))
            b_enemy(b_fireball, b_enemy_x, enemy_y)
        info_pause()
        enemy_avoided(score)
        enemy(o_fireball, enemy_x, enemy_y)
        player(player_x, player_y)
        pygame.display.update()
        clock.tick( 90)
game_intro()
game_loop()
pygame.quit()
quit()
