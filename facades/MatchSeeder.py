import copy
import itertools
import random
from abc import ABC, abstractmethod
from facades.Match import Match
from repository.MatchFixture import MatchFixture


class MatchSeeder(ABC):
    @abstractmethod
    def seed(self):
        pass


class MatchSeederImpl(MatchSeeder):
    def __init__(self, matches):
        self.matchPermutations = list(itertools.permutations(matches, 2))
        self.matchPermutations = list(map(lambda teams: Match(
            teams[0], teams[1], "0000"), self.matchPermutations))

    def seed(self):
        matchFixtureRepository = MatchFixture()

        for match in self.matchPermutations:
            matchFixtureRepository.insert(match, 1)
