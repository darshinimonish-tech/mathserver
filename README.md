# Ex.05 Design a Website for Server Side Processing
# Date:04.10.2025
# AIM:
To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side.

# FORMULA:
P = I2R
P --> Power (in watts)
 I --> Intensity
 R --> Resistance

# DESIGN STEPS:
## Step 1:
Clone the repository from GitHub.

## Step 2:
Create Django Admin project.

## Step 3:
Create a New App under the Django Admin project.

## Step 4:
Create python programs for views and urls to perform server side processing.

## Step 5:
Create a HTML file to implement form based input and output.

## Step 6:
Publish the website in the given URL.

# PROGRAM :


```

math.html

html>
<head>
    <title>Lamp Power Calculator</title>
    <style>
        body {
            background-color: lightblue;
            font-family: Arial, sans-serif;
            text-align: center;
            padding-top: 50px;
        }
        input, button {
            padding: 5px 10px;
            margin: 5px;
        }
    </style>
</head>
<body>
    <h2>Lamp Power Calculator</h2>
    <label>Current (I) in Amperes:</label><br>
    <input type="number" id="current" step="any"><br>
    <label>Resistance (R) in Ohms:</label><br>
    <input type="number" id="resistance" step="any"><br><br>
    <button onclick="calculatePower()">Calculate Power</button>

    <h3 id="result"></h3>

    <script>
        function calculatePower() {
            let I = parseFloat(document.getElementById("current").value);
            let R = parseFloat(document.getElementById("resistance").value);

            if (isNaN(I) || isNaN(R)) {
                alert("Please enter valid numbers for current and resistance.");
                return;
            }

            let P = I * I * R; // P = I² × R
            document.getElementById("result").innerText = "The Power of the Lamp Filament is: " + P + " Watts";
        }
    </script>
</body>
</html>

views.py

from django.shortcuts import render

def lamp_power_calculator(request):
    power = None
    error_message = None

    if request.method == "POST":
        try:
            current = float(request.POST.get("current"))
            resistance = float(request.POST.get("resistance"))
            power = current ** 2 * resistance
        except (ValueError, TypeError):
            error_message = "Please enter valid numbers for current and resistance."

    context = {
        'power': power,
        'error_message': error_message,
    }

    return render(request,'math.html', context)





urls.py




from django.contrib import admin
from django.urls import path
from mathapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('calculate/',views.lamp_power_calculator,name='calculate'),
    
    
]




````


# HOMEPAGE:
![alt text](<Screenshot 2025-10-04 082749.png>)



# RESULT:
The program for performing server side processing is completed successfully.
