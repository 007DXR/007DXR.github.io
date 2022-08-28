#include <bits/stdc++.h>
#include <string>
#include "function.h"
using namespace std;

Function::Function(string Expression, string Name)
{
	variableList.clear();
	functionList.clear();
	this->s = "(" + Expression + ")";
	this->Name = Name;
}
double Function::readDigit()
{
	double num = s[index++] - '0';
	while (index < len && isDigit())
	{
		num = num * 10 + s[index] - '0';
		++index;
	}
	if (index >= len || s[index] != '.')
		return num;
	++index;
	double mi = 0.1;
	while (index < len && isDigit())
	{
		num = num + mi * (s[index] - '0');
		mi *= 0.1;
		++index;
	}

	return num;
}
string Function::readLetter()
{
	string ss = "";
	while (index < len && isLetter())
	{
		ss += {s[index]};
		index++;
	}

	return ss;
}

bool Function::isDigit()
{
	return s[index] >= '0' && s[index] <= '9';
}
bool Function::isLetter()
{
	return (s[index] >= 'a' && s[index] <= 'z') || (s[index] >= 'A' && s[index] <= 'Z');
}
bool Function::isFunc(string ss)
{
	if (isMathOp(ss))
		return 1;
	vector<Function>::iterator it;
	for (it = functionList.begin(); it != functionList.end(); ++it)
		if (it->Name == ss)
			return 1;
	return 0;
}
bool Function::isDualOp(string s)
{
	return s == "+" || s == "-" || s == "*" || s == "/" || s == "%"|| s == "**" || isBinaryOp(s);
}
bool Function::isBinaryOp(string s)
{
	return s == "<<" || s == ">>" || s == "&" || s == "|" || s == "^";
}
double Function::findVal(string ss)
{
	vector<Variable>::iterator it;
	for (it = variableList.begin(); it != variableList.end(); ++it)
		if (it->Name == ss)
			return it->Value;
    throw "findVal error";
}
void Function::calcDualOp(string op)
{
	if (numStack.empty())
		throw "calcDualOp error";
	double b = numStack.top();
	numStack.pop();
	if (numStack.empty())
		throw "calcDualOp error";
	double a = numStack.top();
	numStack.pop();
	cout << a << " " << b << endl;
	if (op == "**")
	{
		numStack.push(pow(a,b));
	}
	if (op == "+")
	{
		numStack.push(a + b);
	}
	if (op == "-")
	{
		numStack.push(a - b);
	}
	if (op == "*")
	{
		numStack.push(a * b);
	}
	if (op == "/")
	{
		if (b == 0)
			throw "division error";
		numStack.push(a / b);
	}
	if (op == "%")
	{
		if (b == 0)
			throw "division error";
		numStack.push(a - int(a / b) * b);
	}
	if (isBinaryOp(op))
	{
		// 位运算
		int aa = a;
		int bb = b;
		if (aa != a || bb != b)
			throw "binary error";
		if (op == "<<")
		{
			numStack.push(aa << bb);
		}
		if (op == ">>")
		{
			numStack.push(aa >> bb);
		}
		if (op == "&")
		{
			numStack.push(aa & bb);
		}
		if (op == "|")
		{
			numStack.push(aa | bb);
		}
		if (op == "^")
		{
			numStack.push(aa ^ bb);
		}
	}
}
bool Function::isMathOp(string s)
{

	return s == "sh" || s == "ch" || s == "th" || s == "sin" || s == "cos" || s == "tan" || s == "ln" || s == "lg" || s == "log";
}
double Function::calcMathOp(string symbol, double number)
{
	if (symbol == "sin")
		number = std::sin(number);
	else if (symbol == "sh")
		number = std::sinh(number);

	else if (symbol == "ch")
		number = std::cosh(number);
	else if (symbol == "cos")
		number = std::cos(number);
	else if (symbol == "ln")
		number = std::log(number);

	else if (symbol == "th")
		number = std::tanh(number);
	else if (symbol == "tan")
		number = std::tan(number);
	else if (symbol == "lg")
		number = std::log10(number);
	return number;
}
double Function::newExpression()
{
	string ss = opStack.top();
	if (isMathOp(ss))
	{
		if (temporaryStack.size() != 1)
			throw "temporaryStack error";
		double number = temporaryStack.top();
		temporaryStack.pop();
		return calcMathOp(ss, number);
	}
	vector<Function>::iterator it;
	for (it = functionList.begin(); it != functionList.end(); ++it)
		if (it->Name == ss)
		{
			if (it->variableList.size() != temporaryStack.size())
				throw "temporaryStack error";
			Function expr(it->s, ss);

			vector<Variable>::iterator var;
			for (var = it->variableList.begin(); var != it->variableList.end(); ++var, temporaryStack.pop())
			{
				if (temporaryStack.empty())
					throw "temporaryStack error";
				expr.variableList.push_back(Variable(var->Name, temporaryStack.top()));
			}
			if (!temporaryStack.empty())
				throw "temporaryStack error";
			return expr.Expression2Value();
		}
	throw "newExpression error";
	cout << "error";
}
int Function::getLevel(string s)
{
	if (s == "(" || isFunc(s))
		return -1;
	if (s == ",")
		return 0;
	if (s == "|")
		return 1;
	if (s == "^")
		return 2;
	if (s == "&")
		return 3;
	if (s == "<<" || s == ">>")
		return 4;
	if (s == "+" || s == "-")
		return 5;
	if (s == "*" || s == "/" || s == "%")
		return 6;
	if (s == "**")
		return 7;
	throw "getLevel error";
	cout << "error";
}

