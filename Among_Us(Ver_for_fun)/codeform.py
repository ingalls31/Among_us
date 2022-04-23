import pgzrun , pgzero
import random
# from pynput import keyboard
FONT_COLOR = (255, 255, 255) #màu RGB
WIDTH = 1300
HEIGHT = 700
CENTER_X = WIDTH / 2
CENTER_Y = HEIGHT / 2
CENTER = (CENTER_X, CENTER_Y)
START_SPEED = 10
COLORS = ["orange","blue"]
COLOR_CHOICE =  ["orange","blue","red"]
current_level = 1
final_level = 5
game_over = False
game_complete = False
start = True
impostors = []
animations = []

def draw():
    global impostors,current_level,game_over,game_complete
    screen.clear()
    screen.blit("dark",(0,0))
    # if start == True :
    #     display_message("Find Impostor","Press Space To Play Again")
    #     start = False
    if game_over:
        display_message("Game Over","Press Space To Play Again")
    elif game_complete:
        display_message("You Won","Press Space To Play Again")
    else :
        for im in impostors:
            im.draw()

def update():
    # pass
    global impostors,current_level,game_over,game_complete
    if len(impostors) == 0:
        impostors = make_impostors(current_level)
    # if start and keyboard.space:
    #     start = false
    elif (game_complete or game_over) and keyboard.space:
        impostors =[]
        current_level = 1
        game_complete = False
        game_over =False

def make_impostors(number_of_impostors):
    colors_to_create = get_colors_to_create(number_of_impostors)
    new_impostor = create_impostors(colors_to_create)
    layout_impostors(new_impostor)
    animate_impostors(new_impostor)
    return new_impostor

def get_colors_to_create(number_of_impostors):
    colors_to_create = ["red"]
    for i in range(number_of_impostors):
        random_color = random.choice(COLORS)
        colors_to_create.append(random_color)
    return colors_to_create

def create_impostors(colors_to_create):
    new_impostor = []
    for color in colors_to_create:
        impostor = Actor(color + "-im")
        new_impostor.append(impostor)
    return new_impostor
def layout_impostors(impostors_to_layout):
    number_of_gaps = len(impostors_to_layout)+1
    gap_size = WIDTH/number_of_gaps
    random.shuffle(impostors_to_layout)
    for index,impostor in enumerate(impostors_to_layout):
        new_x_pos = (index+1) * gap_size
        impostor.x = new_x_pos

def animate_impostors(impostors_to_animate):
    for impostor in impostors_to_animate:
        duration = START_SPEED - current_level
        impostor.anchor = ("center","bottom")
        animation = animate(impostor,duration=duration,on_finished = handle_game_over,y = HEIGHT)
        animations.append(animation)
def handle_game_over():
    global game_over 
    game_over = True
def on_mouse_down(pos):
    global current_level,impostors
    color = random.choice(COLOR_CHOICE)
    for impostor in impostors:
        if impostor.collidepoint(pos):
            if color in impostor.image:
                red_impostor_click()
            else :
                handle_game_over()

def red_impostor_click():
    global current_level, impostors,animations,game_complete
    stop_animations(animations)
    if current_level == final_level:
        game_complete = True
    else:
        current_level = current_level + 1
        impostors = []
        animations = []

def stop_animations(animations_to_stop):
    for animation in animations_to_stop:
        if animation.running:
            animation.stop()

def display_message(heading_text, sub_heading_text):
    screen.draw.text(heading_text ,fontsize = 60, center = CENTER,color = FONT_COLOR)
    screen.draw.text(sub_heading_text,fontsize = 30,center = (CENTER_X,CENTER_Y + 30),color = FONT_COLOR)

pgzrun.go()
