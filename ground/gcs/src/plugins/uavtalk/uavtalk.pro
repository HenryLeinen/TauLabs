QT += network
QT += widgets
TEMPLATE = lib
TARGET = UAVTalk
include(../../taulabsgcsplugin.pri)
include(uavtalk_dependencies.pri)
HEADERS += uavtalk.h \
    uavtalkplugin.h \
    telemetrymonitor.h \
    telemetrymanager.h \
    uavtalk_global.h \
    telemetry.h
SOURCES += uavtalk.cpp \
    uavtalkplugin.cpp \
    telemetrymonitor.cpp \
    telemetrymanager.cpp \
    telemetry.cpp
DEFINES += UAVTALK_LIBRARY
OTHER_FILES += UAVTalk.pluginspec \
    UAVTalk.json