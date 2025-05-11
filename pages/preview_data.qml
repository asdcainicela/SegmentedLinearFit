import QtQuick 2.15
import QtQuick.Controls 2.15
import QtQuick.Layouts 1.15

Rectangle {
    id: root
    anchors.fill: parent
    color: "#1e1e1e"
    property Loader rootLoader

    ColumnLayout {
        anchors.fill: parent
        spacing: 10
        anchors.margins: 10

        Text {
            text: "Vista previa del CSV"
            font.pixelSize: 20
            color: "white"
            Layout.alignment: Qt.AlignHCenter
        }

        // Cabecera
        Rectangle {
            color: "#2a2a2a"
            Layout.fillWidth: true
            height: 30

            Row {
                anchors.fill: parent
                spacing: 5
                leftPadding: 5

                Repeater {
                    model: appLogic_csv.tableModel.columnCountQml()
                    Rectangle {
                        width: 150
                        height: parent.height
                        color: "transparent"

                        Text {
                            anchors.verticalCenter: parent.verticalCenter
                            text: appLogic_csv.tableModel.headerData(index, Qt.Horizontal)
                            font.bold: true
                            color: "lightgray"
                            elide: Text.ElideRight
                            width: parent.width
                        }
                    }
                }
            }
        }

        // Datos
        ListView {
            id: tableView
            Layout.fillWidth: true
            Layout.fillHeight: true
            clip: true

            // Optimizaciones para el rendimiento
            cacheBuffer: 300

            ScrollBar.vertical: ScrollBar {}

            model: appLogic_csv.tableModel.rowCountQml()

            delegate: Rectangle {
                width: tableView.width
                height: 30
                color: index % 2 === 0 ? "#333333" : "transparent"

                property int rowIndex: index

                    Row {
                        anchors.fill: parent
                        spacing: 5
                        leftPadding: 5

                        Repeater {
                            model: appLogic_csv.tableModel.columnCountQml()

                            Rectangle {
                                width: 150
                                height: parent.height
                                color: "transparent"

                                property int colIndex: index

                                    // Usamos una propiedad para almacenar el valor y reducir llamadas
                                    property string cellValue: ""

                                        // Obtenemos el valor sólo una vez
                                        Component.onCompleted: {
                                            cellValue = appLogic_csv.tableModel.value(rowIndex, colIndex);
                                        }

                                        Text {
                                            anchors.verticalCenter: parent.verticalCenter
                                            text: parent.cellValue
                                            color: "white"
                                            elide: Text.ElideRight
                                            width: parent.width
                                        }
                                    }
                                }
                            }
                        }
                    }

                    RowLayout {
                        Layout.alignment: Qt.AlignHCenter
                        spacing: 20

                        Button {
                            text: "Volver"
                            onClicked: rootLoader.source = "pages/init.qml"
                            implicitWidth: 200
                            implicitHeight: 40

                            background: Rectangle {
                                color: parent.down ? "#225378" : (parent.hovered ? "#2980b9" : "#3498db")
                                radius: 4
                            }

                            contentItem: Text {
                                text: parent.text
                                color: "white"
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }
                        }

                        Button {
                            text: "Siguiente"
                            onClicked: rootLoader.source = "pages/results.qml"
                            implicitWidth: 200
                            implicitHeight: 40

                            background: Rectangle {
                                color: parent.down ? "#225378" : (parent.hovered ? "#27ae60" : "#2ecc71") // verde
                                radius: 4
                            }

                            contentItem: Text {
                                text: parent.text
                                color: "white"
                                horizontalAlignment: Text.AlignHCenter
                                verticalAlignment: Text.AlignVCenter
                            }
                        }
                    }

                }
            }