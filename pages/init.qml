import QtQuick
import QtQuick.Controls
import QtQuick.Dialogs
import QtQuick.Layouts
import QtQuick.Window

import "../design" as Design

Rectangle {
    visible: true
    width: parent
    height: parent
    color: Design.colorPalette.dark


    ColumnLayout {
    anchors.centerIn: parent
    spacing: 10

    Button {
        text: "Seleccionar CSV"
        font.pixelSize: 20
        Layout.preferredWidth: 200
        Layout.preferredHeight: 50
        onClicked: fileDialog.open()
    }

    Text {
        id: statusText
        text: ""
        font.pixelSize: 16
        color: "white"
        Layout.preferredWidth: 300
        wrapMode: Text.WordWrap
        horizontalAlignment: Text.AlignHCenter
    }
}


    FileDialog {
        id: fileDialog
        nameFilters: ["CSV files (*.csv)"]
        onAccepted: {
            appLogic_csv.load_csv(fileDialog.currentFile)
        }
    }

    Connections {
        target: appLogic_csv
        function onDataLoaded(message) {
            statusText.text = message
        }
    }
}
