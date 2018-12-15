import json
import udp_channels as udp
import Line


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
            data = {
                'sender': 'joystick',
                'message': 'joy',
                'x': x,
                'y': y,
            }

            message = json.dumps(data)

            print(message)  #for debuging
            self.sender.send_to(message)
        else:
            self.counter += 1
