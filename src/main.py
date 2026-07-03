from config.settings import PROJECT_ROOT
from core.version import APP_NAME, VERSION, AUTHOR
from core.logger import logger


def main():
    logger.info("System startup")
    print(f"Project Root : {PROJECT_ROOT}")

    print("=" * 60)
    print(APP_NAME)
    print(f"Version : {VERSION}")
    print(f"Author  : {AUTHOR}")
    print("=" * 60)
    print("System initialized successfully.")
    print("=" * 60)

    logger.info("Startup completed")


if __name__ == "__main__":
    main()