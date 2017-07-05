#include <iostream>
using namespace std;

int main()
{
	int a, angka = 0;

	cin >> a;
	for (int i = 0; i < a; ++i)
	{
		for(int j = 0; j <= i; j ++)
		{
			cout << angka;
			angka ++;
			if(angka > 9)
				angka = 0;
		}
		cout << endl;
	}
	return 0;
}