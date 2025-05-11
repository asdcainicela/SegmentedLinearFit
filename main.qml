//main.qml
import QtQuick
import QtQuick.Window

import "./design" as Design
import "./pages"
import QtQuick.Controls
import "."

Window {
    visible: true
    width: 800
    height: 600
    title: "SegmentedLinearFit"
    color: Design.colorPalette.background

    Column {
        anchors.fill: parent

        // Zona de título
        Rectangle {
            width: parent.width
            height: 60
            color: Design.colorPalette.card
            border.color: Design.colorPalette.primary

            Text {
                anchors.centerIn: parent
                text: "SegmentedLinearFit"
                font.pixelSize: 22
                color: Design.colorPalette.primaryText
            }
        }

        // Zona de contenido dinámico
        Rectangle {
            width: parent.width
            height: parent.height - 60
            color: Design.colorPalette.background

            Loader {
                id: pageLoader
                anchors.fill: parent
                source: "pages/init.qml"
                onLoaded: {
                    item.rootLoader = pageLoader
                }
            }

        }
    }
}
