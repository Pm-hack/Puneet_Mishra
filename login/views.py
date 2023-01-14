from django.shortcuts import render
from django.http import JsonResponse
import random
import string

# A dictionary to store the OTPs
otp_dict = {}

def generate_otp(request):
    # Get the email from the request body
    email = request.POST.get("email")

    # Generate a random OTP
    otp = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))

    # Store the OTP in the dictionary with the email as the key
    otp_dict[email] = otp
    # Return the OTP
    return JsonResponse({"otp": otp})

def verify_otp(request):
    # Get the OTP from the request body
    otp = request.POST.get("otp")

    # Check if the OTP is valid
    for email, stored_otp in otp_dict.items():
        if otp == stored_otp:
            return JsonResponse({"status": "success", "email": email})
    return JsonResponse({"status": "error"})

