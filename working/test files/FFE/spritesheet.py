import pygame


class SpriteSheet:

    def __init__(self, filename):
        """Load the sheet."""
        self.sheet = pygame.image.load(filename).convert_alpha()


    def image_at(self, rectangle):
        """Load a specific image from a specific rectangle."""
        # Loads image from x, y, x+offset, y+offset.
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return image

    def images_at(self, rects):
        """Load a whole bunch of images and return them as a list."""
        return [self.image_at(rect) for rect in rects]

    def load_sprite_set(self, num_rows, num_cols):
        """Load a grid of images.
        Calls self.images_at() to get list of images.
        """
        sheet_rect = self.sheet.get_rect()
        # sheet_width, sheet_height = sheet_rect.size

        x_sprite_size = 41
        y_sprite_size = 41

        sprite_rects = []
        for row_num in range(num_rows):
            for col_num in range(num_cols):
                x = col_num * x_sprite_size
                y = row_num * y_sprite_size
                sprite_rect = (x, y, x_sprite_size, y_sprite_size)
                sprite_rects.append(sprite_rect)

        sprite_set = self.images_at(sprite_rects)
        print(f"Loaded {len(sprite_set)} grid images.")

        return sprite_set    