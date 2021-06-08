#Ayma Khwaja
#ak6xbg


import pygame
import gamebox


#camera
camera = gamebox.Camera(800,600)

#clouds
clouds =gamebox.from_image(200,450,"cloud.png")


#grounds
ground = gamebox.from_color(0,600,"light green",5000,140)
ground2= gamebox.from_color(0,600,"light green",5000,140)


# scrollspeed
scrollspeed = 3.5
scrollspeed2 = 5


#cacti
cactus1 = gamebox.from_image(700,495,"cactt.png")
cactus1.scale_by(.5)

cactus2 = gamebox.from_image(5034,510,"cactt.png")
cactus2.scale_by(.4)

cactus3 = gamebox.from_image(3320,485,"cactt.png")
cactus3.scale_by(.25)

cactus4 = gamebox.from_image(1920,475,"cactt.png")
cactus4.scale_by(.35)


#sun
sun = gamebox.from_image(6000,85,"sunny.png")
sun.scale_by(0.15)
sun.right = cactus3.right
sun.right = cactus4.right


#positioning
clouds.bottom = ground.top
clouds.right = camera.right


ground = gamebox.from_image(0,0, 'grass.png')
ground.scale_by(0.65)

ground.bottom = camera.bottom
ground2.bottom = camera.bottom
ground.right = clouds.left
ground.right = cactus1.left
ground2.right = cactus1.left

ground.right = cactus2.left
ground2.right = cactus2.left

ground2.right = clouds.left
ground.right = sun.left
ground2.right = sun.left
ground.right = cactus4.left
ground.right = cactus3.left

#dino
dino = gamebox.from_image(200,480,"dinoo.png")
dino.scale_by(1)
dino.left = clouds.right
ground.right = dino.right
ground.top = dino.bottom

#background list
background1 = [clouds, ground, ground2, cactus1, cactus2, sun, dino, cactus4]

def place_background1():
#this positions all of the objects in the background from the
# background1 list to make it appear to move
    if clouds.right < camera.left:
        clouds.left = ground.right
    if clouds.right < camera.left:
        clouds.left = ground2.right
    if dino.right < camera.left:
        clouds.left = dino.right
    if cactus1.right < camera.left:
        cactus1.left = ground.right
    if cactus2.right < camera.left:
        cactus2.left = ground.right
    if cactus3.right < camera.left:
        cactus3.left = ground.right
    if cactus4.right < camera.left:
        cactus4.left = ground.right
    if sun.right < camera.left:
        sun.left = ground.right
    if ground.right < camera.left:
        ground.left = clouds.right
    if ground2.right < camera.left:
        ground2.left = clouds.right
    if ground.right < camera.left:
        ground.left = cactus1.right
    if ground.right < camera.left:
        ground.left = cactus2.right
    if ground.right < camera.left:
        ground.left = sun.right
    ground.right = camera.right
    ground2.right = camera.right
    dino.left = camera.left

#list of cacti images
cacti = [cactus1,cactus2,cactus3,cactus4]

#gavity
gravity = .28

#for scoreboad
score = 0

def tick(keys):
    global time
    global gravity
    global score
    scoreboard = gamebox.from_text(camera.left +170, 20, "Score: " +str(score), 24, 'black')
    camera.draw(scoreboard)
    score +=1
    ''' once the score is above 500, the scroll speed advances and more cacti appear making it 
    harder'''
    if score < 500:
        camera.draw(clouds)
        camera.clear("lightblue")
        scoreboard = gamebox.from_text(camera.left + 170, 20, "Score: " + str(score), 24, 'black')
        camera.draw(scoreboard)
        camera.draw(clouds)
        camera.draw(ground)
        camera.draw(ground2)
        camera.x += scrollspeed
    if score > 500:
        camera.draw(clouds)
        camera.clear("blue")
        scoreboard = gamebox.from_text(camera.left + 170, 20, "Score: " + str(score), 24, 'black')
        camera.draw(scoreboard)
        camera.draw(clouds)
        camera.draw(ground)
        camera.draw(ground2)
        camera.x += scrollspeed2
#space bar + jump function
    if pygame.K_SPACE in keys and dino.bottom_touches(ground):
        dino.speedy = -11
    for thing in [dino]:
        thing.speedy += gravity
        thing.move_speed()
        dino.move_to_stop_overlapping(ground)
    for object in background1:
        place_background1()
        camera.draw(object)
    for cactus in cacti:
        camera.draw(cactus)
    '''how the game resets'''
    if dino.touches(cactus1):
        camera.clear("lightblue")
        score = 0
        time = 0
    if dino.touches(cactus2):
        camera.clear("lightblue")
        score = 0
        time = 0
    if dino.touches(cactus3):
        camera.clear("lightblue")
        score = 0
        time = 0
    if dino.touches(cactus4):
        camera.clear("lightblue")
        score = 0
        time = 0

    camera.display()

gamebox.timer_loop(30, tick)
