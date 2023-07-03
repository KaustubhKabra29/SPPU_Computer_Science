#include <iostream>
#include <vector>
#include <omp.h>
#include <chrono>

using namespace std;
using namespace chrono;

void parallel_bubble_sort(vector<int>& arr) {
    int n = arr.size();
    bool swapped = true;
    omp_set_num_threads(2);  // set number of threads to 2
    for (int i = 0; i < n && swapped; i++) {
        swapped = false;
        #pragma omp parallel for shared(arr)
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
                swapped = true;
            }
        }
    }
}

int main() {
    vector<int> arr = {5, 1, 4, 2, 8, 9, 7, 6, 34, 11, 3, 50};
    cout << "Original array: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;

    auto start = high_resolution_clock::now();

    parallel_bubble_sort(arr);

    auto end = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(end - start);

    cout << "Sorted array: ";
    for (int x : arr) {
        cout << x << " ";
    }
    cout << endl;

    cout << endl;
    cout << "Time taken by bubble sort: " << duration.count() << " microseconds" << endl;

    int num_threads = omp_get_max_threads();
    cout << "Number of threads used by OpenMP: " << num_threads << endl;

    return 0;
}
