from django.conf.urls import url
import main_page
from main_page import views

urlpatterns = [
    url(r'^main/', main_page.views.blog),
]
