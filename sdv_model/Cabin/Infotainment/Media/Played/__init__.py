#!/usr/bin/env python3

"""Played model."""

# pylint: disable=C0103,R0801,R0902,R0915,C0301,W0235


from sdv.model import (
    DataPointFloat,
    DataPointString,
    Model,
)


class Played(Model):
    """Played model.

    Attributes
    ----------
    Source: actuator
        Media selected for playback

        Allowed values: UNKNOWN, SIRIUS_XM, AM, FM, DAB, TV, CD, DVD, AUX, USB, DISK, BLUETOOTH, INTERNET, VOICE, BEEP
    Artist: sensor
        Name of artist being played

    Album: sensor
        Name of album being played

    Track: sensor
        Name of track being played

    URI: sensor
        User Resource associated with the media

    PlaybackRate: actuator
        Current playback rate of media being played.

        The normal playback rate is multiplied by this value to obtain the current rate, so a value of 1.0 indicates normal speed. Values of lower than 1.0 make the media play slower than normal. Values of higher than 1.0 make the media play faster than normal.

    """

    def __init__(self, name, parent):
        """Create a new Played model."""
        super().__init__(parent)
        self.name = name

        self.Source = DataPointString("Source", self)
        self.Artist = DataPointString("Artist", self)
        self.Album = DataPointString("Album", self)
        self.Track = DataPointString("Track", self)
        self.URI = DataPointString("URI", self)
        self.PlaybackRate = DataPointFloat("PlaybackRate", self)
