"""
BMW Car Showroom Data Module
Contains data and functions to access BMW car information
"""

# BMW car data with Indian prices and specifications
bmw_cars = [
    {
        "id": 1,
        "model": "BMW 3 Series",
        "image": "static/images/3series.jpg",
        "fallback_image": "https://www.bmw.in/content/dam/bmw/common/all-models/3-series/sedan/2022/highlights/bmw-3-series-sedan-sp-desktop.jpg",
        "description": "The BMW 3 Series is a compact executive car that combines luxury, performance, and technology in a sleek package.",
        "specifications": {
            "engine": "2.0L TwinPower Turbo 4-cylinder",
            "power": "255 hp",
            "torque": "400 Nm",
            "transmission": "8-speed automatic",
            "acceleration": "0-100 km/h in 5.8 seconds",
            "top_speed": "250 km/h (electronically limited)",
            "fuel_economy": "15-18 km/l"
        },
        "variants": [
            {"name": "330i Sport", "price_inr": "₹ 59.90 Lakh"},
            {"name": "320d Luxury Edition", "price_inr": "₹ 55.50 Lakh"},
            {"name": "330Li M Sport", "price_inr": "₹ 65.90 Lakh"}
        ],
        "colors": [
            {"name": "Alpine White", "code": "#FFFFFF"},
            {"name": "Black Sapphire", "code": "#0A0A0A"},
            {"name": "Mineral Grey", "code": "#696969"},
            {"name": "Portimao Blue", "code": "#1C3C94"},
            {"name": "Sunset Orange", "code": "#E55B13"}
        ]
    },
    {
        "id": 2,
        "model": "BMW 5 Series",
        "image": "static/images/5series.jpg",
        "fallback_image": "https://www.bmw.in/content/dam/bmw/common/all-models/5-series/sedan/2021/highlights/bmw-5-series-sedan-gallery-image-01.jpg",
        "description": "The BMW 5 Series is a mid-size luxury sedan that offers a perfect balance of comfort, driving dynamics, and cutting-edge technology.",
        "specifications": {
            "engine": "2.0L TwinPower Turbo 4-cylinder / 3.0L TwinPower Turbo 6-cylinder",
            "power": "248-335 hp",
            "torque": "350-450 Nm",
            "transmission": "8-speed automatic",
            "acceleration": "0-100 km/h in 5.2-6.1 seconds",
            "top_speed": "250 km/h (electronically limited)",
            "fuel_economy": "13-16 km/l"
        },
        "variants": [
            {"name": "530i M Sport", "price_inr": "₹ 72.90 Lakh"},
            {"name": "520d Luxury Line", "price_inr": "₹ 68.90 Lakh"},
            {"name": "530d M Sport", "price_inr": "₹ 79.90 Lakh"}
        ],
        "colors": [
            {"name": "Alpine White", "code": "#FFFFFF"},
            {"name": "Black Sapphire", "code": "#0A0A0A"},
            {"name": "Mineral Grey", "code": "#696969"},
            {"name": "Phytonic Blue", "code": "#0F2D5B"},
            {"name": "Bernina Grey", "code": "#7D7E7D"}
        ]
    },
    {
        "id": 3,
        "model": "BMW 7 Series",
        "image": "static/images/7series.jpg",
        "fallback_image": "https://www.bmw.in/content/dam/bmw/marketIN/bmw_in/all-models/7-series/sedan/2022/highlights/bmw-7-series-sedan-sp-desktop.jpg",
        "description": "The BMW 7 Series is a full-size luxury sedan that represents the pinnacle of BMW's sedan lineup, offering unmatched luxury, technology, and performance.",
        "specifications": {
            "engine": "3.0L TwinPower Turbo 6-cylinder / 4.4L TwinPower Turbo V8",
            "power": "335-523 hp",
            "torque": "450-750 Nm",
            "transmission": "8-speed automatic",
            "acceleration": "0-100 km/h in 4.3-5.3 seconds",
            "top_speed": "250 km/h (electronically limited)",
            "fuel_economy": "9-13 km/l"
        },
        "variants": [
            {"name": "740i", "price_inr": "₹ 1.70 Crore"},
            {"name": "740Li M Sport", "price_inr": "₹ 1.78 Crore"},
            {"name": "760Li xDrive", "price_inr": "₹ 2.50 Crore"}
        ],
        "colors": [
            {"name": "Alpine White", "code": "#FFFFFF"},
            {"name": "Black Sapphire", "code": "#0A0A0A"},
            {"name": "Mineral White", "code": "#F2F3F0"},
            {"name": "Carbon Black", "code": "#2A2A2A"},
            {"name": "Cashmere Silver", "code": "#C0C0C0"}
        ]
    },
    {
        "id": 4,
        "model": "BMW X3",
        "image": "static/images/x3.jpg",
        "fallback_image": "https://www.bmw.in/content/dam/bmw/common/all-models/x-series/x3/2021/highlights/bmw-x3-onepager-gallery-image-01.jpg",
        "description": "The BMW X3 is a compact luxury SUV that combines versatility, driving pleasure, and premium features in a practical package.",
        "specifications": {
            "engine": "2.0L TwinPower Turbo 4-cylinder",
            "power": "248 hp",
            "torque": "350 Nm",
            "transmission": "8-speed automatic",
            "acceleration": "0-100 km/h in 6.3 seconds",
            "top_speed": "240 km/h",
            "fuel_economy": "13-15 km/l"
        },
        "variants": [
            {"name": "X3 xDrive30i SportX Plus", "price_inr": "₹ 65.00 Lakh"},
            {"name": "X3 xDrive30i M Sport", "price_inr": "₹ 72.90 Lakh"},
            {"name": "X3 xDrive20d Luxury Line", "price_inr": "₹ 68.50 Lakh"}
        ],
        "colors": [
            {"name": "Alpine White", "code": "#FFFFFF"},
            {"name": "Black Sapphire", "code": "#0A0A0A"},
            {"name": "Phytonic Blue", "code": "#0F2D5B"},
            {"name": "Sophisto Grey", "code": "#5B5C5E"},
            {"name": "Carbon Black", "code": "#2A2A2A"}
        ]
    },
    {
        "id": 5,
        "model": "BMW X5",
        "image": "static/images/x5.jpg",
        "fallback_image": "https://www.bmw.in/content/dam/bmw/common/all-models/x-series/x5/2021/highlights/bmw-x5-onepager-gallery-image-01.jpg",
        "description": "The BMW X5 is a mid-size luxury SUV that offers a commanding presence, luxurious interior, and powerful performance capabilities.",
        "specifications": {
            "engine": "3.0L TwinPower Turbo 6-cylinder / 4.4L TwinPower Turbo V8",
            "power": "335-523 hp",
            "torque": "450-750 Nm",
            "transmission": "8-speed automatic",
            "acceleration": "0-100 km/h in 4.3-5.5 seconds",
            "top_speed": "250 km/h (electronically limited)",
            "fuel_economy": "10-14 km/l"
        },
        "variants": [
            {"name": "X5 xDrive40i xLine", "price_inr": "₹ 93.90 Lakh"},
            {"name": "X5 xDrive30d M Sport", "price_inr": "₹ 95.90 Lakh"},
            {"name": "X5 M Competition", "price_inr": "₹ 1.95 Crore"}
        ],
        "colors": [
            {"name": "Alpine White", "code": "#FFFFFF"},
            {"name": "Black Sapphire", "code": "#0A0A0A"},
            {"name": "Mineral White", "code": "#F2F3F0"},
            {"name": "Phytonic Blue", "code": "#0F2D5B"},
            {"name": "Manhattan Green", "code": "#254441"}
        ]
    },
    {
        "id": 6,
        "model": "BMW X7",
        "image": "static/images/x7.jpg",
        "fallback_image": "https://www.bmw.in/content/dam/bmw/common/all-models/x-series/x7/2021/highlights/bmw-x7-onepager-gallery-image-01.jpg",
        "description": "The BMW X7 is a full-size luxury SUV that offers three rows of seating, exceptional comfort, and impressive performance in a flagship package.",
        "specifications": {
            "engine": "3.0L TwinPower Turbo 6-cylinder / 4.4L TwinPower Turbo V8",
            "power": "335-523 hp",
            "torque": "450-750 Nm",
            "transmission": "8-speed automatic",
            "acceleration": "0-100 km/h in 4.7-5.8 seconds",
            "top_speed": "250 km/h (electronically limited)",
            "fuel_economy": "9-13 km/l"
        },
        "variants": [
            {"name": "X7 xDrive40i M Sport", "price_inr": "₹ 1.25 Crore"},
            {"name": "X7 xDrive30d Design Pure Excellence", "price_inr": "₹ 1.22 Crore"},
            {"name": "X7 M50d", "price_inr": "₹ 1.68 Crore"}
        ],
        "colors": [
            {"name": "Alpine White", "code": "#FFFFFF"},
            {"name": "Black Sapphire", "code": "#0A0A0A"},
            {"name": "Mineral White", "code": "#F2F3F0"},
            {"name": "Phytonic Blue", "code": "#0F2D5B"},
            {"name": "Ametrine Metallic", "code": "#4A2639"}
        ]
    },
    {
        "id": 7,
        "model": "BMW M2",
        "image": "static/images/m2.jpg",
        "fallback_image": "https://www.bmw.in/content/dam/bmw/common/all-models/m-series/m2-coupe/2022/highlights/bmw-m2-coupe-onepager-gallery-image-01.jpg",
        "description": "The BMW M2 is a high-performance compact sports coupe that delivers exhilarating driving dynamics and track-ready capabilities.",
        "specifications": {
            "engine": "3.0L TwinPower Turbo 6-cylinder",
            "power": "453 hp",
            "torque": "550 Nm",
            "transmission": "8-speed automatic / 6-speed manual",
            "acceleration": "0-100 km/h in 4.1 seconds",
            "top_speed": "285 km/h (with M Driver's Package)",
            "fuel_economy": "8-10 km/l"
        },
        "variants": [
            {"name": "M2 Competition", "price_inr": "₹ 98.00 Lakh"}
        ],
        "colors": [
            {"name": "Alpine White", "code": "#FFFFFF"},
            {"name": "Black Sapphire", "code": "#0A0A0A"},
            {"name": "Zandvoort Blue", "code": "#0E3773"},
            {"name": "Toronto Red", "code": "#C41E3A"},
            {"name": "Brooklyn Grey", "code": "#5A5A5A"}
        ]
    },
    {
        "id": 8,
        "model": "BMW M4",
        "image": "static/images/m4.jpg",
        "fallback_image": "https://www.bmw.in/content/dam/bmw/common/all-models/m-series/m4-coupe/2021/highlights/bmw-m4-coupe-onepager-gallery-image-01.jpg",
        "description": "The BMW M4 is a high-performance sports coupe that combines aggressive styling with track-focused performance and everyday usability.",
        "specifications": {
            "engine": "3.0L TwinPower Turbo 6-cylinder",
            "power": "503 hp",
            "torque": "650 Nm",
            "transmission": "8-speed automatic",
            "acceleration": "0-100 km/h in 3.5 seconds",
            "top_speed": "290 km/h (with M Driver's Package)",
            "fuel_economy": "8-10 km/l"
        },
        "variants": [
            {"name": "M4 Competition", "price_inr": "₹ 1.53 Crore"},
            {"name": "M4 Competition xDrive", "price_inr": "₹ 1.63 Crore"}
        ],
        "colors": [
            {"name": "Alpine White", "code": "#FFFFFF"},
            {"name": "Black Sapphire", "code": "#0A0A0A"},
            {"name": "Isle of Man Green", "code": "#1E4D3B"},
            {"name": "Sao Paulo Yellow", "code": "#F0E240"},
            {"name": "Toronto Red", "code": "#C41E3A"}
        ]
    }
]

def get_all_cars():
    """Return all BMW cars"""
    return bmw_cars

def get_car_by_id(car_id):
    """Return a specific car by ID"""
    for car in bmw_cars:
        if car["id"] == car_id:
            return car
    return None
