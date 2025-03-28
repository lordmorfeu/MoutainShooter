
from code.Const import ENTITY_SPEED
from code.Entity import Entity


class PlayerShot(Entity):

    def __init__(self, name: str, position: tuple):
        """Initialize the PlayerShot entity with a name and position."""
        super().__init__(name, position)

    def move(self):
        """Move the shot to the right and check if it goes off-screen."""
        self.rect.centerx += ENTITY_SPEED[self.name]
