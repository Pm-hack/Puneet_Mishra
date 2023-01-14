from django.shortcuts import render
from django.http import JsonResponse
import random
import string
from django.views.decorators.csrf import csrf_exempt
import time


# A dictionary to store the OTPs
otp_dict = {}

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def requestOtp(request):
    # Get the email from the request body
    email = request.POST.get("email")

    # Generate a random OTP
    otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Store the OTP in the dictionary with the email as the key
    otp_dict[email] = {"otp": otp, "timestamp": time.time()}
    print(otp)
    # Return the OTP
    return JsonResponse({"otp": otp})

@csrf_exempt
def verifyOtp(request):
    # Get the OTP from the request body
    otp = request.POST["otp"]
    #print(otp)
    # Check if the OTP is valid
    for email, otp_data in otp_dict.items():
        if otp == otp_data["otp"] and time.time() - otp_data["timestamp"] <= 30:
            return JsonResponse({"status": "success", "email": email})
    return JsonResponse({"status": "error"})
