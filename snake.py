import curses

def gameLoop(window):
    personagem = [10, 15]
    window.addch(personagem[0], personagem[1], curses.ACS_DIAMOND)
    while True:
        window.timeout(1000)
        char = window.getch()
        window.cls()
        match char:
            case curses.keyUp:
                personagem[0] -= 1 
            case curses.keyLeft:
                personagem[1] -= 1 
            case curses.keyDown:
                personagem[0] += 1
            case curses.keyRight:
                personagem[1] += 1 
            case _: #não apertou a tecla ou n apertou a tecla correta.
                pass
        window.addch(personagem[0], personagem[1], curses.ACS_DIAMOND)
if __name__ == '__main__':
    curses.wrapper(gameLoop)