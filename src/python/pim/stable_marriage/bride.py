from collections import namedtuple
from typing import List, Optional, Tuple

from src.python.pim.stable_marriage.groom import Groom


class Bride(object):
    def __init__(self, identifier: int, preferences: List[int], held_proposal: Optional["GroomRank"] = None) -> None:
        """The list of preferences will be the length of the number of "grooms" available"""
        self.identifier: int = identifier
        self.preferences: List[int] = preferences
        self.held_proposal: Optional["GroomRank"] = held_proposal

    def __len__(self):
        """should we raise an error depending on # of grooms?"""
        return len(self.preferences)

    def filter_proposal_round(self, all_proposals: List[Tuple[Groom, int]]) -> List[Groom]:
        """ all_proposals: [(1,1), (2, 1), (3, 2), (4, 2)] and bride is #1, should return [1, 2] """
        groom_list: List[Groom] = [x for x in all_proposals[2] if x == self.identifier]
        return groom_list

    def current_proposal(self, groom_ids: List[int], held_proposal: "GroomRank") -> List[int]:
        """If a woman gets new proposals in a round, she immediately rejects every proposer except her most preferred,
        but does not accept that proposal. Returns a tuple of index and groom id"""

        for index in range(len(self.preferences)):
            list_with_ranks: list[GroomRank] = [(x, index) for x in groom_ids if x == self.preferences[index]]
        # return (groom_id, bride_index) and then find smallest one
        sorted_list: list[GroomRank] = list_with_ranks.sort(key=lambda g: g.bride_index)
        selected_proposal: GroomRank = sorted_list.pop(0)
        # compare held proposal to selected
        final_preference: GroomRank = min(list[selected_proposal, held_proposal], key=lambda r: r.bride_index)

        # create list of rejects to send to next round
        rejects: List[int] = [x.groom_id for x in sorted_list]
        if final_preference == selected_proposal:
            reject_list: List[int] = rejects + held_proposal[0]
        else:
            reject_list: List[int] = rejects + selected_proposal.groom_id

        self.held_proposal: Optional[GroomRank] = final_preference
        self.preferences: List[int] = self.preferences[:final_preference.bride_index+1]

        return reject_list


GroomRank = namedtuple("GroomRank", ["groom_id", "bride_index"])
