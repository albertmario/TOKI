#include <iostream>
#include <map>

using namespace std;

int main()
{
	std::map<string, int> m;
	std::map<string, int> ::iterator it;

	int n;
	string name;

	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> name;
		m[name]++;

		cout << distance(m.begin(), m.find(name)) + 1 << endl;
	}

	return 0;
}