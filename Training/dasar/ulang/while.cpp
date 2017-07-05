#include <iostream>
using namespace std;

string scan(string s)
{
	int c;

	while(!cin.eof())
	{
		c = cin.get(); // baca per karakter -> ASCII
		s += c;
	}
	return s.substr(0, s.length()-1);
}

int main()
{
	string s;
	s = scan(s);
	cout << s;
	return 0;
}