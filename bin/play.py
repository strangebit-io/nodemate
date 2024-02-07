from sys import argv
import argparse
import sys
import os

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))
print(os.path.dirname(SCRIPT_DIR))
from lib.nodebook.nodebook import NodeBook
from lib.misc.utils import Config
parser = argparse.ArgumentParser(
                    prog='NodeMate',
                    description='Telecommunication devices provisioning tool')

parser.add_argument('nodebook')
parser.add_argument('config')
args = parser.parse_args()

nodebook = NodeBook()
nodebook.load(args.nodebook)

# Load config
config = Config.load_config(args.config)

for task in nodebook.get_tasks():
    task.execute(config["hostname"], \
                config["ssh_port"], \
                config["ssh_username"], \
                config["ssh_password"])