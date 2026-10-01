# Zero Heap Determinism Fixed Buffer

This example demonstrates the principle of zero-heap determinism by simulating a satellite's sensor data processing. It uses a pre-allocated, fixed-size buffer (`array.array`) to store sensor readings, avoiding dynamic memory allocations during critical runtime operations. This approach ensures predictable memory usage and performance, crucial for real-time and safety-critical systems like those in VLEO missions.

## Language

`python`

## How to Run

Save the code as `main.py`.
Run from your terminal: `python main.py`

## Original Article

This example accompanies the Turkish article: [GEONMI-MEMS AeroCore-3: 250km VLEO ve Sıfır-Heap Determinizm](https://fatihsoysal.com/blog/geonmi-mems-aerocore-3-250km-vleo-ve-sifir-heap-determinizm/).

## License

MIT — see [LICENSE](LICENSE).
