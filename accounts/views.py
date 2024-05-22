from django.shortcuts import render

# Create your views here.
def home_screen_view(request):
	# chat_history = Message_manager.objects.all()
	# context={}
	# context['some_text'] = 'some text from view'
	# context['chat_history'] = chat_history
	return render(request, "base.html")