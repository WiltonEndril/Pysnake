import curses

def gameLoop(window):
    #setup incial
    curses.curs_set(0)
    personagem = [10, 15]

    while True:
        drawScreen(window=window)
        drawPg(pg=personagem, window=window)
        direction = getNewDirection(window=window, timeout=1000)
        if direction is not None:
            movePg(pg=personagem, direction=direction)
        if hitBorder (pg=personagem, window=window):
            return

def drawScreen(window):
        window.cls()
        window.border(0)

def drawPg(pg, window):
        window.addch(pg[0], pg[1], curses.ACS_DIAMOND)
        
def getNewDirection(window, timeout):
        window.timeout(timeout)
        direction = window.getch()
        if direction in [curses.KEY_UP, curses.KEY_LEFT, curses.KEY_DOWN, curses.RIGHT]:
             return direction
        return

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