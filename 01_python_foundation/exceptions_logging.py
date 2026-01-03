# Todo: Exceptions + Logging
# print(): For humans, temporary. logging: for systems, debugging, production. used to record errors, track execution,
# debug failures later, save information to files/ consoles.

import logging  # imports python's standard logging framework

# configuring the logging system using basicConfig()
logging.basicConfig(level=logging.ERROR, filename="error_logs_03_01_26.log")  # to log errors that are critical.
# prevents logging lower levels like debug,info. here, logs are saved into .log file.
# logging levels:- DEBUG - Detailed internal info, INFO - General program flow, WARNING - Something unusual, ERROR -
# program failed at a step, CRITICAL - program cannot continue.

try:
    value = 10 / 0
except Exception as e:  # catches Zero Division error
    logging.error("Calculation failed", exc_info=True)  # exc_info = True includes full exception details stack trace.

print("Program continues without crashing")

# Todo: Enabling specific levels for specific modules.
# logging.getLogger("sensor").setLevel(logging.DEBUG)

# work flow
# 1) python raises exception
# 2) except catches it
# 3) logging records
# 4) program continues safely
