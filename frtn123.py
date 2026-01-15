from flask import Flask, render_template, jsonify, request
import numpy as np
import math

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json

    angle = float(data.get('angle', 45))
    velocity = float(data.get('velocity', 25))
    gravity = float(data.get('gravity', 9.8))
    side_angle = float(data.get('side_angle', 30))

    theta = math.radians(angle)
    phi = math.radians(side_angle)

    t_flight = (2 * velocity * math.sin(theta)) / gravity
    t = np.linspace(0, t_flight, 150)

    x = velocity * math.cos(theta) * math.cos(phi) * t
    y = velocity * math.cos(theta) * math.sin(phi) * t
    z = velocity * math.sin(theta) * t - 0.5 * gravity * t**2

    return jsonify({
        "x": x.tolist(),
        "y": y.tolist(),
        "z": z.tolist()
    })

if __name__ == '__main__':
    app.run(debug=True)
