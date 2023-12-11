from django.shortcuts import render, redirect
from .models import Match
from .forms import CreateMatchForm
from twilio.rest import Client


# import twilio creds
from django.conf import settings

# Create your views here.

def home(request):
    if request.method == 'POST':
        form = CreateMatchForm(request.POST)
        if form.is_valid():
            new_match = Match(
                username1=form.cleaned_data['username1'],
                username2=form.cleaned_data['username2'],
                phone1=form.cleaned_data['phone1'],
                phone2=form.cleaned_data['phone2']
            )
            new_match.save()

            phone1 = str(new_match.phone1)
            if len(phone1) == 10:
                phone1 = "+1" + phone1
            phone2 = str(new_match.phone2)
            if len(phone2) == 10:
                phone2 = "+1" + phone2

            client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)
            print("Here")
            try:
                client.messages.create(
                    body="You've been matched! Visit http://localhost:8000/match/{} to view your match.".format(new_match.uid),
                    from_=settings.TWILIO_NUMBER,
                    to=phone1
                )
                """
                client.messages.create(
                    body="You've been matched! Visit http://localhost:8000/match/{} to view your match.".format(new_match.uid),
                    from_=settings.TWILIO_NUMBER,
                    to=phone2
                )
                """
            except:
                return render(request, 'index.html', {'form': form, 'error': 'Invalid phone number.'})

            return redirect('success_page')
    else:
        form = CreateMatchForm()
    return render(request, 'index.html', {'form': form})

def success_page(request):
    return render(request, 'success.html')

def view_match(request, uid):
    match = Match.objects.get(uid=uid)
    return render(request, 'match.html', {'match': match})