void Function::calcRight()
{
	while (!temporaryStack.empty())
		temporaryStack.pop();
	while (!opStack.empty() && getLevel(opStack.top()) != -1) //没有遇到（
	{
		string op = opStack.top();
		opStack.pop();
        if (op == ","){
            if(numStack.empty()==0) throw "error";
			temporaryStack.push(numStack.top()), numStack.pop();
        }
		else
			calcDualOp(op);
	}
	if (opStack.empty())
		throw "calcRight error";
	if (isFunc(opStack.top()))
	{
		if (numStack.empty())
			throw "calcRight error";
		temporaryStack.push(numStack.top()), numStack.pop();
		numStack.push(newExpression());
		cout << "numStack size" << numStack.size() << endl;
	}
	opStack.pop();
}
string Function::getDualOp()
{
	if (index + 1 < len)
	{
		string c = {s[index], s[index + 1]};
		if (isDualOp(c))
		{
			index += 2;
			return c;
		}
	}
	string c = {s[index]};
	if (isDualOp(c))
	{
		index++;
		return c;
	}
	return "";
}
double Function::Expression2Value()
{
	while (!numStack.empty())
		numStack.pop();
	while (!opStack.empty())
		opStack.pop();
	index = 0;
	len = s.length();
	while (index < len)
	{
		if (isDigit())
		{
			double num = readDigit();
			numStack.push(num);
		}
		else if (isLetter())
		{
			string ss = readLetter();
			if (isFunc(ss))
			{
				opStack.push(ss);
				if (s[index] != '(')
					throw "not found ( error";
				++index;
				if (s[index] == '-')
					numStack.push(0);
			}

			else
				numStack.push(findVal(ss));
		}
		else if (s[index] == '(')
		{
			opStack.push("(");
			index++;
			if (s[index] == '-')
				numStack.push(0);
		}
		else if (s[index] == ')')
		{
			calcRight();
			index++;
		}
		else if (s[index] == ',')
		{
			while (isDualOp(opStack.top())) //opStack.top()!="," && opStack.top()!="("
				calcDualOp(opStack.top()), opStack.pop();
			opStack.push(",");
			index++;
			if (s[index] == '-')
				numStack.push(0);
		}
		else
		{
			string c = getDualOp();
			if (c != "")
			{
                while (opStack.empty()==0 && isDualOp(opStack.top()) && getLevel(c) <= getLevel(opStack.top()))
					calcDualOp(opStack.top()), opStack.pop();
				opStack.push(c);
			}
			else
			{
				cout << "error";
				throw "operator error";
				return 0;
			}
		}
	}
	if (numStack.size() != 1 || opStack.empty()==0)
		throw "operator error";
	return numStack.top();
}
//int main()
//{
//	try
//	{
//		Function x = Function("tan(cos(3.14))+(2<<5-2)", "hel");
//		cout << x.Expression2Value();
//	}
//	catch (char const *Exception)
//	{
//		cout << Exception;
//	}
//}
