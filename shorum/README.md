# BMW Car Showroom Application

A Python Flask application that displays BMW cars, allows users to select a car, and shows detailed information including Indian price lists.

## Features

- Display of BMW car models with images
- Detailed car specifications and information
- Indian price list for each car model and variant
- Responsive design for all devices

## Requirements

- Python 3.6 or higher
- Flask

## Installation

1. Clone this repository or download the files
2. Install the required packages:

```
pip install flask
```

## Running the Application

1. Navigate to the project directory
2. Run the Flask application:

```
python app.py
```

3. Open your web browser and go to `http://127.0.0.1:5000/`

## Project Structure

- `app.py`: Main Flask application file
- `car_data.py`: Contains BMW car data and functions to access it
- `templates/`: HTML templates for the application
  - `base.html`: Base template with common elements
  - `index.html`: Home page showing all cars
  - `car_details.html`: Detailed view of a selected car
- `static/`: Static files for the application
  - `css/style.css`: CSS styles for the application
  - `images/`: Directory for car images

## Note

This is a demonstration application. In a production environment, you would:
- Use a database to store car information
- Implement user authentication for admin features
- Add more interactive features like filtering and searching
- Include actual images of the cars

## License

This project is for educational purposes only. BMW is a registered trademark of Bayerische Motoren Werke AG.
