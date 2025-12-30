from .abstract_ui import UIInterface

class TerminalUI(UIInterface):
    def __init__(self):
        self.running = True
        self.current_screen = "main"

    def run(self, game):
        while self.running and game.state.player.alive:
            if self.current_screen == "main":
                self.main_menu(game)

            elif self.current_screen == "training":
                self.training_menu(game)

            elif self.current_screen == "explore":
                self.explore_menu(game)

            elif self.current_screen == "events":
                self.event_screen(game)

            elif self.current_screen == "status":
                self.status_screen(game)

            elif self.current_screen == "settings":
                self.settings_menu(game)

            elif self.current_screen == "start":
                self.start_menu(game)

    def go(self, screen_name):
        self.current_screen = screen_name

    def quit(self):
        self.running = False

    def main_menu(self, game):
        pass

    def training_menu(self, game):
        pass

    def explore_menu(self, game):
        pass

    def event_screen(self, game):
        pass

    def status_screen(self, game):
        pass

    def settings_menu(self, game):
        pass

    def start_menu(self, game):
        pass