# python-aprs-tracker

A Python program for Ham radio operators and APRS (Automatic Packet Reporting System) trackers to report their location to the APRS network.

The program sends APRS packets containing the operator's callsign, timestamp, and latitude/longitude to an APRS-IS server, which can then be displayed on a map by other APRS users. The program is configurable with the operator's own callsign, destination callsign, APRS-IS server, and beacon interval, making it easy to customize for different use cases.

## Installation

To use this program, you'll need to have Python 3 installed on your system. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

Once you have Python installed, simply clone this repository to your local machine using Git:
    
    git clone [https://github.com/your_username/python-aprs-tracker.git](https://github.com/your_username/python-aprs-tracker.git) 

## Usage

To use the program, simply run it in a Python interpreter or save it to a file with a ".py" extension and run it with the command:
    
    python aprs_tracker.py 

The program will continue running until it is manually stopped. The operator's location will be periodically reported to the APRS network based on the beacon interval configured in the program.

By default, the program is configured with the following settings:

* My callsign: `MYCALLSIGN-15` (replace with your own callsign)
* Destination callsign: `APRS`
* APRS-IS server: `rotate.aprs2.net`
* APRS-IS server port: `14580`
* Beacon interval: `60` seconds
* Latitude: `37.7749` (replace with your own latitude)
* Longitude: `-122.4194` (replace with your own longitude)

You can modify these settings by editing the `aprs_tracker.py` file.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request with your changes. Please ensure that your code is well-tested and adheres to the PEP 8 style guide for Python code.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more information.
