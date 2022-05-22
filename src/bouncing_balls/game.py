#!/usr/bin/env python

import sys
import os
import pygame

from ball import Ball

class Game:
    def __init__(self, args):
        # Game exit codes
        self.EXIT_IS_SUCCESSFUL = 0
        self.EXIT_HAS_ERROR = 1

        # Game window constants
        self.WINDOW_SIZE = (800, 600)
        self.WINDOW_WIDTH = self.WINDOW_SIZE[0]
        self.WINDOW_HEIGHT = self.WINDOW_SIZE[1]
        self.WINDOW_TITLE = "Bouncing Balls"

        # Directories
        self.CURRENT_DIR = os.getcwd()
        self.ASSETS_DIR = os.path.join(self.CURRENT_DIR, "assets")

        # Gameplay constants
        self.BALL_COUNT = int(sys.argv[1])
        self.BACKGROUND_FILEPATH = os.path.join(self.ASSETS_DIR, "background.png")
        self.BALL_FILEPATH = os.path.join(self.ASSETS_DIR, "ball.png")
        self.MUSIC_FILEPATH = os.path.join(self.ASSETS_DIR, "music.ogg")

        # Ball list
        self.balls = []

        if not pygame.mixer:
            print("WARNING: Sound disabled!")

        pygame.init()

    def on_exit(self):
        sys.exit(self.EXIT_IS_SUCCESSFUL)

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self.on_exit()

    def on_init(self):
        pygame.display.set_caption(self.WINDOW_TITLE)
        pygame.mouse.set_visible(False)

        self.display = pygame.display.set_mode(self.WINDOW_SIZE)

        self.clock = pygame.time.Clock()

        self.background = pygame.image.load(self.BACKGROUND_FILEPATH)
        self.background = self.background.convert_alpha()
        self.background = pygame.transform.scale(self.background, self.WINDOW_SIZE)

        for i in range(self.BALL_COUNT):
            ball = Ball("Ball_{0}".format(i), self.BALL_FILEPATH)
            self.balls.append(ball)

        self.sound = pygame.mixer.Sound(self.MUSIC_FILEPATH)
        self.sound.play()

    def on_loop(self):
        self.clock.tick(60)

        self.display.blit(self.background, (0, 0))

        events = pygame.event.get()
        for event in events:
            self.on_event(event)

        for i in range(len(self.balls)):
            ball_current = self.balls[i]
            rect_current = ball_current.get_rectangle().move(ball_current.get_speed())
            ball_current.set_rect(rect_current)
            if rect_current.left < 0 or rect_current.right > self.WINDOW_WIDTH:
                ball_current.get_speed()[0] = -ball_current.get_speed()[0]
            if rect_current.top < 0 or rect_current.bottom > self.WINDOW_HEIGHT:
                ball_current.get_speed()[1] = -ball_current.get_speed()[1]
            self.display.blit(ball_current.get_image(), rect_current)

        pygame.display.flip()

    def on_execute(self):
        self.on_init()

        while True:
            self.on_loop()


if __name__ == "__main__":
    game_instance = Game(sys.argv)
    game_instance.on_execute()

