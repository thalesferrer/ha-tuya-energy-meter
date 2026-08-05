"""Protocol layer for Tuya Energy Meter."""

from __future__ import annotations

import logging
from typing import Any

import tinytuya

from .const import DEFAULT_PROTOCOL_VERSION

_LOGGER = logging.getLogger(__name__)


class TuyaProtocol:
    """Communication wrapper for TinyTuya."""

    def __init__(
        self,
        host: str,
        device_id: str,
        local_key: str,
    ) -> None:
        """Initialize the connection."""

        self._device = tinytuya.Device(
            dev_id=device_id,
            address=host,
            local_key=local_key,
        )

        self._device.set_version(DEFAULT_PROTOCOL_VERSION)

    def status(self) -> dict[str, Any]:
        """Read all datapoints from the device."""

        _LOGGER.debug("Reading device status")

        return self._device.status()