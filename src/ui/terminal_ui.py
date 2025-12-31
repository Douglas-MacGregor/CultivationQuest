from .abstract_ui import UIInterface
import os



class TerminalUI(UIInterface):
    def __init__(self):
        self.running = True

    def run(self, game):
        while self.running:
            if game.events:
                current_event = game.events.pop(0)
                name, description, actions = current_event.trigger()
                print(f"\n=== {name} ===")
                print(description)
                for idx, action in enumerate(actions, 1):
                    print(f"{idx}. {action}")
                choice = input("Choose an action: ")
                try:
                    action_idx = int(choice) - 1
                    if 0 <= action_idx < len(actions):
                        selected_action = actions[action_idx]
                        current_event.resolve(selected_action, game)
                    else:
                        print("Invalid choice. Please try again.")
                        game.events.insert(0, current_event)  # Re-add the event
                except ValueError:
                    print("Please enter a number corresponding to your choice.")
                    game.events.insert(0, current_event)  # Re-add the event
                self.clear()
            else:
                print("No events to process. Exiting UI.")
                self.quit()

    def quit(self):
        self.running = False

    def clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')