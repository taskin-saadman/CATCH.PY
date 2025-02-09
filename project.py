import pygame
import random
from images import Images  #importing Images class to retrieve images

#initializing pygame and mixer module
pygame.init()  
pygame.mixer.init()

#background music plays in infinite loop
pygame.mixer.music.load("music.mp3")  
pygame.mixer.music.play(-1) #-1 for infinite looping

#constant window resolution and frames per second variables
WIDTH, HEIGHT, FPS = 700, 800, 60

#game window and window title
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("CATCH.PY")

images = Images() #instance of Images class (constructor call)
basket_image = images.basket_image  #player basket
apple_image = images.apple_image  #red apple
gApple_image = images.gApple_image  #golden apple
bomb_image = images.bomb_image  #bomb
diagonal_bomb_image = images.diagonal_bomb_image #diagonal bomb (same image as normal bomb)
heart_image = images.heart_image  #heart
bg_image = images.bg_image  #background image
magnet_image = images.magnet_image  #magnet
pause_image = images.pause_image  #pause-sign

#player basket (starts at bottom middle)
player_size = 70 
player = pygame.Rect(WIDTH / 2, HEIGHT - 100, player_size, 80)

object_size = 40  #size of falling objects
falling_objects = []  #list of falling objects
object_speed = 5  #falling speed
bomb_speed_multiplier = 1  #bomb falling speed (gets multiplied later)

score = 0  #player score
hearts = 5  #5 hearts(lives) at the start
magnet_active = False  #flag for magnet powerup
magnet_timer = 0  #timer for magnet powerup
paused = False  #game pause flag
game_over = False  #game over flag
font = pygame.font.SysFont('Comic Sans MS', 36) #font for game texts
clock = pygame.time.Clock() #helps to control game fps

#variables associated with object spawning
spawn_interval = 700  #milliseconds
spawn_timer = 0  #timer for object spawning

#function used to restart game after game over
def restart_game():
    #global variables aren't bound within this function
    global falling_objects, score, hearts, game_over, magnet_active, magnet_timer, bomb_speed_multiplier
    falling_objects.clear()
    score = 0
    hearts = 5
    game_over = False
    magnet_active = False
    magnet_timer = 0
    bomb_speed_multiplier = 1

#function used to display hearts(lives)
def display_hearts():
    for _ in range(hearts):
        window.blit(heart_image, ((WIDTH - (_ + 1) * 50), 20))

#function used to display Game Over screen
def game_over_screen():
    game_over_text = font.render("Game Over! :'(", True, (255, 255, 0))
    restart_text = font.render("Press Space to Restart", True, (255, 255, 255))
    score_text = font.render(f"Final Score: {score}", True, (255, 255, 0))
    author_text = font.render("GitHub: taskin-saadman", True, (255, 255, 255))

    window.blit(game_over_text, ((WIDTH / 2 - game_over_text.get_width() / 2), HEIGHT / 2 - 60))
    window.blit(score_text, ((WIDTH / 2 - score_text.get_width() / 2), HEIGHT / 2))
    window.blit(restart_text, ((WIDTH / 2 - restart_text.get_width() / 2), (HEIGHT / 2 + 50)))
    window.blit(author_text, ((WIDTH / 2 - restart_text.get_width() / 2), (HEIGHT / 2 + 100)))

#function used to display pause screen
def pause_screen():
    window.blit(pause_image, ((WIDTH / 2 - pause_image.get_width() / 2), (HEIGHT / 2 - pause_image.get_height() / 2)))
    pygame.display.flip()

