import pygame, math

pygame.init()
pygame.font.init()

white       = (255,255,255)
black       = (  0,  0,  0)
blue        = (142,165,230)
grey        = (196,197,202)
warm_yellow = (255,255,225)
red         = (251, 77, 93)
green       = ( 79,192,120)
purple      = (159,103,217)
light_pink  = (194,154,170)
light_red   = (218, 81, 33)


infoObject = pygame.display.Info()

display_width = infoObject.current_w
display_height = infoObject.current_h

font_size_big = display_width // 100 + display_height // 100 * 3
font_size_medium = display_width // 100 * 2
font_size_small = display_width // 100 * 2 - 5

delta_h = (display_width // 100 - 12) * 2
delta_big_value = 0

x_part = display_width // 4
y_part =  display_height  // 4

h_mere = (y_part * 3 - 10) / 10

s_mere = (display_width - 10 - (x_part * 1.2)) / 17

s_const = s_mere / 50
h_const = h_mere / 50
mere = 0
small_mere = 50
small_mere1 = 50

#gameDisplay = pygame.display.set_mode([display_width,display_height],pygame.FULLSCREEN)
gameDisplay = pygame.display.set_mode((infoObject.current_w, infoObject.current_h),pygame.FULLSCREEN)
pygame.display.set_caption = ('Throwing a Body with the angle to horizon')

pygame.display.iconify

clock = pygame.time.Clock()
gameDisplay.fill(white)

#vars
height_var = 0
length_var = 0
time_var   = 0.1

v0    = '50'
vx    = 0
h0    = '100'
angle = '45'
g = 9.8
placenow = 'nowhere'
kareta_v0 = ''
kareta_h0 = ''
kareta_angle = ''
arr_of_x = []
arr_of_vy = []
arr_of_v = []
arr_of_t = []
arr_of_abs_vy = []

build1_started = False
build2_started = False
build3_started = False
finish_bool = True
button_1_pushed = False
build_button_pressed = False
main_bool1 = False
main_bool2 = False
main_bool3 = False

first_run = True

value_changed = False

move_bool1 = False
move_bool2 = False
move_bool3 = False

slider1 = [x_part * 0.1 + float(v0) * ((0.8 * x_part - 0.15 * y_part) / 1000), y_part * 0.82]
slider2 = [x_part * 0.1 + float(h0) * ((0.8 * x_part - 0.15 * y_part) / 1000), y_part * 1.82]
slider3 = [x_part * 0.1 + float(angle) * ((0.8 * x_part - 0.15 * y_part) / 89), y_part * 2.82]

current_graph = 'h-s'

def return_word(string,size):
    font = pygame.font.SysFont('Arial',size)
    rendered_text = font.render(string, True, black)
    return rendered_text

def slider(number):
    global move_bool1
    global move_bool2
    global move_bool3
    global v0
    global h0
    global angle
    global finish_bool
    global value_changed
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if number == 1:
        x = slider1[0]
        y = slider1[1]
    if number == 2:
        x = slider2[0]
        y = slider2[1]
    if number == 3:
        x = slider3[0]
        y = slider3[1]


    w = 0.15 * y_part
    h = 0.1 * y_part
    if finish_bool == True:
        if move_bool1 == True and not move_bool2 == True and not move_bool3 == True:
            value_changed = True
            if number == 1:
                if  (x_part * 0.1 < mouse[0] - w//2)  and (mouse[0] < x_part * 0.9 - w // 2):
                    slider1[0] = mouse[0] - 0.15 * y_part // 2
        if move_bool2 == True and not move_bool1 == True and not move_bool3 == True:
            value_changed = True
            if number == 2:
                if  (x_part * 0.1 < mouse[0] - w//2)  and (mouse[0] < x_part * 0.9 - w // 2):
                    slider2[0] = mouse[0] - 0.15 * y_part // 2
        if move_bool3 == True and not move_bool1 == True and not move_bool2 == True:
            value_changed = True
            if number == 3:
                if  (x_part * 0.1 < mouse[0] - w//2)  and (mouse[0] < x_part * 0.9 - w // 2):
                    slider3[0] = mouse[0] - 0.15 * y_part // 2

        if (x < mouse[0] < x + w) and (y < mouse[1] < y + h):

            if click[0] == 1:
                value_changed = True
                if number == 1:
                    if  (x_part * 0.1 < mouse[0] - w//2)  and (mouse[0] < x_part * 0.9 - w // 2):
                        move_bool1 = True
                        slider1[0] = mouse[0] - 0.15 * y_part // 2
                if number == 2:
                    if  (x_part * 0.1 < mouse[0] - w//2)  and (mouse[0] < x_part * 0.9 - w // 2):
                        move_bool2 = True
                        slider2[0] = mouse[0] - 0.15 * y_part // 2
                if number == 3:
                    if  (x_part * 0.1 < mouse[0] - w//2)  and (mouse[0] < x_part * 0.9 - w // 2):
                        move_bool3 = True
                        slider3[0] = mouse[0] - 0.15 * y_part // 2
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if click[0] == 0:
        if number == 1:
            move_bool1 = False
        if number == 2:
            move_bool2 = False
        if number == 3:
            move_bool3 = False


    if number == 1:
        pygame.draw.rect(gameDisplay, green , [slider1[0], slider1[1], 0.15 * y_part,0.1 * y_part], 0)
    if number == 2:
        pygame.draw.rect(gameDisplay, green , [slider2[0], slider2[1], 0.15 * y_part,0.1 * y_part], 0)
    if number == 3:
        pygame.draw.rect(gameDisplay, green , [slider3[0], slider3[1], 0.15 * y_part,0.1 * y_part], 0)
    if value_changed:
        v0 = str(math.ceil((slider1[0] - x_part * 0.1) / ((0.8 * x_part - 0.15 * y_part) / 1000)))
        h0 = str(math.ceil((slider2[0] - x_part * 0.1) / ((0.8 * x_part - 0.15 * y_part) / 1000)))
        angle = str(math.ceil((slider3[0] - x_part * 0.1) / ((0.8 * x_part - 0.15 * y_part) / 89)))
        value_changed = False


def draw_axes():
    global main_bool1
    global main_bool2
    global main_bool3
    global delta_big_value
    pygame.draw.rect(gameDisplay, warm_yellow, [x_part + 3, 0, x_part * 3, y_part * 3.5])

    for i in range(1,11):
        pygame.draw.line(gameDisplay,blue,[x_part*1.2, y_part * 3 - i * h_mere],[display_width, y_part * 3 - i * h_mere],1)
    for i in range(1,18):
        pygame.draw.line(gameDisplay,blue,[x_part * 1.2 + i * h_mere,y_part * 3],[x_part * 1.2 + i * h_mere,0],1)

    #h axe
    pygame.draw.line(gameDisplay,black,[x_part*1.2,10],[x_part * 1.2,y_part * 3],2)
    pygame.draw.line(gameDisplay,black,[x_part*1.2,10],[x_part*1.22,40],2)
    pygame.draw.line(gameDisplay,black,[x_part*1.2,10],[x_part*1.18,40],2)
    for i in range(1,10):
        pygame.draw.line(gameDisplay,black,[x_part*1.2 - 9, y_part * 3 - i * h_mere],[x_part * 1.2 + 9 , y_part * 3 - i * h_mere],2)
        word = return_word(str(0+i*small_mere1),font_size_medium - len(str(0+15*small_mere1))*2 + 3)
        gameDisplay.blit(word,(x_part*1.2 - 50 - delta_h * 1.2, y_part * 3 - i * h_mere - 15))
    if current_graph == 'h-s':
        word = return_word('H,м',font_size_small)
    elif current_graph == 'v-t':
        word = return_word('V,м/с',font_size_small)
    elif current_graph == 'vy-t':
        word = return_word('|Vy|,м/с',font_size_small)
    gameDisplay.blit(word,(x_part*1.2 - 50 - delta_h * 2.5, y_part * 3 - 10 * h_mere - 10))


    #length axe
    pygame.draw.line(gameDisplay,black,[x_part * 1.2,y_part * 3],[display_width - 10,y_part * 3],2)
    pygame.draw.line(gameDisplay,black,[display_width - 10,y_part * 3],[display_width - 40,y_part * 3.05],2)
    pygame.draw.line(gameDisplay,black,[display_width - 10,y_part * 3],[display_width - 40,y_part * 2.95],2)

    for i in range(1,16):
        pygame.draw.line(gameDisplay,black,[x_part * 1.2 + i * h_mere,y_part * 3.05],[x_part * 1.2 + i * h_mere,y_part * 2.95],2)
        word = return_word(str(0+i*small_mere),font_size_medium - len(str(0+15*small_mere))*2 + 3)
        gameDisplay.blit(word,(x_part * 1.2 + i * h_mere - word.get_rect().width / 2,y_part * 3.1))
    if current_graph == 'h-s':
        word = return_word('S,м',font_size_small)
    elif current_graph == 'v-t':
        word = return_word('t,c',font_size_small)
    elif current_graph == 'vy-t':
        word = return_word('t,c',font_size_small)
    gameDisplay.blit(word,(x_part * 1.2 + 16.5 * s_mere - word.get_rect().width / 2 - 10,y_part * 3.1))
    # 0 on the axes
    word = return_word(str('0'),font_size_medium)
    gameDisplay.blit(word,[x_part * 1.2 - 35,y_part * 3.1])

    if main_bool1 == False:
        main_bool1 = True
        if current_graph == 'h-s':
            crop_surf = pygame.transform.chop(pygame.transform.chop(gameDisplay,(0,0,x_part,0)),(display_width - x_part,y_part * 3.5,display_width ,y_part * 3.5))
            pygame.image.save(crop_surf,'surface2.png')
    if main_bool2 == False:
        main_bool2 = True
        if current_graph == 'v-t':
            crop_surf = pygame.transform.chop(pygame.transform.chop(gameDisplay,(0,0,x_part,0)),(display_width - x_part,y_part * 3.5,display_width ,y_part * 3.5))
            pygame.image.save(crop_surf,'surface2.png')
    if main_bool3 == False:
        main_bool3 = True
        if current_graph == 'vy-t':
            crop_surf = pygame.transform.chop(pygame.transform.chop(gameDisplay,(0,0,x_part,0)),(display_width - x_part,y_part * 3.5,display_width ,y_part * 3.5))
            pygame.image.save(crop_surf,'surface2.png')


def draw_gui(x_part,y_part):
    global build_button_pressed
    pygame.draw.line(gameDisplay,black,[x_part,0],[x_part,display_height],4)
    pygame.draw.line(gameDisplay,black,[0,y_part],[x_part,y_part],4)
    pygame.draw.line(gameDisplay,black,[0,y_part * 2],[x_part,y_part * 2],4)
    pygame.draw.line(gameDisplay,black,[0,y_part * 3],[x_part,y_part * 3],4)
    pygame.draw.line(gameDisplay,black,[x_part,y_part * 3.5],[display_width,y_part * 3.5],4)

    pygame.draw.line(gameDisplay,black,[x_part*1.5,y_part * 3.5],[x_part*1.5,display_height],4)
    pygame.draw.line(gameDisplay,black,[x_part*2,y_part * 3.5],[x_part*2,display_height],4)
    pygame.draw.line(gameDisplay,black,[x_part*2.5,y_part * 3.5],[x_part*2.5,display_height],4)
    pygame.draw.line(gameDisplay,black,[x_part*3.25,y_part * 3.5],[x_part*3.25,display_height],4)
    #v0
    word = return_word('Начальная скорость', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 0.1))
    button(v0, x_part * 0.1, y_part * 0.45,x_part * 0.8,y_part * 0.3, white, grey,'v0')
    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 0.45,x_part * 0.8,y_part * 0.3],3)
    word = return_word('v0 = ' + v0 + kareta_v0 + ' м/с', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 0.5))

    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 0.82,x_part * 0.8,y_part * 0.1],3)


    slider(1)
    pygame.draw.rect(gameDisplay,purple, [x_part * 0.1, y_part * 0.82,slider1[0] - x_part * 0.1,y_part * 0.1],0)
    #h0
    word = return_word('Начальная высота', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 1.1))
    button(h0, x_part * 0.1, y_part * 1.45,x_part * 0.8,y_part * 0.3, white, grey,'h0')
    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 1.45,x_part * 0.8,y_part * 0.3],3)
    word = return_word('h0 = ' + h0 + kareta_h0 + ' м', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 1.5))

    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 1.82,x_part * 0.8,y_part * 0.1],3)

    slider(2)
    pygame.draw.rect(gameDisplay,purple, [x_part * 0.1, y_part * 1.82,slider2[0] - x_part * 0.1,y_part * 0.1],0)
    #angle
    word = return_word('Угол', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 2.1))
    button(angle, x_part * 0.1, y_part * 2.45,x_part * 0.8,y_part * 0.3, white, grey,'angle')
    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 2.45,x_part * 0.8,y_part * 0.3],3)
    word = return_word('a = ' + angle + kareta_angle + ' град', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 2.5))

    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 2.82,x_part * 0.8,y_part * 0.1],3)

    slider(3)
    pygame.draw.rect(gameDisplay,purple, [x_part * 0.1, y_part * 2.82,slider3[0] - x_part * 0.1,y_part * 0.1],0)

    if not build_button_pressed or current_graph == 'h-s':
        button_build(x_part * 3.25, y_part * 3.5,x_part * 0.75,y_part * 0.5, white, blue)
    word = return_word('Построить', font_size_big)
    gameDisplay.blit(word,(x_part * 3.65 - word.get_rect().width / 2 , y_part * 3.65))

    button_stop(x_part * 2.5, y_part * 3.5,x_part * 0.75,y_part * 0.5, white, blue)
    word = return_word('Завершить', font_size_big)
    gameDisplay.blit(word,(x_part * 2.9 - word.get_rect().width / 2 , y_part * 3.65))

    word = return_word('H(max) : ' + str(height_var) + ' м', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 3.2))

    word = return_word('Дальность : ' + str(length_var) + ' м', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 3.4))

    word = return_word('Время : ' + str(time_var) + ' с', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 3.6))


    button_1(x_part * 1, y_part * 3.5,x_part * 0.5,y_part * 0.5, white, blue)
    word = return_word('f=H(S)', font_size_big)
    gameDisplay.blit(word,(x_part * 1.25 - word.get_rect().width / 2 , y_part * 3.6))

    button_2(x_part * 1.5, y_part * 3.5,x_part * 0.5,y_part * 0.5, white, blue)
    word = return_word('f=V(t)', font_size_big)
    gameDisplay.blit(word,(x_part * 1.75 - word.get_rect().width / 2 , y_part * 3.6))

    button_3(x_part * 2, y_part * 3.5,x_part * 0.5,y_part * 0.5, white, blue)
    word = return_word('f=|Vy(t)|', font_size_big)
    gameDisplay.blit(word,(x_part * 2.25 - word.get_rect().width / 2 , y_part * 3.6))

    exit_button()


