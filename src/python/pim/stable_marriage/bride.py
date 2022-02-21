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

    def filter_proposal_round(self, all_proposals: List["GroomChoices"]) -> List[Groom]:
        """ all_proposals: [(1,1), (2, 1), (3, 2), (4, 2)] and bride is #1, should return [1, 2] """
        groom_list: List[Groom] = [x[0] for x in all_proposals if x[1] == self.identifier]
        return groom_list

    def current_proposal(self, groom_ids: List[Groom], held_proposal: "GroomRank") -> List[Groom]:
        """If a woman gets new proposals in a round, she immediately rejects every proposer except her most preferred,
        but does not accept that proposal. Returns a tuple of index and groom id"""
        list_with_ranks: list[GroomRank] = \
            [(groom_ids[j], i) for i in range(len(self.preferences)) for j in range(len(groom_ids))
             if self.preferences[i] == groom_ids[j].identifier]

        selected_proposal: GroomRank = min(list_with_ranks, key=lambda r: r[1])
        # compare held proposal to selected
        if held_proposal is None:
            final_preference: GroomRank = selected_proposal
        elif selected_proposal is None:
            final_preference: GroomRank = held_proposal
            # this shouldn't happen, we shouldn't get this far if there are no possible proposals to select from
        elif held_proposal and selected_proposal is None:
            pass
        else:
            final_preference: GroomRank = min((selected_proposal, held_proposal), key=lambda r: r[1])
            # todo: why can't I use list[] in that function above?
            #  -> TypeError: 'types.GenericAlias' object is not iterable

        rejected_proposals: list[GroomRank] = list(filter(lambda x: x != selected_proposal, list_with_ranks))
        # reject either held or selected
        if held_proposal is None:
            rejects = rejected_proposals
        elif selected_proposal is None:
            rejects = rejected_proposals
            # this shouldn't happen, we shouldn't get this far if there are no possible proposals to select from
        elif final_preference == selected_proposal:
            rejects: List[GroomRank] = rejected_proposals.append(held_proposal)
        else:
            rejects: List[GroomRank] = rejected_proposals.append(selected_proposal)

        # decouple from bride index
        reject_list: List[Groom] = [x[0] for x in rejects]

        self.held_proposal: Optional[GroomRank] = final_preference
        self.preferences: List[int] = self.preferences[:final_preference[1] + 1]

        return reject_list


GroomRank = namedtuple("GroomRank", ["groom_id", "bride_index"])
GroomChoices = namedtuple("GroomChoices", ["groom_id", "desired_bride_id"])
