#include <iostream>
#include <cmath>
using namespace std;

string cekPrima(int angka)
{
	if(angka == 1)
		return "BUKAN";
	else if(angka == 2)
		return "YA";

	for (int i = 2; i < sqrt(angka) + 1; ++i)
		if(angka % i == 0)
			return "BUKAN";

	return "YA";
}

int main()
{
	int a, angka;

	cin >> a;
	for(int i = 0; i < a; i++)
	{
		cin >> angka;
		cout << cekPrima(angka) << endl;
	}
	return 0;
}