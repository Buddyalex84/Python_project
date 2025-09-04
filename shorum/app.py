from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

# Import BMW car data
from car_data import get_all_cars, get_car_by_id

@app.route('/')
def index():
    """Home page showing all BMW cars"""
    cars = get_all_cars()
    return render_template('index.html', cars=cars)

@app.route('/car/<int:car_id>')
def car_details(car_id):
    """Show detailed information about a specific car"""
    car = get_car_by_id(car_id)
    if car:
        return render_template('car_details.html', car=car)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
