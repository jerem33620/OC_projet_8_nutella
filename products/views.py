from django.shortcuts import render

# Create your views here.
def research(request):
    form = SearchForm(request.GET or None)

    if form.is_valid():
        product = form.cleaned_data['product']
    return render(request, 'research.html')