#include <iostream>
#include <iomanip>

using namespace std;

int main()
{
	double a, t, l;
	
	cin >> a >> t;
	l = a * t / 2;
	cout << fixed << setprecision(2) << l << endl;

	return 0;
}