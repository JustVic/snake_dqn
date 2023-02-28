import pygame
import time
import random

import cv2
 
pygame.init()
 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
gray = (200, 200, 200)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 400
dis_height = 400

 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake a')
 
clock = pygame.time.Clock()
 
snake_block = 25
snake_speed = 40
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
x1 = 0
y1 = 0

snake_List = []
Length_of_snake = 1

terminal = False;

reward = 0

game_over = False

oldx = 0
oldy = 0

oldchangex = 0
oldchangey = 0

direction = 0
olddirection = 0



foodx = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
foody = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0

 
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
 
def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
 
 
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])



def init():
    global x1,y1,x1_change,y1_change,foodx,foody,terminal,snake_List,Length_of_snake;
    x1 = dis_width / 2
    y1 = dis_height / 2
 
    x1_change = 0
    y1_change = 0
 
    snake_List = []
    Length_of_snake = 1
 
    foodx = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
    foody = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0

    terminal = False;


def step(input_actions):

    global x1,y1,foodx,foody,Length_of_snake,terminal,olddirection,direction,x1_change,y1_change;

    reward = 0
    if terminal == True:
        init();

    
    if input_actions[0] == 1:
        if(olddirection != 1):
            direction = 0
            x1_change = -snake_block
            y1_change = 0
    elif input_actions[1] == 1:
        if(olddirection != 0):
            direction = 1
            x1_change = snake_block
            y1_change = 0
    elif input_actions[2] == 1:
        if(olddirection !=3):
            direction = 2
            y1_change = -snake_block
            x1_change = 0
    elif input_actions[3] == 1:
        if(olddirection !=2):
            direction = 3
            y1_change = snake_block
            x1_change = 0

    if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
        terminal = True
        reward = -1
    oldx = x1
    oldy = y1


    x1 += x1_change
    y1 += y1_change

    olddirection = direction


    dis.fill(white)
    pygame.draw.rect(dis, gray, [foodx, foody, snake_block, snake_block])
    snake_Head = []
    snake_Head.append(x1)
    snake_Head.append(y1)
    snake_List.append(snake_Head)
    if len(snake_List) > Length_of_snake:
        del snake_List[0]

    for x in snake_List[:-1]:
        if x == snake_Head:
            terminal = True
            reward = -1
 
    our_snake(snake_block, snake_List)
    #Your_score(Length_of_snake - 1)

    #image_data = cv2.cvtColor(cv2.resize(image_data, (84, 84)), cv2.COLOR_BGR2GRAY)

    #img_bgr = cv2.cvtColor(image_data, cv2.COLOR_RGB2BGR)
    #cv2.imshow("Screenshot", img_bgr);

    #cv2.waitKey(10);

    pygame.display.update()

    image_data = pygame.surfarray.array3d(dis) 
    image_data = image_data.transpose([1, 0, 2])

     
    if x1 == foodx and y1 == foody:
        foodx = round(random.randrange(0, dis_width - snake_block) / 25.0) * 25.0
        foody = round(random.randrange(0, dis_height - snake_block) / 25.0) * 25.0
        Length_of_snake += 1
        reward = 10
    clock.tick(snake_speed)
    return image_data, reward, terminal;

 
#    pygame.quit()
#    quit()
