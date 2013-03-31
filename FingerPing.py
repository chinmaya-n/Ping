################################################################################
# Copyright (C) 2012-2013 Leap Motion, Inc. All rights reserved.               #
# Leap Motion proprietary and confidential. Not for distribution.              #
# Use subject to the terms of the Leap Motion SDK Agreement available at       #
# https://developer.leapmotion.com/sdk_agreement, or another agreement         #
# between Leap Motion and you, your company or other organization.             #
################################################################################

__author__ = 'inblueswithu'

import Leap, sys
from PyQt4.QtCore import pyqtSignal, QUrl
from PyQt4.QtDeclarative import QDeclarativeView
from PyQt4.QtGui import QApplication

#Global Variables
rootObject  = object

class FingerPing(Leap.Listener) :
    
    # Variables & Signals
    previous_frame_fingers = []
    finger_position_change = pyqtSignal(str,float,float)
    new_finger = pyqtSignal(str,float,float)
    remove_finger = pyqtSignal(str)

    # Now we will implement some methods
    def on_init(self, controller):
        print("Initialized")
        
    def on_connect(self, controller):
        self.finger_position_change.connect(rootObject.fingerPostionChange)
        self.new_finger.connect(rootObject.newFinger)
        self.remove_finger.connect(rootObject.removeFinger)
        print("Connected")
        
    def on_disconnect(self, controller):
        print("Disconnected")

    def on_exit(self, controller):
        print("Exited")

    def on_frame(self, controller):
        print("Frame Data")
        frame = controller.frame()
        fingerList = frame.fingers()
        frame_fingers = []
        for finger in fingerList :
            
            fingerId = finger.id
            
            # if finger not present then send a signel to create
            if finger.id not in self.previous_frame_fingers :
                self.new_finger.emit(str(fingerId), finger.tipPosition.x, finger.tipPosition.y)
                
            # if finger is present then send a signel for its position
            else :
                self.finger_position_change.emit(str(fingerId), finger.tipPosition.x, finger.tipPosition.y)
                self.previous_frame_fingers.remove(fingerId)
                
            # accumulate present frame finger Ids
            frame_fingers.append(fingerId)
        
        # Delete any old fingers from previous_frame_fingers by comparing frame_fingers, the finger Id accumulator
        for fingerId in self.previous_frame_fingers :
            self.remove_finger.emit(str(fingerId))
        
        # Assign frame_fingers as previous_frame_fingers for next iteration purpose
        self.previous_frame_fingers = frame_fingers


def main():
    # Main function to be executed while running the program

    # Generate QML View
    app = QApplication(sys.argv)
    view = QDeclarativeView()
    view.setSource(QUrl('Fingers.qml'))
    view.setResizeMode(QDeclarativeView.SizeRootObjectToView)

    # Get Root Object for communication
    rootObject = view.rootObject()
    
    # Connect to start Leap signal.
    rootObject.qmlStarted.connect(startLeap)
    
    # Connect to stop Leap signal
    rootObject.qmlStop.connect(stopLeap)
    
    # Display the component
    view.setGeometry(100, 100, 800, 600)
    view.show()
    app.exec_()    
    

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
