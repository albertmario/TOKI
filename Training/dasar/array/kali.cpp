#include <iostream>
using namespace std;

int main()
{
	int N, M, P;
	int A[101][101], B[101][101];

	cin >> N >> M >> P;
	for (int i = 0; i < N; ++i)
		for (int j = 0; j < M; ++j)
			cin >> A[i][j];

	for (int i = 0; i < M; ++i)
		for (int j = 0; j < P; ++j)
			cin >> B[i][j];

	for (int i = 0; i < N; ++i)
	{
		for (int j = 0; j < P; ++j)
		{
			int hasil = 0;
			for(int k = 0; k < M; ++k)
				hasil += A[i][k] * B[k][j];

			if(j == P - 1)
				cout << hasil << endl;
			else
				cout << hasil << " ";
		}
	}
	return 0;
}

/*
00 01 02


00 01
10 11
20 21
*/
