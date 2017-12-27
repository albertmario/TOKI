#include <bits/stdc++.h>

using namespace std;

const int N = 10e5 + 5;

int main()
{
	long long int T;
	long long int num;
	long long int arr[N];
	long long int temp;

	std::vector<long long int> hasil;

	for(long long int i = 0; i < N; i++)
		arr[i] = 1;

	//make prime list
	for (long long int i = 2; i < N; ++i)
	{
		if(arr[i])
			hasil.push_back(i);

		temp = i * i;
		while(temp < N)
		{
			arr[temp] = 0;
			temp += i;
		}
	}

	cin >> T;
	while(T--)
	{
		cin >> num;
		cout << hasil.at(num - 1) << endl;
	}



	return 0;
}