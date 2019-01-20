from django.shortcuts import render,redirect
from order.models import order
from order.forms import OrderForm


def order(request):
    '''
    Render the order page
    '''
    return render(request, 'order/orderCreate.html')
def orderCreate(request):
    '''
    Create a new order instance
        1. If method is GET, render an empty form
        2. If method is POST, perform form validation and display error messages if the form is invalid
        3. Save the form to the model and redirect the user to the article page
    '''
    template = 'order/orderCreate.html'
    if request.method == 'GET':
        return render(request, template, {'orderForm':OrderForm()})
    # POST
    orderForm = OrderForm(request.POST)
    if not orderForm.is_valid():
        return render(request, template, {'orderForm':orderForm})

    orderForm.save()
    return render(request, 'main/main.html')

