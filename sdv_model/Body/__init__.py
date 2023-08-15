#!/usr/bin/env python3

"""Body model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointString,
    DataPointUint8,
    Model,
)

from sdv_model.Body.Hood import Hood
from sdv_model.Body.Horn import Horn
from sdv_model.Body.Lights import Lights
from sdv_model.Body.Mirrors import Mirrors
from sdv_model.Body.Raindetection import Raindetection
from sdv_model.Body.Trunk import Trunk
from sdv_model.Body.Windshield import Windshield


class Body(Model):
    """Body model.

    Attributes
    ----------
    BodyType: attribute (string)
        Body type code as defined by ISO 3779.

    RefuelPosition: attribute (string)
        Location of the fuel cap or charge port.

        Allowed values: FRONT_LEFT, FRONT_RIGHT, MIDDLE_LEFT, MIDDLE_RIGHT, REAR_LEFT, REAR_RIGHT
    Hood: branch
        Hood status.

        The hood is the hinged cover over the engine compartment of a motor vehicles. Depending on vehicle, it can be either in the front or back of the vehicle. Luggage compartments are in VSS called trunks, even if they are located at the front of the vehicle.

    Trunk: branch
        Trunk status.

        A trunk is a luggage compartment in a vehicle. Depending on vehicle, it can be either in the front or back of the vehicle. Some vehicles may have trunks both at the front and at the rear of the vehicle.

    Horn: branch
        Horn signals.

    Raindetection: branch
        Rainsensor signals.

    Windshield: branch
        Windshield signals.

    Lights: branch
        Exterior lights.

    Mirrors: branch
        All mirrors.

    RearMainSpoilerPosition: actuator
        Rear spoiler position, 0% = Spoiler fully stowed. 100% = Spoiler fully exposed.

        Value range: [0, 100]
        Unit: percent
    PowerOptimizeLevel: actuator
        Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.

        Value range: [0, 10]
    """

    def __init__(self, name, parent):
        """Create a new Body model."""
        super().__init__(parent)
        self.name = name

        self.BodyType = DataPointString("BodyType", self)
        self.RefuelPosition = DataPointString("RefuelPosition", self)
        self.Hood = Hood("Hood", self)
        self.Trunk = TrunkCollection("Trunk", self)
        self.Horn = Horn("Horn", self)
        self.Raindetection = Raindetection("Raindetection", self)
        self.Windshield = WindshieldCollection("Windshield", self)
        self.Lights = Lights("Lights", self)
        self.Mirrors = MirrorsCollection("Mirrors", self)
        self.RearMainSpoilerPosition = DataPointFloat("RearMainSpoilerPosition", self)
        self.PowerOptimizeLevel = DataPointUint8("PowerOptimizeLevel", self)

class TrunkCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Front = Trunk("Front", self)
        self.Rear = Trunk("Rear", self)

    def element(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range [1, 2]")
        _options = {{
            1: self.Front,
            2: self.Rear,
        }
        return _options.get(index)

class WindshieldCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Front = Windshield("Front", self)
        self.Rear = Windshield("Rear", self)

    def element(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range [1, 2]")
        _options = {{
            1: self.Front,
            2: self.Rear,
        }
        return _options.get(index)

class MirrorsCollection(Model):
    def __init__(self, name, parent):
        super().__init__(parent)
        self.name = name
        self.Left = Mirrors("Left", self)
        self.Right = Mirrors("Right", self)

    def element(self, index: int):
        if index < 1 or index > 2:
            raise IndexError(f"Index {index} is out of range [1, 2]")
        _options = {{
            1: self.Left,
            2: self.Right,
        }
        return _options.get(index)
