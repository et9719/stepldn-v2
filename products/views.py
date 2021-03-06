''' Imports '''
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Product, Category
from .forms import ProductForm, ReviewForm


def all_products(request):
    """ A view to show all products, including sorting and search queries """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        # get products using sort key
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

    if request.GET:
        # get products just in certain category.
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

    if request.GET:
        # get products using search bar
        if 'q' in request.GET:
            query = request.GET['q']
            # if nothing matches what was searched show error message.
            if not query:
                messages.error(
                    request,
                    "You didn't enter any search criteria!"
                    )
                return redirect(reverse('products'))

            queries = Q(
                name__icontains=query
                ) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


def product_detail(request, product_id):
    """ A view to show individual product details """
    # get product
    product = get_object_or_404(Product, pk=product_id)
    reviews = product.reviews.filter(active=True)
    new_review = None
    # Reviews posted
    if request.method == 'POST':
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():

            # Create Review object but don't save to database yet
            new_review = review_form.save(commit=False)
            # Assign the current post to the comment
            new_review.product = product
            # Save the comment to the database
            new_review.save()
    else:
        review_form = ReviewForm()

    context = {
        'product': product,
        'reviews': reviews,
        'new_review': new_review,
        'review_form': review_form
    }
    # return products context
    return render(request, 'products/product_detail.html', context)


@login_required
def add_product(request):
    """ Add a product to the store """
    # if user is not admin show error message
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        # if form is filled out correctly save
        # product and show success message.
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # if form is invalid show error message.
            messages.error(request, 'Failed to add product. \
                Please ensure the form is valid.')
    else:
        form = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    # if user is not admin show error message.
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    # get product
    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        # if form is edited correctly save form and show success message.
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            # if form is invalid show error message.
            messages.error(request, 'Failed to update product.\
                 Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    # if user is not admin show error message.
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    # get product
    product = get_object_or_404(Product, pk=product_id)
    # delete product
    product.delete()
    # show success message.
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))
