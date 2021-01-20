import logging, json
from subprocess import PIPE, Popen
from easysettings import load_json_settings


config = load_json_settings('app.json')
app_name = config['app_name']


def Ssh(host, command):
    """
    Send shell command
    """
    out, err = Popen(["ssh", "%s" % host, command],
                     stdin=PIPE, stdout=PIPE, stderr=PIPE).communicate()
    if err == []:
        return err
    else:
        return out

class Log():
    """
    Log program data
    """
    def __init__(self, name):         
        # Create an app logger
        self.log = logging.getLogger(name)

        # Create handlers
        self.c_handler = logging.StreamHandler()
        self.f_handler = logging.FileHandler('%s.log' % name)
        self.c_handler.setLevel(logging.WARNING)
        self.f_handler.setLevel(logging.ERROR)

        # Create formatters and add it to handlers
        self.c_format = logging.Formatter('[%(levelname)s] %(message)s')
        self.f_format = logging.Formatter( '%(asctime)s [%(levelname)s] %(message)s')
        self.c_handler.setFormatter( self.c_format)
        self.f_handler.setFormatter( self.f_format)

        # Add handlers to the logger
        self.log.addHandler(self.c_handler)
        self.log.addHandler(self.f_handler)

    def Console(self, msg):
        self.log.warning(msg)
        #log.error('This is an error')
