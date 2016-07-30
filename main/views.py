from django.shortcuts import render
from django.views.generic import View

class Home(View):
	def get(self,request):
		template_name = 'home.html'
		user = request.user
		return render(request,template_name, {'usuario':user})
