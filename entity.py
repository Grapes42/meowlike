class Entity:
    """
    A generic object to represent players, enemies, items, etc.
    """

    def __init__ (self, x: int, y: int, char: str):
        self.x = x
        self.y = y
        self.char = char

    def move(self, dx: int, dy: int) -> None:
        # Move the entity by a given amount
        self.x += dx
        self.y += dy