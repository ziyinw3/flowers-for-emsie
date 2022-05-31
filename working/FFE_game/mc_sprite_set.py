"""Module to represent a chess set, and individual pieces."""

from spritesheet import SpriteSheet

class McSpriteSet:
    """Represents a set of mc sprites.
    Each piece is an object of the McSprite class.
    """

    def __init__(self, FFE_game):
        """Initialize attributes to represent the overall set of sprites."""

        self.FFE_game = FFE_game
        self.pieces = []
        self._load_pieces()

    def _load_pieces(self):
        filename = 'images/chess_pieces.bmp'
        piece_ss = SpriteSheet(filename)

        # Load all piece images.
        piece_images = piece_ss.load_grid_images(2, 6, x_margin=64,
        x_padding=72, y_margin=68, y_padding=48)

        # Create a new McSprite object for every image.
        for image in piece_images:
            piece = McSprite(self.FFE_game)
            piece.image = image
            self.pieces.append(piece)


class McSprite:
    """Represents a chess piece."""

    def __init__(self, FFE_game):
        """Initialize attributes to represent a chess piece."""
        self.image = None
        self.name = ''
        self.color = ''

        self.screen = FFE_game.screen

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)