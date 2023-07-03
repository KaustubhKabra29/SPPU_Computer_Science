# -*- coding: utf-8 -*-
# 
# Automatically generated by Colaboratory.
#
# Original file is located at
#     https://colab.research.google.com/drive/1Y_-y7spbriy19a0m6_v5-N6iVOEQ2EnV

"""
!nvcc --version

!pip install git+https://github.com/andreinechaev/nvcc4jupyter.git

# Commented out IPython magic to ensure Python compatibility.

# %load_ext nvcc_plugin

# Commented out IPython magic to ensure Python compatibility.
# Vector Addition

# %%cu
# #include <stdio.h>
# #include <stdlib.h>
# #include <math.h>
#  
# // CUDA kernel. Each thread takes care of one element of c
# __global__ void vecAdd(double *a, double *b, double *c, int n)
# {
#     // Get our global thread ID
#     int id = blockIdx.x*blockDim.x+threadIdx.x;
#  
#     // Make sure we do not go out of bounds
#     if (id < n)
#         c[id] = a[id] + b[id];
# }
#  
# int main( int argc, char* argv[] )
# {
#     // Size of vectors
#     int n = 100000;
#  
#     // Host input vectors
#     double *h_a;
#     double *h_b;
#     //Host output vector
#     double *h_c;
#  
#     // Device input vectors
#     double *d_a;
#     double *d_b;
#     //Device output vector
#     double *d_c;
#  
#     // Size, in bytes, of each vector
#     size_t bytes = n*sizeof(double);
#  
#     // Allocate memory for each vector on host
#     h_a = (double*)malloc(bytes);
#     h_b = (double*)malloc(bytes);
#     h_c = (double*)malloc(bytes);
#  
#     // Allocate memory for each vector on GPU
#     cudaMalloc(&d_a, bytes);
#     cudaMalloc(&d_b, bytes);
#     cudaMalloc(&d_c, bytes);
#  
#     int i;
#     // Initialize vectors on host
#     for( i = 0; i < n; i++ ) {
#         h_a[i] = 1;
#         h_b[i] = 2;
#     }
#  
#     // Copy host vectors to device
#     cudaMemcpy( d_a, h_a, bytes, cudaMemcpyHostToDevice);
#     cudaMemcpy( d_b, h_b, bytes, cudaMemcpyHostToDevice);
#  
#     int blockSize, gridSize;
#  
#     // Number of threads in each thread block
#     blockSize = 1024;
#  
#     // Number of thread blocks in grid
#     gridSize = (int)ceil((float)n/blockSize);
#  
#     // Execute the kernel
#     vecAdd<<<gridSize, blockSize>>>(d_a, d_b, d_c, n);
#  
#     // Copy array back to host
#     cudaMemcpy( h_c, d_c, bytes, cudaMemcpyDeviceToHost );
#     
#     // Sum up vector c and print result divided by n, this should equal 1 within error
#    
#     for(i=0; i<n; i++)
#        
#     printf("final result: %f\n", h_c[i]);
#  
#     // Release device memory
#     cudaFree(d_a);
#     cudaFree(d_b);
#     cudaFree(d_c);
#  
#     // Release host memory
#     free(h_a);
#     free(h_b);
#     free(h_c);
#  
#     return 0;
# }
"""


