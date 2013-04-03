import QtQuick 1.1
import "ManageFingers.js" as FC

Rectangle {

    //initialize
    id: mainView
    color: "black"
    focus: true
    width: 800
    height: 400

    //Signals
    signal qmlStarted
    signal qmlStop

    //Custom Properties
    property double changeAxisX: width/2
    property double changeAxisY: height/2

    // Move the axis to the center of the Rectangle so that to be in sync
    // with Leap


    //Build a Component for refering finger tip position
    //Has to be child of the root element
    Component {
        id: fingerTip
        Rectangle {
            height: 20; width: height; radius: height/2
            color: "skyblue"
        }
    }

    //Have a status Display for easy understanding of the state of the frame
    Text {
        id: status
        anchors.centerIn: parent
        text: "Status Display"
        color: "white"
    }

    //For Initiating the Leap raise a signal
    MouseArea {
        anchors.fill: parent
        onClicked: qmlStarted()
    }

    //Listen if a component has to be created
    function newFinger(fingerId, x, y) {
        x = x+changeAxisX
        y = y+changeAxisY
        FC.newFinger(fingerId,x,y)
    }

    //Listen if a component has to be destroyed
    function removeFinger(fingerId) {
        FC.removeFinger(fingerId)
    }

    //Listen for the placement of the fingers
    function fingerPositionChange(fingerId, x, y) {
        x = x+changeAxisX
        y = y+changeAxisY
        FC.fingerPositionChange(fingerId,x,y)
    }

    //On Building & Destructing the Component
    Component.onCompleted: {
        // Raise a Signal to start Leap Motion
        FC.fingerInitialize(fingerTip, mainView, status)
        qmlStarted()
    }

    Component.onDestruction: {
        // Raise a signal
        qmlStop()
    }
}

