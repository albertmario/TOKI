#include <bits/stdc++.h>

using namespace std;

string patt;
string input;
int n;

bool solve()
{
	if(patt == "*")
		return true;
	else
		if(patt[0] == '*')
		{
			string temp = "";
			string temp2 = "";

			for (int i = input.length(); i >= 0 ; --i)
				temp += input[i];

			for (int i = patt.length(); i >= 0; --i)
				temp2 += patt[i];

			for (int i = 0; i < temp2.length(); ++i)
				if(temp2[i] == '*')
					return true;
				else
					if(temp2[i] != temp[i])
						return false;
		}

		else if(patt[patt.length() - 1] == '*')
		{
			for (int i = 0; i < patt.length(); ++i)
				if(patt[i] == '*')
					return true;
				else
					if(patt[i] != input[i])
						return false;
		}
		else
		{
			int benar = 0;
			for (int i = 0; i < patt.length(); ++i)
				if(patt[i] == '*')
				{
					benar++;
					break;
				}
				else
					if(patt[i] != input[i])
						return false;

			string temp = "";
			string temp2 = "";

			for (int i = input.length(); i >= 0 ; --i)
				temp += input[i];

			for (int i = patt.length(); i >= 0; --i)
				temp2 += patt[i];

			for (int i = 0; i < temp2.length(); ++i)
				if(temp2[i] == '*')
				{
					benar++;
					if(benar == 2)
						return true;
				}
				else
					if(temp2[i] != temp[i])
						return false;
		}
}

int main()
{

	cin >> patt;
	cin >> n;

	for (int i = 0; i < n; ++i)
	{
		cin >> input;
		if (solve())
			cout << input << endl;
	}

	return 0;
}