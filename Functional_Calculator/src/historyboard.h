#ifndef HISTORYBOARD_H
#define HISTORYBOARD_H

#include <QWidget>
#include <QVBoxLayout>
#include <QListWidget>
#include <QtWidgets>
class HistoryBoard : public QListWidget
{
    Q_OBJECT
public:
    explicit HistoryBoard(QWidget *parent = nullptr);
    void AddItem(QString Key,QString Value);
    QVBoxLayout *HistoryLayout;
signals:

};

#endif // HISTORYBOARD_H