def draw_gui_build(x_part,y_part):

    pygame.draw.line(gameDisplay,black,[x_part,0],[x_part,display_height],4)
    pygame.draw.line(gameDisplay,black,[0,y_part],[x_part,y_part],4)
    pygame.draw.line(gameDisplay,black,[0,y_part * 2],[x_part,y_part * 2],4)
    pygame.draw.line(gameDisplay,black,[0,y_part * 3],[x_part,y_part * 3],4)
    pygame.draw.line(gameDisplay,black,[x_part,y_part * 3.5],[display_width,y_part * 3.5],4)

    pygame.draw.line(gameDisplay,black,[x_part*1.5,y_part * 3.5],[x_part*1.5,display_height],4)
    pygame.draw.line(gameDisplay,black,[x_part*2,y_part * 3.5],[x_part*2,display_height],4)
    pygame.draw.line(gameDisplay,black,[x_part*2.5,y_part * 3.5],[x_part*2.5,display_height],4)
    pygame.draw.line(gameDisplay,black,[x_part*3.25,y_part * 3.5],[x_part*3.25,display_height],4)
    #v0
    word = return_word('Start speed', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 0.1))
    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 0.45,x_part * 0.8,y_part * 0.3],3)
    word = return_word('v0 = ' + v0 + kareta_v0 + ' м/с', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 0.5))

    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 0.82,x_part * 0.8,y_part * 0.1],3)
    slider(1)
    pygame.draw.rect(gameDisplay,purple, [x_part * 0.1, y_part * 0.82,slider1[0] - x_part * 0.1,y_part * 0.1],0)
    #h0
    word = return_word('Start height', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 1.1))
    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 1.45,x_part * 0.8,y_part * 0.3],3)
    word = return_word('h0 = ' + h0 + kareta_h0 + ' м', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 1.5))

    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 1.82,x_part * 0.8,y_part * 0.1],3)
    slider(2)
    pygame.draw.rect(gameDisplay,purple, [x_part * 0.1, y_part * 1.82,slider2[0] - x_part * 0.1,y_part * 0.1],0)
    #angle
    word = return_word('Angle', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 2.1))
    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 2.45,x_part * 0.8,y_part * 0.3],3)
    word = return_word('a = ' + angle + kareta_angle + ' град', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 2.5))

    pygame.draw.rect(gameDisplay,black, [x_part * 0.1, y_part * 2.82,x_part * 0.8,y_part * 0.1],3)
    slider(3)
    pygame.draw.rect(gameDisplay,purple, [x_part * 0.1, y_part * 2.82,slider3[0] - x_part * 0.1,y_part * 0.1],0)

    #button_build(x_part * 3.25, y_part * 3.5,x_part * 0.75,y_part * 0.5, white, blue)
    word = return_word('Build', font_size_big)
    gameDisplay.blit(word,(x_part * 3.65 - word.get_rect().width / 2 , y_part * 3.65))

    button_stop(x_part * 2.5, y_part * 3.5,x_part * 0.75,y_part * 0.5, white, blue)
    word = return_word('Finish', font_size_big)
    gameDisplay.blit(word,(x_part * 2.9 - word.get_rect().width / 2 , y_part * 3.65))

    word = return_word('Max. height : ' + str(height_var) + ' м', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 3.2))

    word = return_word('Distance : ' + str(length_var) + ' м', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 3.4))

    word = return_word('Time : ' + str(time_var) + ' c', font_size_big)
    gameDisplay.blit(word,(x_part * 0.5 - word.get_rect().width / 2 , y_part * 3.6))

    button_1(x_part * 1, y_part * 3.5,x_part * 0.5,y_part * 0.5, white, blue)
    word = return_word('f=H(S)', font_size_big)
    gameDisplay.blit(word,(x_part * 1.25 - word.get_rect().width / 2 , y_part * 3.6))

    #button_2(x_part * 1.5, y_part * 3.5,x_part * 0.5,y_part * 0.5, white, blue)
    word = return_word('f=V(t)', font_size_big)
    gameDisplay.blit(word,(x_part * 1.75 - word.get_rect().width / 2 , y_part * 3.6))

    #button_3(x_part * 2, y_part * 3.5,x_part * 0.5,y_part * 0.5, white, blue)
    word = return_word('f=|Vy(t)|', font_size_big)
    gameDisplay.blit(word,(x_part * 2.25 - word.get_rect().width / 2 , y_part * 3.6))

    exit_button()


