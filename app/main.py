import logging
from logging.handlers import TimedRotatingFileHandler
from os.path import join
import sys
from pathlib import Path

# Append root dir path to the sys path so that imports are correctly working no matters from where the app is run.
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import uvicorn
from fastapi import FastAPI

import settings as app_settings
from database import create_db_and_tables
from routers.default import router as default_router
from routers.ticket import router as ticket_router
application = FastAPI()
application.include_router(default_router)
application.include_router(ticket_router)


def configure_logging(console_handler: bool = False):
    """Function configures logging so that logs are saved to a file.

    Args:
        console_handler (bool): If true, a console handler will be configured and logs wil show in the consoles.

    Returns:
        None:
    """
    log_filename = f"{join(app_settings.LOGS_DIR, app_settings.APP_NAME)}.log"
    timed_rotating_file_handler = TimedRotatingFileHandler(log_filename, "midnight")

    log_handlers = [timed_rotating_file_handler]
    if console_handler:
        log_handlers.append(logging.StreamHandler())

    logging.basicConfig(
        format="%(asctime)s [%(threadName)-10s] - %(levelname)s - "
        "%(module)s.%(funcName)s(%(lineno)d): %(message)s",
        level=app_settings.LOGS_LEVEL,
        handlers=log_handlers,
    )
    logging.debug("Logger successfully configured")


def setup_app():
    """Function's goal is to set up the prerequisites before starting the application.

    Returns:
        None:
    """
    configure_logging(True)
    create_db_and_tables()


if __name__ == "__main__":
    setup_app()
    uvicorn.run(application, port=8000, host="localhost")
