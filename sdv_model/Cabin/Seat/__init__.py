#!/usr/bin/env python3

"""Seat model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt8,
    DataPointUint16,
    DataPointUint8,
    Model,
)

from sdv_model.Cabin.Seat.Airbag import Airbag
from sdv_model.Cabin.Seat.Backrest import Backrest
from sdv_model.Cabin.Seat.Headrest import Headrest
from sdv_model.Cabin.Seat.Occupant import Occupant
from sdv_model.Cabin.Seat.Seating import Seating
from sdv_model.Cabin.Seat.Switch import Switch


class Seat(Model):
    """Seat model.

    Attributes
    ----------
    IsOccupied: sensor
        Does the seat have a passenger in it.

    Occupant: branch
        Occupant data.

    IsBelted: sensor
        Is the belt engaged.

    Heating: actuator
        Seat cooling / heating. 0 = off. -100 = max cold. +100 = max heat.

        Value range: [-100, 100]
        Unit: percent
    Massage: actuator
        Seat massage level. 0 = off. 100 = max massage.

        Value range: [0, 100]
        Unit: percent
    Position: actuator
        Seat position on vehicle x-axis. Position is relative to the frontmost position supported by the seat. 0 = Frontmost position supported.

        Value range: [0, ]
        Unit: mm
    Height: actuator
        Seat position on vehicle z-axis. Position is relative within available movable range of the seating. 0 = Lowermost position supported.

        Value range: [0, ]
        Unit: mm
    Tilt: actuator
        Tilting of seat (seating and backrest) relative to vehicle x-axis. 0 = seat bottom is flat, seat bottom and vehicle x-axis are parallel. Positive degrees = seat tilted backwards, seat x-axis tilted upward, seat z-axis is tilted backward.

        In VSS it is assumed that tilting a seat affects both seating (seat bottom) and backrest, i.e. the angle between seating and backrest will not be affected when changing Tilt.

        Unit: degrees
    Backrest: branch
        Describes signals related to the backrest of the seat.

    Seating: branch
        Describes signals related to the seat bottom of the seat.

        Seating is here considered as the part of the seat that supports the thighs. Additional cushions (if any) for support of lower legs is not covered by this branch.

    Headrest: branch
        Headrest settings.

    Airbag: branch
        Airbag signals.

    Switch: branch
        Seat switch signals

    """

    def __init__(self, name, parent):
        """Create a new Seat model."""
        super().__init__(parent)
        self.name = name

        self.IsOccupied = DataPointBoolean("IsOccupied", self)
        self.Occupant = Occupant("Occupant", self)
        self.IsBelted = DataPointBoolean("IsBelted", self)
        self.Heating = DataPointInt8("Heating", self)
        self.Massage = DataPointUint8("Massage", self)
        self.Position = DataPointUint16("Position", self)
        self.Height = DataPointUint16("Height", self)
        self.Tilt = DataPointFloat("Tilt", self)
        self.Backrest = Backrest("Backrest", self)
        self.Seating = Seating("Seating", self)
        self.Headrest = Headrest("Headrest", self)
        self.Airbag = Airbag("Airbag", self)
        self.Switch = Switch("Switch", self)
