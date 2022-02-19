from dataclasses import dataclass
from typing import List, Set

Ingredient = str


@dataclass
class Client:
    likes: Set[Ingredient]
    dislikes: Set[Ingredient]


@dataclass
class Problem:
    name: str
    clients: List[Client]
    '''a set with one of each ingredient liked by anyone'''
    ingredients: Set[Ingredient]


@dataclass
class Solution:
    """score will be -1 if we don't know what it is"""
    score: int
    pizza: Set[Ingredient]
