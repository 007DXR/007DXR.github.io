#ifndef SETFUNCTION_H
#define SETFUNCTION_H

#include <QWidget>
#include <QDialog>
#include<QtWidgets>
using namespace std;
class SetFunction : public QDialog
{
    Q_OBJECT
public:
    explicit SetFunction(QWidget *parent = nullptr);
    QLineEdit *FunctionNameEdit;
    QLineEdit *ParameterNameEdit1;
    QLineEdit *ParameterNameEdit2;
    QLineEdit *ParameterNameEdit3;
    QLineEdit *ExpressionNameEdit;
    bool  isLetter(char c);
    bool check();
    bool  checkString(string s);
signals:

};

#endif // SETFUNCTION_H
