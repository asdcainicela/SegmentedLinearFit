pragma Singleton

import QtQuick

QtObject {
    // Fondo principal oscuro
    property color background: "#1E1E2F" // Azul muy oscuro grisáceo
    property color surface: "#2A2A3B" // Un poco más claro que el fondo
    property color card: "#323244" // Tarjetas o paneles
    property color dark: "#444444" // Oscuridad total, útil para capas más profundas

    // Texto
    property color primaryText: "#E0E6ED" // Gris muy claro, buena legibilidad
    property color secondaryText: "#A0A4AE" // Gris claro para texto secundario
    property color disabledText: "#5A5E68" // Gris opaco para texto deshabilitado

    // Bordes y líneas
    property color divider: "#3D3D4D" // Divisores tenues
    property color outline: "#4C4C5C" // Bordes sutiles

    // Acciones primarias (azul moderno)
    property color primary: "#4A90E2" // Azul moderno
    property color primaryLight: "#6BAEF9"
    property color primaryDark: "#2B6CB0"

    // Acciones neutrales
    property color neutral: "#A0A4AE" // Gris claro
    property color neutralLight: "#B9BDC6"
    property color neutralDark: "#4C4F5A"

    // Estados positivos
    property color success: "#22C55E" // Verde moderno brillante
    property color successLight: "#4ADE80"
    property color successDark: "#15803D"

    // Estados de advertencia
    property color warning: "#FBBF24" // Amarillo suave
    property color warningLight: "#FACC15"
    property color warningDark: "#B45309"

    // Estados de error
    property color error: "#EF4444" // Rojo moderno
    property color errorLight: "#F87171"
    property color errorDark: "#B91C1C"
}