# Commented out IPython magic to ensure Python compatibility.
# Matrix Multiplication
"""
%%cu
#include <iostream>
#include <cuda.h>

using namespace std;

#define BLOCK_SIZE 2

__global__ void gpuMM(float *A, float *B, float *C, int N)
{
    // Matrix multiplication for NxN matrices C=A*B
    // Each thread computes a single element of C
    int row = blockIdx.y*blockDim.y + threadIdx.y;
    int col = blockIdx.x*blockDim.x + threadIdx.x;

    float sum = 0.f;
    for (int n = 0; n < N; ++n)
        sum += A[row*N+n]*B[n*N+col];

    C[row*N+col] = sum;
}

int main(int argc, char *argv[])
{int N;float K;
    // Perform matrix multiplication C = A*B
    // where A, B and C are NxN matrices
    // Restricted to matrices where N = K*BLOCK_SIZE;
	cout<<"Enter a Value for Size/2 of matrix";
	cin>>K;

    K = 2;
    N = K*BLOCK_SIZE;

    cout << "Executing Matrix Multiplcation" << endl;
    cout << "Matrix size: " << N << "x" << N << endl;

    // Allocate memory on the host
    float *hA,*hB,*hC;
    hA = new float[N*N];
    hB = new float[N*N];
    hC = new float[N*N];

    // Initialize matrices on the host
    for (int j=0; j<N; j++){
        for (int i=0; i<N; i++){
           hA[j*N+i] = 2;
           hB[j*N+i] = 4;

        }
    }

    // Allocate memory on the device
    int size = N*N*sizeof(float);    // Size of the memory in bytes
    float *dA,*dB,*dC;
    cudaMalloc(&dA,size);
    cudaMalloc(&dB,size);
    cudaMalloc(&dC,size);

    dim3 threadBlock(BLOCK_SIZE,BLOCK_SIZE);
    dim3 grid(K,K);
    cout<<"\nInput Matrix 1 \n";
    for (int row=0; row<N; row++){
            for (int col=0; col<N; col++){

                   cout<<hA[row*col]<<"	";

            }
            cout<<endl;
        }
    cout<<"\nInput Matrix 2 \n";
    for (int row=0; row<N; row++){
            for (int col=0; col<N; col++){

                   cout<<hB[row*col]<<"	";

            }
            cout<<endl;
        }
    // Copy matrices from the host to device
    cudaMemcpy(dA,hA,size,cudaMemcpyHostToDevice);
    cudaMemcpy(dB,hB,size,cudaMemcpyHostToDevice);

    //Execute the matrix multiplication kernel

    gpuMM<<<grid,threadBlock>>>(dA,dB,dC,N);

    // Now do the matrix multiplication on the CPU
   /*float sum;
    for (int row=0; row<N; row++){
        for (int col=0; col<N; col++){
            sum = 0.f;
            for (int n=0; n<N; n++){
                sum += hA[row*N+n]*hB[n*N+col];
            }
            hC[row*N+col] = sum;
            cout << sum <<"	";


        }
        cout<<endl;
    }*/

    // Allocate memory to store the GPU answer on the host
    float *C;
    C = new float[N*N];

    // Now copy the GPU result back to CPU
    cudaMemcpy(C,dC,size,cudaMemcpyDeviceToHost);

    // Check the result and make sure it is correct
    cout <<"\n\n\n\n\n Resultant matrix\n\n";
    for (int row=0; row<N; row++){
        for (int col=0; col<N; col++){

               cout<<C[row*col]<<"	";

        }
        cout<<endl;
    }

    cout << "Finished." << endl;

}
"""



