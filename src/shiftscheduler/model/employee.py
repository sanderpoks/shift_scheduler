from dataclasses import dataclass
from datetime import Date

@dataclass
class Employee():
    """ This class contains all the information about a specific person
    working at the department. """
    first_name : str
    last_name : str
    dob : Date
    positions : list[Position] = field(default_factory=list)
    tags : dict = field(default_factory=dict)
    shifts : list[Shift] = field(default_factory=list)
    vacations : list[Vacation] = field(default_factory=list)

