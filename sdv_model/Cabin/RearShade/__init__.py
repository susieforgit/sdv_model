#!/usr/bin/env python3

"""RearShade model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointString,
    DataPointUint8,
    Model,
)


class RearShade(Model):
    """RearShade model.

    Attributes
    ----------
    Switch: actuator
        Switch controlling sliding action such as window, sunroof, or blind.

        Allowed values: INACTIVE, CLOSE, OPEN, ONE_SHOT_CLOSE, ONE_SHOT_OPEN
    Position: actuator
        Position of window blind. 0 = Fully retracted. 100 = Fully deployed.

        Value range: [0, 100]
        Unit: percent
    """

    def __init__(self, name, parent):
        """Create a new RearShade model."""
        super().__init__(parent)
        self.name = name

        self.Switch = DataPointString("Switch", self)
        self.Position = DataPointUint8("Position", self)
