from typing import List

from src.python.pim.stable_marriage import stable_marriage
from src.python.pim.stable_marriage.bride import Bride
from src.python.pim.stable_marriage.cohort import Cohort
from src.python.pim.stable_marriage.groom import Groom
from src.python.pim.stable_marriage.stable_marriage import StableMarriage


def run() -> None:
    groom_one: Groom = Groom(1, [1, 2, 4, 3])
    groom_two: Groom = Groom(2, [1, 4, 3, 2])
    groom_three: Groom = Groom(3, [2, 3, 1, 4])
    groom_four: Groom = Groom(4, [2, 1, 3, 4])
    #groom_five: Groom = Groom(5, [2, 5, 1, 3, 4])

    groom_list: List[Groom] = [groom_one, groom_two, groom_three, groom_four]

    bride_one: Bride = Bride(1, [4, 3, 1, 2])
    bride_two: Bride = Bride(2, [1, 2, 3, 4])
    bride_three: Bride = Bride(3, [4, 2, 1, 3])
    bride_four: Bride = Bride(4, [1, 4, 2, 3])
    #bride_five: Bride = Bride(5, [5, 1, 2, 4, 3])

    bride_list: List[Bride] = [bride_one, bride_two, bride_three, bride_four]

    small_cohort: Cohort = Cohort(groom_list, bride_list)

    marriages: StableMarriage = stable_marriage.complete_marriages(small_cohort)
    print(marriages)


if __name__ == "__main__":
    run()
