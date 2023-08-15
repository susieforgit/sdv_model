#!/usr/bin/env python3

"""Vehicle model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointBoolean,
    DataPointFloat,
    DataPointInt16,
    DataPointString,
    DataPointUint16,
    DataPointUint8,
    Model,
)

from sdv_model.ADAS import ADAS
from sdv_model.Acceleration import Acceleration
from sdv_model.AngularVelocity import AngularVelocity
from sdv_model.Body import Body
from sdv_model.Cabin import Cabin
from sdv_model.Chassis import Chassis
from sdv_model.Connectivity import Connectivity
from sdv_model.CurrentLocation import CurrentLocation
from sdv_model.Driver import Driver
from sdv_model.Exterior import Exterior
from sdv_model.LowVoltageBattery import LowVoltageBattery
from sdv_model.OBD import OBD
from sdv_model.Powertrain import Powertrain
from sdv_model.Service import Service
from sdv_model.Trailer import Trailer
from sdv_model.VehicleIdentification import VehicleIdentification
from sdv_model.VersionVSS import VersionVSS


class Vehicle(Model):
    """Vehicle model.

    Attributes
    ----------
    VersionVSS: branch
        Supported Version of VSS.

    VehicleIdentification: branch
        Attributes that identify a vehicle.

    LowVoltageSystemState: sensor
        State of the supply voltage of the control units (usually 12V).

        Allowed values: UNDEFINED, LOCK, OFF, ACC, ON, START
    LowVoltageBattery: branch
        Signals related to low voltage battery.

    Speed: sensor
        Vehicle speed.

        Unit: km/h
    TravelledDistance: sensor
        Odometer reading, total distance traveled during the lifetime of the vehicle.

        Unit: km
    TraveledDistance: sensor
        Odometer reading, total distance traveled during the lifetime of the vehicle.

        Unit: km
    TraveledDistanceSinceStart: sensor
        Distance traveled since start of current trip.

        A new trip is considered to start when engine gets enabled (e.g. LowVoltageSystemState in ON or START mode). A trip is considered to end when engine is no longer enabled. The signal may however keep the value of the last trip until a new trip is started.

        Unit: km
    StartTime: attribute (string)
        Start time of current or latest trip, formatted according to ISO 8601 with UTC time zone.

        This signal is supposed to be set whenever a new trip starts. A new trip is considered to start when engine gets enabled (e.g. LowVoltageSystemState in ON or START mode). A trip is considered to end when engine is no longer enabled. The default value indicates that the vehicle never has been started, or that latest start time is unknown.

    TripDuration: sensor
        Duration of latest trip.

        This signal is not assumed to be continuously updated, but instead set to 0 when a trip starts and set to the the actual duration of the trip when a trip ends. A new trip is considered to start when engine gets enabled (e.g. LowVoltageSystemState in ON or START mode). A trip is considered to end when engine is no longer enabled.

        Unit: s
    TripMeterReading: actuator
        Trip meter reading.

        The trip meter is an odometer that can be manually reset by the driver

        Unit: km
    IsBrokenDown: sensor
        Vehicle breakdown or any similar event causing vehicle to stop on the road, that might pose a risk to other road users. True = Vehicle broken down on the road, due to e.g. engine problems, flat tire, out of gas, brake problems. False = Vehicle not broken down.

        Actual criteria and method used to decide if a vehicle is broken down is implementation specific.

    IsMoving: sensor
        Indicates whether the vehicle is stationary or moving.

    AverageSpeed: sensor
        Average speed for the current trip.

        A new trip is considered to start when engine gets enabled (e.g. LowVoltageSystemState in ON or START mode). A trip is considered to end when engine is no longer enabled. The signal may however keep the value of the last trip until a new trip is started. Calculation of average speed may exclude periods when the vehicle for example is not moving or transmission is in neutral.

        Unit: km/h
    Acceleration: branch
        Spatial acceleration. Axis definitions according to ISO 8855.

    AngularVelocity: branch
        Spatial rotation. Axis definitions according to ISO 8855.

    RoofLoad: attribute (int16)
        The permitted total weight of cargo and installations (e.g. a roof rack) on top of the vehicle.

        Unit: kg
    CargoVolume: attribute (float)
        The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.

        Value range: [0, ]
        Unit: l
    EmissionsCO2: attribute (int16)
        The CO2 emissions.

        Unit: g/km
    CurrentOverallWeight: sensor
        Current overall Vehicle weight. Including passengers, cargo and other load inside the car.

        Unit: kg
    CurbWeight: attribute (uint16)
        Vehicle curb weight, including all liquids and full tank of fuel, but no cargo or passengers.

        Unit: kg
    GrossWeight: attribute (uint16)
        Curb weight of vehicle, including all liquids and full tank of fuel and full load of cargo and passengers.

        Unit: kg
    MaxTowWeight: attribute (uint16)
        Maximum weight of trailer.

        Unit: kg
    MaxTowBallWeight: attribute (uint16)
        Maximum vertical weight on the tow ball of a trailer.

        Unit: kg
    Length: attribute (uint16)
        Overall vehicle length.

        Unit: mm
    Height: attribute (uint16)
        Overall vehicle height.

        Unit: mm
    Width: attribute (uint16)
        Overall vehicle width.

        Unit: mm
    Trailer: branch
        Trailer signals.

    CurrentLocation: branch
        The current latitude and longitude of the vehicle.

    PowerOptimizeLevel: actuator
        Power optimization level for this branch/subsystem. A higher number indicates more aggressive power optimization. Level 0 indicates that all functionality is enabled, no power optimization enabled. Level 10 indicates most aggressive power optimization mode, only essential functionality enabled.

        Value range: [0, 10]
    Powertrain: branch
        Powertrain data for battery management, etc.

    Body: branch
        All body components.

    Cabin: branch
        All in-cabin components, including doors.

    ADAS: branch
        All Advanced Driver Assist Systems data.

    Chassis: branch
        All data concerning steering, suspension, wheels, and brakes.

    OBD: branch
        OBD data.

    Driver: branch
        Driver data.

    Exterior: branch
        Information about exterior measured by vehicle.

    Service: branch
        Service data.

    Connectivity: branch
        Connectivity data.

    """

    def __init__(self, name):
        """Create a new Vehicle model."""
        super().__init__()
        self.name = name

        self.VersionVSS = VersionVSS("VersionVSS", self)
        self.VehicleIdentification = VehicleIdentification("VehicleIdentification", self)
        self.LowVoltageSystemState = DataPointString("LowVoltageSystemState", self)
        self.LowVoltageBattery = LowVoltageBattery("LowVoltageBattery", self)
        self.Speed = DataPointFloat("Speed", self)
        self.TravelledDistance = DataPointFloat("TravelledDistance", self)
        self.TraveledDistance = DataPointFloat("TraveledDistance", self)
        self.TraveledDistanceSinceStart = DataPointFloat("TraveledDistanceSinceStart", self)
        self.StartTime = DataPointString("StartTime", self)
        self.TripDuration = DataPointFloat("TripDuration", self)
        self.TripMeterReading = DataPointFloat("TripMeterReading", self)
        self.IsBrokenDown = DataPointBoolean("IsBrokenDown", self)
        self.IsMoving = DataPointBoolean("IsMoving", self)
        self.AverageSpeed = DataPointFloat("AverageSpeed", self)
        self.Acceleration = Acceleration("Acceleration", self)
        self.AngularVelocity = AngularVelocity("AngularVelocity", self)
        self.RoofLoad = DataPointInt16("RoofLoad", self)
        self.CargoVolume = DataPointFloat("CargoVolume", self)
        self.EmissionsCO2 = DataPointInt16("EmissionsCO2", self)
        self.CurrentOverallWeight = DataPointUint16("CurrentOverallWeight", self)
        self.CurbWeight = DataPointUint16("CurbWeight", self)
        self.GrossWeight = DataPointUint16("GrossWeight", self)
        self.MaxTowWeight = DataPointUint16("MaxTowWeight", self)
        self.MaxTowBallWeight = DataPointUint16("MaxTowBallWeight", self)
        self.Length = DataPointUint16("Length", self)
        self.Height = DataPointUint16("Height", self)
        self.Width = DataPointUint16("Width", self)
        self.Trailer = Trailer("Trailer", self)
        self.CurrentLocation = CurrentLocation("CurrentLocation", self)
        self.PowerOptimizeLevel = DataPointUint8("PowerOptimizeLevel", self)
        self.Powertrain = Powertrain("Powertrain", self)
        self.Body = Body("Body", self)
        self.Cabin = Cabin("Cabin", self)
        self.ADAS = ADAS("ADAS", self)
        self.Chassis = Chassis("Chassis", self)
        self.OBD = OBD("OBD", self)
        self.Driver = Driver("Driver", self)
        self.Exterior = Exterior("Exterior", self)
        self.Service = Service("Service", self)
        self.Connectivity = Connectivity("Connectivity", self)


vehicle = Vehicle("Vehicle")
