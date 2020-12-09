import logging
from subprocess import PIPE, Popen
from easysettings import load_json_settings


config = load_json_settings('app.json')
app_name=config['app_name']

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


# Create a custom logger
logger = logging.getLogger(__name__)

# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('%s.log' % app_name)
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(levelname)s: %(message)s')
f_format = logging.Formatter(
    '%(asctime)s: %(levelname)s: %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
logger.addHandler(c_handler)
logger.addHandler(f_handler)

# Test logs
#logger.warning('This is a warning')
#logger.error('This is an error')
