from collections import namedtuple
from dataclasses import dataclass, field
from typing import List

from src.python.pim.stable_marriage.cohort import Cohort
from src.python.pim.stable_marriage.groom import Groom


@dataclass(order=True)
class StableMarriage:
    marriage_pairs: List["Marriage"]


def complete_marriages(input_cohort: Cohort, initial_grooms: List[Groom]) -> StableMarriage:
    next_grooms: List[Groom] = initial_grooms

    while len(next_grooms) != 0:
        next_grooms: List[Groom] = Cohort.matching_round(input_cohort, next_grooms)

    # todo: it shouldn't get here until all the grooms have a match...
    #  so no bride should show up with a NoneType held_proposal, however I think the next_grooms isn't working right
    marriages: List["Marriage"] = []
    for x in input_cohort.bride_cohort:
        new_marriage: Marriage = (x.held_proposal[0].identifier, x.identifier)
        marriages.append(new_marriage)

    return StableMarriage(marriages)


Marriage = namedtuple("Marriage", ["groom_id", "bride_id"])


