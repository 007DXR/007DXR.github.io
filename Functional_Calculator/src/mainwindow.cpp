//姓名：董欣然
//学号：1900013018
//项目：程序员计算器

#include "mainwindow.h"
#include <QDebug>
#include <cctype>
#include <cmath>
#include <QDialog>
#if _WIN32
#define SEPARATOR '.'
#endif

#if __unix
#define SEPARATOR ','
#endif

MainWindow::MainWindow(QWidget *parent) : QMainWindow(parent)
{

    setWindowTitle("标准计算器");
    setWindowOpacity(0.98);
    setMinimumSize(780, 450);
    setMaximumSize(780, 450);

    CreateSimpleCalcWidget();
    CreateComplCalcWidget();
    CreateDefaultCalcWidget();
    mainWidget = new QWidget;
    historyWidget = new HistoryBoard();
    SpawnSimpleMode();
    //qDebug()<<"InitText:"<<lineEdit->text();
    setFunction = new SetFunction();
    setvariable = new SetVariable();
    expr = new Function("", "");
    lineEdit->installEventFilter(this);
    timer.setSingleShot(true);
    timer.setInterval(500);

    connect(lineEdit, SIGNAL(textEdited(QString)), &timer, SLOT(start()));
}

MainWindow::~MainWindow()
{
    //    delete ui;
}

void MainWindow::SwitchSimpleMode()
{

    qDebug() << "simple";
    delete mainLayout;
    setWindowTitle("标准计算器");
    setMinimumSize(780, 450);
    setMaximumSize(780, 450);
    SpawnSimpleMode();
}
void MainWindow::SwitchComplMode()
{

    qDebug() << "complex";
    delete mainLayout;
    setWindowTitle("科学计算器");
    setMinimumSize(1050, 450);
    setMaximumSize(1050, 450);
    SpawnComplMode();
}
void MainWindow::ModifyFunction()
{
    qDebug() << "ModifyFunction";
    setFunction->FunctionNameEdit->setText("");
    setFunction->ParameterNameEdit1->setText("");
    setFunction->ParameterNameEdit2->setText("");
    setFunction->ParameterNameEdit3->setText("");
    setFunction->ExpressionNameEdit->setText("");

    setFunction->FunctionNameEdit->setPlaceholderText("请输入只含字母的字符串");
    setFunction->ParameterNameEdit1->setPlaceholderText("请输入只含字母的字符串");
    setFunction->ParameterNameEdit2->setPlaceholderText("请输入只含字母的字符串");
    setFunction->ParameterNameEdit3->setPlaceholderText("请输入只含字母的字符串");
    setFunction->ExpressionNameEdit->setPlaceholderText("请输入表达式");
    int Respond = setFunction->exec();
    if (Respond == QDialog::Accepted)
    {
        if (setFunction->check() == 0)
        {
            historyWidget->addItem("请输入只含字母的函数名和参数名");
            return;
        }

        QString FunctionName = setFunction->FunctionNameEdit->text();
        QString ParameterName1 = setFunction->ParameterNameEdit1->text();
        QString ParameterName2 = setFunction->ParameterNameEdit2->text();
        QString ParameterName3 = setFunction->ParameterNameEdit3->text();
        QString ExpressionName = setFunction->ExpressionNameEdit->text();
        qDebug() << "accept "; //<<varName;                //点击确定按钮走这里
        QString Expression = FunctionName + "(" + ParameterName1 + "," + ParameterName2 + "," + ParameterName3 + ")";
        Function *subExpr = new Function(ExpressionName.toStdString(), FunctionName.toStdString());
        if (ParameterName1 != "")
            subExpr->variableList.push_back(Variable(ParameterName1.toStdString(), 0));
        if (ParameterName2 != "")
            subExpr->variableList.push_back(Variable(ParameterName2.toStdString(), 0));
        if (ParameterName3 != "")
            subExpr->variableList.push_back(Variable(ParameterName3.toStdString(), 0));
        expr->functionList.push_back(*subExpr);
        historyWidget->AddItem(Expression, ExpressionName);
    }
    else if (Respond == QDialog::Rejected)
    {
        qDebug() << "reject"; //点击取消按钮走这里
    }
}
void MainWindow::ModifyVariable()
{
    qDebug() << "ModifyVariable";
    if (!Equals())
        return;
    //    if (!isDigitValue(lineEdit->text())) return;
    //    try{Equals();}
    //    catch(...){ return ;}
    setvariable->VariableNameLabel->setText("将数值" + lineEdit->text() + "设置为变量:");
    setvariable->VariableNameEdit->setText("");
    setvariable->VariableNameEdit->setPlaceholderText("请输入只含字母的字符串");
    int Respond = setvariable->exec();
    if (Respond == QDialog::Accepted)
    {
        if (setvariable->check() == 0)
        {
            historyWidget->addItem("请输入只含字母的变量名");
            return;
        }
        QString varName = setvariable->VariableNameEdit->text();
        qDebug() << "accept " << varName; //点击确定按钮走这里stod(lineEdit->text().toStdString())
        Variable *var = new Variable(varName.toStdString(), lineEdit->text().toDouble());
        expr->variableList.push_back(*var);
        qDebug() << varName << " " << lineEdit->text().toDouble();
        historyWidget->AddItem(varName, lineEdit->text());
        //        centralWidget()->layout()->setContentsMargins(0, 0, 0, 0);
    }
    else if (Respond == QDialog::Rejected)
    {
        qDebug() << "reject"; //点击取消按钮走这里
    }
}
void MainWindow::SpawnSimpleMode()
{
    mainLayout = new QGridLayout;
    mainLayout->setSpacing(0);
    complCalcWidget->hide();
    mainLayout->addWidget(defaultCalcWidget, 0, 0, 1, 1);
    mainLayout->addWidget(simpleCalcWidget, 1, 0, 2, 1);
    mainLayout->addWidget(historyWidget, 0, 1, 3, 1);

    mainWidget->setLayout(mainLayout);
    setCentralWidget(mainWidget);
    centralWidget()->layout()->setContentsMargins(0, 0, 0, 0);
}

