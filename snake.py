import curses

def gameLoop(window):
    curses.curs_set(0)
    window.border(0)
    height, widht = window.getmaxyx()

    personagem = [10, 15]
    window.addch(personagem[0], personagem[1], curses.ACS_DIAMOND)
    while True:
        window.timeout(1000)
        char = window.getch()
        window.cls()
        window.border(0)
        match char:
            case curses.KEY_UP:
                personagem[0] -= 1 
            case curses.KEY_LEFT:
                personagem[1] -= 1 
            case curses.KEY_DOWN:
                personagem[0] += 1
            case curses.KEY_RIGHT:
                personagem[1] += 1 
            case _: #não apertou a tecla ou n apertou a tecla correta.
                pass
        if (personagem[0] <= 0) or (personagem[1] >= height-1):
            return
        if (personagem[1] <= 0) or (personagem[1] >= widht-1):
            return
        
        window.addch(personagem[0], personagem[1], curses.ACS_DIAMOND)
if __name__ == '__main__':
    curses.wrapper(gameLoop)
    print('Você perdeu')