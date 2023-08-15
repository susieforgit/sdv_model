#!/usr/bin/env python3

"""Lights model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointString,
    Model,
)

from sdv_model.Body.Lights.Backup import Backup
from sdv_model.Body.Lights.Beam import Beam
from sdv_model.Body.Lights.Brake import Brake
from sdv_model.Body.Lights.DirectionIndicator import DirectionIndicator
from sdv_model.Body.Lights.Fog import Fog
from sdv_model.Body.Lights.Hazard import Hazard
from sdv_model.Body.Lights.LicensePlate import LicensePlate
from sdv_model.Body.Lights.Parking import Parking
from sdv_model.Body.Lights.Running import Running


class Lights(Model):
    """Lights model.

    Attributes
    ----------
    LightSwitch: actuator
        Status of the vehicle main light switch.

        A vehicle typically does not support all alternatives. Which lights that actually are lit may vary according to vehicle configuration and local legislation. OFF is typically indicated by 0. POSITION is typically indicated by ISO 7000 symbol 0456. DAYTIME_RUNNING_LIGHTS (DRL) can be indicated by ISO 7000 symbol 2611. AUTO indicates that vehicle automatically selects suitable lights. BEAM is typically indicated by ISO 7000 symbol 0083.

        Allowed values: OFF, POSITION, DAYTIME_RUNNING_LIGHTS, AUTO, BEAM
    IsHighBeamSwitchOn: actuator
        Status of the high beam switch. True = high beam enabled. False = high beam not enabled.

        This signal indicates the status of the switch and does not indicate if low or high beam actually are on. That typically depends on vehicle logic and other signals like Lights.LightSwitch and Vehicle.LowVoltageSystemState.

    Beam: branch
        Beam lights.

    Running: branch
        Running lights.

    Backup: branch
        Backup lights.

    Parking: branch
        Parking lights.

    Fog: branch
        Fog lights.

    LicensePlate: branch
        License plate lights.

    Brake: branch
        None

    Hazard: branch
        Hazard lights.

    DirectionIndicator: branch
        Indicator lights.

    """

    def __init__(self, name, parent):
        """Create a new Lights model."""
        super().__init__(parent)
        self.name = name

        self.LightSwitch = DataPointString("LightSwitch", self)
        self.IsHighBeamSwitchOn = DataPointBoolean("IsHighBeamSwitchOn", self)
        self.Beam = BeamCollection("Beam", self)
        self.Running = Running("Running", self)
        self.Backup = Backup("Backup", self)
        self.Parking = Parking("Parking", self)
        self.Fog = FogCollection("Fog", self)
        self.LicensePlate = LicensePlate("LicensePlate", self)
        self.Brake = Brake("Brake", self)
        self.Hazard = Hazard("Hazard", self)
        self.DirectionIndicator = DirectionIndicatorCollection("DirectionIndicator", self)

class BeamCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Low = Beam("Low", self)
        self.High = Beam("High", self)

    def element(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range [1, 2]")
        _options = {{
            1: self.Low,
            2: self.High,
        }
        return _options.get(index)

class FogCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Rear = Fog("Rear", self)
        self.Front = Fog("Front", self)

    def element(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range [1, 2]")
        _options = {{
            1: self.Rear,
            2: self.Front,
        }
        return _options.get(index)

class DirectionIndicatorCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Left = DirectionIndicator("Left", self)
        self.Right = DirectionIndicator("Right", self)

    def element(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range [1, 2]")
        _options = {{
            1: self.Left,
            2: self.Right,
        }
        return _options.get(index)
