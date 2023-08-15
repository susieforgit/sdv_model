#!/usr/bin/env python3

"""HVAC model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointUint8,
    Model,
)

from sdv_model.Cabin.HVAC.Station import Station


class HVAC(Model):
    """HVAC model.

    Attributes
    ----------
    Station: branch
        HVAC for single station in the vehicle

    IsRecirculationActive: actuator
        Is recirculation active.

    IsFrontDefrosterActive: actuator
        Is front defroster active.

    IsRearDefrosterActive: actuator
        Is rear defroster active.

    IsAirConditioningActive: actuator
        Is Air conditioning active.

    AmbientAirTemperature: sensor
        Ambient air temperature inside the vehicle.

        Unit: celsius
    PowerOptimizeLevel: actuator
        Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.

        Value range: [0, 10]
    """

    def __init__(self, name, parent):
        """Create a new HVAC model."""
        super().__init__(parent)
        self.name = name

        self.Station = StationCollection("Station", self)
        self.IsRecirculationActive = DataPointBoolean("IsRecirculationActive", self)
        self.IsFrontDefrosterActive = DataPointBoolean("IsFrontDefrosterActive", self)
        self.IsRearDefrosterActive = DataPointBoolean("IsRearDefrosterActive", self)
        self.IsAirConditioningActive = DataPointBoolean("IsAirConditioningActive", self)
        self.AmbientAirTemperature = DataPointFloat("AmbientAirTemperature", self)
        self.PowerOptimizeLevel = DataPointUint8("PowerOptimizeLevel", self)

class StationCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Row1 = self.RowType("Row1", self)
        self.Row2 = self.RowType("Row2", self)
        self.Row3 = self.RowType("Row3", self)
        self.Row4 = self.RowType("Row4", self)

    def Row(self, index: int):
        if index < 1 or index > 4:
            raise IndexError(f"Index {index} is out of range [1, 4]")
        _options = {{
            1: self.Row1,
            2: self.Row2,
            3: self.Row3,
            4: self.Row4,
        }
        return _options.get(index)

    class RowType(Model):
        def __init__(self, name, parent):
            super().__init__(parent)
            self.name = name
            self.Left = Station("Left", self)
            self.Right = Station("Right", self)

        def element(self, index: int):
            if index < 1 or index > 2:
                raise IndexError(f"Index {index} is out of range [1, 2]")
            _options = {{
                1: self.Left,
                2: self.Right,
            }
            return _options.get(index)
