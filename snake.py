import curses

def gameLoop(window):
    #setup incial
    curses.curs_set(0)
    snake = [
        [10, 15],
        [9, 15],
        [8, 15],
        [7, 15],
        [6, 15],
    ]

    curretDirection = curses.KEY_DOWN

    while True:
        drawScreen(window=window)
        drawSnake(pg=snake, window=window)
        direction = getNewDirection(window=window, timeout=1000)
        if direction is None:
            direction = curretDirection
            moveSnake(pg=snake, direction=direction)
        if hitBorder (pg=snake, window=window):
            return
        curretDirection = direction

def snakeHitBorder(Snake, window):
     head = snake[0]
     return snakeHitBorder(pg=head, window=window)

def drawScreen(window):
        window.cls()
        window.border(0)

def drawSnake(snake, window, char):
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

def moveSnake(snake, direction):
    head = snake[0].copy()
    movePg(pg=head, direction=direction)
    snake.insert(0, head)
    snake.pop()


def movePg(pg, direction):
        match direction:
            case curses.KEY_UP:
                pg[0] -= 1 
            case curses.KEY_LEFT:
                pg[1] -= 1 
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
        
    
if __name__ == '__main__':
    curses.wrapper(gameLoop)
    print('Você perdeu')