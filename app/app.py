from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import datetime

app = Flask(__name__)
CORS(app)  # Allow frontend to connect

# Database setup (SQLite)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///complaints.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Complaint Model
class Complaint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    photo_url = db.Column(db.String(300), nullable=True)   # For storing photo path/URL
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(50), default="Pending")   # Pending / In Progress / Resolved
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "photo_url": self.photo_url,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "status": self.status,
            "created_at": self.created_at.strftime("%Y-%m-%d %H:%M:%S")
        }

# Routes
@app.route('/')
def home():
    return "Road Hazard Reporting Backend is running 🚧"

# Add a complaint
@app.route('/add_complaint', methods=['POST'])
def add_complaint():
    data = request.json
    new_complaint = Complaint(
        description=data['description'],
        photo_url=data.get('photo_url', None),  # Optional
        latitude=data['latitude'],
        longitude=data['longitude']
    )
    db.session.add(new_complaint)
    db.session.commit()
    return jsonify({"message": "Complaint added successfully!"}), 201

# Get all complaints
@app.route('/get_complaints', methods=['GET'])
def get_complaints():
    complaints = Complaint.query.all()
    return jsonify([c.to_dict() for c in complaints])

# Update complaint status
@app.route('/update_status/<int:complaint_id>', methods=['PUT'])
def update_status(complaint_id):
    data = request.json
    complaint = Complaint.query.get(complaint_id)
    if not complaint:
        return jsonify({"error": "Complaint not found"}), 404
    
    complaint.status = data['status']
    db.session.commit()
    return jsonify({"message": "Status updated successfully!"})

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Creates DB file
    app.run(debug=True)