def button_1(x, y, w, h, ic, ac):
    global finish_bool
    global current_graph
    global button_1_pushed

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < mouse[0] < x + w) and (y < mouse[1] < y + h):
        pygame.draw.rect(gameDisplay, ac, [x + 5, y + 5 , w - 10, h - 10])
        if current_graph == 'h-s':
            pygame.draw.rect(gameDisplay, light_pink, [x + 5, y + 5 , w - 10, h - 10])
        if click[0] == 1:
            #finish_bool = True
            if current_graph == 'h-s':
                pass
            else:
                button_1_pushed = True
                current_graph = 'h-s'

                calculate_values()
                if build1_started and first_run == True:
                    build_trajectory()
    else:
        if current_graph == 'h-s':
            pygame.draw.rect(gameDisplay, light_pink, [x + 5, y + 5 , w - 10, h - 10])
        else:
            pygame.draw.rect(gameDisplay, ic, [x + 5, y + 5 , w - 10, h - 10])

def button_2(x, y, w, h, ic, ac):
    global finish_bool
    global current_graph

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < mouse[0] < x + w) and (y < mouse[1] < y + h):
        pygame.draw.rect(gameDisplay, ac, [x + 5, y + 5 , w - 10, h - 10])
        if current_graph == 'v-t':
            pygame.draw.rect(gameDisplay, light_pink, [x + 5, y + 5 , w - 10, h - 10])
        if click[0] == 1:
            finish_bool = True
            if current_graph == 'v-t':
                pass
            else:
                current_graph = 'v-t'
                calculate_values()
                build_v()
    else:
        if current_graph == 'v-t':
            pygame.draw.rect(gameDisplay, light_pink, [x + 5, y + 5 , w - 10, h - 10])
        else:
            pygame.draw.rect(gameDisplay, ic, [x + 5, y + 5 , w - 10, h - 10])

