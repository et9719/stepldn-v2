''' Imports '''
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages

from products.models import Product


def view_bag(request):
    """ A view that renders the bag contents page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the shopping bag """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    size = None
    # if the item in the bag has a size, size is equal to the product_size.
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        if item_id in list(bag.keys()):
            # if item with same size is already in bag
            # and user adds another, update current item.
            if size in bag[item_id]['items_by_size'].keys():
                bag[item_id]['items_by_size'][size] += quantity
                messages.success(
                    request,
                    f'Updated size {size.upper()} {product.name}' +
                    f'quantity to {bag[item_id]["items_by_size"][size]}'
                )
            #  if item with same size is not already in the bag,
            #  add item to bag.
            else:
                bag[item_id]['items_by_size'][size] = quantity
                messages.success(
                    request,
                    f'Added size {size.upper()} {product.name} to your bag'
                )
        # if item is in bag but not the same size add this as new item.
        else:
            bag[item_id] = {'items_by_size': {size: quantity}}
            messages.success(
                request,
                f'Added size {size.upper()} {product.name} to your bag'
            )
    else:
        # if item is in bag but doesnt have a size, update items quantity
        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
            )
        # if item has no size and is not in bag, add to bag
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {product.name} to your bag')

    request.session['bag'] = bag
    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the specified amount"""

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    size = None
    if 'product_size' in request.POST:
        size = request.POST['product_size']
    bag = request.session.get('bag', {})

    if size:
        # if the item has a size and is already in the bag update size/quantity
        if quantity > 0:
            bag[item_id]['items_by_size'][size] = quantity
            messages.success(
                request,
                f'Updated size {size.upper()} {product.name}' +
                f'quantity to {bag[item_id]["items_by_size"][size]}'
            )
        # remove item form bag
        else:
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
            )
    else:
        # if item has no size, adjust quantity.
        if quantity > 0:
            bag[item_id] = quantity
            messages.success(
                request,
                f'Updated {product.name} quantity to {bag[item_id]}'
            )
        # remove item
        else:
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

    request.session['bag'] = bag
    return redirect(reverse('view_bag'))


def remove_from_bag(request, item_id):
    """Remove the item from the shopping bag"""

    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if 'product_size' in request.POST:
            size = request.POST['product_size']
        bag = request.session.get('bag', {})

        if size:
            # delete item with size
            del bag[item_id]['items_by_size'][size]
            if not bag[item_id]['items_by_size']:
                bag.pop(item_id)
            messages.success(
                request,
                f'Removed size {size.upper()} {product.name} from your bag'
            )
        else:
            # delete item with no size
            bag.pop(item_id)
            messages.success(request, f'Removed {product.name} from your bag')

        request.session['bag'] = bag
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(request, f'Error removing item: {e}')
        return HttpResponse(status=500)
