#include <bits/stdc++.h>

using namespace std;

long long int gcd(long long int a, long long int b)
{
	if(b == 0)
		return a;
	else
		return gcd(b, a % b);
}

int main()
{
	long long int A, B, C, D;
	long long int E, F;
	long long int temp;

	cin >> A >> B >> C >> D;

	E = A * D + B * C;
	F = B * D;
	temp = gcd(E, F);

	cout << E / temp << " " << F / temp << endl;

	return 0;

}