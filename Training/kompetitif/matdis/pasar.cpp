#include <bits/stdc++.h>

using namespace std;

int gcd(long long int a, long long int b)
{
	if(b == 0)
		return a;
	else
		return gcd(b, a % b);
}

int main()
{
	int n;
	long long int arr[22];
	long long int val = 1;

	cin >> n;
	for (int i = 0; i < n; ++i)
		cin >> arr[i];

	for (int i = 0; i < n; ++i)
		val = val * arr[i] / gcd(val, arr[i]);

	cout << val << endl;

	return 0;
}