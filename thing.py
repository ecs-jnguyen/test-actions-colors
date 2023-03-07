import structlog

if __name__ == "__main__":
    logger = structlog.get_logger()
    logger.info("hello", name="me", age=123)
    logger.warning("bye", name="me", age=123)
    logger.error("ohno", name="me", age=123)
