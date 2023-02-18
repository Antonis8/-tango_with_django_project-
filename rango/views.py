from django.shortcuts import render
from rango.models import Category, Page

# Create your views here.

from django.http import HttpResponse

def show_category(request, category_name_slug):
    context_dict = {}
    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
    
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:

        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    return render(request, 'rango/category.html', context=context_dict)



def index(request):

    category_list = Category.objects.order_by('-likes')[:5]
    pages_list = Page.objects.order_by('-views')[:5]
    context_dict = {}
    context_dict['boldmessage']=  'Crunchy, creamy, cookie, candy, cupcake!' #boldmessage will become crunchy etc
    context_dict["categories"] = category_list
    context_dict['pages'] = pages_list
    
    return render(request, 'rango/index.html', context= context_dict)

    
def about(request):
    
    context_dict= {'boldmessage':  'This tutorial has been put together by Antonis'}
    return render(request, 'rango/about.html', context= context_dict)
    #return HttpResponse("Rango says here is the about page. <a href='/rango/'>Index</a>")