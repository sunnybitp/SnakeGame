import pygame
import random

pygame.mixer.init()
pygame.mixer.music.load('gallery/audio/welcome.mp3')
pygame.mixer.music.play()

pygame.init()
width=500
height=500

# define color
red=(255,0,0)
yellow=(255,255,0)
black=(0,0,0)
white=(255,255,255)
green=(0,128,0)

win=pygame.display.set_mode((width,height))
pygame.display.set_caption("SunnyGame")
img=pygame.image.load('gallery/image/gameOver.png')

bgimg=pygame.image.load('gallery/image/background.jpg')
bgimg =pygame.transform.scale(bgimg,(width,height)).convert_alpha()

clock=pygame.time.Clock()

# defining variables

def mytext(text,color,x,y):
   font=pygame.font.SysFont('Showcard Gothic',30)
   screentext=font.render(text,True,color)
   win.blit(screentext,(x,y))

def plot_snake(window,color,snake_list,snake_size):
   for x,y in snake_list:
      pygame.draw.rect(window,color,(x,y,snake_size,snake_size))



def welcome():
   exit_game=False
   while not exit_game:
      win.fill(white)

      win.blit(bgimg,(0,0))

      mytext("Snake Game",red,10,300)
      mytext("Developed By:",white,10,350)
      mytext("Sunny Suman",white,80,400)
      mytext("Press SpaceBar To Play",red,10,450)

      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            exit_game = True
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
               pygame.mixer.music.load('gallery/audio/background.mp3')
               pygame.mixer.music.play()

               gameloop()
      pygame.display.update()
      clock.tick(30)

               



def gameloop():
      exit_game=False
      game_over=False
      snake_x=50
      snake_y=50
      snake_size=10
      food_x = random.randint(0,width)/2
      food_y = random.randint(0,width)/2
      food_size=10
      vel_x=0
      vel_y=0
      score=0
      snake_list=[]
      snake_length=1
      while not exit_game:


            if game_over:
               win.fill(white)
               win.blit(img,(100,200))
               
               mytext("Press Enter To Continue",red,60,300)
               for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     exit_game=True

                  if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_RETURN:
                        pygame.mixer.music.load('gallery/audio/welcome.mp3')
                        pygame.mixer.music.play()
                        welcome()

            else:
               for event in pygame.event.get():
                  if event.type == pygame.QUIT:
                     exit_game=True



                  if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_UP:
                        vel_y = -5
                        vel_x = 0

                     if event.key == pygame.K_DOWN:
                        vel_y = 5
                        vel_x = 0

                     if event.key == pygame.K_LEFT:
                        vel_x = -5
                        vel_y = 0

                     if event.key == pygame.K_RIGHT:
                        vel_x = 5
                        vel_y = 0

               snake_x = snake_x + vel_x
               snake_y = snake_y + vel_y

               if abs(snake_x - food_x)<6 and abs(snake_y - food_y)<6:
                  score = score + 10
                  food_x = random.randint(0,width)
                  food_y = random.randint(0,width)
                  snake_length = snake_length + 5


               head=[]
               head.append(snake_x)
               head.append(snake_y)
               snake_list.append(head)

              

               if len(snake_list) > snake_length:
                  del snake_list[0]


               if head in snake_list[:-1]:
                  game_over=True
                  pygame.mixer.music.load('gallery/audio/gameover.mp3')
                  pygame.mixer.music.play()


               if snake_x<0 or snake_x>width or snake_y<0 or snake_y>height:
                  game_over=True
                  pygame.mixer.music.load('gallery/audio/gameover.mp3')
                  pygame.mixer.music.play()


               win.fill(black)

               # text
               mytext("Score : " + str(score),yellow,5,5)

               plot_snake(win,green,snake_list,snake_size) # to draw a snake
               
               pygame.draw.rect(win,red,(food_x,food_y,food_size,food_size))

            
            clock.tick(30)
            pygame.display.update()

      pygame.quit()
      quit()

welcome()
