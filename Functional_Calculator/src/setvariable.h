#ifndef SETVARIABLE_H
#define SETVARIABLE_H

#include <QDialog>
#include <QtWidgets>
using namespace std;
namespace Ui {
class SetVariable;
}

class SetVariable : public QDialog
{
    Q_OBJECT

public:
    explicit SetVariable(QWidget *parent = nullptr);
    ~SetVariable();
    QLineEdit *VariableNameEdit;
    QLabel *VariableNameLabel;
void VariableTab(QWidget* parent);
bool  isLetter(char c);
bool check();
private:
    Ui::SetVariable *ui;
};

#endif // SETVARIABLE_H
