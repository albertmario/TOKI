#include <iostream>
using namespace std;

int main()
{
	int a, angka, hasil = 0, i;

	cin >> a;
	for(i = 0 ; i < a; i ++)
	{
		cin >> angka;
		hasil += angka;
	}

	cout << hasil << endl;
	return 0;
}