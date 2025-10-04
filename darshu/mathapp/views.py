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