void MainWindow::SpawnComplMode()
{
    mainLayout = new QGridLayout;
    mainLayout->setSpacing(0);
    mainLayout->addWidget(defaultCalcWidget, 0, 0, 1, 2);
    mainLayout->addWidget(complCalcWidget, 1, 0, 2, 1);
    mainLayout->addWidget(simpleCalcWidget, 1, 1, 2, 1);
    mainLayout->addWidget(historyWidget, 0, 2, 3, 1);
    complCalcWidget->show();

    mainWidget->setLayout(mainLayout);
    setCentralWidget(mainWidget);
    centralWidget()->layout()->setContentsMargins(0, 0, 0, 0);
}

void MainWindow::CreateSimpleCalcWidget()
{
    QPushButton *pushButton0 = new QPushButton("0");
    QPushButton *pushButton1 = new QPushButton("1");
    QPushButton *pushButton2 = new QPushButton("2");
    QPushButton *pushButton3 = new QPushButton("3");
    QPushButton *pushButton4 = new QPushButton("4");
    QPushButton *pushButton5 = new QPushButton("5");
    QPushButton *pushButton6 = new QPushButton("6");
    QPushButton *pushButton7 = new QPushButton("7");
    QPushButton *pushButton8 = new QPushButton("8");
    QPushButton *pushButton9 = new QPushButton("9");
    QPushButton *pushButtonDot = new QPushButton(".");
    QPushButton *pushButtonPlus = new QPushButton("+");
    QPushButton *pushButtonMinus = new QPushButton("-");
    //    QPushButton* pushButtonMinus =  new QPushButton(QString::fromUtf8("-"));
    QPushButton *pushButtonMult = new QPushButton(QString::fromUtf8("*"));
    QPushButton *pushButtonDivide = new QPushButton(QString::fromUtf8("/"));
    QPushButton *pushButtonEquals = new QPushButton("=");
    QPushButton *pushButtonLeft = new QPushButton("(");
    QPushButton *pushButtonRight = new QPushButton(")");
    QPushButton *pushButtonBackSpace = new QPushButton(QString::fromUtf8("\u232B"), this);
    QPushButton *pushButtonClear = new QPushButton(QString::fromUtf8("C"), this);

    pushButton0->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton1->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton2->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton3->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton4->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton5->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton6->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton7->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton8->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton9->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonPlus->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonMinus->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonDot->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonMult->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonDivide->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonEquals->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonLeft->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonRight->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonBackSpace->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonClear->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);

    QString StyleSheetBackSpace = "QPushButton { color: black; background-color: #E6E6E6; border: none; font: 17pt 'Microsoft YaHei UI Light'; outline: none; } QPushButton:hover { background-color: #D8D8D8; border-style: solid; border-width: 3px; border-color: #E6E6E6; } QPushButton:pressed { background-color: #A4A4A4; border-style: solid; border-width: 3px; border-color: #E6E6E6; }";
    QString StyleSheetClear = "QPushButton { color: black; background-color: #E6E6E6; border: none; font: 17pt 'Microsoft YaHei UI'; outline: none; } QPushButton:hover { background-color: #D8D8D8; border-style: solid; border-width: 3px; border-color: #E6E6E6; } QPushButton:pressed { background-color: #A4A4A4; border-style: solid; border-width: 3px; border-color: #E6E6E6; }";
    QString StyleSheetNumbers = "QPushButton { color: black; background-color: #FAFAFA; border: 3px inset #D8D8D8; font: 17pt 'Microsoft YaHei UI'; outline: none;} QPushButton:hover { background-color: #D8D8D8; border-style: solid; border-width: 3px; border-color: #F2F2F2; } QPushButton:pressed { background-color: #A4A4A4; border-style: solid; border-width: 3px; border-color: #E6E6E6; }";
    QString StyleSheetSigns = "QPushButton { color: black; background-color: #E6E6E6; border: none; font: 19pt 'Microsoft YaHei UI Light'; outline: none; } QPushButton:hover { background-color: #2ECCFA; border-style: solid; border-width: 3px; border-color: #58D3F7; } QPushButton:pressed { background-color: #81DAF5; border-style: solid; border-width: 3px; border-color: #A9E2F3; }";
    pushButton0->setStyleSheet(StyleSheetNumbers);
    pushButton1->setStyleSheet(StyleSheetNumbers);
    pushButton2->setStyleSheet(StyleSheetNumbers);
    pushButton3->setStyleSheet(StyleSheetNumbers);
    pushButton4->setStyleSheet(StyleSheetNumbers);
    pushButton5->setStyleSheet(StyleSheetNumbers);
    pushButton6->setStyleSheet(StyleSheetNumbers);
    pushButton7->setStyleSheet(StyleSheetNumbers);
    pushButton8->setStyleSheet(StyleSheetNumbers);
    pushButton9->setStyleSheet(StyleSheetNumbers);
    pushButtonDot->setStyleSheet(StyleSheetNumbers);
    pushButtonPlus->setStyleSheet(StyleSheetSigns);
    pushButtonMinus->setStyleSheet(StyleSheetSigns);
    pushButtonMult->setStyleSheet(StyleSheetSigns);
    pushButtonDivide->setStyleSheet(StyleSheetSigns);
    pushButtonEquals->setStyleSheet(StyleSheetSigns);
    pushButtonLeft->setStyleSheet(StyleSheetSigns);
    pushButtonRight->setStyleSheet(StyleSheetSigns);
    pushButtonBackSpace->setStyleSheet(StyleSheetBackSpace);
    pushButtonClear->setStyleSheet(StyleSheetClear);
    //    pushButtonInvert->setStyleSheet(StyleSheetSigns);
    //    pushButtonSqrt->setStyleSheet(  StyleSheetSigns);

    simpleCalcLayout = new QGridLayout(this);
    simpleCalcLayout->setSpacing(0);
    simpleCalcLayout->setContentsMargins(0, 0, 0, 0);

    simpleCalcLayout->addWidget(pushButtonBackSpace, 0, 0, 1, 1);
    simpleCalcLayout->addWidget(pushButtonClear, 0, 1, 1, 1);
    simpleCalcLayout->addWidget(pushButtonLeft, 0, 2, 1, 1);
    simpleCalcLayout->addWidget(pushButtonRight, 0, 3, 1, 1);

    simpleCalcLayout->addWidget(pushButton7, 1, 0, 1, 1);
    simpleCalcLayout->addWidget(pushButton8, 1, 1, 1, 1);
    simpleCalcLayout->addWidget(pushButton9, 1, 2, 1, 1);
    simpleCalcLayout->addWidget(pushButtonDivide, 1, 3, 1, 1);
    //    simpleCalcLayout->addWidget(pushButtonDivide,   0, 4, 1, 1);
    simpleCalcLayout->addWidget(pushButton4, 2, 0, 1, 1);
    simpleCalcLayout->addWidget(pushButton5, 2, 1, 1, 1);
    simpleCalcLayout->addWidget(pushButton6, 2, 2, 1, 1);
    simpleCalcLayout->addWidget(pushButtonMult, 2, 3, 1, 1);
    //    simpleCalcLayout->addWidget(pushButtonInvert, 1, 4, 1, 1);
    simpleCalcLayout->addWidget(pushButton1, 3, 0, 1, 1);
    simpleCalcLayout->addWidget(pushButton2, 3, 1, 1, 1);
    simpleCalcLayout->addWidget(pushButton3, 3, 2, 1, 1);
    simpleCalcLayout->addWidget(pushButtonMinus, 3, 3, 1, 1);

    simpleCalcLayout->addWidget(pushButton0, 4, 0, 1, 1);
    simpleCalcLayout->addWidget(pushButtonDot, 4, 1, 1, 1);
    simpleCalcLayout->addWidget(pushButtonEquals, 4, 2, 1, 1);
    simpleCalcLayout->addWidget(pushButtonPlus, 4, 3, 1, 1);

    simpleCalcWidget = new QWidget(this);
    simpleCalcWidget->setLayout(simpleCalcLayout);

    connect(pushButton0, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton1, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton2, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton3, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton4, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton5, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton6, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton7, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton8, SIGNAL(clicked()), this, SLOT(NumberClicked()));
    connect(pushButton9, SIGNAL(clicked()), this, SLOT(NumberClicked()));

    connect(pushButtonPlus, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonMinus, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonMult, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonDivide, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonLeft, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonRight, SIGNAL(clicked()), this, SLOT(BinFnClicked()));

    connect(pushButtonDot, SIGNAL(clicked()), this, SLOT(DotClicked()));
    connect(pushButtonEquals, SIGNAL(clicked()), this, SLOT(Equals()));
    connect(pushButtonClear, SIGNAL(clicked()), this, SLOT(ClearInput()));
    connect(pushButtonBackSpace, SIGNAL(clicked()), this, SLOT(BackSpace()));

    //    connect(pushButtonInvert, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
}

