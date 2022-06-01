"""Module to represent a chess set, and individual pieces."""

from spritesheet import SpriteSheet

from ss_storages import coords_di

class McSpriteSet:
    """Represents a set of mc sprites.
    Each piece is an object of the McSprite class.
    """

    def __init__(self, FFE_game):
        """Initialize attributes to represent the overall set of sprites."""

        self.FFE_game = FFE_game
        self.pieces = []
        self._load_pieces()

    def _load_pieces(self, lis):
        filename = 'images/mc_ss.png'
        mc_ss = SpriteSheet(filename)
        lis = coords_di
        
        # Load all piece images.
        piece_images = mc_ss.images_at(self, lis)
        i = 0
        # Create a new McSprite object for every image.
        for image in piece_images:
            i += 1
            sprite = McSprite(self.FFE_game)
            sprite.image = image
            self.pieces.append(sprite)


class McSprite:
    """Represents a chess piece."""

    def __init__(self, FFE_game):
        """Initialize attributes to represent a chess piece."""

        for i in range(0, 13):
            mc_sprite = McSprite(self.FFE_game)
            mc_sprite.name = "di_" + str(i)
            mc_sprite.facing = 'V'
            mc_sprite.moving = False
            mc_sprite.f_count = i

        self.screen = FFE_game.screen

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        """Draw the piece at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)