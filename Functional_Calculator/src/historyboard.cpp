#include "historyboard.h"

HistoryBoard::HistoryBoard(QWidget *parent) : QListWidget(parent)
{
addItem("预设函数/值:\n");
setMinimumSize(0, 450);
setMaximumSize(280, 450);
}
void HistoryBoard::AddItem(QString Key,QString Value)
{
    addItem(Key+"="+Value);

}