def button_3(x, y, w, h, ic, ac):
    global finish_bool
    global current_graph

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < mouse[0] < x + w) and (y < mouse[1] < y + h):
        pygame.draw.rect(gameDisplay, ac, [x + 5, y + 5 , w - 10, h - 10])
        if current_graph == 'vy-t':
            pygame.draw.rect(gameDisplay, light_pink, [x + 5, y + 5 , w - 10, h - 10])
        if click[0] == 1:
            finish_bool = True
            if current_graph == 'vy-t':
                pass
            else:
                current_graph = 'vy-t'
                calculate_values()
                build_vy()
    else:
        if current_graph == 'vy-t':
            pygame.draw.rect(gameDisplay, light_pink, [x + 5, y + 5 , w - 10, h - 10])
        else:
            pygame.draw.rect(gameDisplay, ic, [x + 5, y + 5 , w - 10, h - 10])

def button_stop(x, y, w, h, ic, ac):
    global finish_bool
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < mouse[0] < x + w) and (y < mouse[1] < y + h):
        pygame.draw.rect(gameDisplay, ac, [x + 5, y + 5 , w - 10, h - 10])
        if click[0] == 1:
            finish_bool = True
    else:
        pygame.draw.rect(gameDisplay, ic, [x + 5, y + 5 , w - 10, h - 10])

