from pathlib import Path
import sys

# Adiciona a raiz do projeto ao PYTHONPATH
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from custom_components.tuya_energy_meter.protocol import TuyaProtocol


HOST = "192.168.1.212"          # <-- coloque o IP do medidor
DEVICE_ID = "eb8f6bd02037969225kqoh"
LOCAL_KEY = "`BOz7TFTOX&3L<QS"


def main():
    protocol = TuyaProtocol(
        host=HOST,
        device_id=DEVICE_ID,
        local_key=LOCAL_KEY,
    )

    status = protocol.status()

    print(status)


if __name__ == "__main__":
    main()