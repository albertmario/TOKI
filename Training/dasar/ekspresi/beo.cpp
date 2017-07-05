#include <iostream>
using namespace std;

string scan(string s)
{
	int c;

	while(!cin.eof())
	{
		c = cin.get(); // baca per karakter -> ASCII
		
		if (c == '\n')
			break;

		s += c;
	}
	return s;
}

int main()
{
	string s;
	s = scan(s);

	cout << s << endl;

	return 0;
}
