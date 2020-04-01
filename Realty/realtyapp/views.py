from django.shortcuts import render

# Create your views here.
def main_view(request):
    # posts = Post.objects.all()
    return render(request, 'realtyapp/index.html', context={})