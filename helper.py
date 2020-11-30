from subprocess import PIPE, Popen
from easysettings import load_json_settings

config = load_json_settings('config.json')

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