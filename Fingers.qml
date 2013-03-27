import QtQuick 1.1
import "ManageFingers.js" as FC

Rectangle {

    //Signals
    signal qmlStart
    signal qmlStop

    //initialize
    id: mainView
    color: "black"
    focus: true

    //Build a Component for refering finger tip position
    //Has to be child of the root element
    Component {
        id: fingerTip
        Rectangle {
            height: 20; width: height; radius: height/2
            color: "skyblue"
        }
    }


    //Destroy the Component when index is given


    //Listen if a component has to be created


    //Listen if a component has to be destroyed


    //Listen for the placement of the fingers
    //Apply the placement


    //Keys & Status Display
    property int idNo : 1

    Keys.onPressed: {
        if(event.key===Qt.Key_Up) {
            FC.createFinger(fingerTip,mainView,status)
        }
        if(event.key===Qt.Key_Down) {
            var fingerId = 'finger'+idNo
            FC.destroyFinger(fingerId, status)
            idNo++
        }
    }

    Text {
        id: status
        anchors.centerIn: parent
        text: "Status Display"
        color: "white"
    }

    //On Building the Component
    Component.onCompleted: {
        // Raise a Signal
        qmlStart()
    }
    Component.onDestruction: {
        // Raise a signal
        qmlStop()
    }
}
