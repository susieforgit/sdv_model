#!/usr/bin/env python3

"""Infotainment model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointUint8,
    Model,
)

from sdv_model.Cabin.Infotainment.HMI import HMI
from sdv_model.Cabin.Infotainment.Media import Media
from sdv_model.Cabin.Infotainment.Navigation import Navigation
from sdv_model.Cabin.Infotainment.SmartphoneProjection import SmartphoneProjection


class Infotainment(Model):
    """Infotainment model.

    Attributes
    ----------
    Media: branch
        All Media actions

    Navigation: branch
        All navigation actions

    HMI: branch
        HMI related signals

    SmartphoneProjection: branch
        All smartphone projection actions.

    PowerOptimizeLevel: actuator
        Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.

        Value range: [0, 10]
    """

    def __init__(self, name, parent):
        """Create a new Infotainment model."""
        super().__init__(parent)
        self.name = name

        self.Media = Media("Media", self)
        self.Navigation = Navigation("Navigation", self)
        self.HMI = HMI("HMI", self)
        self.SmartphoneProjection = SmartphoneProjection("SmartphoneProjection", self)
        self.PowerOptimizeLevel = DataPointUint8("PowerOptimizeLevel", self)
