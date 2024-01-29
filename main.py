#imports libary duh
#wiat rbbrbb
import pygame
import time
import random
#initalize font
pygame.font.init()
#initalizes pygame
pygame.init()
# Load and play the music file
pygame.mixer.music.load('tacos.mp3')  # Replace with your music file path
pygame.mixer.music.play(-1)# '-1' makes the music loop indefinitely
pygame.mixer.music.set_volume(.2)  

#constants (window size and display name)
WIDTH, HEIGHT = 1920, 1080
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge Lang")
#puts background on screen
BG = pygame.transform.scale(pygame.image.load("bg.jpg"), (WIDTH, HEIGHT))
#constants
PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60

PLAYER_VEL = 10
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3
font = pygame.font.SysFont("comicsans", 30)

#creates player 1
def draw (player, elapsed_time, stars):
    WIN.blit(BG, (0, 0))

    time_text = font.render(f"Time: {round(elapsed_time)}s", 1, (255, 255, 255))
    WIN.blit(time_text, (10, 10))

    pygame.draw.rect(WIN, "red", player)

    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    #display update
    pygame.display.update()

def main():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0


    star_add_increament = 2000
    star_count = 0

    stars = []
    hit = False

    while run:  #I HAVE NO IDEA WHAT THE HELL THIS DOES
        star_count += clock.tick(60)

        if star_count > star_add_increament: 
            for _ in range (3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, 0, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)
            star_add_increament = max(200, star_add_increament - 50)
            star_count = 0

        elapsed_time = time.time() - start_time
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
                
                #MOVEMNT    
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_d] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for star in stars[:]: 
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        if hit:
            lost_text = font.render("You lost!", 1, "white")
            WIN.blit(lost_text, ((WIDTH - lost_text.get_width()) / 2, (HEIGHT - lost_text.get_height()) / 2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, stars)

    pygame.quit()  
#idk what this is but if you remove it the entire thing breaks 4 some reason...
if __name__ == "__main__":
    main()
