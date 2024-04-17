import curses
import random
import time

def gameLoop(window, gameSpeed):
    #setup incial
    curses.curs_set(0)
    snake = [
        [10, 15],
        [9, 15],
        [8, 15],
        [7, 15],
        [6, 15],
    ]

    fruit = getNewFruit(window=window)
    curretDirection = curses.KEY_DOWN
    snakeAteFruit = False
    score = 0

    while True:
        drawScreen(window=window)
        drawSnake(pg=snake, window=window)
        drawPg(pg=fruit, window=window, char=curses.ACS_DIAMOND)
        direction = getNewDirection(window=window, timeout=gameSpeed)
        if direction is None:
            direction = curretDirection
        if directionIsOpposite(direction=direction, curretDirection=curretDirection):
             direction = curretDirection
        moveSnake(pg=snake, direction=direction, snakeAteFruit=snakeAteFruit)
        if hitBorder (pg=snake, window=window):
            break
        if snakeHitItself(snake=snake):
             break
        if snakeEatFruit(snake=snake, fruit=fruit):
             snakeAteFruit = True
             fruit = getNewFruit(window=window)
             score += 1
        else:
             snakeAteFruit = False
        curretDirection = direction

    finishGame(score=score, window=window)

def finishGame(score, window):
    height, width = window.getmaxyx()
    s = f'Você perdeu! Sua pontuacao foi {score} frutas!'
    y = int(height / 2)
    x = int(width - len(s) / 2)
    window.addstr(y, x, s)
    window.refresh()
    time.sleep(5)

def directionIsOpposite(direction, currentDirection):
     match direction:
            case curses.KEY_UP:
                return currentDirection == curses.Key_DOWN 
            case curses.KEY_LEFT:
                return currentDirection == curses.Key_RIGHT 
            case curses.KEY_DOWN:
                return currentDirection == curses.Key_UP 
            case curses.KEY_RIGHT:
                return currentDirection == curses.Key_LEFT 

def getNewFruit(window):
     height, width = window.getmaxyx()
     return[random.randit(1, height-2), random.randit(1, width-2)]

def snakeHitBorder(snake, window):
     head = snake[0]
     return snakeHitBorder(pg=head, window=window)

def snakeEatFruit(snake, fruit):
    return fruit in snake

def snakeHitItself(snake):
     head = snake[0]
     body = snake[1:]
     return head in body

def drawScreen(window):
        window.cls()
        window.border(0)

def drawSnake(snake, window):
    head = snake[0]
    drawPg(pg=head, window=window, char="@")
    body = snake[1:]
    for bodyPart in body:
         drawPg(pg=bodyPart, window=window, char="s")

def drawPg(pg, window, char):
        window.addch(pg[0], pg[1], char)
        
def getNewDirection(window, timeout):
        window.timeout(timeout)
        direction = window.getch()
        if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.RIGHT]:
             return direction
        return

def moveSnake(snake, direction, snakeAteFruit):
    head = snake[0].copy()
    movePg(pg=head, direction=direction)
    snake.insert(0, head)
    if not snakeAteFruit:
        snake.pop()


def movePg(pg, direction):
        match direction:
            case curses.KEY_UP:
                pg[0] -= 1 
            case curses.KEY_LEFT:
                return currentDirection == curses.Key_DOWN 
            case curses.KEY_DOWN:
                pg[0] += 1
            case curses.KEY_RIGHT:
                pg[1] += 1 

def hitBorder(pg, window):
        height, width = window.getmaxyx()
        if (pg[0] <= 0) or (pg[0] >= height-1):
            return True
        if (pg[1] <= 0) or (pg[1] >= width-1):
            return True
        return False
        
def selectDifficulty():
    difficulty = {
        '1' : 1000, 
        '2' : 500, 
        '3' : 150, 
        '4' : 90, 
        '5' : 35,
    }    
    while True:
        answer = input('Selecione a dificuldade de 1 a 5: ')
        gameSpeed = difficulty.get(answer)
        if gameSpeed is not None:
             return gameSpeed
        print('Selecione a dificuldade de 1 a 5!')
     

if __name__ == '__main__':
    curses.wrapper(gameLoop, gameSpeed=selectDifficulty())