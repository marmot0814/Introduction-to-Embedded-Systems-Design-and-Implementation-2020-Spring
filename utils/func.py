import datetime

def speed_of_sound(t):
    return 331.3 + 0.606 * t

def now():
    return datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S")

def log(device):
    return "[%s]@%-10s" % (now(), device)
