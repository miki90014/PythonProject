import os
import sys
import unittest
import client
from client.enemy import spawnEnemy

from client.player import Player
from client.powerUp import spawnPowerUp
from client.variables import WIDTH, HEIGHT



class BoardTests(unittest.TestCase):
    def test_board_ship1(self):
        player = Player(-50,-50, 40, 40, (0, 255, 0))
        self.assertEqual(player.border(), True, "incorrect board for ship")

    def test_board_ship2(self):
        player = Player(WIDTH+50, HEIGHT + 50, 40, 40, (0, 255, 0))
        self.assertEqual(player.border(), True, "incorrect board for ship")

class Spawn(unittest.TestCase):
    def test_spawn_enemies(self):
        self.assertEqual(len(spawnEnemy(10, [], 3, 3, 3, 0)), 0, "spawn enemies error")
    def test_spawn_powerup(self):
        self.assertEqual(len(spawnPowerUp(10, [], 3)), 1, "spawn powerup error")

if __name__ == '__main__':
    unittest.main()