#include <iostream>
using namespace std; 

template<typename ptr_t, typename T, typename op_t>
T accumulate3(ptr_t first, ptr_t last, T init, op_t op)
{
	while(first != last)
	{
		init = op(init, *first);
		++first;
	}
	return init;
}

class Add // functor class
{
	public:
	int operator()(int x, int y) { return x + y; }
};

class Vector
{
	public:
	Vector(int n) : n_(n), p_(new int[n]) { 
		for(int i = 0; i < n; ++i)
		{
			p_[i] = i * i * i;
		}
	}
	~Vector() { delete [] p_; }
	Vector& operator=(const Vector&) = delete;
	Vector(const Vector&) = delete;
	public:
	class Iterator
	{
		public:
		Iterator(int *p_) : p_it_(p_) { }
		int operator*() { return *p_it_;} 
		bool operator==(const Iterator& rhs ) const
		{
			return p_it_ == rhs.p_it_;
		}
		bool operator!=(const Iterator& rhs ) const
		{
			return !(*this == rhs);
		}
		Iterator operator++(int) // post
		{
			Iterator temp(*this);
			++*this;
			return temp;
		
		}
		Iterator& operator++() // pre
		{
			++p_it_;
			return *this;
		}
		private:
		int* p_it_;
	};
	
	Iterator begin()
	{
		return Iterator(p_);
	}
	Iterator end()
	{
		return Iterator(p_ + n_);
	}
	private:
	int *p_;
	int n_;
};
int main()
{
 	Vector v(5);
	cout << accumulate3(v.begin(), v.end(), 0, Add()) << "\n";
}







