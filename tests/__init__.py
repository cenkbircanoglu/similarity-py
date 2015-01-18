__author__ = 'cenk'

import logging
import sys

test_logger = logging.getLogger()
test_logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('\t%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
test_logger.addHandler(ch)