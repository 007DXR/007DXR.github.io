#include "setvariable.h"
//#include "ui_setvariable.h"
#include <QtWidgets>
#include <QLayout>
SetVariable::SetVariable(QWidget *parent) : QDialog(parent)
{
    VariableNameLabel = new QLabel();
    VariableNameEdit = new QLineEdit();

    QDialogButtonBox* buttonBox = new QDialogButtonBox(QDialogButtonBox::Ok
                                     | QDialogButtonBox::Cancel);

    connect(buttonBox, &QDialogButtonBox::accepted, this, &QDialog::accept);
    connect(buttonBox, &QDialogButtonBox::rejected, this, &QDialog::reject);

    QVBoxLayout *mainLayout = new QVBoxLayout;
//    mainLayout->addWidget(VariableWidget);
    mainLayout->addWidget(VariableNameLabel);
    mainLayout->addWidget(VariableNameEdit);
    mainLayout->addWidget(buttonBox);
    setLayout(mainLayout);
    setWindowTitle("设置变量");
}
bool  SetVariable::isLetter(char c)
{
    return 'a'<=c && c<='z'|| 'A'<=c && c<='Z';
}
bool SetVariable::check()
{
string s=VariableNameEdit->text().toStdString();
for (int i=0; i<s.length(); ++i)
    if (!isLetter(s[i])) return 0;
return 1;
}
SetVariable::~SetVariable(){

}
