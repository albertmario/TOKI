#include <iostream>
#include <cmath>
using namespace std;

string cekAgak(int angka)
{
	int count = 0;

	for (int i = 2; i <= sqrt(angka) + 1; i++)
	{
		if(angka % i == 0)
			count += 2;
		if(count > 2)
			return "BUKAN";
	}
	return "YA";
}

int main()
{
	int a, angka;
	cin >> a;

	for(int i = 0; i < a;i++)
	{
		cin >> angka;
		cout << cekAgak(angka) << endl;
	}

	return 0;
}