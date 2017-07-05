#include <iostream>
using namespace std;

int main()
{
	int a[101][101];
	int x, y;

	cin >> x >> y;

	for (int i = 0; i < x; ++i)
		for (int j = 0; j < y; ++j)
			cin >> a[i][j];

	for (int i = 0; i < y; ++i)
		for (int j = x - 1; j >= 0; --j)
			if(j)
				cout << a[j][i] << " ";
			else
				cout << a[j][i] << endl;
	
	return 0;
}