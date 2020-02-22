import os
dir_of_executable = os.path.dirname(__file__)

# colors
YELLOW = '\033[33m'
RED = '\033[91m'
ENDC = '\033[0m'
IPFORWARD = '/proc/sys/net/ipv4/ip_forward'
CONFIG_FILE = dir_of_executable + 'settings/config.ini'
LOG_ALL = dir_of_executable + 'logs/everything.log'