# Loos Gauge

A Raspberry Pi-based force measurement system using a load cell and HX711 amplifier to measure and report tension/force in real time.

The project reads measurements from a load cell, converts the raw reading into a force value, and continuously outputs the result in Newtons.

## Overview

The system uses an **HX711 load-cell amplifier** connected to a Raspberry Pi.

```text
Load Cell
    │
    ▼
 HX711 ADC
    │
    ▼
Raspberry Pi
    │
    ▼
Raw Measurement
    │
    ▼
Force Conversion
    │
    ▼
Force (N)
```

The Raspberry Pi continuously samples the HX711 and converts the measured value into an approximate force:

```text
Force = (measurement / 1000) × 9.8
```

The result is printed in Newtons every 0.1 seconds.

## Hardware

* Raspberry Pi
* Load cell
* HX711 load-cell amplifier
* Jumper wires

### GPIO Connections

| HX711 | Raspberry Pi |
| ----- | -----------: |
| DOUT  |       GPIO 5 |
| SCK   |       GPIO 6 |

The project uses the Raspberry Pi's BCM GPIO numbering.

## Software

The project is written in Python and uses:

* Python
* `RPi.GPIO`
* `HX711`
* Raspberry Pi GPIO
* Load-cell sensing

## How It Works

On startup, the program:

1. Configures the Raspberry Pi GPIO interface.
2. Initialises the HX711.
3. Sets the HX711 reading format.
4. Performs a tare to establish the zero point.
5. Continuously reads the load-cell measurement.
6. Converts the reading into force.
7. Prints the force in Newtons.
8. Repeats every 100 ms.

The current implementation uses a reference unit of `1`, meaning the system still requires calibration for accurate physical measurements.

## Installation

Clone the repository:

```bash
git clone https://github.com/TobyStanislaus/Loos-Gauge.git
cd Loos-Gauge
```

Install the required Python packages:

```bash
pip install RPi.GPIO
pip install hx711
```

The project requires a Raspberry Pi with an HX711 and load cell connected.

## Running

Run:

```bash
python read_values.py
```

After the initial tare, the program will continuously output measurements such as:

```text
Tare done. Start reading values...
Force: 12.4 newtons
Force: 12.7 newtons
Force: 12.5 newtons
```

Press `Ctrl+C` to stop the program. GPIO pins are cleaned up automatically when the program exits.

## Calibration

The current implementation contains:

```python
hx.set_reference_unit(1)
```

The reference unit should be calibrated against a known weight before using the system for accurate force measurements.

## Project Structure

```text
Loos-Gauge/
│
├── read_values.py    # Load-cell reading and force calculation
├── README.md         # Project documentation
├── LICENSE           # Apache 2.0 licence
└── .gitignore
```

## Applications

A system like this could be used for:

* Measuring sailing rigging tension
* Experimental instrumentation
* Force and tension monitoring
* Raspberry Pi sensor projects
* Real-time physical measurements
* Data collection for further analysis

## Future Improvements

Possible extensions include:

* Proper load-cell calibration
* Filtering and smoothing noisy measurements
* Logging measurements to CSV
* Real-time plotting
* A graphical dashboard
* Wireless transmission of measurements
* Automatic detection of tension thresholds
* Data analysis and visualisation
* Battery-powered operation
