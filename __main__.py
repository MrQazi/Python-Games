import pygame,time,random
from mylib import game

pygame.init()

game_display_width = 800
game_display_height = 800

game_display = pygame.display.set_mode((game_display_width,game_display_height))
frame_rate = pygame.time.Clock()

def home(msg,center,color,size):
    game_display.fill((150,50,0))
    surf, body = game.message(msg,center,size,color)
    game_display.blit(surf,body)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()


def main():
    
    snake = [(400,400),(400,402),(400,404),(400,406),(400,408)]
    score = 0
    speed = 5
    direction = (0,-speed)

    food = (random.randint(20,780),random.randint(20,780))


    while True:
                    
        game_display.fill((50,50,50))
        surf,body = game.message("Score : "+str(score),(750,750),20,(200,200,200))
        game_display.blit(surf,body)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if direction[1] == 0:
                    if event.key == pygame.K_UP:
                        direction = (0,-speed)
                    if event.key == pygame.K_DOWN:
                        direction = (0,speed)
                if direction[0] == 0:
                    if event.key == pygame.K_LEFT:
                        direction = (-speed,0)
                    if event.key == pygame.K_RIGHT:
                        direction = (speed,0)

        for point in range(len(snake)-1,0,-1):
            snake[point] = snake[point-1]

        if snake[0][0] < 10 or snake[0][0] > 790 or snake[0][1] < 10 or snake[0][1] > 790 :
            time.sleep(0.5)
            home("Oops! You Crashed",(400,400),(0,0,150),50)
        
        if len(snake) > 10:
            for i in range(10,len(snake)-1):
                if snake[i][0]-15 < snake[0][0] < snake[i][0]+15 and snake[i][1]-15 < snake[0][1] < snake[i][1]+15 :
                    time.sleep(0.5)
                    home("Oops! You Crashed",(400,400),(0,0,150),50)

        snake[0] = (snake[0][0]+direction[0],snake[0][1]+direction[1])

        if food != None:
            pygame.draw.circle(game_display,(200,0,0),(food),10,10)
            if food[0]-15 < snake[0][0] < food[0]+15 and food[1]-15 < snake[0][1] < food[1]+15:
                food = (random.randint(20,780),random.randint(20,780))
                score += 1
                snake.append((snake[len(snake)-1][0]+(snake[len(snake)-1][0]-snake[len(snake)-2][0]),snake[len(snake)-1][1]+(snake[len(snake)-1][1]-snake[len(snake)-2][1])))


        for point in range(len(snake)):
            pygame.draw.circle(game_display,(0,250*(1-(point/(len(snake)))),0),snake[point],10,10)
        
        pygame.display.update()
        frame_rate.tick(60)

main()