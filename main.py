import array
import time
import random

# Constants for our simulated satellite system
MAX_SENSOR_READINGS = 10  # Fixed size for our sensor data buffer
SENSOR_DATA_TYPE = 'f'    # 'f' for float (single precision)

class SatelliteSystem:
    """
    Simulates a satellite system designed with zero-heap determinism principles.
    All critical data structures are pre-allocated to avoid dynamic memory
    allocations during runtime, ensuring predictable performance.
    """
    def __init__(self):
        # Pre-allocate a fixed-size array for sensor readings.
        # This avoids dynamic memory allocation during operation, a core principle of zero-heap determinism.
        self.sensor_buffer = array.array(SENSOR_DATA_TYPE, [0.0] * MAX_SENSOR_READINGS)
        self.buffer_index = 0
        self.total_readings_processed = 0
        print(f"System initialized with a fixed-size sensor buffer of {MAX_SENSOR_READINGS} floats.")
        print(f"Initial buffer state: {list(self.sensor_buffer)}")

    def _get_simulated_sensor_data(self):
        """Simulates reading data from a sensor."""
        # In a real system, this would read from hardware.
        # We simulate a temperature reading in Celsius.
        return 20.0 + random.uniform(-2.0, 2.0)

    def process_sensor_data(self):
        """
        Processes new sensor data without dynamic memory allocation.
        New data overwrites the oldest data in the fixed buffer (circular buffer logic).
        """
        # Read new data from the simulated sensor
        new_reading = self._get_simulated_sensor_data()

        # Store the new reading in the pre-allocated buffer.
        # This operation does not allocate new memory on the heap, adhering to zero-heap principles.
        self.sensor_buffer[self.buffer_index] = new_reading
        
        # Move to the next position, wrapping around if necessary (circular buffer)
        self.buffer_index = (self.buffer_index + 1) % MAX_SENSOR_READINGS
        self.total_readings_processed += 1

        # Perform a simple, deterministic calculation on the current buffer state.
        # This also avoids heap allocations by iterating over the existing buffer.
        current_sum = 0.0
        for val in self.sensor_buffer:
            current_sum += val
        
        current_average = current_sum / MAX_SENSOR_READINGS

        print(f"[{self.total_readings_processed:03d}] New reading: {new_reading:.2f}C | "
              f"Buffer: {[f'{x:.2f}' for x in self.sensor_buffer]} | "
              f"Avg: {current_average:.2f}C")
        
        # Example of a deterministic decision based on sensor data
        if current_average > 21.0:
            print("  [ALERT] Average temperature high, initiating cooling sequence.")
        elif current_average < 19.0:
            print("  [ALERT] Average temperature low, initiating heating sequence.")

def main():
    print("--- GEONMI-MEMS AeroCore-3: Zero-Heap Determinism Example ---")
    print("Demonstrates avoiding dynamic memory allocation for predictable real-time performance.")
    print("-------------------------------------------------------------\n")

    satellite = SatelliteSystem()

    # Simulate continuous operation
    for i in range(15): # Run for a few cycles to show buffer behavior
        print(f"\n--- Cycle {i+1} ---")
        satellite.process_sensor_data()
        time.sleep(0.5) # Simulate real-time delay

    print("\n--- Simulation Complete ---")
    print(f"Total sensor readings processed: {satellite.total_readings_processed}")
    print("Note: In a true zero-heap system (e.g., C/Rust), memory would be pre-allocated")
    print("at compile time or during system initialization, and no 'malloc' calls would occur")
    print("during critical runtime operations.")

if __name__ == "__main__":
    main()
