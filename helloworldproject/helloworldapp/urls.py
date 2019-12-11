from django.urls import path
from .views import hellofunction

urlpatterns = [
    # project側のhello/とurls.pyにhelloworldapp.urlsと書いてあるので、hello/worldが呼ばれると
    path('world/', hellofunction),
]
