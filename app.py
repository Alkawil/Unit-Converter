from flask import Flask,render_template,request

app = Flask(__name__)

def length_converter(value,from_unit,to_unit):
    conversion_scale = {
        "millimeter": 1, "centimeter": 10, "meter": 1000,
        "kilometer": 1_000_000, "inch": 25.4,
        "foot": 304.8, "yard": 914.4, "mile": 1_609_344,
    }

    value_mm = value * conversion_scale[from_unit]
    return value_mm / conversion_scale[to_unit]


def weight_converter(value,from_unit,to_unit):
    conversion_scale = {
        "milligram": 1, "gram": 1000, "kilogram": 1_000_000,
        "ounce": 28_349.5, "pound": 453_592,
    }

    value_mm = value * conversion_scale[from_unit]
    return value_mm / conversion_scale[to_unit]


def temprature_converter(value,from_unit,to_unit):
    if from_unit == to_unit:
        return value
    
    if from_unit == "Celsius":
        return value * 9/5 + 32 if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    

@app.route('/')
def home():
    return render_template("base.html")

@app.route('/length',methods=["GET",'POST'])
def length():
    if request.method == "POST":
        try:

            value = float(request.form["value"])
            from_unit = request.form["from_unit"]
            to_unit = request.form["to_unit"]

            result = length_converter(value,from_unit,to_unit)
            return render_template(
                "length.html",
                result=result,
                value=value,
                from_unit=from_unit,
                to_unit=to_unit,
            )
        except KeyError:
            # Handle missing or invalid form data
            return render_template("length.html", result=None)
    # For a GET request, just display the form
    return render_template("length.html", result=None)

@app.route('/weight',methods =["GET","POST"])
def weight():
        if request.method == "POST":
            try:
                value = float(request.form["value"])
                from_unit = request.form["from_unit"]
                to_unit = request.form["to_unit"]
                
                result = weight_converter(value,from_unit,to_unit)
                return render_template(
                "weight.html",
                result=result,
                value=value,
                from_unit=from_unit,
                to_unit=to_unit,
                )
            
            except KeyError:
            # Handle missing or invalid form data
                return render_template("weight.html", result=None)
    # For a GET request, just display the form
        return render_template("weight.html", result=None)



@app.route('/temperatures',methods =["GET","POST"])
def temperature():
        if request.method == "POST":
            try:
                value = float(request.form["value"])
                from_unit = request.form["from_unit"]
                to_unit = request.form["to_unit"]
                
                result = temprature_converter(value,from_unit,to_unit)
                return render_template(
                "temperature.html",
                result=result,
                value=value,
                from_unit=from_unit,
                to_unit=to_unit,
                )
            
            except KeyError:
            # Handle missing or invalid form data
                return render_template("temperature.html", result=None)
    # For a GET request, just display the form
        return render_template("temperature.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)