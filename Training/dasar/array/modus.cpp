#include <iostream>
using namespace std;

int main()
{
	int arr[1001] = {0};
	int a, angka, max = 0, max2;

	cin >> a;
	for (int i = 0; i < a; ++i)
	{
		cin >> angka;
		arr[angka]++;
	}

	for (int i = 0; i < 1001; ++i)
	{
		if(arr[i] >= max)
		{
			max = arr[i];
			max2 = i;
		}
	}	

	cout << max2 << endl;
	return 0;
}