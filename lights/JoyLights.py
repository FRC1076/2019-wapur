import json
import udp_channels as udp


class JoyLights:
    def __init__(self, ard_addr, joystick):
        # create a socket to send to the arduion
        # initialize a counter to 0
        self.counter = 0

    def update_lights(self, x, y):
        # everth 10th that this is called. do this:
        # read joystick values
        # build json packet
        # send json packet to arduion.

        if (self.counter == 10):
            counter = 0
            data = {'sender': 'joystick', 'message': 'joy', 'x': x, 'y': y}
            message = json.dumps(data)
            sender = udp.UDPChannel()
            sender.send_to(message)
        else:
            counter += 1
