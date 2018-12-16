import json
import udp_channels as udp
from Line import get_line

LOCALIP = "localhost"
LOCALPORT = 8877
REMOTEPORT = 8877
REMOTEIP = "localhost"


def cart_to_neo(location):
    x, y = location
    #check if even

    if (x % 2 == 0):
        #x is even
        val = (x * 8) + (7 - y)

    else:
        #x is odd
        val = (x * 8) + y

    if (y < 0):
        val += 256

    #print(val)
    return val


class JoyLights:
    def __init__(self, ard_addr, joystick):
        # create a socket to send to the arduion
        # initialize a counter to 0
        self.counter = 0

        self.sender = udp.UDPChannel()
        self.receiver = udp.UDPChannel(
            local_ip=LOCALIP,
            local_port=LOCALPORT,
            remote_port=REMOTEPORT,
            remote_ip=REMOTEIP)

    def update_lights(self, x, y):
        # everth 10th that this is called. do this:
        # read joystick values
        # build json packet
        # send json packet to arduion.

        if (self.counter == 10):
            self.counter = 0

            l = get_line(start=(0, 0), end=(round(x * 8), round(y * 8)))
            print(l)
            w = []
            for a in l:
                w.append(cart_to_neo(location=a))
            data = {
                'sender': 'joystick',
                'message': 'raw_display',
                'num_pixels': len(w),
                'pixel_values': w
            }

            message = json.dumps(data)

            print(message)  #for debuging
            self.sender.send_to(message)
        else:
            self.counter += 1
