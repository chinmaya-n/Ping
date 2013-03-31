import QtQuick 1.1
import "ManageFingers.js" as FC

Rectangle {

    //Signals
    signal qmlStarted
    signal qmlStop

    //initialize
    id: mainView
    color: "black"
    focus: true
    width: 800
    height: 400

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

    //Listen if a component has to be created
    function newFinger(fingerId, x, y) {
        FC.newFinger(fingerId,x,y)
    }

    //Listen if a component has to be destroyed
    function removeFinger(fingerId) {
        FC.removeFinger(fingerId)
    }

    //Listen for the placement of the fingers
    function fingerPositionChange(fingerId, x, y) {
        FC.fingerPostionChange(fingerId,x,y)
    }

    Text {
        id: status
//        anchors.left: parent.right - status.width
//        anchors.bottom: parent.bottom
        anchors.centerIn: parent
        text: "Status Display"
        color: "white"
    }

    MouseArea {
        anchors.fill: parent
        onClicked: qmlStarted()
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

//Keys & Status Display
//    property int idNo : 1

//    Keys.onPressed: {
//        if(event.key===Qt.Key_Up) {
//            FC.createFinger(fingerTip,mainView,status)
//        }
//        if(event.key===Qt.Key_Down) {
//            var fingerId = 'finger'+idNo
//            FC.destroyFinger(fingerId, status)
//            idNo++
//        }
//    }