def button_build(x, y, w, h, ic, ac):
    global build_button_pressed
    global first_run
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < mouse[0] < x + w) and (y < mouse[1] < y + h):
        pygame.draw.rect(gameDisplay, ac, [x + 5, y + 5 , w - 10, h - 10])
        if click[0] == 1:
            build_button_pressed = True
            if current_graph == 'h-s':
                calculate_values()
                first_run = False
                build_trajectory()
            elif current_graph == 'v-t':
                calculate_values()
                build_v()
            elif current_graph == 'vy-t':
                calculate_values()
                build_vy()

    else:
        pygame.draw.rect(gameDisplay, ic, [x + 5, y + 5 , w - 10, h - 10])

def button(message, x, y, w, h, ic, ac, place):
    global kareta_v0
    global kareta_h0
    global kareta_angle
    global placenow
    global v0
    global h0
    global angle
    global slider1
    global slider2
    global slider3
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x < mouse[0] < x + w) and (y < mouse[1] < y + h):
        pygame.draw.rect(gameDisplay, ac, [x + 5, y + 5 , w - 10, h - 10])
        if click[0] == 1:
            if place == 'v0':
                placenow = 'v0'
                kareta_v0 = '_'
                kareta_h0 = ''
                kareta_angle = ''

            elif place == 'h0':
                placenow = 'h0'
                kareta_v0 = ''
                kareta_h0 = '_'
                kareta_angle = ''

            elif place == 'angle':
                placenow = 'angle'
                kareta_v0 = ''
                kareta_h0 = ''
                kareta_angle = '_'
    else:
        if placenow == place:
            if click[0] == 1:
                if v0 == '':
                    v0    = '50'
                if h0 == '':
                    h0    = '100'
                if angle == '':
                    angle = '45'
                if v0 == '0':
                    v0 = '1'
                if float(v0) > 1000:
                    v0 = '1000'
                if float(h0) > 1000:
                    h0 = '1000'
                if float(angle) >= 90:
                    angle = '89'
                placenow = 'nowhere'
                kareta_v0 = ''
                kareta_h0 = ''
                kareta_angle = ''

                slider1 = [x_part * 0.1 + float(v0) * ((0.8 * x_part - 0.15 * y_part) / 1000), y_part * 0.82]
                slider2 = [x_part * 0.1 + float(h0) * ((0.8 * x_part - 0.15 * y_part) / 1000), y_part * 1.82]
                slider3 = [x_part * 0.1 + float(angle) * ((0.8 * x_part - 0.15 * y_part) / 89), y_part * 2.82]

def exit_button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (display_width - x_part* 0.1  < mouse[0] < display_width) and (0 < mouse[1] < x_part* 0.1):
        pygame.draw.rect(gameDisplay, light_red, [display_width - x_part* 0.1,0,x_part* 0.1,x_part* 0.1], 0)
        if click[0] == 1:
            pygame.quit()
            quit()
    else:
        pygame.draw.rect(gameDisplay, red, [display_width - x_part* 0.1,0,x_part* 0.1,x_part* 0.1], 0)
    pygame.draw.line(gameDisplay, white, [display_width - x_part* 0.1,0],[display_width,x_part* 0.1], 3)
    pygame.draw.line(gameDisplay, white, [display_width,0],[display_width - x_part* 0.1,x_part* 0.1], 3)

