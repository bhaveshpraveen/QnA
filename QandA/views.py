from django.shortcuts import render
from django.views.generic.base import View
from django.contrib import messages
from .models import QuestionAndAnswers


class Response(View):

    def get(self, request):
        return render(request, 'base.html', {})

    def post(self, request, *args, **kwargs):
        user_name = request.POST.get('user')
        answer = request.POST.get('answer')
        QuestionAndAnswers.objects.create(user=user_name, answer=answer)
        messages.success(request, 'Your answer was saved successfully')
        return render(request, 'base.html', {'username': user_name})