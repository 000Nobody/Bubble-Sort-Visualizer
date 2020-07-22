import pygame
import sys
import random
from pygame.locals import *

pygame.init()

WINDOW_SIZE = (1200, 800)
screen = pygame.display.set_mode(WINDOW_SIZE)
display = pygame.Surface(WINDOW_SIZE)

amount_numbers = 75
numbers = []
# Generate random numbers
for i in range(amount_numbers):
    numbers.append(random.randint(5, WINDOW_SIZE[1] - 50))
sorted_numbers = sorted(numbers)

# Create variables
bars = []
low_search = 0
high_search = 1

class Bar():
    def __init__(self, value, x, y, width, color = (0, 0, 0)):
        self.value = value
        self.x = x
        self.y = y
        self.width = width
        self.height = value
        self.color = color
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def update(self):
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        pygame.draw.rect(display, self.color, self.rect)

# Create bars
for i, n in enumerate(numbers):
    width = (WINDOW_SIZE[0] - len(numbers)) / len(numbers)
    x = i * width + i
    y = WINDOW_SIZE[1] - n
    bars.append(Bar(n, x, y, width))

def swap_items(l, item1, item2):
    l[item1], l[item2] = l[item2], l[item1]

def bubble_sort():
    global low_search, high_search
    if numbers != sorted_numbers:
        if numbers[low_search] > numbers[high_search]: # Compare two adjacent bars
            bars[low_search].x, bars[high_search].x = bars[high_search].x, bars[low_search].x # If the left bar is greater than the right, swap their x pos
            bars[low_search].color = (200, 0, 0)
            bars[high_search].color = (0, 200, 0)
            for bar in bars:
                if bar != bars[low_search]:
                    if bar != bars[high_search]:
                        bar.color = (0, 0, 0)
            # Swap items in the lists
            swap_items(numbers, low_search, high_search)
            swap_items(bars, low_search, high_search)
            low_search += 1
            high_search += 1
        else:
            low_search += 1
            high_search += 1
        # Reset search values when reaching the end
        if low_search >= len(numbers) - 1:
            low_search = 0
        if high_search >= len(numbers):
            high_search = 1
    # Once sorted, set color to black for all bars
    else:
        for bar in bars:
            bar.color = (0, 0, 0)

def draw():
    display.fill((255, 255, 255))

    for bar in bars:
        bar.draw()

    screen.blit(display, (0, 0))
    pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    bubble_sort()

    for bar in bars:
        bar.update()

    draw()