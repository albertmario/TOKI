#include <iostream>
using namespace std;

int main()
{
	int max, pola, i;

	cin >> max >> pola;
	for(i = 1; i <= max; i ++)
	{
		if(i % pola == 0)
			cout << "*";
		else
			cout << i;

		if(i == max)
			cout << endl;
		else
			cout << " ";
	}
	return 0;
}