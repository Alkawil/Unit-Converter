# Unit-Converter

This is a Unit Converter web application built with Flask for the backend and HTML templates for the frontend. It allows users to convert between different units of Length, Weight, and Temperature.

---

## Features
- **Length Conversion**: Convert between units such as meters, kilometers, feet, and miles.
- **Weight Conversion**: Convert between units such as kilograms, grams, pounds, and ounces.
- **Temperature Conversion**: Convert between Celsius, Fahrenheit, and Kelvin.

---

## Project Structure
```plaintext
Unit Converter/
├── app.py
├── templates/
│   ├── base.html
│   ├── length.html
│   ├── weight.html
│   └── temperature.html
```

- **app.py**: The main Flask application file containing the route logic.
- **templates/**: Directory containing HTML templates for the web pages.
  - **base.html**: Base template for consistent layout.
  - **length.html**: Template for length conversion.
  - **weight.html**: Template for weight conversion.
  - **temperature.html**: Template for temperature conversion.

---

## Installation and Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/Alkawil/Unit-Converter.git
   cd Unit-Converter
   ```

2. **Set Up Virtual Environment** (Optional but recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install flask
   ```

4. **Run the Application**
   ```bash
   python app.py
   ```

