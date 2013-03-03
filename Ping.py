################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

__author__ = 'inblueswithu'

import Leap, sys

class Ping(Leap.Listener) :

    # Now we will implement some methods
    def on_connect(self, controller):
        print "Just got Connected"
        controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP, True)
        controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE, True)
        if controller.is_gesture_enabled(Leap.Gesture.TYPE_KEY_TAP or Leap.Gesture.TYPE_CIRCLE) :
            print("Key Tap Gesture or Circle Gesture is enabled")

    def on_disconnect(self, controller):
        print("Disconnected")

    def on_init(self, controller):
        print("Initialized")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        frame = controller.frame()
        print("\n")

        #Frame Information
        print("Frame Information")
        print "Id:", frame.id, "; Timestamp:", frame.timestamp, " isValid:", ("no","yes")[frame.is_valid==True]

        #Hand Information
        _hands_count = len(frame.hands)
        print "Hands:", _hands_count,
        hands = frame.hands
        for hand in hands :
            print "Hand ids:", hand.id, "Hand "

        #Finger Information based on both hand & frame
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
        elif len(frame.fingers)>0 :
            print "Finger ids: \r"
            for finger in frame.fingers :
                print finger.id,
                print "length:", finger.length, "width:", finger.width,  "tip-position:", finger.tip_position,\
                    "vector:", finger.direction, #"to-string", finger.to_String,
                if finger.is_finger :
                    print "Valid Finger \r"

        #Tools Information
        if len(frame.tools)>0 :
            print("Tools Information")
            print("Count:", len(frame.tools))
            for tool in frame.tools :
                print("Id",tool.id,"Length:",tool.length,"Width",tool.width,"Tip Position:",tool.tip_position,"Vector",
                      tool.direction,"Velocity",tool.tip_velocity, "isValid:",("no","yes")[tool.is_tool==True],
                      "Hand associated id:",tool.hand.id)

        #Gesture Information
        if len(frame.gestures())>0 :
            for gesture in frame.gestures() :
                if gesture.type == Leap.Gesture.TYPE_KEY_TAP :
                    keyStroke = Leap.KeyTapGesture(gesture)
                    finger = keyStroke.pointable
                    print("Gesture id:", gesture.id,"Key Tap Gesture Type:", gesture.type, "Finger id associated:", finger.id, "Gesture duration(ms):", gesture.duration)
                elif gesture.type == Leap.Gesture.TYPE_CIRCLE :
                    print("Gesture id:", gesture.id,"Circle Gesture Type:", gesture.type, "Finger id associated:", gesture.pointable.id, "Gesture duration(ms):", gesture.duration)

        else :
            print("No Gestures")


def main() :
    # Main function to be executed while running the program
    controller = Leap.Controller()
    while not controller.is_connected :
        print "Controller status: OFF"
    if controller.is_connected :
        print "Controller status: ON"
    listener = Ping()
    controller.add_listener(listener)
    print "Added Listener!"
    print "Press any key to close the Ping"
    sys.stdin.readline()
    controller.remove_listener(listener)

if __name__ == '__main__' :
    main()