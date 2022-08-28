//姓名：董欣然
//学号：1900013018
//项目：程序员计算器

#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QGridLayout>
#include <QPushButton>
#include <QStack>
#include <QtWidgets>
#include <QtCore>

#include "setvariable.h"
#include "setfunction.h"
#include "historyboard.h"
#include "function.h"
using namespace std;
namespace Ui
{
    class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

    bool OnlyDigits();
    void SetDigits(bool);
    int getLevel(const QChar &oper); //得到运算符等级
    //初始化操作.不仅开头调用，每次计算完结果都会调用。
    void init();
    void toPostfix();
    void evaluation();
    bool eventFilter(QObject *obj, QEvent *ev) override;

private:
    Ui::MainWindow *ui;
    QLineEdit *lineEdit;
    QWidget *defaultCalcWidget;
    QWidget *simpleCalcWidget;
    QWidget *complCalcWidget;
    QWidget *mainWidget;
    QTimer timer;
    QGridLayout *defaultCalcLayout;
    QGridLayout *simpleCalcLayout;
    QGridLayout *complCalcLayout;
    QGridLayout *mainLayout;

    SetVariable *setvariable;
    SetFunction *setFunction;
    HistoryBoard *historyWidget;
    Function *expr;
    void CreateDefaultCalcWidget();
    void CreateSimpleCalcWidget();
    void CreateComplCalcWidget();

    void SpawnSimpleMode();
    void SpawnComplMode();

    bool digits_only = true;

public slots:
    //    void SwitchMode();
    void SwitchComplMode();
    void SwitchSimpleMode();
    void ModifyFunction();
    void ModifyVariable();
    void NumberClicked();
    void UnFnClicked();
    void BinFnClicked();
    void DotClicked();

    void ClearInput();
    void BackSpace();
    bool Equals();
};

#endif // MAINWINDOW_H
