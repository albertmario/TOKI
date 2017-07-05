#include <iostream>
using namespace std;

int main()
{
	int max = 0, min = 0, n, angka;

	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> angka;
		if(i == 0)
		{
			max = angka;
			min = angka;
		}
		else
		{
			if(angka < min)
				min = angka;
			if(angka > max)
				max = angka;
		}
	}
	cout << max << " " << min << endl;
	return 0;
}