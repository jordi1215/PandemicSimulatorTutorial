# Confidential, Copyright 2020, Sony Corporation of America, All rights reserved.
from dataclasses import dataclass

from ..interfaces import NonEssentialBusinessLocationState, ContactRate, SimTimeTuple, NonEssentialBusinessBaseLocation

__all__ = ['University', 'UniversityState']


@dataclass
class UniversityState(NonEssentialBusinessLocationState):
    contact_rate: ContactRate = ContactRate(5, 1, 0, 0.1, 0., 0.1)
    open_time: SimTimeTuple = SimTimeTuple(hours=tuple(range(8, 20)), week_days=tuple(range(0, 6)))
    # 0-6 represents Saturdays and college game days
    # TODO: add university holidays with parameter days
    # TODO: model different weekday and weekend activities


class University(NonEssentialBusinessBaseLocation[UniversityState]):
    """Implements a simple university"""

    state_type = UniversityState
