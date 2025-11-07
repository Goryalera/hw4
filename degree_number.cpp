#include <iostream>
using namespace std;

double power(double x, int n) {
    if (n == 0) {
        return 1;
    } else if (n > 0) {
        return x * power(x, n - 1);
    } else {
        return 1 / power(x, -n);
    }
}

int main() {
    cout << power(2, 3) << endl;   // 8
    cout << power(5, 0) << endl;   // 1
    cout << power(2, -2) << endl;  // 0.25
    return 0;
}

