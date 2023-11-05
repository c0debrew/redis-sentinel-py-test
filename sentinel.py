import logging
import time

from redis import Sentinel
from redis.sentinel import MasterNotFoundError

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main() -> None:
    sentinel = Sentinel(
        [("172.31.14", 5000), ("172.31.15", 5000), ("172.31.16", 5000)],
        socket_connect_timeout=1,
    )

    client = sentinel.master_for("mymaster", socket_timeout=0.1)
    while True:
        try:
            ip, port = client.get_connection_kwargs()[
                "connection_pool"
            ].get_master_address()
            logging.info(f"Master -> {ip}:{port}")
        except MasterNotFoundError:
            logging.warning(
                "Master not found. Sentinel is performing election. Sleep for 1 sec."
            )
            time.sleep(1)


if __name__ == "__main__":
    main()
