from django.shortcuts import render
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = "base.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

def about(request):
    tags = ["обучение", "программирование", "python", "oop"]
    return render(
        request,
        "about.html",
        context={"tags": tags},
    )
    
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.shortcuts import redirect, render


def index(request):
    return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        next_url = (
            request.POST.get("next")
            or request.GET.get("next")
            or request.META.get("HTTP_REFERER")
            or "index"
        )

        user, created = User.objects.get_or_create(username="testuser")
        login(request, user)
        return redirect(next_url)

    return redirect(request.META.get("HTTP_REFERER", "index"))


def logout_view(request):
    next_url = request.META.get("HTTP_REFERER") or "index"
    logout(request)
    return redirect(next_url)
