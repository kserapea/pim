from collections import namedtuple
from dataclasses import dataclass, field
from typing import List

from src.python.pim.stable_marriage.bride import Bride, GroomRank, GroomChoices
from src.python.pim.stable_marriage.groom import Groom


@dataclass(order=True)
class Cohort:
    groom_cohort: List[Groom]
    bride_cohort: List[Bride]

    def __post_init__(self):
        if len(self.bride_cohort) != len(self.groom_cohort):
            raise ValueError('Cohorts do not contain equal numbers.')

    def __len__(self):
        return len(self.groom_cohort)

    def matching_round(self, grooms_involved: List[Groom]) -> List[Groom]:
        proposal_list: List[GroomChoices] = proposal_round(grooms_involved)

        rejects: List[Groom] = []

        for y in self.bride_cohort:
            groom_list: List[Groom] = Bride.filter_proposal_round(y, proposal_list)
            groom_ids: List[Groom] = [i for i in groom_list]
            if len(groom_ids) == 0:
                continue
            new_rejects: List[Groom] = Bride.current_proposal(y, groom_ids, y.held_proposal)
            if new_rejects is None:
                continue
            else:
                rejects.extend(new_rejects)

        # reject_grooms: List[Groom] = [x for x in self.groom_cohort if x.identifier in rejects]

        return rejects


def proposal_round(grooms_involved: List[Groom]) -> List[GroomChoices]:
    """returns the current proposals for the round and also deletes the used preference from groom"""
    proposal_list: List[GroomChoices] = []
    for x in grooms_involved:
        proposal_list += [(x, x.preferences[0])]
    for x in grooms_involved:
        x.preferences.pop(0)
    return proposal_list
