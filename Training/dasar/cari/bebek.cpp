#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
	vector <int> v;
	vector <int> ::iterator bawah, atas;

	int n, berat, q, x, y;
	int kiri, kanan;

	cin >> n;
	for (int i = 0; i < n; ++i)
	{
		cin >> berat;
		v.push_back(berat);
	}

	cin >> q;
	for (int i = 0; i < q; ++i)
	{
		cin >> x;
		cin >> y;

		bawah = upper_bound(v.begin(), v.end(), x);
		atas = upper_bound(v.begin(), v.end(), y);

		kiri = bawah - v.begin();
		kanan = atas - v.begin();

		// cout << kiri << " " << kanan << endl;

		cout << kanan - kiri << endl;
	}

}