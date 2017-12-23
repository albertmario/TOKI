#include <bits/stdc++.h>

using namespace std;

const int N = 22;
char arr[N][N];

int main()
{
	int R, C;
	char enter;

	scanf("%d %d", &R, &C);
	// isi
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
			scanf(" %c", &arr[i][j]);
	
	}

	// geser
	while(1)
	{
		int loc = -1;

		for (int i = 0; i < R; ++i)
		{
			bool isLine = true;
			for (int j = 0; j < C; ++j)
				if(arr[i][j] == '0')
					isLine = false;

			if(isLine)
			{
				for (int j = 0; j < C; ++j)
					arr[i][j] = '0';

				loc = i;
			}
		}

		if(loc == -1)
			break;

		for (int i = loc; i >= 0; --i)
		{
			for (int j = 0; j < C; ++j)
			{
				int k = i;
				while(arr[k + 1][j] == '0' && k + 1 <= R - 1)
					k++;

				swap(arr[i][j], arr[k][j]);
			}
		}
	}

	// cetak
	for (int i = 0; i < R; ++i)
	{
		for (int j = 0; j < C; ++j)
			printf("%c", arr[i][j]);

		printf("\n");
	}

	return 0;



}
