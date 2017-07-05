#include <iostream>
using namespace std;

int main()
{
	int N, M, K, arr[102][102], hasil = 1, baris = 102, kolom = 102;

	for (int i = 0; i < 102; ++i)
		for (int j = 0; j < 102; ++j)
			arr[i][j] = 0;

	cin >> N >> M >> K;

	for(int i = 1; i <= N; i++)
		for (int j = 1; j <= M; ++j)
			cin >> arr[i][j];

	for (int i = 1; i <= N; ++i)
		for (int j = 1; j <= M; ++j)
		{
			if(arr[i - 1][j] > 0)
				hasil *= arr[i - 1][j];
			
			if(arr[i + 1][j] > 0)
				hasil *= arr[i + 1][j];
			
			if(arr[i][j - 1] > 0)
				hasil *= arr[i][j - 1];
			
			if(arr[i][j + 1] > 0)
				hasil *= arr[i][j + 1];

			if(hasil == K)
				if(j < kolom)
				{
					baris = i;
					kolom = j;
				}


			hasil = 1;
		}
	
	if(baris == 102)
		cout << 0 << " " << 0 << endl;
	else
		cout << baris << " " << kolom << endl;
	return 0;
}