#!/usr/bin/env python3

"""ADAS model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointString,
    DataPointUint8,
    Model,
)

from sdv_model.ADAS.ABS import ABS
from sdv_model.ADAS.CruiseControl import CruiseControl
from sdv_model.ADAS.EBA import EBA
from sdv_model.ADAS.EBD import EBD
from sdv_model.ADAS.ESC import ESC
from sdv_model.ADAS.LaneDepartureDetection import LaneDepartureDetection
from sdv_model.ADAS.ObstacleDetection import ObstacleDetection
from sdv_model.ADAS.TCS import TCS


class ADAS(Model):
    """ADAS model.

    Attributes
    ----------
    ActiveAutonomyLevel: sensor
        Indicates the currently active level of autonomy according to SAE J3016 taxonomy.

        Follows https://www.sae.org/news/2019/01/sae-updates-j3016-automated-driving-graphic taxonomy. For SAE levels 3 and 4 the system is required to alert the driver before it will disengage. Level 4 systems are required to reach a safe state even if a driver does not take over. Only level 5 systems are required to not rely on a driver at all. While level 2 systems require the driver to be monitoring the system at all times, many level 2 systems, often termed "level 2.5" systems, do warn the driver shortly before reaching their operational limits, therefore we also support the DISENGAGING state for SAE_2.

        Allowed values: SAE_0, SAE_1, SAE_2_DISENGAGING, SAE_2, SAE_3_DISENGAGING, SAE_3, SAE_4_DISENGAGING, SAE_4, SAE_5
    SupportedAutonomyLevel: attribute (string)
        Indicates the highest level of autonomy according to SAE J3016 taxonomy the vehicle is capable of.

        Allowed values: SAE_0, SAE_1, SAE_2, SAE_3, SAE_4, SAE_5
    CruiseControl: branch
        Signals from Cruise Control system.

    LaneDepartureDetection: branch
        Signals from Lane Departure Detection System.

    ObstacleDetection: branch
        Signals form Obstacle Sensor System.

    ABS: branch
        Antilock Braking System signals.

    TCS: branch
        Traction Control System signals.

    ESC: branch
        Electronic Stability Control System signals.

    EBD: branch
        Electronic Brakeforce Distribution (EBD) System signals.

    EBA: branch
        Emergency Brake Assist (EBA) System signals.

    PowerOptimizeLevel: actuator
        Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.

        Value range: [0, 10]
    """

    def __init__(self, name, parent):
        """Create a new ADAS model."""
        super().__init__(parent)
        self.name = name

        self.ActiveAutonomyLevel = DataPointString("ActiveAutonomyLevel", self)
        self.SupportedAutonomyLevel = DataPointString("SupportedAutonomyLevel", self)
        self.CruiseControl = CruiseControl("CruiseControl", self)
        self.LaneDepartureDetection = LaneDepartureDetection("LaneDepartureDetection", self)
        self.ObstacleDetection = ObstacleDetection("ObstacleDetection", self)
        self.ABS = ABS("ABS", self)
        self.TCS = TCS("TCS", self)
        self.ESC = ESC("ESC", self)
        self.EBD = EBD("EBD", self)
        self.EBA = EBA("EBA", self)
        self.PowerOptimizeLevel = DataPointUint8("PowerOptimizeLevel", self)
