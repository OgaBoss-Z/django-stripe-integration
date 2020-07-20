from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import JsonResponse



import stripe
stripe.api_key = "sk_test_hHjrGycdvzUznbaj3gA24bwW00ZrjaRkFK"


# Create your views here.
def home(request):
   context = {}
   return render(request, 'base/home.html', context)


def charge(request):
   amount = int(request.POST['amount'])
   if request.method == 'POST':
      print('Data:', request.POST)
      
      customer = stripe.Customer.create(
         email = request.POST['email'],
         name = request.POST['name'],
         source = request.POST['stripeToken'],
      )
      
      # `source` is obtained with Stripe.js; see https://stripe.com/docs/payments/accept-a-payment-charges#web-create-token
      stripe.Charge.create(
         customer = customer,
         amount=amount * 100,
         currency="inr",
         description="Donation",
      )
   return redirect(reverse('success', args=[amount]))


def successMsg(request, args):
   amount = args
   return render(request, 'base/success.html', {'amount':amount})
