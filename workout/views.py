import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.shortcuts import render



def index(request, year=datetime.now().year, month=datetime.now().month):
    cal = HTMLCalendar().formatmonth(year, month)
    now = f"{datetime.now().day} {datetime.now().strftime('%B')}, {datetime.now().year}"
    context = {  
        'year': year,
        'month': month,
        "cal": cal,
        'now': now
    }
    
    return render(request, "index.html", context)
  