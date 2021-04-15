#urls.py
from django.urls import path, include 
from .views import NewClaim,ClaimList
urlpatterns = [
	path('', Home,name = 'home-page'),
	path('newclaim/',NewClaim,name='newclaim-page'),
	path('claimlist/',ClaimList,name='claimlist-page'),
]