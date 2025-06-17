import os

from camel.logger import get_logger, set_log_file, set_log_level

# Set log output to a file using an absolute path
log_path = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'camel.log',
)
print(log_path)
set_log_file(log_path)

# Set the logging level
set_log_level('DEBUG')

# Use the logger
logger = get_logger(__name__)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')