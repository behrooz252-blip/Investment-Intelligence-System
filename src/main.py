from config.settings import PROJECT_ROOT
from core.version import APP_NAME, VERSION, AUTHOR
from core.logger import logger
from data_sources.tsetmc.collector import TSETMCCollector
from storage.file_storage import FileStorage


def main():

    print("=" * 60)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")
    print("=" * 60)

    logger.info("System startup")

    print(f"Project Root : {PROJECT_ROOT}")

    collector = TSETMCCollector()

    collector.connect()

    snapshot = collector.fetch()

    print(snapshot)

    storage = FileStorage()

    sample_data = {
        "index": snapshot.index_value,
        "equal_weight": snapshot.equal_weight_index,
        "timestamp": str(snapshot.timestamp),
    }

    saved_file = storage.save_json(sample_data, "market")

    print(f"Saved to : {saved_file}")

    print("=" * 60)
    print("System initialized successfully.")
    print("=" * 60)

    logger.info("Startup completed")


if __name__ == "__main__":
    main()