# Commented out IPython magic to ensure Python compatibility.
# Find Max using parallel reduction
"""
%%cu
#include <stdio.h>
#include <string.h>
#include <stdlib.h> // for rand()
#include <errno.h>

#include <cuda_runtime_api.h>
#include <math_constants.h>

#define N 500

/* host buffer */
float *data;
/* device buffers */
float *dSrc, *dDst;

void check_error(cudaError error, const char *message) {
    if (error != cudaSuccess) {
        fprintf(stderr, "%s (%s)\n", message,
            cudaGetErrorString(error));
        if (dSrc)
            cudaFree(dSrc);
        if (dDst)
            cudaFree(dDst);
        exit(1);
    }
}

#define WARP_SIZE 32
#define BLOCK_SIZE (12*WARP_SIZE)

__global__ void findmax(float *dDst, const float *dSrc, uint dim)
{
    __shared__ float cache[BLOCK_SIZE];					//cache is shared array between the block of threads

    uint gix = threadIdx.x + blockDim.x*blockIdx.x;

#define tid threadIdx.x

    float acc = CUDART_NAN_F;		//acc is initialized to certain random floating point value

    while (gix < dim) {				//this code executed by each thread
        acc = fmax(acc, dSrc[gix]);
        gix += blockDim.x*gridDim.x;
    }

    cache[tid] = acc;				//each thread keeps its result in cache index

    uint active = blockDim.x >> 1;	//active is incremented by 1

    do {
        __syncthreads();			// guarantee that all threads are in the same iteration of the do- while loop at the same time
        if (tid < active)
            cache[tid] = fmax(cache[tid], cache[tid+active]);			//calculate final result by comparing the values kept by each thread in cache
        active >>= 1;
    } while (active > 0);

    if (tid == 0)					//executed by parent thread
        dDst[blockIdx.x] = cache[0];
}

int main(int argc, char **argv) {
    data = (float*) calloc(N, sizeof(float));
    size_t data_size = N * sizeof(float);				// Here, N = 8
    float max = nan(""), d_max = nan("");				// returns a value of type double

    for (size_t i = 0; i < N; ++i) {
        data[i] = i; 									// input array
        max = fmax(max, data[i]);						// calculate max value sequentially
    }
    printf("%u elements generated, max %g, data size %zu \n",
            N, max, data_size);

    cudaError_t err;

    err = cudaMalloc(&dSrc, data_size);
    check_error(err, "allocating array");

    err = cudaMemcpy(dSrc, data, data_size, cudaMemcpyHostToDevice);		// copy array to device
    check_error(err, "copy UP");

    uint nblocks = 8;

    err = cudaMalloc(&dDst, nblocks*sizeof(*dDst));
    check_error(err, "allocating Dst array");

    cudaEvent_t start, stop;
    float runtime;
    cudaEventCreate(&start);				//Creates an event object for the current device
    cudaEventCreate(&stop);					//Creates an event object for the current device

    cudaEventRecord(start, 0);				// records an event. first parameter: event object, second parameter:stream in which to record the event, if value is zero, records the event after all preceding operations are completed
    findmax<<<nblocks,BLOCK_SIZE>>>(dDst, dSrc, N);		//call kernel function
    findmax<<<1,BLOCK_SIZE>>>(dDst, dDst, nblocks);
    cudaEventRecord(stop, 0);

    cudaEventSynchronize(stop);				//Wait until the completion of all device work preceding the most recent call to cudaEventRecord()
    cudaEventElapsedTime(&runtime, start, stop);		//Computes the elapsed time between two events and stores in first parameter

    /* Giga-elements per second */
    printf("%u elements processed in %gms: %gGE/s\n",
        N, runtime, (N/runtime)/(1000000));

    /* Actual bandwith in GB/s */
    uint total_els = N + nblocks;
    float sizeMB = float(total_els)*sizeof(float)/(1024*1024);
    printf("Bandwidth: %u elements (%gMB) read in two steps. "
        "Runtime: %gms (%gGB/s)\n",
        total_els, sizeMB, runtime, sizeMB/runtime);

    err = cudaMemcpy(&d_max, dDst, sizeof(d_max), cudaMemcpyDeviceToHost);		//copy the result back to host
    check_error(err, "copy DOWN");

    cudaFree(dSrc); dSrc = NULL;
    cudaFree(dDst); dDst = NULL;
    free(data);

    printf("Parallel max: %g vs %g\n", d_max, max);
}
"""

