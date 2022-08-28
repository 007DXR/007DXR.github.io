#include "setfunction.h"
#include<QtWidgets>
#include <QDialog>
SetFunction::SetFunction(QWidget *parent) : QDialog(parent)
{

    QLabel *FunctionNameLabel = new QLabel(tr("函数名:"));
    FunctionNameEdit = new QLineEdit();

    QLabel *ParameterNameLabel1= new QLabel(tr("参数名1:"));
    ParameterNameEdit1 = new QLineEdit();

    //    ParameterNameEdit1->setFrameStyle(QFrame::Panel | QFrame::Sunken);
    QLabel *ParameterNameLabel2= new QLabel(tr("参数名2:"));
    ParameterNameEdit2 = new QLineEdit();
    QLabel *ParameterNameLabel3= new QLabel(tr("参数名3:"));
    ParameterNameEdit3 = new QLineEdit();
    QLabel *ExpressionNameLabel= new QLabel(tr("表达式（科学计算器中所有函数均可使用）:"));
    ExpressionNameEdit = new QLineEdit();

    QVBoxLayout *mainLayout = new QVBoxLayout;
    mainLayout->addWidget(FunctionNameLabel);
    mainLayout->addWidget(FunctionNameEdit);

    mainLayout->addWidget(ParameterNameLabel1);
    mainLayout->addWidget(ParameterNameEdit1);
    mainLayout->addWidget(ParameterNameLabel2);
    mainLayout->addWidget(ParameterNameEdit2);
    mainLayout->addWidget(ParameterNameLabel3);
    mainLayout->addWidget(ParameterNameEdit3);

    mainLayout->addWidget(ExpressionNameLabel);
    mainLayout->addWidget(ExpressionNameEdit);
    mainLayout->addStretch(1);


    QDialogButtonBox* buttonBox = new QDialogButtonBox(QDialogButtonBox::Ok
                                     | QDialogButtonBox::Cancel);

    connect(buttonBox, &QDialogButtonBox::accepted, this, &QDialog::accept);
    connect(buttonBox, &QDialogButtonBox::rejected, this, &QDialog::reject);


    mainLayout->addWidget(buttonBox);
    setLayout(mainLayout);
    setWindowTitle(tr("设置函数"));
//    show();
}

bool  SetFunction::isLetter(char c)
{
    return 'a'<=c && c<='z'|| 'A'<=c && c<='Z';
}
bool SetFunction::checkString(string s)
{
    int len=s.length();
    for (int i=0; i<len; ++i)
        if (!isLetter(s[i])) return 0;
    return 1;
}

bool SetFunction::check()
{
    if (!checkString(FunctionNameEdit->text().toStdString())
            ||!checkString(ParameterNameEdit1->text().toStdString())
            ||!checkString(ParameterNameEdit2->text().toStdString())
            ||!checkString(ParameterNameEdit3->text().toStdString())) return 0;
    return 1;


}
