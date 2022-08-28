#include<bits/stdc++.h>
 #include<string>
// #include<string>
// #include<Function.h>
using namespace std;
class Variable{
	public:
		string Name;
		double Value;
	Variable(string Name,double Value){
		this->Name=Name;
		this->Value=Value;
	}
};
class Function{
	public:
		int index=0;
		int len;
		string s;
		string Name;
		vector<Variable> variableList;
		vector<Function> functionList;
		stack<string> opStack;
		stack<double> numStack;
		stack<double> temporaryStack;
		Function(string Expression,string Name);
		Function();
		double readDigit();
		string readLetter();
		bool isDigit();
        bool isLetter();
        bool isFunc(string ss);
        bool isDualOp(string s);
		bool isBinaryOp(string s);
		
		bool isMathOp(string s);
        double findVal(string ss);
		string getDualOp();
        void calcDualOp(string c);
		double calcMathOp(string symbol, double number);
        double newExpression();
        int getLevel(string s);
        void calcRight();
        double Expression2Value();
        
};
