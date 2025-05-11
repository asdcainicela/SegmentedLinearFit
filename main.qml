// main.qml
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
    color: "#1e1e1e" // fondo oscuro

    Column {
        anchors.fill: parent

        // Zona de título
        Rectangle {
            width: parent.width
            height: 60
            color: "#2a2a2a" // color oscuro para cabecera
            border.color: "#3498db" // azul vivo como borde

            Text {
                anchors.centerIn: parent
                text: "SegmentedLinearFit"
                font.pixelSize: 22
                color: "white"
            }
        }

        // Zona de contenido dinámico
        Rectangle {
            width: 19*parent.width/20
            height: parent.height - 60
            anchors.horizontalCenter: parent.horizontalCenter
            color: "#1e1e1e" // fondo igual al de root

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
