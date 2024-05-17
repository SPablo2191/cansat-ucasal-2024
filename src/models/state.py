from enum import StrEnum

class State(StrEnum):
    PRE_LAUNCH = "Pre Launch"
    ASCENT = "Ascent"
    DESCENT = "Descent"
    SEPARATION = "Separation"
    LANDED = "Landed"
