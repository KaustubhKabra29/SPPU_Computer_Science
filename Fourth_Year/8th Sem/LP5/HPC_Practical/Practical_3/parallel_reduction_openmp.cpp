#include <iostream>
#include <vector>
#include <omp.h>
#include <climits>
#include <random>


using namespace std;

void min_reduction(vector<int>& arr) {
  int min_value = INT_MAX;
  #pragma omp parallel for reduction(min: min_value)
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] < min_value) {
      min_value = arr[i];
    }
  }
  cout << "Minimum value: " << min_value << endl;
}

void max_reduction(vector<int>& arr) {
  int max_value = INT_MIN;
  #pragma omp parallel for reduction(max: max_value)
  for (int i = 0; i < arr.size(); i++) {
    if (arr[i] > max_value) {
      max_value = arr[i];
    }
  }
  cout << "Maximum value: " << max_value << endl;
}

void sum_reduction(vector<int>& arr) {
  int sum = 0;
   #pragma omp parallel for reduction(+: sum)
   for (int i = 0; i < arr.size(); i++) {
    sum += arr[i];
  }
  cout << "Sum: " << sum << endl;
}

void average_reduction(vector<int>& arr) {
  int sum = 0;
  #pragma omp parallel for reduction(+: sum)
  for (int i = 0; i < arr.size(); i++) {
    sum += arr[i];
  }
  cout << "Average: " << (double)sum / arr.size() << endl;
}

int main() {
    const int size = 100;
    vector<int> vec(size);
    random_device rd;
    mt19937 gen(rd());
    uniform_int_distribution<int> dis(1, 1000);
    cout<<"Size of Vector :"<<vec.size()<<endl;

    cout<<"Vector values:";
    for (int i = 0; i < size; ++i) {
        vec[i] = dis(gen);
        cout<<vec[i]<<" ";
    }
    cout<<endl;

    double start_time = omp_get_wtime();
    min_reduction(vec);
    max_reduction(vec);
    sum_reduction(vec);
    average_reduction(vec);
    double end_time = omp_get_wtime();
    cout << "Runtime: " << end_time - start_time << " seconds" << endl;
}
