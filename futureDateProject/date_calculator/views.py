from django.shortcuts import render
from datetime import datetime, timedelta
from .forms import DateCalculatorForm


def calculator(request):
    future_date = None
    if request.method == 'POST':
        form = DateCalculatorForm(request.POST)
        if form.is_valid():
            days = form.cleaned_data['days']
            current_date = datetime.now()
            future_date = current_date + timedelta(days=days)
            future_date = future_date.strftime('%B %d, %Y')
    else:
        form = DateCalculatorForm()
    
    return render(request, 'date_calculator/calculate.html', {'form': form, 'future_date': future_date})
