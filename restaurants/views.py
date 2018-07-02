from django.shortcuts import render

# Create your views here.
def some_function(request):
	context = {
	"msg":"Hello World!",
	}
	return render(request, "test.html", context)
