# smart-gas-leakage-project
## About

The Smart Gas Leakage Detection System is a Python-based project designed to monitor gas levels and identify potential gas leakage risks. It uses threshold values to classify gas levels as SAFE, WARNING, or DANGER. Based on the detected status, the system displays alerts and simulates safety actions.
## testing
## Features

* Gas Level Monitoring: Generates simulated gas readings between 100 and 800 ppm.
* AI Risk Analysis: Classifies gas levels into SAFE, WARNING, and DANGER categories based on predefined thresholds.
* Cloud Monitoring: Displays the gas level and current status.
* Emergency Alert: Simulates a gas leakage alert when a dangerous level is detected.
* Automatic Ventilation: Simulates activation of the ventilation system.
* Automatic Gas Booking: Simulates a new gas cylinder booking request.
* Mobile Tracking: Simulates real-time gas status updates.
* Continuous Monitoring: Checks gas levels every five seconds.
  
## Gas Threshold Levels
SAFE: Below 200 ppm
WARNING: From 200 ppm to below 500 ppm
DANGER: 500 ppm and above

## How It Works
-The program generates a simulated gas level.
-The AI risk analysis function checks the gas level against the predefined thresholds.
-The cloud monitoring function displays the gas level and status.
-If the status is WARNING, mobile tracking is simulated.
-If the status is DANGER, the program simulates an emergency alert, ventilation activation, gas booking request, and mobile tracking update.
-The monitoring cycle repeats every five seconds.

## Applications
* Smart Home Safety Systems
* Gas Leakage Monitoring Concepts
* IoT-Based Safety Projects
