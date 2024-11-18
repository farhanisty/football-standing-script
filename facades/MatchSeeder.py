from abc import ABC, abstractmethod


class MatchSeeder(ABC):
    @abstractmethod
    def seed(self):
        pass


class MatchSeederImpl(MatchSeeder):
    def seed(self):
        print("hello world")
