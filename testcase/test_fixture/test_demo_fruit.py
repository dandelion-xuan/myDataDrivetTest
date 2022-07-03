#!/usr/bin/env python
# -*-coding:utf-8 -*-
# @Time    : 2022/7/3 12:26
# @Author  : xuan
# @Desc    : 
# @File    : test_demo_fruit.py
# @Software: PyCharm
import pytest


class Fruit:
    def __init__(self, name):
        self.name = name
        self.cubed = False

    def cube(self):
        self.cubed = True

class FruitSalad:
    def __init__(self, *fruit_bowls):
        self.fruit = fruit_bowls
        self._cube_fruit()

    def _cube_fruit(self):
        for fruit in self.fruit:
            fruit.cube()

@pytest.fixture
def fruit_bowl():
    return [Fruit("apple"), Fruit("banana")]

def test_fruit_salad(fruit_bowl):
    # Act
    fruit_salad = FruitSalad(*fruit_bowl)

    # Assert
    assert all(fruit.cubed for fruit in fruit_salad.fruit)

if __name__ == '__main__':
    pytest.main(['-vs'])