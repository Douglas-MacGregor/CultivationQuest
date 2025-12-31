from src.game import Game
from src.events.backend_event import StartScreenEvent
from src.ui.terminal_ui import TerminalUI

def main():
    game = Game(ui= TerminalUI())
    game.ui.clear()
    game.events.append(StartScreenEvent(game))
    game.ui.run(game)

if __name__ == "__main__":
    main()