import os
import sys
import logging
from logging import Logger

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

log_dir = os.path.join(os.getcwd(), "logs")
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger:Logger = logging.getLogger("mlproject2Logger")
