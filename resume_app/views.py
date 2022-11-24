from django.shortcuts import render
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent


def homePageView(request):
    #using guide at https://pypi.org/project/django-user-agents/
    user_agent = get_user_agent(request)
    if user_agent.is_mobile:
        return render(request, "home_mobile.html")
    else:
        return render(request, "home.html")

