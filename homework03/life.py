import pathlib
import random
import typing as tp

import pygame
from pygame.locals import *

Cell = tp.Tuple[int, int]
Cells = tp.List[int]
Grid = tp.List[Cells]


class GameOfLife:
    def __init__(
        self,
        size: tp.Tuple[int, int],
        randomize: bool = True,
        max_generations: tp.Optional[float] = float("inf"),
    ) -> None:
        # Размер клеточного поля
        self.rows, self.cols = size
        # Предыдущее поколение клеток
        self.prev_generation = self.create_grid()
        # Текущее поколение клеток
        self.curr_generation = self.create_grid(randomize=randomize)
        # Максимальное число поколений
        self.max_generations = max_generations
        # Текущее число поколений
        self.generations = 1

    def create_grid(self, randomize: bool = False) -> Grid:
        # Copy from previous assignment
        grid = [[0 for i in range(int(self.cols))] for j in range(int(self.rows))]
        if randomize:
            for i in range(self.rows):
                for j in range(self.cols):
                    grid[i][j] = random.randint(0, 1)
        else:
            return grid
        return grid

    def get_neighbours(self, cell: Cell) -> Cells:
        # Copy from previous assignment
        g = self.curr_generation
        a = cell[0]
        b = cell[1]
        if cell[0] == 0 and cell[1] == 0:
            return [g[a][b + 1], g[a + 1][b], g[a + 1][b + 1]]
        elif cell[1] == self.cols - 1 and cell[0] == 0:
            return [g[a][b - 1], g[a + 1][b], g[a + 1][b - 1]]
        elif cell[0] == self.rows - 1 and cell[1] == 0:
            return [g[a][b + 1], g[a - 1][b], g[a - 1][b + 1]]
        elif cell[0] == self.rows - 1 and cell[1] == self.cols - 1:
            return [g[a][b - 1], g[a - 1][b], g[a - 1][b - 1]]
        elif cell[0] == 0:
            return [g[a][b - 1], g[a][b + 1], g[a + 1][b - 1], g[a + 1][b], g[a + 1][b + 1]]
        elif cell[0] == self.rows - 1:
            return [g[a][b - 1], g[a][b + 1], g[a - 1][b - 1], g[a - 1][b], g[a - 1][b + 1]]
        elif cell[1] == 0:
            return [g[a - 1][b], g[a + 1][b], g[a - 1][b + 1], g[a][b + 1], g[a + 1][b + 1]]
        elif cell[1] == self.cols - 1:
            return [g[a - 1][b], g[a + 1][b], g[a - 1][b - 1], g[a][b - 1], g[a + 1][b - 1]]
        else:
            return [
                g[a - 1][b - 1],
                g[a - 1][b],
                g[a - 1][b + 1],
                g[a][b - 1],
                g[a][b + 1],
                g[a + 1][b - 1],
                g[a + 1][b],
                g[a + 1][b + 1],
            ]

    def get_next_generation(self) -> Grid:
        # Copy from previous assignment
        h = []
        for l in range(self.rows):
            g = []
            for d in range(self.cols):
                g.append(self.curr_generation[l][d])
            h.append(g)
        for i in range(self.rows):
            for j in range(self.cols):
                c = self.get_neighbours((i, j))
                if self.curr_generation[i][j] == 1:
                    if sum(c) != 2 and sum(c) != 3:
                        h[i][j] = 0
                    else:
                        h[i][j] = 1
                if self.curr_generation[i][j] == 0:
                    if sum(c) == 3:
                        h[i][j] = 1
                    else:
                        h[i][j] = 0

        return h

    def step(self) -> None:
        """
        Выполнить один шаг игры.
        """
        self.prev_generation = self.curr_generation
        self.curr_generation = self.get_next_generation()
        self.generations += 1

    @property
    def is_max_generations_exceeded(self) -> bool:
        """
        Не превысило ли текущее число поколений максимально допустимое.
        """

        return self.generations == self.max_generations

    @property
    def is_changing(self) -> bool:
        """
        Изменилось ли состояние клеток с предыдущего шага.
        """
        return self.prev_generation != self.curr_generation

    @staticmethod
    def from_file(filename: pathlib.Path) -> "GameOfLife":
        """
        Прочитать состояние клеток из указанного файла.
        """
        f = open(filename, "r")

        grid: Grid = []
        for i in f.readlines():
            grid.append([])
            for j in i:
                grid[-1].append(int(j))

        rows = len(grid)
        cols = len(grid[0])

        a = GameOfLife(size=(rows, cols), randomize=False)
        a.curr_generation = grid

        f.close()

        return a

    def save(self, filename: pathlib.Path) -> None:
        """
        Сохранить текущее состояние клеток в указанный файл.
        """

        s = "\n".join(map(lambda x: "".join(map(str, x)), self.curr_generation))
        with open(filename, "w") as a:
            a.write(s)
