#include <iostream>
#include <cmath>
using namespace std;

int main()
{
	int a, i=0, cek = 0;

	cin >> a;
	while(1)
	{
		if(pow(2, i) > a)
			break;
		else if(pow(2, i) == a)
		{
			cek = 1;
			break;
		}
		i ++;
	}

	if(cek)
		cout << "ya" << endl;
	else
		cout << "bukan" << endl;

	return 0;
}