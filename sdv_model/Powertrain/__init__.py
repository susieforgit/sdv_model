#!/usr/bin/env python3

"""Powertrain model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointString,
    DataPointUint32,
    DataPointUint8,
    Model,
)

from sdv_model.Powertrain.CombustionEngine import CombustionEngine
from sdv_model.Powertrain.ElectricMotor import ElectricMotor
from sdv_model.Powertrain.FuelSystem import FuelSystem
from sdv_model.Powertrain.TractionBattery import TractionBattery
from sdv_model.Powertrain.Transmission import Transmission


class Powertrain(Model):
    """Powertrain model.

    Attributes
    ----------
    AccumulatedBrakingEnergy: sensor
        The accumulated energy from regenerative braking over lifetime.

        Unit: kWh
    Range: sensor
        Remaining range in meters using all energy sources available in the vehicle.

        Unit: m
    Type: attribute (string)
        Defines the powertrain type of the vehicle.

        For vehicles with a combustion engine (including hybrids) more detailed information on fuels supported can be found in FuelSystem.SupportedFuelTypes and FuelSystem.SupportedFuels.

        Allowed values: COMBUSTION, HYBRID, ELECTRIC
    PowerOptimizeLevel: actuator
        Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.

        Value range: [0, 10]
    CombustionEngine: branch
        Engine-specific data, stopping at the bell housing.

    Transmission: branch
        Transmission-specific data, stopping at the drive shafts.

    ElectricMotor: branch
        Electric Motor specific data.

    TractionBattery: branch
        Battery Management data.

    FuelSystem: branch
        Fuel system data.

    """

    def __init__(self, name, parent):
        """Create a new Powertrain model."""
        super().__init__(parent)
        self.name = name

        self.AccumulatedBrakingEnergy = DataPointFloat("AccumulatedBrakingEnergy", self)
        self.Range = DataPointUint32("Range", self)
        self.Type = DataPointString("Type", self)
        self.PowerOptimizeLevel = DataPointUint8("PowerOptimizeLevel", self)
        self.CombustionEngine = CombustionEngine("CombustionEngine", self)
        self.Transmission = Transmission("Transmission", self)
        self.ElectricMotor = ElectricMotor("ElectricMotor", self)
        self.TractionBattery = TractionBattery("TractionBattery", self)
        self.FuelSystem = FuelSystem("FuelSystem", self)