def calculate_values():
    global time_var
    global length_var
    global height_var
    global arr_of_x
    global arr_of_y
    global arr_of_vy
    global arr_of_v
    global arr_of_t
    global arr_of_abs_vy
    global vx
    global mere
    global small_mere
    global small_mere1
    global h_const
    global s_const
    #calculation bottom values
    #length
    length_var = (float(v0)*float(v0)/(2*g))*math.sin(2*math.radians(float(angle)))*(1 + math.sqrt(1 + (2*(g)*float(h0))/(float(v0)*float(v0)
    * math.sin(math.radians(float(angle)))*math.sin(math.radians(float(angle))))))

    str1 = str(length_var - math.floor(length_var))
    str1 = str1[2]
    length_var = math.floor(length_var) + float(str1) * 0.1
    #time
    vrem = math.sin(math.radians(-float(angle)))
    time_var = math.fabs(length_var / (float(v0)*math.cos(math.radians(float(angle)))))
    str1 = str(time_var - math.floor(time_var))
    str1 = str1[2]
    time_var = math.floor(time_var) + float(str1) * 0.1
    #height
    vrem = math.sin(math.radians(float(angle)))
    height_var = (float(h0) + (float(v0)*float(v0)*vrem*vrem)/(2*g))
    str1 = str(height_var - math.floor(height_var))
    str1 = str1[2]
    height_var = math.floor(height_var) + (float(str1) * 0.1)
    if current_graph == 'h-s':
        if length_var > height_var:
            mere = length_var
        else :
            mere = height_var
        mere = math.ceil(mere)

        while not mere % 100 == 0:
            mere += 1

        if length_var > height_var:
            small_mere = mere // 10
            small_mere1  = mere // 10
        else :
            small_mere = mere // 10
            small_mere1 = mere // 10

        s_const = s_mere / small_mere
        h_const = h_mere / small_mere
    elif current_graph == 'v-t':
        mere = time_var
        mere = math.floor(mere)
        while not mere % 10 == 0:
            mere += 1
        small_mere = mere / 10
        h_const = h_mere / small_mere
        small_mere = math.ceil(small_mere)

        max_speed = math.sqrt(float(v0)*float(v0) - 2 * float(v0) * g * time_var * math.sin(math.radians(float(angle))) + g * g * time_var * time_var)
        mere = max_speed
        mere = math.ceil(mere)

        while not mere % 100 == 0:
            mere += 1

        small_mere1 = mere // 10
        s_const = s_mere / small_mere1
    elif current_graph == 'vy-t':
        mere = time_var
        mere = math.floor(mere)
        while not mere % 10 == 0:
            mere += 1
        small_mere = mere / 10
        h_const = h_mere / small_mere
        small_mere = math.ceil(small_mere)

        max_speed = abs(float(v0) * math.sin(math.radians(float(angle))) - g * time_var)
        mere = max_speed
        mere = math.ceil(mere)

        while not mere % 100 == 0:
            mere += 1
        small_mere1 = mere // 10
        s_const = s_mere / small_mere1

    t = 0.0
    y_center = y_part * 3
    x_center = x_part*1.2

    arr_of_x = [x_part*1.2]
    arr_of_y = [y_part * 3 - float(h0) * h_const]
    arr_of_v = [y_part * 3 - float(v0) * s_const]
    arr_of_t = [x_part*1.2]

    vx = float(v0) * math.cos(math.radians(float(angle))) * h_const
    arr_of_vy = [float(v0) * math.sin(math.radians(float(angle)))]
    arr_of_abs_vy = [y_center - arr_of_vy[0] * s_const]
    while arr_of_y[len(arr_of_y)-1] <= y_part * 3 :
    #while t <= time_var:
        arr_of_x.append((float(v0)*t*math.cos(math.radians(-float(angle))))*h_const + x_center)
        arr_of_y.append((float(v0)*t*math.sin(math.radians(-float(angle))) - (-g) * (t ** 2)/2) * h_const + y_center - float(h0) * h_const)
        arr_of_vy.append(((float(v0) * math.sin(math.radians(float(angle))) + (-g) * t)) * h_const)
        arr_of_abs_vy.append(y_center - abs((float(v0) * math.sin(math.radians(float(angle))) + (-g) * t)) * s_const)

        arr_of_v.append(y_center - math.sqrt(float(v0)*float(v0)*math.cos(math.radians(float(angle))) * math.cos(math.radians(float(angle)))
        + (float(v0)*math.sin(math.radians(float(angle))) - g * t)*(float(v0)*math.sin(math.radians(float(angle))) - g * t)) * s_const)

        arr_of_t.append(t * h_const + x_center)

        t += 1 / 30
    #перевести s в пиксели


def build_v():
    global build2_started
    build2_started = True
    calculate_values()
    gameDisplay.fill(white)

    draw_axes()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

    for i in range(0,len(arr_of_v)-2):
        pygame.draw.line(gameDisplay,red,[arr_of_t[i],arr_of_v[i]],[arr_of_t[i+1],arr_of_v[i+1]],4)

    draw_gui(x_part,y_part)

    crop_surf = pygame.transform.chop(pygame.transform.chop(gameDisplay,(0,0,x_part,0)),(display_width - x_part,y_part * 3.5,display_width ,y_part * 3.5))
    pygame.image.save(crop_surf,'surface2.png')
    pygame.display.update()


def build_vy():
    global build3_started
    build3_started = True
    calculate_values()
    gameDisplay.fill(white)

    draw_axes()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()

    for i in range(0,len(arr_of_abs_vy)-2):
        pygame.draw.line(gameDisplay,red,[arr_of_t[i],arr_of_abs_vy[i]],[arr_of_t[i+1],arr_of_abs_vy[i+1]],4)

    draw_gui(x_part,y_part)

    crop_surf = pygame.transform.chop(pygame.transform.chop(gameDisplay,(0,0,x_part,0)),(display_width - x_part,y_part * 3.5,display_width ,y_part * 3.5))
    pygame.image.save(crop_surf,'surface3.png')
    pygame.display.update()


