.pragma library

//Finger List Management using different functions
var dynamicObjectList = new Object() ;
var fingerComponent,rootView, statusText;

function append(fingerId,fingerObj) {
    dynamicObjectList[fingerId] = fingerObj
}

function remove(fingerId) {
    delete dynamicObjectList[fingerId]
}

function get(fingerId) {
    return dynamicObjectList[fingerId]
}

function fingerCount() {
    var noOfFingers = 0
    for(var fingerId in dynamicObjectList) {
        noOfFingers++
    }
    return noOfFingers
}


// Finger Operations for creating, removing and modifying positions etc.
function fingerInitialize(component, root, status) {
    fingerComponent = component
    rootView = root
    statusText = status
}

function newFinger(fingerId, x, y) {
    fingerId = 'finger' + fingerId
    var fingerObject = fingerComponent.createObject(rootView,{"x": x , "y": y })
    append(fingerId,fingerObject)
    statusText.text = fingerCount() + 'fingers'
}

function fingerPositionChange(fingerId, x, y) {
    fingerId = 'finger' + fingerId
    var finger = get(fingerId)
    finger.x = x ; finger.y = y;
    statusText.text = fingerCount() + 'fingers'
}

function removeFinger(fingerId) {
    fingerId = 'finger' + fingerId
    get(fingerId).destroy()
    remove(fingerId)
    statusText.text = fingerCount() + 'fingers'
}


////simple variables
//var xValue = 0
//var count = 1

//function createFinger(fingerTip,mainView,status) {
//    var fingerObject = fingerTip.createObject(mainView,{x: xValue}); xValue+=20
//    var fingerId = 'finger'+count; count++
//    append(fingerId, fingerObject)
//    status.text = fingerCount() + 'fingers'
//}

//function destroyFinger(fingerId,status) {
//    get(fingerId).destroy()
//    remove(fingerId)
//    status.text = fingerCount() + 'fingers'
//}