void MainWindow::CreateComplCalcWidget()
{
    QPushButton *pushButtonSqrt = new QPushButton(QString::fromUtf8("\u221A"));
    QPushButton *pushButtonInvert = new QPushButton(QString::fromUtf8("x\u207B\u00B9"));
    QPushButton *pushButtonSinh = new QPushButton("sh");
    QPushButton *pushButtonSin = new QPushButton("sin");
    QPushButton *pushButtonExp = new QPushButton(QString::fromUtf8("e\u207F"));
    QPushButton *pushButtonXSq = new QPushButton(QString::fromUtf8("x\u00B2"));
    QPushButton *pushButtonCosh = new QPushButton("ch");
    QPushButton *pushButtonCos = new QPushButton("cos");
    QPushButton *pushButtonLn = new QPushButton("ln");
    QPushButton *pushButtonXCubed = new QPushButton(QString::fromUtf8("x\u00B3"));
    QPushButton *pushButtonTanh = new QPushButton("th");
    QPushButton *pushButtonTan = new QPushButton("tan");
    QPushButton *pushButtonLog = new QPushButton("lg");
    QPushButton *pushButtonXNed = new QPushButton(QString::fromUtf8("x\u207F")); //x^n
    QPushButton *pushButtonFact = new QPushButton("n!");
    QPushButton *pushButtonPi = new QPushButton(QString::fromUtf8("\u03C0"));
    QPushButton *pushButtonCubeRoot = new QPushButton(QString::fromUtf8("\u00B3\u221A"));
    QPushButton *pushButtonNRoot = new QPushButton(QString::fromUtf8("\u207F\u221A"));
    //    new
    QPushButton *pushButtonAnd = new QPushButton("&&");
    QPushButton *pushButtonXor = new QPushButton("^");
    QPushButton *pushButton_Or = new QPushButton("|");
    QPushButton *pushButtonRhs = new QPushButton(">>");
    QPushButton *pushButtonLhs = new QPushButton("<<");
    QPushButton *pushButtonMod = new QPushButton("%");

    pushButtonSinh->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonSin->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonExp->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonXSq->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonCosh->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonCos->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonLn->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonXCubed->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonTanh->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonTan->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonLog->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonXNed->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonFact->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonPi->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonCubeRoot->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonNRoot->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonInvert->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonSqrt->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    //new
    pushButtonAnd->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonXor->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButton_Or->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonRhs->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonLhs->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    pushButtonMod->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);

    QString StyleSheetSpecSigns = "QPushButton {max-width: 77px; color: black; background-color: #E6E6E6; border: none; font: 14pt 'Microsoft YaHei UI Light'; outline: none; } QPushButton:hover { background-color: #D8D8D8; border-style: solid; border-width: 3px; border-color: #E6E6E6; } QPushButton:pressed { background-color: #A4A4A4; border-style: solid; border-width: 3px; border-color: #E6E6E6; }";
    QString StyleSheetSpecRoot = "QPushButton {max-width: 77px; color: black; background-color: #E6E6E6; border: none; font: 16pt 'Microsoft YaHei UI Light'; outline: none; } QPushButton:hover { background-color: #D8D8D8; border-style: solid; border-width: 3px; border-color: #E6E6E6; } QPushButton:pressed { background-color: #A4A4A4; border-style: solid; border-width: 3px; border-color: #E6E6E6; }";
    pushButtonCosh->setStyleSheet(StyleSheetSpecSigns);
    pushButtonCos->setStyleSheet(StyleSheetSpecSigns);
    pushButtonSinh->setStyleSheet(StyleSheetSpecSigns);
    pushButtonSin->setStyleSheet(StyleSheetSpecSigns);
    pushButtonTanh->setStyleSheet(StyleSheetSpecSigns);
    pushButtonTan->setStyleSheet(StyleSheetSpecSigns);
    pushButtonLn->setStyleSheet(StyleSheetSpecSigns);
    pushButtonLog->setStyleSheet(StyleSheetSpecSigns);
    pushButtonXSq->setStyleSheet(StyleSheetSpecSigns);  //x^2
    pushButtonXNed->setStyleSheet(StyleSheetSpecSigns); //x^n
    //new create
    pushButtonAnd->setStyleSheet(StyleSheetSpecSigns);
    pushButtonXor->setStyleSheet(StyleSheetSpecSigns);
    pushButton_Or->setStyleSheet(StyleSheetSpecSigns);
    pushButtonRhs->setStyleSheet(StyleSheetSpecSigns);
    pushButtonLhs->setStyleSheet(StyleSheetSpecSigns);
    pushButtonMod->setStyleSheet(StyleSheetSpecSigns);

    complCalcLayout = new QGridLayout(this);
    complCalcLayout->setSpacing(0);
    complCalcLayout->setContentsMargins(0, 0, 0, 0);

    complCalcLayout->addWidget(pushButtonSinh, 0, 0, 1, 1);
    complCalcLayout->addWidget(pushButtonSin, 0, 1, 1, 1);
    complCalcLayout->addWidget(pushButtonAnd, 0, 2, 1, 1);
    complCalcLayout->addWidget(pushButtonLhs, 0, 3, 1, 1); //x^2

    complCalcLayout->addWidget(pushButtonCosh, 1, 0, 1, 1);
    complCalcLayout->addWidget(pushButtonCos, 1, 1, 1, 1);
    complCalcLayout->addWidget(pushButton_Or, 1, 2, 1, 1);
    complCalcLayout->addWidget(pushButtonRhs, 1, 3, 1, 1);

    complCalcLayout->addWidget(pushButtonTanh, 2, 0, 1, 1);
    complCalcLayout->addWidget(pushButtonTan, 2, 1, 1, 1);
    complCalcLayout->addWidget(pushButtonXor, 2, 2, 1, 1);
    complCalcLayout->addWidget(pushButtonMod, 2, 3, 1, 1);

    complCalcLayout->addWidget(pushButtonLn, 3, 0, 1, 1);
    complCalcLayout->addWidget(pushButtonLog, 3, 1, 1, 1);
    complCalcLayout->addWidget(pushButtonXSq, 3, 2, 1, 1);
    complCalcLayout->addWidget(pushButtonXNed, 3, 3, 1, 1);

    complCalcWidget = new QWidget(this);
    complCalcWidget->setLayout(complCalcLayout);

    connect(pushButtonSin, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
    connect(pushButtonSinh, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
    connect(pushButtonCos, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
    connect(pushButtonCosh, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
    connect(pushButtonTan, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
    connect(pushButtonTanh, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
    connect(pushButtonLn, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
    connect(pushButtonLog, SIGNAL(clicked()), this, SLOT(UnFnClicked()));
    connect(pushButtonXNed, SIGNAL(clicked()), this, SLOT(BinFnClicked())); //x^n
    connect(pushButtonXSq, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    //new
    connect(pushButtonAnd, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonXor, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButton_Or, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonRhs, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonLhs, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
    connect(pushButtonMod, SIGNAL(clicked()), this, SLOT(BinFnClicked()));
}

void MainWindow::CreateDefaultCalcWidget()
{

    QString StyleSheetRadioButton = "QButton {background-color: #E6E6E6; font: 10pt 'Microsoft YaHei UI Light'; padding: 0px 0px 0px 20px;} QRadioButton::indicator { width: 20px; height: 20px; } QRadioButton::indicator::unchecked {image: url(radio_normal.svg);} QRadioButton::indicator:unchecked:hover {image: url(radio_normal.svg);} QRadioButton::indicator:unchecked:pressed {image: url(radio_checked.svg);} QRadioButton::indicator:checked {image: url(radio_checked.svg);} QRadioButton::indicator:checked:hover {image: url(radio_checked.svg);} QRadioButton::indicator:checked:pressed {image: url(radio_checked.svg);}";
    QString StyleSheetLine = "QLineEdit {font: 26pt 'Microsoft YaHei UI'; qproperty-alignment: AlignRight; padding: 5px; border: none; background-color: #F2F2F2;}";
    QPushButton *ButtonSimple = new QPushButton("标准");
    QPushButton *ButtonCompl = new QPushButton("科学/程序员");
    QPushButton *ButtonFuction = new QPushButton("设置函数");
    QPushButton *ButtonVariable = new QPushButton("设置变量");
    //    lineEdit->setReadOnly(true);
    ButtonSimple->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    ButtonCompl->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    ButtonFuction->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);
    ButtonVariable->setSizePolicy(QSizePolicy::Preferred, QSizePolicy::Preferred);

    connect(ButtonSimple, SIGNAL(clicked()), SLOT(SwitchSimpleMode()));
    connect(ButtonCompl, SIGNAL(clicked()), SLOT(SwitchComplMode()));
    connect(ButtonFuction, SIGNAL(clicked()), SLOT(ModifyFunction()));
    connect(ButtonVariable, SIGNAL(clicked()), SLOT(ModifyVariable()));

    lineEdit = new QLineEdit();
    lineEdit->setPlaceholderText("0");
    lineEdit->setStyleSheet(StyleSheetLine);

    defaultCalcLayout = new QGridLayout(this);
    defaultCalcLayout->setSpacing(0);
    defaultCalcLayout->setContentsMargins(0, 0, 0, 0);

    defaultCalcLayout->addWidget(lineEdit, 0, 0, 2, 4);
    defaultCalcLayout->addWidget(ButtonSimple, 2, 0, 1, 1);
    defaultCalcLayout->addWidget(ButtonCompl, 2, 1, 1, 1);

    defaultCalcLayout->addWidget(ButtonFuction, 2, 2, 1, 1);
    defaultCalcLayout->addWidget(ButtonVariable, 2, 3, 1, 1);

    defaultCalcWidget = new QWidget(this);
    defaultCalcWidget->setLayout(defaultCalcLayout);
}

bool MainWindow::OnlyDigits()
{
    return digits_only;
}

void MainWindow::SetDigits(bool new_state)
{
    digits_only = new_state;
}
void MainWindow::NumberClicked()
{
    lineEdit->setText(lineEdit->text() + ((QPushButton *)sender())->text());
}
void MainWindow::DotClicked()
{
    lineEdit->setText(lineEdit->text() + ((QPushButton *)sender())->text());
}
void MainWindow::BinFnClicked()
{ //二元运算
    QString symbol = ((QPushButton *)sender())->text();
    if (symbol == "x\u207F") // x^n
        lineEdit->setText(lineEdit->text() + "**");
    else if (symbol == "x\u00B2") // x^2
        lineEdit->setText(lineEdit->text() + "**2");
    else if (symbol == "&&")
        lineEdit->setText(lineEdit->text() + "&");
    else
        lineEdit->setText(lineEdit->text() + ((QPushButton *)sender())->text());
}
void MainWindow::UnFnClicked()
{ //一元函数运算
    QString symbol = ((QPushButton *)sender())->text();
    lineEdit->setText(lineEdit->text() + ((QPushButton *)sender())->text() + "(");
}

void MainWindow::ClearInput()
{
    lineEdit->clear();
    SetDigits(true);
}

void MainWindow::BackSpace()
{
    int length = lineEdit->text().length();
    if (length)
    {
        char last_char = lineEdit->text().at(length - 1).toLatin1();
        if (!std::isdigit(last_char))
            SetDigits(true);
        lineEdit->setText(lineEdit->text().left(length - 1));
    }
}
bool MainWindow::eventFilter(QObject *obj, QEvent *ev)
{

    if (ev->type() == QEvent::KeyPress)
    {
        int key = static_cast<QKeyEvent *>(ev)->key();
        switch (key)
        {
        case Qt::Key_Enter:
        case Qt::Key_Return:
        case Qt::Key_Equal:
            Equals();
            break;
        default:
            lineEdit->setFocus();
            lineEdit->event(ev);
            //            lineEdit->hide();
            break;
        }
        //lineEdit->setText(lineEdit->text().left(length - 1));
        return true;
    }

    return QWidget::eventFilter(obj, ev);
}
//等于号的槽函数。
void MainWindow::init()
{
    while (!expr->opStack.empty())
        expr->opStack.pop();
    while (!expr->numStack.empty())
        expr->numStack.pop();
    while (!expr->temporaryStack.empty())
        expr->temporaryStack.pop();
}
bool MainWindow::Equals()
{
    //    如果还没输入，那么等于号不起作用
    if (lineEdit->text() == "")
        return 0;

    init();
    expr->s = "(" + lineEdit->text().toStdString() + ")\0";
    qDebug() << lineEdit->text();
    try
    {
        lineEdit->setText(QString::number(expr->Expression2Value()));
        return true;
    }
    catch (char const *Exception)
    {
        //        qDebug() << Exception;
        QDialog errorWindow;
        QLabel titleLabel("非法操作！请注意表达式的合法性!\n\n注意事项：\n1.请不要输入冗余的空格\n2.请使用已申明的变量和函数\n3.请使用计算器给出的操作符\n3.请注意括号匹配\n4.请注意变量名和函数名只可以由字母组成\n5.请注意参与位运算的数值必须是整数\n6.请注意除法运算/和取模运算%的除数必须非零\n7.请注意函数的参数个数是否和输入相符\n8.若计算结果与预期不符，请考虑运算符的优先级\n");
        QLabel contextLabel("运算符说明：\n1.sh(),ch(),th()双曲函数\n2.sin(),cos(),tan()三角函数\n3.ln()自然对数\n4.lg()以10为底的对数\n5.位运算：&按位与，|按位或，^按位异或\n6.位移运算：<<左移运算，>>右移运算\n7.%取模操作\n8.x的n次方写作x**n\n");
        QLabel authorLabel("开发者：董欣然\n学号：1900013018");
        QVBoxLayout mainLayout;
        mainLayout.addWidget(&titleLabel);
        mainLayout.addWidget(&contextLabel);
        mainLayout.addWidget(&authorLabel);
        errorWindow.setLayout(&mainLayout);
        errorWindow.setWindowTitle("使用须知");
        errorWindow.exec();
        return false;
        //throw "error";
    }
}
