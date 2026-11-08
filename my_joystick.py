
from donkeycar.parts.controller import Joystick, JoystickController


class MyJoystick(Joystick):
    #An interface to a physical joystick available at /dev/input/js0
    def __init__(self, *args, **kwargs):
        super(MyJoystick, self).__init__(*args, **kwargs)

            
        self.button_names = {
            0x130 : 'X',
            0x133 : 'Y',
            0x132 : 'B',
            0x131 : 'A',
            0x136 : 'LT',
            0x134 : 'LB',
            0x137 : 'RT',
            0x135 : 'RB',
        }


        self.axis_names = {
            0x0 : 'LS',
            0x5 : 'RS',
            0x11 : 'DP',
        }



class MyJoystickController(JoystickController):
    #A Controller object that maps inputs to actions
    def __init__(self, *args, **kwargs):
        super(MyJoystickController, self).__init__(*args, **kwargs)


    def init_js(self):
        #attempt to init joystick
        try:
            self.js = MyJoystick(self.dev_fn)
            self.js.init()
        except FileNotFoundError:
            print(self.dev_fn, "not found.")
            self.js = None
        return self.js is not None


    def init_trigger_maps(self):
        #init set of mapping from buttons to function calls
            
        self.button_down_trigger_map = {
            'RT' : self.increase_max_throttle,
            'LT' : self.decrease_max_throttle,
            'LB' : self.toggle_constant_throttle,
            'B' : self.emergency_stop,
            'A' : self.toggle_mode,
            'Y' : self.erase_last_N_records,
            'X' : self.toggle_manual_recording,
        }


        self.axis_trigger_map = {
            'LS' : self.set_steering,
            'RS' : self.set_throttle,
        }


