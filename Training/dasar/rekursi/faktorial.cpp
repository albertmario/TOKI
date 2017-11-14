#include <iostream>
using namespace std;

int faktorial(int n)
{
	if(n == 1)
		return 1;

	return (n % 2) ? n * faktorial(n - 1) : (n / 2) * faktorial(n - 1);
}

int main()
{
	int n;
	cin >> n;

	cout << faktorial(n) << endl;
	return 0;
}