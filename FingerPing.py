################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

__author__ = 'inblueswithu'

import Leap, sys
from QtCore import pyqtSignal
from QtDeclarative import QDeclarativeView
from QtGui import QApplication


class FingerPing(Leap.Listener) :
    
    # Variables & Signals
    previous_frame_fingers = []
    finger_position_change = pyqtSignal()
    new_finger = pyqtSignal()
    remove_finger = pyqtSignal()

    # Now we will implement some methods
    def on_init(self, controller):
        print("Initialized")
        
    def on_connect(self, controller):
        print("Connected")
        finger_position_change.connect(fingerPostionChange)
        new_finger.connect()
        remove_finger.connect()
        
    def on_disconnect(self, controller):
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        print("Frame Data")
        frame = controller.frame()
        fingerList = controller.fingers()
        for finger in fingerList :
            # send finger info like - x,y positions & finger id
            hi = 1


def main():
    # Main function to be executed while running the program

    # Generate QML View and show it
    view = QDeclarativeView()
    view.setSource(QUrl('Fingers.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)
    view.setGeometry(100, 100, 400, 240)
    view.show()

    # Get Root Object for inter-communication
    rootObject = view.rootObject()
    
    # Connect to start Leap signal.
    rootObject.qmlStarted.connect(startLeap)
    
    # Connect to stop Leap signal
    rootObject.qmlStop.connect(stopLeap)
    

def startLeap():
    
    # Creating Controller
    controller = Leap.Controller()
    while not controller.is_connected :
        print "Controller status: OFF"
    if controller.is_connected :
        print "Controller status: ON"
        
    # Adding Listener to Controller. Then, Controller will respond automatically
    listener = FingerPing()
    controller.add_listener(listener)
    print "Added Listener!"

def stopLeap():
    """
    () -> int
    This method stops Leap by removing listener from controller.
    
    """
    
    # Removes Listener
    controller.remove_listener(listener)
    return 0
    
if __name__ == '__main__' :
    main()
