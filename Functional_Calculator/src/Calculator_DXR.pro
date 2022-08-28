#-------------------------------------------------
#
# Project created by QtCreator 2017-11-03T23:09:46
#
#-------------------------------------------------

QT       += core gui

CONFIG += c++11

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = Calculator_DXR
TEMPLATE = app

# The following define makes your compiler emit warnings if you use
# any feature of Qt which has been marked as deprecated (the exact warnings
# depend on your compiler). Please consult the documentation of the
# deprecated API in order to know how to port your code away from it.
DEFINES += QT_DEPRECATED_WARNINGS

# You can also make your code fail to compile if you use deprecated APIs.
# In order to do so, uncomment the following line.
# You can also select to disable deprecated APIs only up to a certain version of Qt.
#DEFINES += QT_DISABLE_DEPRECATED_BEFORE=0x060000    # disables all the APIs deprecated before Qt 6.0.0


SOURCES += \
        historyboard.cpp \
        main.cpp \
        mainwindow.cpp \
        setfunction.cpp \
        setvariable.cpp\
function.cpp

HEADERS += \
        historyboard.h \
        mainwindow.h \
        setfunction.h \
        setvariable.h\
function.h

#FORMS += \
#        mainwindow.ui \
#        setvariable.ui

qnx: target.path = /tmp/$${TARGET}/bin
else: unix:!android: target.path = /opt/$${TARGET}/bin
!isEmpty(target.path): INSTALLS += target