"""
Commented out IPython magic to ensure Python compatibility.
%%cu
#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512 // You can change this
#define NUM_OF_ELEMS 4096 // You can change this

#define funcCheck(stmt) {                                            \
    cudaError_t err = stmt;                                          \
    if (err != cudaSuccess)                                          \
    {                                                                \
        printf( "Failed to run stmt %d ", __LINE__);                 \
        printf( "Got CUDA error ...  %s ", cudaGetErrorString(err)); \
        return -1;                                                   \
    }                                                                \
}

__global__  void total(float * input, float * output, int len) 
{
    // Load a segment of the input vector into shared memory
    __shared__ float partialSum[2*BLOCK_SIZE];
    int globalThreadId = blockIdx.x*blockDim.x + threadIdx.x;
    unsigned int t = threadIdx.x;
    unsigned int start = 2*blockIdx.x*blockDim.x;

    if ((start + t) < len)
    {
        partialSum[t] = input[start + t];      
    }
    else
    {       
        partialSum[t] = 0.0;
    }
    if ((start + blockDim.x + t) < len)
    {   
        partialSum[blockDim.x + t] = input[start + blockDim.x + t];
    }
    else
    {
        partialSum[blockDim.x + t] = 0.0;
    }

    // Traverse reduction tree
    for (unsigned int stride = blockDim.x; stride > 0; stride /= 2)
    {
      __syncthreads();
        if (t < stride)
            partialSum[t] += partialSum[t + stride];
    }
    __syncthreads();

    // Write the computed sum of the block to the output vector at correct index
    if (t == 0 && (globalThreadId*2) < len)
    {
        output[blockIdx.x] = partialSum[t];
    }
}

int main(int argc, char ** argv) 
{
    int ii;

    float * hostInput; // The input 1D vector
    float * hostOutput; // The output vector
    float * deviceInput;
    float * deviceOutput;

    int numInputElements = NUM_OF_ELEMS; // number of elements in the input list
    int numOutputElements; // number of elements in the output list
    hostInput = (float *) malloc(sizeof(float) * numInputElements);

    for (int i=0; i < NUM_OF_ELEMS; i++)
    {
        hostInput[i] = 1.0;     // Add your input values
    }

    numOutputElements = numInputElements / (BLOCK_SIZE<<1);
    if (numInputElements % (BLOCK_SIZE<<1)) 
    {
        numOutputElements++;
    }
    hostOutput = (float*) malloc(numOutputElements * sizeof(float));

    //@@ Allocate GPU memory here
    funcCheck(cudaMalloc((void **)&deviceInput, numInputElements * sizeof(float)));
    funcCheck(cudaMalloc((void **)&deviceOutput, numOutputElements * sizeof(float)));

    // Copy memory to the GPU here
    cudaMemcpy(deviceInput, hostInput, numInputElements * sizeof(float), cudaMemcpyHostToDevice);

    // Initialize the grid and block dimensions here
    dim3 DimGrid( numOutputElements, 1, 1);
    dim3 DimBlock(BLOCK_SIZE, 1, 1);

    // Launch the GPU Kernel here
    total<<<DimGrid, DimBlock>>>(deviceInput, deviceOutput, numInputElements);

    // Copy the GPU memory back to the CPU here
    cudaMemcpy(hostOutput, deviceOutput, numOutputElements * sizeof(float), cudaMemcpyDeviceToHost);

    /********************************************************************
     * Reduce output vector on the host
     ********************************************************************/
    for (ii = 1; ii < numOutputElements; ii++) 
    {
        hostOutput[0] += hostOutput[ii];
    }

    printf("Reduced Sum from GPU = %f\n", hostOutput[0]);   

    // Free the GPU memory here
    cudaFree(deviceInput);
    cudaFree(deviceOutput); 
    free(hostInput);
    free(hostOutput);

    return 0;
}

"""

