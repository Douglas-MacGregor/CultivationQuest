"""
Abstract UI Interface for Cultivation Quest

This module defines the abstract base class for all UI implementations in the game.
"""

from abc import ABC, abstractmethod


class UIInterface(ABC):
    """
    Abstract base class for all UI interfaces in Cultivation Quest.
    
    This class defines the common interface that all UI implementations
    must follow, whether it's a console UI, GUI, web interface, etc.
    """
    
    @abstractmethod
    def run(self) -> None:
        """
        Start and run the UI main loop.
        
        This method should initialize the UI and enter the main event loop,
        handling user input and updating the display until the application
        is terminated.
        """
        pass
    
    @abstractmethod
    def go(self) -> None:
        """
        Begin or continue the game flow.
        
        This method should start the main game sequence or continue
        from where it was paused. It handles the primary game loop
        and user interactions.
        """
        pass
    
    @abstractmethod
    def quit(self) -> None:
        """
        Cleanly shutdown the UI and exit the application.
        
        This method should perform any necessary cleanup operations,
        save any pending data, and terminate the UI gracefully.
        """
        pass
