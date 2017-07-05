#include <iostream>
using namespace std;

int main()
{
	int a;
	cin >> a;

	if(a > 9999)
		cout << "puluhribuan" << endl;
	else if(a > 999)
		cout << "ribuan" << endl;
	else if (a > 99)
		cout << "ratusan" << endl;
	else if (a > 9)
		cout << "puluhan" << endl;
	else
		cout << "satuan" << endl;

	return 0;
}