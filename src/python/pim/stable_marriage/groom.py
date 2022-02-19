from typing import List


class Groom(object):
    def __init__(self, identifier: int, preferences: List[int]) -> None:
        """The list of preferences will be the length of the number of "grooms" available"""
        self.identifier: int = identifier
        self.preferences: List[int] = preferences

    def __len__(self):
        return len(self.preferences)