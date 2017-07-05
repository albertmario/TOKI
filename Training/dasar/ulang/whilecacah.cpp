#include <iostream>
using namespace std;

int main()
{
	int hasil = 0, angka;

	while(!cin.eof())
	{
		cin >> angka;
		hasil += angka;
	}
	cout << hasil - angka << endl;

	return 0;

}