#function containing game's main loop
def main():
    #global variables aren't bound within this function
    global spawn_timer, paused, game_over, magnet_active, magnet_timer, hearts, score, bomb_speed_multiplier
    
    running = True #game running flag

    while running:
        window.blit(bg_image, (0, 0))
        window.blit(basket_image, (player.x, player.y))

        #event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #player quits manually
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE: #spacebar was pressed
                    if game_over:
                        restart_game()
                    else:
                        paused = not(paused) #toggle between pause & play

        #player movement (left or right)
        if not(game_over or paused):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and player.x > 0:
                player.x -= 8
            if keys[pygame.K_RIGHT] and player.x < WIDTH - 100:
                player.x += 8
            '''
            when spawn_timer greater or equal to spawn_interval,
            new object is spawned, spawn_timer is reset.

            unless special conditions, 50-50 chance for apple or bomb spawning.
            '''
            spawn_timer += clock.get_time()
            
            if spawn_timer >= spawn_interval:
                spawn_timer = 0
                obj_type: str #name of falling object
                
                if score >= 20 and random.randint(1,14) == 1:
                    #after player scores 20, 1/14 chance to spawn a magnet
                    obj_type = 'magnet'
                elif hearts < 3 and random.randint(1,7) == 1:
                    #if user has less than 3 hearts, 1/7 chance to spawn golden apple
                    obj_type = 'gApple'
                else:
                    if score >= 30 and random.randint(1,5) == 1:
                        #after score is 30, 1/5 chance to spawn a diagonal bomb
                        obj_type = 'diagonal_bomb'
                    elif random.randint(1,2) == 1:
                        #50% chance to spawn a normal bomb if diagonal bomb wasn't spawned
                        obj_type = 'bomb'
                    else:
                        obj_type = 'apple'

                obj_x = random.randint(0, WIDTH - object_size) #random horizontal position of spawned object
                #randomly choose if diagonal bomb goes left or right
                obj_direction = random.choice([-1, 1]) if (obj_type == 'diagonal_bomb') else 0
                falling_objects.append((obj_type, pygame.Rect(obj_x, 0, object_size, object_size), obj_direction))

            #loop handling falling object movement
            for obj in falling_objects.copy(): #using copy, otherwise main list is affected
                obj_type, obj_rect, obj_direction = obj #a tuple of data of spawned object
                #magnets and golden apples fall a bit faster
                obj_rect.y += object_speed * (2.15 if obj_type in ['magnet', 'gApple'] else 1)
                
                if obj_type == 'bomb':
                    obj_rect.y += bomb_speed_multiplier
                
                elif obj_type == 'diagonal_bomb':
                    obj_rect.x += obj_direction * 1.33 #update horizontal movement while falling
                    obj_rect.y += bomb_speed_multiplier

                if obj_rect.y > HEIGHT: #object has fallen below screen
                    falling_objects.remove(obj) #we dont need fallen object in memory anymore
                    if obj_type == 'apple': #if fallen obj was an apple
                        hearts -= 1 #deduct heart
                        game_over = True if hearts == 0 else False
                    continue #handle next object

                if obj_rect.colliderect(player): #falling object collides with player
                    falling_objects.remove(obj) #dont need it in memory anymore
                    if obj_type == 'apple':
                        score += 1
                        #now check if score is a multiple of 20
                        if score % 20 == 0: #bomb speed increases for each 20 score
                            bomb_speed_multiplier *= 1.1
                    elif obj_type == 'gApple':
                        hearts = 5 #hearts refilled
                    elif obj_type in ['bomb', 'diagonal_bomb']:
                        game_over = True
                    elif obj_type == 'magnet':
                        magnet_active = True
                        magnet_timer = pygame.time.get_ticks()

            #magnet lasts 6 seconds
            if magnet_active and (pygame.time.get_ticks() - magnet_timer) <= 6000:
                for obj in falling_objects:
                    obj_type, obj_rect, obj_direction = obj
                    if obj_type in ['apple', 'gApple']:
                        #any apple moves towards middle of the player basket
                        if obj_rect.x < player.x + (player_size / 2):
                            obj_rect.x += 5
                        elif obj_rect.x > player.x + (player_size / 2):
                            obj_rect.x -= 5
            else:
                magnet_active = False #after 6s, update flag

            #display object image (eval() converts str to pythonic expression)
            #based on object name, different falling objects are being accessed
            for obj in falling_objects:
                obj_type, obj_rect, obj_direction = obj
                window.blit(eval(f"{obj_type}_image"), (obj_rect.x, obj_rect.y))

            score_text = font.render(f"Score: {score}", True, (255, 255, 255))
            window.blit(score_text, (10, 10))
            display_hearts()
        elif paused:
            pause_screen()
        else:
            game_over_screen()

        pygame.display.flip()
        clock.tick(FPS) #helps run the game at specified FPS

    pygame.mixer.music.stop()
    pygame.quit()

if __name__ == "__main__":
    main()