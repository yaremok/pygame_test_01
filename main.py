import pygame


p = [
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
]


class Sprite(pygame.sprite.Sprite):
    def __init__(self, pos, width=30, height=30):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([width, height])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()

        self.rect.center = pos

    def set_color(self, color):
        self.image.fill(color)

    def set_image(self, image):
        self.image = image


def is_player_hit_wall(player, wall_group):
    hit = pygame.sprite.spritecollide(player, wall_group, False)
    return hit


def main():
    pygame.init()
    clock = pygame.time.Clock()
    fps = 50
    size = [600, 400]

    screen = pygame.display.set_mode(size)

    player_img = pygame.image.load('player_small.png').convert_alpha()

    player_size = 25
    player = Sprite([40, 50], width=player_size, height=player_size)
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5
    player.set_image(player_img)

    player_group = pygame.sprite.Group()
    player_group.add(player)

    bricks_img = pygame.image.load('bricks_small.png').convert_alpha()

    wall_group = pygame.sprite.Group()
    cell_size = 30
    p_width = len(p[0])
    p_height = len(p)
    for line in range(p_height):
        for column in range(p_width):
            if p[line][column] == 1:
                wall_x = column * cell_size
                wall_y = line * cell_size
                wall = Sprite([wall_x, wall_y], width=cell_size, height=cell_size)
                wall.set_color((100, 100, 100))
                wall.set_image(bricks_img)
                wall_group.add(wall)

    runing = True
    while runing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runing = False

        key = pygame.key.get_pressed()

        if key[pygame.K_LEFT]:
            new_x = player.rect.x - player.vx
            if new_x >= 0:
                old_x = player.rect.x
                player.rect.x = new_x
                if is_player_hit_wall(player, wall_group):
                    player.rect.x = old_x

        if key[pygame.K_RIGHT]:
            new_x = player.rect.x + player.vx
            if new_x <= size[0] - player.rect[2]:
                old_x = player.rect.x
                player.rect.x = new_x
                if is_player_hit_wall(player, wall_group):
                    player.rect.x = old_x

        if key[pygame.K_UP]:
            new_y = player.rect.y - player.vy
            if new_y >= 0:
                old_y = player.rect.y
                player.rect.y = new_y
                if is_player_hit_wall(player, wall_group):
                    player.rect.y = old_y

        if key[pygame.K_DOWN]:
            new_y = player.rect.y + player.vy
            if new_y <= size[1] - player.rect[3]:
                old_y = player.rect.y
                player.rect.y = new_y
                if is_player_hit_wall(player, wall_group):
                    player.rect.y = old_y

        bg_color = (0, 0, 0)
        screen.fill(bg_color)

        wall_group.draw(screen)
        player_group.draw(screen)

        pygame.display.update()
        clock.tick(fps)

    pygame.quit()


if __name__ == '__main__':
    main()
