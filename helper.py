import logging
import json
from subprocess import PIPE, Popen
from easysettings import load_json_settings


config = load_json_settings('config.json')
app_name = config['app_name']


def Ssh(host, command):
    """Send ssh command.
    """
    out, err = Popen(["ssh", "%s" % host, command],
                     stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()
    if err == []:
        return err.decode().strip('\r\n')
    else:
        return out.decode().strip('\r\n')


class Log():
    """Log program data.
    """

    def __init__(self, name=__name__):
        # Create an app logger
        self.log = logging.getLogger(name)

        # Create handlers
        self.c_handler = logging.StreamHandler()
        self.f_handler = logging.FileHandler('%s.log' % name)
        logging.addLevelName(31, 'INF')
        self.c_handler.setLevel('INF')
        logging.addLevelName(32, 'LOG')
        self.f_handler.setLevel('LOG')

        # Create formatters and add it to handlers
        self.c_format = logging.Formatter('[%(levelname)s] %(message)s')
        self.f_format = logging.Formatter(
            '%(asctime)s %(message)s', '%Y-%m-%d %H:%M:%S')
        self.c_handler.setFormatter(self.c_format)
        self.f_handler.setFormatter(self.f_format)

        # Add handlers to the logger
        self.log.addHandler(self.c_handler)
        self.log.addHandler(self.f_handler)

    def Console(self, msg):
        self.log.log(31, msg)

    def File(self, msg):
        self.log.log(32, msg)
