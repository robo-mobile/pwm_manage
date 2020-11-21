import logging
from systemd.journal import JournaldLogHandler


def logger():
    Logger = logging.getLogger("pwm_manage")
    journald_handler = JournaldLogHandler()

    # set a formatter to include the level name
    journald_handler.setFormatter(logging.Formatter(
        '[%(levelname)s] %(message)s'
    ))

    # add the journald handler to the current logger
    Logger.addHandler(journald_handler)
    Logger.addHandler(logging.StreamHandler())

    # optionally set the logging level
    Logger.setLevel(logging.DEBUG)
    return Logger
