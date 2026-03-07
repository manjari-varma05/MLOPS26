import logging

class ColorFormatter(logging.Formatter):

    COLORS = {
        "INFO": "\033[92m",
        "WARNING": "\033[93m",
        "ERROR": "\033[91m",
        "RESET": "\033[0m"
    }

    def format(self, record):
        color = self.COLORS.get(record.levelname, "")
        reset = self.COLORS["RESET"]
        message = super().format(record)
        return f"{color}{message}{reset}"


def setup_logger():
    logger = logging.getLogger("mlops")
    logger.setLevel(logging.INFO)

    handler = logging.StreamHandler()
    formatter = ColorFormatter("%(levelname)s - %(message)s")

    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger


if __name__ == "__main__":
    logger = setup_logger()

    logger.info("Pipeline started")
    logger.warning("Warning example")
    logger.error("Error example")