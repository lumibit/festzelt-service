import json
import logging

log = logging.getLogger(__name__)


def storage_load(filename):
    """Load Data from a JSON File

    Arguments:
        filename {string} -- Path to JSON File to load

    Returns:
        [dict] -- [description]
    """

    try:
        with open(filename, encoding="utf-8") as f:
            loaded_content = json.load(f)
        loaded_data = loaded_content["data"]
        log.info('Last Run from stored data:' + loaded_content["last_state"])
    except:
        loaded_data = None
        log.warning('Loading JSON Data Failed. Maybe first run?')

    return loaded_data


def storage_dump(filename, last_run, content):
    """Stores the gathered data back to json

    Arguments:
        filename {string} -- Storage Filename
        last_run {string} -- Date and Time of Last job Execution
        content {[string]} -- Crawled data from jobs
    """

    data = {"last_state": last_run, "data": content}

    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
