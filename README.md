# drone-simulator
A 3D Drone Flight Simulator that visualizes projectile motion using physics-based equations and real-time animation.
The project is built with a Python Flask backend for computation and a Plotly.js frontend for interactive 3D visualization.

Users can adjust launch parameters such as angle, velocity, and yaw to observe how the drone’s trajectory changes in real time.
FEATURES

Physics-based projectile motion simulation

Real-time backend computation using Flask

Interactive 3D visualization using Plotly.js

Manual frame-by-frame animation for smooth motion

Live controls for angle, velocity, and yaw

Lightweight and easy-to-understand project structure

PHYSICS MODEL

The simulator uses classical kinematic equations of motion.

Horizontal motion along X and Y axes

Vertical motion along Z axis under gravity

Yaw (side angle) to simulate 3D spread

The backend calculates the full trajectory and sends the data to the frontend as JSON.
The frontend animates the drone manually frame by frame to ensure smooth playback across browsers.

TECH STACK

Python

Flask

NumPy

HTML

Tailwind CSS

Plotly.js

PROJECT STRUCTURE

drone-simulator
│
├── frtn123.py
├── templates
│ └── index.html
├── .gitignore
└── README.txt

HOW TO RUN LOCALLY

Install required libraries

pip install flask numpy

Run the Flask server

python frtn123.py

Open the application in a browser

http://127.0.0.1:5000

You can then launch the drone and adjust the sliders to observe the simulation.

FUTURE IMPROVEMENTS

Wind and air drag simulation

Camera-follow mode

Trajectory statistics such as maximum height and range

Slow-motion and replay controls

Online deployment

AUTHOR

Created by Shreyas
Project focused on learning physics simulation, backend development, and interactive visualization.
