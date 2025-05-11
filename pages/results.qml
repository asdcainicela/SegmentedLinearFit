// results.qml  
import QtQuick  
import QtQuick.Layouts  
import QtQuick.Controls 

Rectangle {
    id: root
    anchors.fill: parent
    color: "#1e1e1e"

    property Loader rootLoader


    ColumnLayout {
        anchors.fill: parent
        spacing: 8
        anchors.margins: 12

        Text {
            text: "Ecuaciones de cada tramo"
            color: "white"
            font.pixelSize: 20
            Layout.alignment: Qt.AlignHCenter
        }

        // Área de ecuaciones
        ListView {
            id: eqList
            Layout.fillWidth: true
            Layout.fillHeight: true
            model: plainModel

            delegate: Text {
                text: modelData          // OUT = m · IN + b
                color: "lightgray"
                font.pixelSize: 16
            }
        }

        // Botón para volver
        Button {
            text: "Volver"
            onClicked: rootLoader.source = "pages/preview_data.qml"
            background: Rectangle { color: "#3498db"; radius: 4 }
            contentItem: Text {
                text: parent.text; color: "white"
                horizontalAlignment: Text.AlignHCenter
                verticalAlignment: Text.AlignVCenter
            }
        }
    }

    ListModel { id: plainModel }

    /* --- Conexión a la lógica --- */
    Component.onCompleted: appLogic_csv.run_analysis()

    Connections {
        target: appLogic_csv
        function onResultReady(plain, latex) {
            plainModel.clear()
            for (var i = 0; i < plain.length; ++i)
                plainModel.append({ "modelData": plain[i] })
        }
    }
}
