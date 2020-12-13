from .models import Category

def product_categories(request):
    categories = Category.objects.all()
    return {'categories': categories}