"""
Commented out IPython magic to ensure Python compatibility.
%%cu
#include <stdio.h>
#include <string.h>
#include <stdlib.h> // for rand()
#include <errno.h>

#include <cuda_runtime_api.h>
#include <math_constants.h>

#define N 2*2*2

/* host buffer */
float *data;
/* device buffers */
float *dSrc, *dDst;

void check_error(cudaError error, const char *message) {
    if (error != cudaSuccess) {
        fprintf(stderr, "%s (%s)\n", message,
            cudaGetErrorString(error));
        if (dSrc)
            cudaFree(dSrc);
        if (dDst)
            cudaFree(dDst);
        exit(1);
    }
}

#define WARP_SIZE 32
#define BLOCK_SIZE (12*WARP_SIZE)

__global__ void findMin(float *dDst, const float *dSrc, uint dim)
{
    __shared__ float cache[BLOCK_SIZE];			//cache is shared array between the block of threads

    uint gix = threadIdx.x + blockDim.x*blockIdx.x;

#define tid threadIdx.x

    float acc = CUDART_NAN_F;			//acc is initialized to certain random floating point value

    while (gix < dim) {					//this code executed by each thread
        acc = fmin(acc, dSrc[gix]);
        gix += blockDim.x*gridDim.x;
    }

    cache[tid] = acc;					//each thread keeps its result in cache index

    uint active = blockDim.x >> 1;		//active is incremented by 1

    do {
        __syncthreads();				// guarantee that all threads are in the same iteration of the do- while loop at the same time
        if (tid < active)
            cache[tid] = fmin(cache[tid], cache[tid+active]);   //calculate final result by comparing the values kept by each thread in cache
        active >>= 1;
    } while (active > 0);

    if (tid == 0)						//executed by parent thread
        dDst[blockIdx.x] = cache[0];	
}

int main(int argc, char **argv) {
    data = (float*) calloc(N, sizeof(float));
    size_t data_size = N * sizeof(float);			// Here, N = 8
    float min = nan(""), d_min = nan("");			// returns a value of type double


    for (size_t i = 0; i < N; ++i) {
        data[i] = i; 								// input array
        min = fmin(min, data[i]);					// calculate min value sequentially
    }
    printf("%u elements generated, min %g, data size %zu (%zuMB)\n",
            N, min, data_size, data_size>>20);

    cudaError_t err;

    err = cudaMalloc(&dSrc, data_size);
    check_error(err, "allocating array");

    err = cudaMemcpy(dSrc, data, data_size, cudaMemcpyHostToDevice);		// copy array to device
    check_error(err, "copy UP");

    uint nblocks = 8;

    err = cudaMalloc(&dDst, nblocks*sizeof(*dDst));
    check_error(err, "allocating Dst array");

    cudaEvent_t start, stop;
    float runtime;
    cudaEventCreate(&start);		//Creates an event object for the current device
    cudaEventCreate(&stop);			//Creates an event object for the current device

    cudaEventRecord(start, 0);		// records an event. first parameter: event object, second parameter:stream in which to record the event, if value is zero, records the event after all preceding operations are completed
    findMin<<<nblocks,BLOCK_SIZE>>>(dDst, dSrc, N);	//call kernel function
    findMin<<<1,BLOCK_SIZE>>>(dDst, dDst, nblocks);
    cudaEventRecord(stop, 0);

    cudaEventSynchronize(stop);		//Wait until the completion of all device work preceding the most recent call to cudaEventRecord()
    cudaEventElapsedTime(&runtime, start, stop);	//Computes the elapsed time between two events and stores in first parameter

    /* Giga-elements per second */
    printf("%u elements processed in %gms: %gGE/s\n",
        N, runtime, (N/runtime)/(1000000));

    /* Actual bandwith in GB/s */
    uint total_els = N + nblocks;
    float sizeMB = float(total_els)*sizeof(float)/(1024*1024);
    printf("Bandwidth: %u elements (%gMB) read in two steps. "
        "Runtime: %gms (%gGB/s)\n",
        total_els, sizeMB, runtime, sizeMB/runtime);

    err = cudaMemcpy(&d_min, dDst, sizeof(d_min), cudaMemcpyDeviceToHost);	//copy the result back to host
    check_error(err, "copy DOWN");

    cudaFree(dSrc); dSrc = NULL;
    cudaFree(dDst); dDst = NULL;
    free(data);

    printf("Parallel min: %g vs %g\n", d_min, min);
}

"""


