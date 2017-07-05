#include <iostream>
using namespace std;

int main()
{
	int a[3][3], i, j;

	for(i = 0; i < 3; i++)
		for(j = 0; j < 3; j++)
			cin >> a[i][j];

	for(i = 0; i < 3; i++)
		for(j = 0; j < 3; j++)
			if (j == 2)
				cout << a[j][i] << endl;
			else
				cout << a[j][i] << " ";
	
	return 0;
}



/*
00 01 02
10 11 12 
20 21 22

00 10 20
01 11 21
02 12 22
*/
