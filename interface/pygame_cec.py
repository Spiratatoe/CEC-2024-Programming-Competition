import pygame
import random
pygame.init()

black = (0, 0, 0)
white = (255, 255, 255)
green = (0, 100, 0)
red = (255, 0, 0)
blue = (116,204,244)


display_width = 1000
display_height = 600

screen = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption("Team Tunnel Data Visualization")
clock = pygame.time.Clock()

font = pygame.font.Font(None, 48)
small_font = pygame.font.Font(None, 25)

x = [0,2,1,2,0,1,1,0,2,2,2,0,0,0,0,0,0,0,0,1,0,0,0,2,0,0,0,0,0,0]
y = [3,2,2,2,3,2,2,3,2,1,2,3,2,1,3,2,3,1,3,2,2,2,3,0,3,3,3,3,2,3]


num_of_images = 30


#Import all images from files
images = []
num = 0
for i in range(num_of_images):
    stringtest = str(num) + ".png"
    images.append(pygame.image.load(stringtest).convert())
    num += 1 

exit = False
current_image = 0
#Main application loop
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True 
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if current_image > 0:
                    current_image -= 1
            elif event.key == pygame.K_RIGHT:
                if current_image < num_of_images-1:
                    current_image += 1
    

    screen.fill(blue)
    
    #Text
    stringtemp = "Day " + str(current_image)
    text = font.render(stringtemp, True, black)
    size = text.get_rect().width
    screen.blit(text, ((display_width/2)-(size/2),10))
    
    text = font.render("x: " + str(x[current_image]), True, black)
    size = text.get_rect().width
    screen.blit(text, ((1000/2)-(size/2),400))
    text = font.render("y: " + str(y[current_image]), True, black)
    size = text.get_rect().width
    screen.blit(text, ((1000/2)-(size/2),450))


    
    text = small_font.render("< Left Arrow", True, black)
    size = text.get_rect().width
    screen.blit(text, (10,580))
    text = small_font.render("Right Arrow >", True, black)
    size = text.get_rect().width
    screen.blit(text, (880,580))

    #Images
    tempimage = pygame.transform.scale(images[current_image], (400, 300))
    screen.blit(tempimage, ((1000/2)-(400/2),60))

    #Refresh
    pygame.display.update()
    clock.tick(60)
