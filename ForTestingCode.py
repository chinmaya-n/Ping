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
    
    previous_frame_fingers = []

    # Now we will implement some methods
    def on_connect(self, controller):
        print "Just got Connected"
        #controller.enable_gesture(Leap.Gesture.TYPE_KEY_TAP, True)
        #controller.enable_gesture(Leap.Gesture.TYPE_CIRCLE, True)
        #if controller.is_gesture_enabled(Leap.Gesture.TYPE_KEY_TAP or Leap.Gesture.TYPE_CIRCLE) :
            #print("Key Tap Gesture or Circle Gesture is enabled")

    def on_disconnect(self, controller):
        print("Disconnected")

    def on_init(self, controller):
        print("Initialized")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        frame = controller.frame()
        print("Frame Data: ", frame.id, "; No of Fingers: ", len(frame.fingers))
        fingerList = frame.fingers
        frame_fingers = []
        for finger in fingerList :
            
            fingerId = finger.id
            
            # if finger not present then send a signel to create
            if fingerId not in self.previous_frame_fingers :
                vec = Leap.Vector(finger.tip_position)
                print("NewFinger", str(fingerId), vec.x) #, finger.tipPosition)
                #print(str(fingerId), finger.tipPosition.x, finger.tipPosition.y) # for testing
                #self.sig.emitNewFinger(str(fingerId), finger.tipPosition.x, finger.tipPosition.y)
                
            # if finger is present then send a signel for its position
            else :
                print("Update Finger: ", str(fingerId) ) #, finger.tipPosition.x, finger.tipPosition.y)
                #self.sig.emitFingerPositionChange(str(fingerId), finger.tipPosition.x, finger.tipPosition.y)
                self.previous_frame_fingers.remove(fingerId)
                
            # accumulate present frame finger Ids
            frame_fingers.append(fingerId)
        
        # Delete any old fingers from previous_frame_fingers by comparing frame_fingers, the finger Id accumulator
        for fingerId in self.previous_frame_fingers :
            print("This finger ", fingerId, " is not present now")
            #self.sig.emitRemoveFinger(str(fingerId))
        
        # Assign frame_fingers as previous_frame_fingers for next iteration purpose
        self.previous_frame_fingers = frame_fingers        


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