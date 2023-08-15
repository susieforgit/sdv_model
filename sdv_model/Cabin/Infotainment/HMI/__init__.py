#!/usr/bin/env python3

"""HMI model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointString,
    Model,
)


class HMI(Model):
    """HMI model.

    Attributes
    ----------
    CurrentLanguage: sensor
        ISO 639-1 standard language code for the current HMI

    DateFormat: actuator
        Date format used in the current HMI

        Allowed values: YYYY_MM_DD, DD_MM_YYYY, MM_DD_YYYY, YY_MM_DD, DD_MM_YY, MM_DD_YY
    TimeFormat: actuator
        Time format used in the current HMI

        Allowed values: HR_12, HR_24
    DistanceUnit: actuator
        Distance unit used in the current HMI

        Allowed values: MILES, KILOMETERS
    FuelVolumeUnit: actuator
        Fuel volume unit used in the current HMI

        Allowed values: LITER, GALLON_US, GALLON_UK
    FuelEconomyUnits: actuator
        Fuel economy unit used in the current HMI

        Allowed values: MPG_UK, MPG_US, MILES_PER_LITER, KILOMETERS_PER_LITER, LITERS_PER_100_KILOMETERS
    EVEconomyUnits: actuator
        EV fuel economy unit used in the current HMI

        Allowed values: MILES_PER_KILOWATT_HOUR, KILOMETERS_PER_KILOWATT_HOUR, KILOWATT_HOURS_PER_100_MILES, KILOWATT_HOURS_PER_100_KILOMETERS, WATT_HOURS_PER_MILE, WATT_HOURS_PER_KILOMETER
    TemperatureUnit: actuator
        Temperature unit used in the current HMI

        Allowed values: C, F
    TirePressureUnit: actuator
        Tire pressure unit used in the current HMI

        Allowed values: PSI, KPA, BAR
    Brightness: actuator
        Brightness of the HMI, relative to supported range. 0 = Lowest brightness possible. 100 = Maximum Brightness possible.

        The value 0 does not necessarily correspond to a turned off HMI, as it may not be allowed/supported to turn off the HMI completely.

        Value range: [0, 100]
        Unit: percent
    DayNightMode: actuator
        Current display theme

        Allowed values: DAY, NIGHT
    """

    def __init__(self, name, parent):
        """Create a new HMI model."""
        super().__init__(parent)
        self.name = name

        self.CurrentLanguage = DataPointString("CurrentLanguage", self)
        self.DateFormat = DataPointString("DateFormat", self)
        self.TimeFormat = DataPointString("TimeFormat", self)
        self.DistanceUnit = DataPointString("DistanceUnit", self)
        self.FuelVolumeUnit = DataPointString("FuelVolumeUnit", self)
        self.FuelEconomyUnits = DataPointString("FuelEconomyUnits", self)
        self.EVEconomyUnits = DataPointString("EVEconomyUnits", self)
        self.TemperatureUnit = DataPointString("TemperatureUnit", self)
        self.TirePressureUnit = DataPointString("TirePressureUnit", self)
        self.Brightness = DataPointFloat("Brightness", self)
        self.DayNightMode = DataPointString("DayNightMode", self)
