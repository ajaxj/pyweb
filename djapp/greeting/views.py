# Create your views here.
import datetime
from django.http import HttpResponse
from greeting.models import Greeting


def index(request):
    greet = Greeting(
        author="django",
        content="Welcome to couchdbkit world",
        date=datetime.datetime.utcnow()
    )
    greet.save()
    return HttpResponse("this is greeting")