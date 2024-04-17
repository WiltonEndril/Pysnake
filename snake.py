import curses

def gameLoop(window):
    window.addstr(f'Aperte alguma tecla:\n')
    while True:
        window.timeout(1000)
        char = window.getch()
        window.cls()
        match char:
            case curses.keyUp:
                window.addstr('Mover para cima')
            case curses.keyLeft:
                window.addstr('Move para esquerda')
            case curses.keyDown:
                window.addstr('Move para baixo')
            case curses.keyRight:
                window.addstr('Move para direita')
            case _:
                window.addstr('Não mover')

if __name__ == '__main__':
    curses.wrapper(gameLoop)