def build_trajectory():
    global build1_started
    global button_1_pushed
    global build_button_pressed
    global finish_bool
    #button_1_pushed = False
    build_button_pressed = False
    finish_bool = False
    build1_started = True
    calculate_values()
    global k
    k = 0
    while True:

        if k == len(arr_of_x)-1 :
            crop_surf = pygame.transform.chop(pygame.transform.chop(gameDisplay,(0,0,x_part,0)),(display_width - x_part,y_part * 3.5,display_width ,y_part * 3.5))
            pygame.image.save(crop_surf,'surface1.png')
            break

        gameDisplay.fill(white)

        draw_axes()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                quit()

        if finish_bool == True or (button_1_pushed and first_run):
            k = len(arr_of_x) - 2
            finish_bool = False
            button_1_pushed = False

        finish_bool = False


        for i in range(0,k):
            pygame.draw.line(gameDisplay,red,[arr_of_x[i],arr_of_y[i]],[arr_of_x[i+1],arr_of_y[i+1]],4)

        pygame.draw.line(gameDisplay,green,[arr_of_x[k],arr_of_y[k]],[arr_of_x[k],arr_of_y[k] - arr_of_vy[k]],4)
        pygame.draw.line(gameDisplay,green,[arr_of_x[k],arr_of_y[k]],[arr_of_x[k] + vx,arr_of_y[k]],4)
        pygame.draw.line(gameDisplay,red,[arr_of_x[k],arr_of_y[k]],[arr_of_x[k] + vx,arr_of_y[k] - arr_of_vy[k]],4)

        i = 0
        while i < vx:
            pygame.draw.line(gameDisplay,green,[arr_of_x[k] + i,arr_of_y[k] - arr_of_vy[k]],[arr_of_x[k] + i + 3,arr_of_y[k] - arr_of_vy[k]],3)
            i += 9
        if  arr_of_vy[k] > 0:
            i = 0
            while i < arr_of_vy[k]:
                pygame.draw.line(gameDisplay,green,[arr_of_x[k] + vx,arr_of_y[k] - i],[arr_of_x[k] + vx,arr_of_y[k] - i - 3],3)
                i += 9
        else:
            i = 0
            while i < - arr_of_vy[k]:
                pygame.draw.line(gameDisplay,green,[arr_of_x[k] + vx,arr_of_y[k] + i],[arr_of_x[k] + vx,arr_of_y[k] + i + 3],3)
                i += 9

        if arr_of_y[k] <= arr_of_y[k] - arr_of_vy[k]:
            pygame.draw.line(gameDisplay,green,[arr_of_x[k],arr_of_y[k] - arr_of_vy[k]],[arr_of_x[k] + 6,arr_of_y[k] - arr_of_vy[k] - 10],4)
            pygame.draw.line(gameDisplay,green,[arr_of_x[k],arr_of_y[k] - arr_of_vy[k]],[arr_of_x[k] - 6,arr_of_y[k] - arr_of_vy[k] - 10],4)
            pygame.draw.line(gameDisplay,red,[arr_of_x[k] + vx,arr_of_y[k] - arr_of_vy[k]],[arr_of_x[k] + vx,arr_of_y[k] - arr_of_vy[k] - 8],4)
        else :
            pygame.draw.line(gameDisplay,green,[arr_of_x[k],arr_of_y[k] - arr_of_vy[k]],[arr_of_x[k] + 6,arr_of_y[k] - arr_of_vy[k] + 10],4)
            pygame.draw.line(gameDisplay,green,[arr_of_x[k],arr_of_y[k] - arr_of_vy[k]],[arr_of_x[k] - 6,arr_of_y[k] - arr_of_vy[k] + 10],4)
            pygame.draw.line(gameDisplay,red,[arr_of_x[k] + vx,arr_of_y[k] - arr_of_vy[k]],[arr_of_x[k] + vx,arr_of_y[k] - arr_of_vy[k] + 8],4)

        pygame.draw.line(gameDisplay,red,[arr_of_x[k] + vx,arr_of_y[k] - arr_of_vy[k]],[arr_of_x[k] + vx - 8,arr_of_y[k] - arr_of_vy[k]],4)

        pygame.draw.line(gameDisplay,green,[arr_of_x[k] + vx,arr_of_y[k]],[arr_of_x[k] - 10 + vx,arr_of_y[k] + 6],4)
        pygame.draw.line(gameDisplay,green,[arr_of_x[k] + vx,arr_of_y[k]],[arr_of_x[k] - 10 + vx,arr_of_y[k] - 6],4)

        pygame.draw.circle(gameDisplay, purple , [math.floor(arr_of_x[k]),math.floor(arr_of_y[k])], 7, 0)
        k += 1

        i = 0
        while i < display_width - x_part*1.2:
            pygame.draw.line(gameDisplay,black,[x_part*1.2 + i,y_part * 3 - height_var * h_const],[x_part*1.2 + i + 1,y_part * 3 - height_var * h_const],2)
            i += 5
        draw_gui_build(x_part,y_part)
        pygame.display.update()
        clock.tick(30)
    finish_bool = True
    button_1_pushed = False

