from typing import List, Dict
from dataclasses import dataclass, field
from functools import reduce

from src.python.pim.stable_marriage import stable_marriage
from src.python.pim.stable_marriage.bride import Bride
from src.python.pim.stable_marriage.cohort import Cohort
from src.python.pim.stable_marriage.groom import Groom
from src.python.pim.stable_marriage.stable_marriage import StableMarriage


def run() -> None:
    groom_one: Groom = Groom(1, [1, 2, 4, 3])
    groom_two: Groom = Groom(2, [1, 3, 4, 2])
    groom_three: Groom = Groom(3, [2, 3, 1, 4])
    groom_four: Groom = Groom(4, [2, 1, 3, 4])

    groom_list: List[Groom] = [groom_one, groom_two, groom_three, groom_four]
    # [(1, 1), (2, 1), (3, 2), (4, 2)
    #  groom_one: Groom = Groom(1, [2, 4, 3])
    #
    # bride_one holding 1
    # bride_two holding 3
    #
    # 2, 4 are rejected ->  propose [(2, 3), (4, 1)
    #
    # bride_three holding 2
    # bride_one holds 4
    #
    # rejects 1 -> propose [(1, 2)]
    #
    # bride_two holding 1, reject 3
    #
    # 3 proposes to 3 gets rejected
    # 3 proposes to 1 gets rejeted
    # 3 proposed to 4 and gets her
    #
    # bride_four holds 3

    bride_one: Bride = Bride(1, [4, 3, 1, 2])
    bride_two: Bride = Bride(2, [1, 2, 3, 4])
    bride_three: Bride = Bride(3, [4, 2, 1, 3])
    bride_four: Bride = Bride(4, [1, 4, 2, 3])

    small_cohort: Cohort = Cohort([groom_one, groom_two, groom_three, groom_four],
                                  [bride_one, bride_two, bride_three, bride_four])

    marriages: StableMarriage = stable_marriage.complete_marriages(small_cohort, groom_list)
    print(marriages)

if __name__ == "__main__":
    run()
