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
        return len(self.preferences)

    def filter_proposal_round(self, all_proposals: List["GroomChoices"]) -> List[Groom]:
        """ all_proposals: [(1, 1), (2, 1), (3, 2), (4, 2)] and bride is #1, should return [1, 2] """
        groom_list: List[Groom] = [x.groom_id for x in all_proposals if x.desired_bride_id == self.identifier]
        return groom_list

    def current_proposal(self, groom_ids: List[Groom]) -> List[Groom]:
        """If a woman gets new proposals in a round, she immediately rejects every proposer except her most preferred,
        but does not accept that proposal. Returns a tuple of index and groom id"""
        list_with_ranks: List[GroomRank] = \
            [GroomRank(groom_ids[groom], preference) for preference in range(len(self.preferences)) for groom in
             range(len(groom_ids))
             if self.preferences[preference] == groom_ids[groom].identifier]

        # list1_with_ranks: List[GroomRank] =
        # [GroomRank(groom, self.preferences.index(groom.identifier)) for groom in groom_ids]

        selected_proposal: GroomRank = min(list_with_ranks, key=lambda r: r.bride_index)
        # compare held proposal to selected
        if self.held_proposal is None:
            final_preference: GroomRank = selected_proposal
        else:
            final_preference: GroomRank = min((selected_proposal, self.held_proposal), key=lambda r: r.bride_index)

        rejected_proposals: list[GroomRank] = list(filter(lambda x: x != selected_proposal, list_with_ranks))
        # reject either held or selected
        if self.held_proposal is None:
            pass
        elif final_preference == selected_proposal:
            rejected_proposals.append(self.held_proposal)
        else:
            rejected_proposals.append(selected_proposal)

        # decouple from bride index
        if rejected_proposals is None:
            reject_list: List[Groom] = []
        else:
            reject_list: List[Groom] = [x[0] for x in rejected_proposals]

        self.held_proposal: Optional[GroomRank] = final_preference
        self.preferences: List[int] = self.preferences[:final_preference[1] + 1]

        return reject_list


GroomRank = namedtuple("GroomRank", ["groom_id", "bride_index"])
GroomChoices = namedtuple("GroomChoices", ["groom_id", "desired_bride_id"])
