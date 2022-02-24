from dataclasses import dataclass
from typing import List, Dict, Tuple, DefaultDict

Skill = str


@dataclass
class Contributor:
    name: str
    """between 1 to 10"""
    skills: DefaultDict[Skill, int]


@dataclass
class Project:
    name: str
    """between 1 to 10^5"""
    days_needed: int
    """between 1 to 10^5"""
    score_reward: int
    """between 1 to 10^5"""
    best_before_date: int
    """between 1 to 100"""
    roles_needed: List[Tuple[Skill, int]]


@dataclass
class Problem:
    """name of the problem file."""
    name: str
    """between 1 to 10^5"""
    contributors: List[Contributor]
    """between 1 to 10^5"""
    projects: List[Project]


@dataclass
class Solution:
    projects: List[Project]
    """
    for each project in this solution (first index), which contributors match each role (second index)
    """
    contributors: List[List[Contributor]]


@dataclass
class ScoredSolution:
    solution: Solution
    score: int
