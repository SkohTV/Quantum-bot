"""
Get all stdout from the bot
Add them to logs database
Send it to host console
"""
from datetime import datetime
from sty import ef, fg, rs


def logger(text:str, *specific:str) -> None:
    """Receive all stdout and process them

    Args:
        text (str): Message to add to logs seen on console and discord msg logs
        specific (tuple): Custom kind of notification to log (priority, error...)
    """
    now = str(datetime.now())
    time = f'[{now[0:4]}-{now[5:7]}-{now[8:10]} {now[11:13]}:{now[14:16]}:{now[17:19]}]'
    if len(specific) == 0:
        message = ("{} {}".format(time, text))
    elif specific[0] == 'err':
        message = ("{} {}".format(fg(255,0,0) + time + fg.rs, fg(255,0,0) + text + fg.rs))
    print(message)