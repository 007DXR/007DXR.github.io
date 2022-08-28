//
// Created by Bychin on 17.11.2017.
//

#include "mainwindow.h"
#include <QApplication>
#include<bits/stdc++.h>
#include<string.h>
using namespace std;
int main(int argc, char *argv[]) {


    QApplication a(argc, argv);
    a.setWindowIcon(QIcon("logo.png"));

    MainWindow window;
    window.show();

    return a.exec();
}
