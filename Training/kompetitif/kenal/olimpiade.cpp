#include <bits/stdc++.h>

using namespace std;

int main()
{
	std::map<float, string> map;
	long long int T, n, peringkat, bantu;
	float nilai1, nilai2, nilai3, total;
	string nama;
	string target;

	cin >> T;
	while(T--)
	{
		cin >> n >> peringkat;
		cin >> target;
		bantu = n;

		while(n--)
		{
			cin >> nama >> nilai1 >> nilai2 >> nilai3;
			total = nilai3 * 0.123 + nilai2 * 0.00000123 + nilai1 * 0.00000000123;
			map[total] = nama;
		}

		int x = 0;
		for(auto i : map)
		{
			x++;
			if(i.second == target)
				break;
			
		}

		if (bantu + 1 - x <= peringkat)
			cout << "YA" << endl;
		else
			cout << "TIDAK" << endl;

	}

	return 0;
}