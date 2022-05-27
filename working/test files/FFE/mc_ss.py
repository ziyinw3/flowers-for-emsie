from spritesheet import SpriteSheet

"""Module to represent an animation set and an individual sprite."""

class mc_sprite_set:
    """Represents a set of sprites.
    Each sprite is an object of the mc_sprite class.
    """

    def __init__(self, FFE):
        """Initialize attributes to represent the overall set of sprites."""

        self.FFE = FFE
        self.mc_sprites = []
        self._load_mc_sprites()

    def _load_mc_sprites(self):
        """Builds the overall set:
        - Loads images from the sprite sheet.
        - Creates a mc_sprite object, and sets appropriate attributes
          for that piece.
        - Adds each piece to the group self.mc_sprites.
        """
        filename = 'working\\test files\FFE\images\mc_m_sheet.png'
        mc_sprite_set = SpriteSheet(filename)

          # Load all piece images.
        sprite_images = mc_sprite_set.load_sprite_set(1, 12)

        # Create a new Piece object for every image.
        for image in sprite_images:
            sprite = mc_sprite(self.FFE)
            sprite.image = image
            self.mc_sprite_set.append(sprite)



class mc_sprite:
    """Represents a sprite image."""

    def __init__(self, FFE):
        """Initialize attributes to represent a sprite."""
        self.image = None
        self.name = ''
        self.f_dir = ''
        self.m_dir = ''

        self.screen = FFE.screen

        # Start each piece off at the top left corner.
        self.x, self.y = 0.0, 0.0

    def blitme(self):
        """Draw the sprite at its current location."""
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x, self.y
        self.screen.blit(self.image, self.rect)