while True:
    gameDisplay.fill(white)
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            quit()
        if placenow != 'nowhere':
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    if placenow == 'v0':
                        if float(v0 + '0') <= 1000:
                            v0 = v0 + '0'
                    if placenow == 'h0':
                        if float(h0 + '0') <= 1000:
                            h0 = h0 + '0'
                    if placenow == 'angle':
                        if float(angle + '0') <= 89:
                            angle = angle + '0'
                if event.key == pygame.K_1:
                    if placenow == 'v0':
                        if float(v0 + '1') <= 1000:
                            v0 = v0 + '1'
                    if placenow == 'h0':
                        if float(h0 + '1') <= 1000:
                            h0 = h0 + '1'
                    if placenow == 'angle':
                        if float(angle + '1') <= 89:
                            angle = angle + '1'
                if event.key == pygame.K_2:
                    if placenow == 'v0':
                        if float(v0 + '2') <= 1000:
                            v0 = v0 + '2'
                    if placenow == 'h0':
                        if float(h0 + '2') <= 1000:
                            h0 = h0 + '2'
                    if placenow == 'angle':
                        if float(angle + '2') <= 89:
                            angle = angle + '2'
                if event.key == pygame.K_3:
                    if placenow == 'v0':
                        if float(v0 + '3') <= 1000:
                            v0 = v0 + '3'
                    if placenow == 'h0':
                        if float(h0 + '3') <= 1000:
                            h0 = h0 + '3'
                    if placenow == 'angle':
                        if float(angle + '3') <= 89:
                            angle = angle + '3'
                if event.key == pygame.K_4:
                    if placenow == 'v0':
                        if float(v0 + '4') <= 1000:
                            v0 = v0 + '4'
                    if placenow == 'h0':
                        if float(h0 + '4') <= 1000:
                            h0 = h0 + '4'
                    if placenow == 'angle':
                        if float(angle + '4') <= 89:
                            angle = angle + '4'
                if event.key == pygame.K_5:
                    if placenow == 'v0':
                        if float(v0 + '5') <= 1000:
                            v0 = v0 + '5'
                    if placenow == 'h0':
                        if float(h0 + '5') <= 1000:
                            h0 = h0 + '5'
                    if placenow == 'angle':
                        if float(angle + '5') <= 89:
                            angle = angle + '5'
                if event.key == pygame.K_6:
                    if placenow == 'v0':
                        if float(v0 + '6') <= 1000:
                            v0 = v0 + '6'
                    if placenow == 'h0':
                        if float(h0 + '6') <= 1000:
                            h0 = h0 + '6'
                    if placenow == 'angle':
                        if float(angle + '6') <= 89:
                            angle = angle + '6'
                if event.key == pygame.K_7:
                    if placenow == 'v0':
                        if float(v0 + '7') <= 1000:
                            v0 = v0 + '7'
                    if placenow == 'h0':
                        if float(h0 + '7') <= 1000:
                            h0 = h0 + '7'
                    if placenow == 'angle':
                        if float(angle + '7') <= 89:
                            angle = angle + '7'
                if event.key == pygame.K_8:
                    if placenow == 'v0':
                        if float(v0 + '8') <= 1000:
                            v0 = v0 + '8'
                    if placenow == 'h0':
                        if float(h0 + '8') <= 1000:
                            h0 = h0 + '8'
                    if placenow == 'angle':
                        if float(angle + '8') <= 89:
                            angle = angle + '8'
                if event.key == pygame.K_9:
                    if placenow == 'v0':
                        if float(v0 + '9') <= 1000:
                            v0 = v0 + '9'
                    if placenow == 'h0':
                        if float(h0 + '9') <= 1000:
                            h0 = h0 + '9'
                    if placenow == 'angle':
                        if float(angle + '9') <= 89:
                            angle = angle + '9'
                if event.key == pygame.K_BACKSPACE:
                    if placenow == 'v0' and len(v0) >= 1:
                        v0 = v0[0:len(v0)-1]
                    if placenow == 'h0' and len(h0) >= 1:
                        h0 = h0[0:len(h0)-1]
                    if placenow == 'angle' and len(angle) >= 1:
                        angle = angle[0:len(angle)-1]
                if v0 != '':
                    slider1 = [x_part * 0.1 + float(v0) * ((0.8 * x_part - 0.15 * y_part) / 1000), y_part * 0.82]
                if h0 != '':
                    slider2 = [x_part * 0.1 + float(h0) * ((0.8 * x_part - 0.15 * y_part) / 1000), y_part * 1.82]
                if angle != '':
                    slider3 = [x_part * 0.1 + float(angle) * ((0.8 * x_part - 0.15 * y_part) / 89), y_part * 2.82]
    draw_axes()
    if build1_started :
        if current_graph == 'h-s':
            surfaceImage = pygame.image.load('surface1.png')
            gameDisplay.blit(surfaceImage,(x_part,0))
    if current_graph == 'v-t':
        surfaceImage = pygame.image.load('surface2.png')
        gameDisplay.blit(surfaceImage,(x_part,0))
    if current_graph == 'vy-t':
        surfaceImage = pygame.image.load('surface3.png')
        gameDisplay.blit(surfaceImage,(x_part,0))


    if current_graph == 'h-s':
        if not build1_started:
            arr_of_x = [x_part*1.2]
            if h0 != '' and v0 != '' and angle != '' and v0 != '0' and angle != '90' and v0 != '0.' and v0 != '0.0' and v0 != '0.00':
                calculate_values()
        if h0 != '' and v0 != '' and angle != '':
            arr_of_y = [y_part * 3 - float(h0) * h_const]
            if not build1_started:
                pygame.draw.circle(gameDisplay, purple, [math.floor(arr_of_x[0]),math.floor(arr_of_y[0])], 7, 0)


    draw_gui(x_part,y_part)

    build_button_pressed = False

    pygame.display.update()
    clock.tick(30)
