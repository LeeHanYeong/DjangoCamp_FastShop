from django.shortcuts import render

from product.models import Category


def index(request):
    root_categories = Category.objects.filter(parent__isnull=True).order_by('priority')
    context = {
        'root_categories': root_categories,
    }
    return render(request, 'etcpage/index.html', context)
