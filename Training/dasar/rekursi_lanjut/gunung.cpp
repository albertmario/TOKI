#include <iostream>
#include <cstdlib>

using namespace std;

string draw_n(int n)
{
	string hasil;

	for (int i = 0; i < n; ++i)
		hasil += "*";
	hasil += "\n";

	return hasil;
}

string draw(int n, string hasil = "")
{
	if(n == 1)
		return "*\n";
	
	if(n == 2)
	{
		hasil += "*\n" ;
		hasil += "**\n" ;
		hasil += "*\n" ;
		return hasil;
	}

	return draw(n - 1) + draw_n(n) + draw(n - 1);
}

int main()
{
	int n;

	cin >> n;
	cout << draw(n);
	return 0;
}