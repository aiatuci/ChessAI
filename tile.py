from settings import *


class Tile:
    def __init__(self, piece, x, y):
        self.piece = piece
        self.x = x
        self.y = y
        self.color = BLACK
        self.surface = pygame.Surface((TILE_SIZE, TILE_SIZE))

    def fill(self, color):
        """
        Fills tile with specified color
        :param color: color to fill tile with (tuple)
        :return: None
        """
        self.surface.fill(color)

    def select(self):
        """
        Applies highlighted effect to tile, indicating selection
        :return: None
        """
        if self.contains_piece():
            self.fill(HIGHLIGHT_COLOR)
            self.draw()

    def draw(self):
        """
        Draws tile and the piece it contains (if applicable)
        :return: None
        """
        SCREEN.blit(self.surface, to_coords(self.x, self.y))
        if self.piece:
            self.piece.draw()

    def contains_piece(self):
        """
        Checks if tile contains a piece
        :return: bool representing whether or not tile contains piece
        """
        if self.piece.image is None:
            return False
        return True

    def copy(self):
        """
        Creates a deep copy of the current tile
        :return: reference to a new Tile object
        """
        piece = None
        if self.piece:
            piece = self.piece.copy()
        copy = Tile(piece, self.x, self.y)
        copy.fill(self.color)
        return copy
