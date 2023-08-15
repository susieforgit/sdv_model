#!/usr/bin/env python3

"""Axle model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointUint16,
    DataPointUint8,
    Model,
)

from sdv_model.Chassis.Axle.Wheel import Wheel


class Axle(Model):
    """Axle model.

    Attributes
    ----------
    WheelCount: attribute (uint8)
        Number of wheels on the axle

    WheelDiameter: attribute (float)
        Diameter of wheels (rims without tires), in inches, as per ETRTO / TRA standard.

        Unit: inch
    WheelWidth: attribute (float)
        Width of wheels (rims without tires), in inches, as per ETRTO / TRA standard.

        Unit: inch
    SteeringAngle: sensor
        Single track two-axle model steering angle. Angle according to ISO 8855. Positive = degrees to the left. Negative = degrees to the right.

        Single track two-axle model steering angle refers to the angle that a centrally mounted wheel would have.

        Unit: degrees
    TireDiameter: attribute (float)
        Outer diameter of tires, in inches, as per ETRTO / TRA standard.

        Unit: inch
    TireWidth: attribute (uint16)
        Nominal section width of tires, in mm, as per ETRTO / TRA standard.

        Unit: mm
    TireAspectRatio: attribute (uint8)
        Aspect ratio between tire section height and tire section width, as per ETRTO / TRA standard.

        Unit: percent
    Wheel: branch
        Wheel signals for axle

    """

    def __init__(self, name, parent):
        """Create a new Axle model."""
        super().__init__(parent)
        self.name = name

        self.WheelCount = DataPointUint8("WheelCount", self)
        self.WheelDiameter = DataPointFloat("WheelDiameter", self)
        self.WheelWidth = DataPointFloat("WheelWidth", self)
        self.SteeringAngle = DataPointFloat("SteeringAngle", self)
        self.TireDiameter = DataPointFloat("TireDiameter", self)
        self.TireWidth = DataPointUint16("TireWidth", self)
        self.TireAspectRatio = DataPointUint8("TireAspectRatio", self)
        self.Wheel = WheelCollection("Wheel", self)

class WheelCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Left = Wheel("Left", self)
        self.Right = Wheel("Right", self)

    def element(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range [1, 2]")
        _options = {{
            1: self.Left,
            2: self.Right,
        }
        return _options.get(index)