"""
Commented out IPython magic to ensure Python compatibility.
%%cu
#include <cuda.h>
#include <stdio.h>
#include <stdlib.h>

#define BLOCK_SIZE 512 // You can change this
#define NUM_OF_ELEMS 4096 // You can change this

#define funcCheck(stmt) {                                            \
    cudaError_t err = stmt;                                          \
    if (err != cudaSuccess)                                          \
    {                                                                \
        printf( "Failed to run stmt %d ", __LINE__);                 \
        printf( "Got CUDA error ...  %s ", cudaGetErrorString(err)); \
        return -1;                                                   \
    }                                                                \
}

__global__  void total(float * input, float * output, int len) 
{
    // Load a segment of the input vector into shared memory
    __shared__ float partialSum[2*BLOCK_SIZE];
    int globalThreadId = blockIdx.x*blockDim.x + threadIdx.x;
    unsigned int t = threadIdx.x;
    unsigned int start = 2*blockIdx.x*blockDim.x;

    if ((start + t) < len)
    {
        partialSum[t] = input[start + t];      
    }
    else
    {       
        partialSum[t] = 0.0;
    }
    if ((start + blockDim.x + t) < len)
    {   
        partialSum[blockDim.x + t] = input[start + blockDim.x + t];
    }
    else
    {
        partialSum[blockDim.x + t] = 0.0;
    }

    // Traverse reduction tree
    for (unsigned int stride = blockDim.x; stride > 0; stride /= 2)
    {
      __syncthreads();
        if (t < stride)
            partialSum[t] += partialSum[t + stride];
    }
    __syncthreads();

    // Write the computed sum of the block to the output vector at correct index
    if (t == 0 && (globalThreadId*2) < len)
    {
        output[blockIdx.x] = partialSum[t];
    }
}

int main(int argc, char ** argv) 
{
    int ii;

    float * hostInput; // The input 1D vector
    float * hostOutput; // The output vector
    float * deviceInput;
    float * deviceOutput;

    int numInputElements = NUM_OF_ELEMS; // number of elements in the input list
    int numOutputElements; // number of elements in the output list
    hostInput = (float *) malloc(sizeof(float) * numInputElements);

    for (int i=0; i < NUM_OF_ELEMS; i++)
    {
        hostInput[i] = 1.0;     // Add your input values
    }

    numOutputElements = numInputElements / (BLOCK_SIZE<<1);
    if (numInputElements % (BLOCK_SIZE<<1)) 
    {
        numOutputElements++;
    }
    hostOutput = (float*) malloc(numOutputElements * sizeof(float));

    //@@ Allocate GPU memory here
    funcCheck(cudaMalloc((void **)&deviceInput, numInputElements * sizeof(float)));
    funcCheck(cudaMalloc((void **)&deviceOutput, numOutputElements * sizeof(float)));

    // Copy memory to the GPU here
    cudaMemcpy(deviceInput, hostInput, numInputElements * sizeof(float), cudaMemcpyHostToDevice);

    // Initialize the grid and block dimensions here
    dim3 DimGrid( numOutputElements, 1, 1);
    dim3 DimBlock(BLOCK_SIZE, 1, 1);

    // Launch the GPU Kernel here
    total<<<DimGrid, DimBlock>>>(deviceInput, deviceOutput, numInputElements);

    // Copy the GPU memory back to the CPU here
    cudaMemcpy(hostOutput, deviceOutput, numOutputElements * sizeof(float), cudaMemcpyDeviceToHost);

    /********************************************************************
     * Reduce output vector on the host
     ********************************************************************/
    for (ii = 1; ii < numOutputElements; ii++) 
    {
        hostOutput[0] += hostOutput[ii];
    }

    printf("Reduced Sum from GPU = %f\n", hostOutput[0]);   
    printf("Average is=%f\n",hostOutput[0]/4096);

    // Free the GPU memory here
    cudaFree(deviceInput);
    cudaFree(deviceOutput); 
    free(hostInput);
    free(hostOutput);

    return 0;
}
"""