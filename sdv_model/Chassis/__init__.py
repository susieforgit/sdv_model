#!/usr/bin/env python3

"""Chassis model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointUint16,
    DataPointUint8,
    Model,
)

from sdv_model.Chassis.Accelerator import Accelerator
from sdv_model.Chassis.Axle import Axle
from sdv_model.Chassis.Brake import Brake
from sdv_model.Chassis.ParkingBrake import ParkingBrake
from sdv_model.Chassis.SteeringWheel import SteeringWheel


class Chassis(Model):
    """Chassis model.

    Attributes
    ----------
    Wheelbase: attribute (uint16)
        Overall wheel base, in mm.

        Unit: mm
    Track: attribute (uint16)
        Overall wheel tracking, in mm.

        Unit: mm
    Axle: branch
        Axle signals

    AxleCount: attribute (uint8)
        Number of axles on the vehicle

    ParkingBrake: branch
        Parking brake signals

    SteeringWheel: branch
        Steering wheel signals

    Accelerator: branch
        Accelerator signals

    Brake: branch
        Brake system signals

    """

    def __init__(self, name, parent):
        """Create a new Chassis model."""
        super().__init__(parent)
        self.name = name

        self.Wheelbase = DataPointUint16("Wheelbase", self)
        self.Track = DataPointUint16("Track", self)
        self.Axle = AxleCollection("Axle", self)
        self.AxleCount = DataPointUint8("AxleCount", self)
        self.ParkingBrake = ParkingBrake("ParkingBrake", self)
        self.SteeringWheel = SteeringWheel("SteeringWheel", self)
        self.Accelerator = Accelerator("Accelerator", self)
        self.Brake = Brake("Brake", self)

class AxleCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Row1 = Axle("Row1", self)
        self.Row2 = Axle("Row2", self)

    def Row(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range [1, 2]")
        _options = {{
            1: self.Row1,
            2: self.Row2,
        }
        return _options.get(index)
