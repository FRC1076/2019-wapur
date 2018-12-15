import json
import udp_channels as udp
from Line import get_line


def cart_to_neo(location):
    x, y = location
    #check if even

    if (x % 2 == 0):
        #x is even
        val = (x * 8) + (7 - y)

    else:
        #x is odd
        val = (x * 8) + y

    #print(val)
    return val


class JoyLights:
    def __init__(self, ard_addr, joystick):
        # create a socket to send to the arduion
        # initialize a counter to 0
        self.counter = 0

        self.sender = udp.UDPChannel()
        self.receiver = udp.UDPChannel(
            local_ip="10.10.76.2",
            local_port=8877,
            remote_port=8877,
            remote_ip="10.10.76.7")

    def update_lights(self, x, y):
        # everth 10th that this is called. do this:
        # read joystick values
        # build json packet
        # send json packet to arduion.

        if (self.counter == 10):
            self.counter = 0

            l = get_line(start=(0, 0), end=(round(4 * 8), round(4 * 8)))

            for a in l:
                w = cart_to_neo(location=a)

            data = {'sender': 'joystick', 'message': 'joy', 'values': w}

            message = json.dumps(data)

            print(message)  #for debuging
            self.sender.send_to(message)s
        else:
            self.counter += 1
