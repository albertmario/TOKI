#include <iostream>
#include <cmath>
using namespace std;

string biner(int n, string hasil)
{
	if(n == 0)
		return hasil;

	return biner(floor(n / 2), (n % 2) ? "1"+hasil : "0"+hasil);
}

int main()
{
	int n;
	cin >> n;
	cout << biner(n, "") << endl;
	return 0;
}