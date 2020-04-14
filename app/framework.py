import os
import logging
from datetime import datetime
from logging import INFO, DEBUG, WARNING, ERROR, CRITICAL

'''
    LOGGER LEVELS:
 |   DEBUG	    Detailed information, typically of interest only when diagnosing problems.
 |   INFO	    Confirmation that things are working as expected.
 |   WARNING	An indication that something unexpected happened, or indicative of some problem in the near future (e.g. ‘disk space low’). The software is still working as expected.
 |   ERROR	    Due to a more serious problem, the software has not been able to perform some function.
 V   CRITICAL   A serious error, indicating that the program itself may be unable to continue running.
 '''

# set up logging
LOGLEVEL = logging.getLevelName(os.environ.get("PYTHON_LOGLEVEL", "INFO"))


def set_logging():

    if os.environ.get("AWS_EXECUTION_ENV", ""):
        logging.getLogger('').setLevel(LOGLEVEL)

    else:
        # create console handler with a higher log level
        log_to_console = logging.StreamHandler()
        FORMATTER = logging.Formatter('%(levelname)-7s %(name)20s %(message)s')
        log_to_console.setFormatter(FORMATTER)
        logging.getLogger('').addHandler(log_to_console)
        logging.getLogger('').setLevel(LOGLEVEL)

        # Set path for logging
        logfile_path = 'data/logs' + os.sep + \
            str(datetime.now().strftime("%Y%m%d_%H%M%S"))+".log"

        # make dir if it is not existing
        os.makedirs(os.path.dirname(logfile_path), exist_ok=True)

        log_to_file = logging.FileHandler(logfile_path, mode='w')
        log_to_file.setLevel(LOGLEVEL)
        FORMATTER = logging.Formatter(
            '%(asctime)s %(name)20s %(levelname)7s %(message)s')
        log_to_file.setFormatter(FORMATTER)
        logging.getLogger('').addHandler(log_to_file)


set_logging()
