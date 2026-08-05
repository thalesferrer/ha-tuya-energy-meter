"""Constants for Tuya Energy Meter."""

from datetime import timedelta

DOMAIN = "tuya_energy_meter"

NAME = "Tuya Energy Meter"

MANUFACTURER = "Tuya"

MODEL = "QS-WIFI-S10-CT02"

VERSION = "0.1.0"

DEFAULT_PORT = 6668

DEFAULT_PROTOCOL_VERSION = 3.5

DEFAULT_TIMEOUT = 5

DEFAULT_SCAN_INTERVAL = timedelta(seconds=5)