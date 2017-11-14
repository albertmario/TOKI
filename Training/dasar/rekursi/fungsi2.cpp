#include <iostream>
using namespace std;

int hitung(int A, int B, int K, int x)
{
	if(K == 1)
		return abs(A * x + B);

	return hitung(A, B, K - 1, abs(A * x + B));
}

int main()
{
	int A, B, K, x;

	cin >> A >> B >> K >> x;
	cout << hitung(A,B,K,x) << endl;

	return 0;
}