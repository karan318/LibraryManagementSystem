import logging

def setup_logging():
  logger = logging.getLogger()
  logger.setLevel(logging.DEBUG)
  debug_handler = logging.FileHandler(filename='debug.log')
  debug_handler.setLevel(logging.DEBUG)
  debug_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  debug_handler.setFormatter(debug_format)

  error_handler = logging.FileHandler("error.log")
  error_handler.setLevel(logging.ERROR)
  error_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
  error_handler.setFormatter(error_format)
  logger.addHandler(debug_handler)
  logger.addHandler(error_handler)

