__author__ = 'inblueswithu'

import Leap, sys

class Ping(Leap.Listener) :

    # Now we will implement some methods
    def on_connect(self, controller):
        print "Just got Connected"

    def on_disconnect(self, controller):
        print("Disconnected")

    def on_init(self, controller):
        print("Initialized")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        frame = controller.frame()
        print "Frame id:", frame.id, "; Frame Timestamp:", frame.timestamp, "\r"
        _hands_count = len(frame.hands)
        print "Hands:", _hands_count, "Hand ids:",
        hands = frame.hands
        for hand in hands :
            print hand.id,
        if _hands_count > 0 :
            for hand in hands :
                _fingers_count = len(hand.fingers)
                print "Hand with id:", hand.id , "has", _fingers_count, "Fingers\r"
                print "Finger ids: \r"
                for finger in hand.fingers :
                    print finger.id,
                    print "length:", finger.length, "width:", finger.width,  "tip-position:", finger.tip_position, \
                        "vector:", finger.direction, # "to-string", finger.to_String,
                    if finger.is_finger :
                        print "Valid Finger \r"
                print "\r"


def main() :
    # Main function to be executed while running the program
    controller = Leap.Controller()
    while not controller.is_connected :
        pass
    if controller.is_connected :
        print "Controller status: ON"
    else :
        print "Controller status: OFF"
    listener = Ping()
    controller.add_listener(listener)
    print "Added Listener!"
    print "Press any key to close the Ping"
    sys.stdin.readline()
    controller.remove_listener(listener)

if __name__ == '__main__' :
    main()