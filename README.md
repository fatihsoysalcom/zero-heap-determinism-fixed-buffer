# zero-heap-determinism-fixed-buffer
This example demonstrates the principle of zero-heap determinism by simulating a satellite's sensor data processing. It uses a pre-allocated, fixed-size buffer (`array.array`) to store sensor readings, avoiding dynamic memory allocations during critical runtime operations. This approach ensures predictable memory usage and performance, crucial for 
