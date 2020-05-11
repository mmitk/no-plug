import psutil
import threading
#import Tkinter
#import tkMessageBox

class battery_indicator:
    def __init__(self):
        self.battery = psutil.sensors_battery()
        self.is_charging = self.battery.power_plugged
        self.percent = self.battery.percent
        self.status = False

    @property
    def is_plugged(self):
        return self.is_plugged

    def update(self):
        self.percent = self.battery.percent
        self.is_charging = self.battery.power_plugged

        if self.is_charging == True and self.percent == 99:
            self.status = True
    
    def get_status(self):
        return self.status


def loop():
    bat_indicator = battery_indicator()
    global unplug_status 
    unplug_status = True
    while not bat_indicator.get_status():
        bat_indicator.update()
        if not bat_indicator.is_charging: 
            unplug_status = False
            return False




if __name__ == "__main__":
    #avail = threading.Event()
    thread = threading.Thread(target = loop)
    thread.start()
    
    thread.join()


    if unplug_status:
        msg = 'You\'re battery is charged! time to unplug!'
    else:
        msg = 'Battery unplugged, charge is: {}'.format(psutil.sensors_battery().percent)

    import ctypes  # An included library with Python install.   
    ctypes.windll.user32.MessageBoxW(0, msg, "Battery Indicator", 1)
#print('Current Battery Perecentage: {}\n Plugged in status: {}'.format(str(percent), str(is_plugged)))