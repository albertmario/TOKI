#include <iostream>
#include <map>
#include <vector>
#include <string>
using namespace std;

string palindrome(string s, char depan, char belakang)
{
	if(depan != belakang)
		return "BUKAN";

	if(s == "")
		return "YA";

	s = s.substr(1, s.length() - 2);
	depan = s[0];
	belakang = s[s.length() - 1];

	return palindrome(s, depan, belakang);
}

int main()
{	
	string s;
	char depan, belakang;

	cin >> s;
	depan = s[0];
	belakang = s[s.length() - 1];

	cout << palindrome(s, depan, belakang) << endl;

	return 0;
}