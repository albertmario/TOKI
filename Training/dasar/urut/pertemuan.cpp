#include <iostream>
#include <map>
#include <string>

using namespace std;

int main()
{
	std::map<int, std::map<string, int>> map;
	int n;
	string name;

	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> name;
		map[name.length()][name]++;
	}

	for(auto i : map)
		for(auto j : i.second)
		{
			int temp = j.second;
			while(temp--)
				cout << j.first << endl;
		}

	return 0;
}