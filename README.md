https://www.shutterstock.com/
    <div class="container mb-2">
        <div class="row">
            <div class="col s-white-container "></div>
        </div>
        <div class="row">
            <div class="col">
                <hr>
                <h2 class="logo-f text-center mb-4">Your Shopping Bag</h2>
                <hr>
                <br>
                <br>
                <br>
            </div>
        </div>
        <div class="row bg-color">
            <div class="col-6">
                {% if bag_items %}
                    {% for item in bag_items %}
                        <div class="box-container s-box-left">
                            <div class="row">
                                <div class="col">
                                    <img class="bag-img" src="{{ item.product.image.url }}">
                                </div>
                                <div class="col">
                                    <p class="my-0"><strong>{{ item.product.name }}</strong></p>
                                    <p class="my-0 small text-muted">SKU: {{ item.product.sku|upper }}</p>
                                    <p class="my-0">${{ item.product.price }}</p>
                                </div>
                            </div>
                            <br>
                            <div class="row">
                                <div class="col-4">
                                    <p class="my-0"><strong>Size: </strong>{% if item.product.has_sizes %}{{ item.size|upper }}{% else %}N/A{% endif %}</p>
                                </div>
                                <div class="col-4">
                                    <form class="form update-form" method="POST" action="{% url 'adjust_bag' item.item_id %}">
                                        {% csrf_token %}
                                        <div class="form-group">
                                            <div class="input-group">
                                                <div class="input-group-prepend">
                                                    <button class="decrement-qty btn btn-sm btn-black rounded-0" 
                                                        data-item_id="{{ item.item_id }}" id="decrement-qty_{{ item.item_id }}">
                                                        <span>
                                                            <i class="fas fa-minus fa-sm"></i>
                                                        </span>
                                                    </button>
                                                </div>
                                                <input class="form-control form-control-sm qty_input" type="number"
                                                    name="quantity" value="{{ item.quantity }}" min="1" max="99"
                                                    data-item_id="{{ item.item_id }}"
                                                    id="id_qty_{{ item.item_id }}">
                                                <div class="input-group-append">
                                                    <button class="increment-qty btn btn-sm btn-black rounded-0"
                                                        data-item_id="{{ item.item_id }}" id="increment-qty_{{ item.item_id }}">
                                                        <span>
                                                            <i class="fas fa-plus fa-sm"></i>
                                                        </span>
                                                    </button>
                                                </div>
                                                {% if item.product.has_sizes %}
                                                    <input type="hidden" name="product_size" value="{{ item.size }}">
                                                {% endif %}
                                            </div>
                                        </div>
                                    </form>
                                    <a class="update-link text-info"><small>Update</small></a>
                                    <a class="remove-item text-danger float-right" id="remove_{{ item.item_id }}" data-product_size="{{ item.size }}"><small>Remove</small></a>  
                                </div>
                                <div class="col-4">
                                    <p class="my-0">  ${{ item.product.price | calc_subtotal:item.quantity }}</p>
                                </div>
                            </div>
                        </div>
                        <br>   
                    {% endfor %}
                    <br>
                    <div class="col-12 box-container box-up">

                        <h6><strong>Bag Total: ${{ total|floatformat:2 }}</strong></h6>
                        <h6>Delivery: ${{ delivery|floatformat:2 }}</h6>
                        <h4 class="mt-4"><strong>Grand Total: ${{ grand_total|floatformat:2 }}</strong></h4>
                        {% if free_delivery_delta > 0 %}
                            <p class="mb-1 text-danger">
                                You could get free delivery by spending just <strong>${{ free_delivery_delta }}</strong> more!
                            </p>
                        {% endif %}
                        <a href="{% url 'products' %}" class="btn btn-outline-black rounded-0 btn-lg">
                            <span class="icon">
                                <i class="fas fa-chevron-left"></i>
                            </span>
                            <span class="text-uppercase">Keep Shopping</span>
                        </a>
                        <a href="{% url 'checkout' %}" class="btn btn-black rounded-0 btn-lg">
                            <span class="text-uppercase">Secure Checkout</span>
                            <span class="icon">
                                <i class="fas fa-lock"></i>
                            </span>
                        </a>
                    </div>
                {% else %}
                    <p class="lead mb-5">Your bag is empty.</p>
                    <a href="{% url 'products' %}" class="btn btn-outline-black rounded-0 btn-lg">
                        <span class="icon">
                            <i class="fas fa-chevron-left"></i>
                        </span>
                        <span class="text-uppercase">Keep Shopping</span>
                    </a>
                {% endif %}
            </div>
            <div class="col-4 offset-1 box-container box-up">
                <p class="text-muted">Order Summary ({{ product_count }})</p>
                <div class="row">
                <div class="col-7 offset-2">
                    <p class="mb-1 mt-0 small text-muted">Item</p>
                </div>
                <div class="col-3 text-right">
                    <p class="mb-1 mt-0 small text-muted">Subtotal</p>
                </div>
            </div>
            {% for item in bag_items %}
                <div class="row">
                    <div class="col-2 mb-1">
                        <a href="{% url 'product_detail' item.product.id %}">
                            {% if item.product.image %}
                                <img class="w-100" src="{{ item.product.image.url }}" alt="{{ product.name }}">
                            {% else %}
                                <img class="w-100" src="{{ MEDIA_URL }}noimage.png" alt="{{ product.name }}">
                            {% endif %}
                        </a>
                    </div>
                    <div class="col-7">
                        <p class="my-0"><strong>{{ item.product.name }}</strong></p>
                        <p class="my-0 small">Size: {% if item.product.has_sizes %}{{ item.size|upper }}{% else %}N/A{% endif %}</p>
                        <p class="my-0 small text-muted">Qty: {{ item.quantity }}</p>
                    </div>
                    <div class="col-3 text-right">
                        <p class="my-0 small text-muted">${{ item.product.price | calc_subtotal:item.quantity }}</p>
                    </div>
                </div>
            {% endfor %}
            <hr class="my-0">
            <div class="row text-black text-right">
                <div class="col-7 offset-2">
                    <p class="my-0">Order Total:</p>
                    <p class="my-0">Delivery:</p>
                    <p class="my-0">Grand Total:</p>
                </div>
                <div class="col-3">
                    <p class="my-0">${{ total | floatformat:2 }}</p>
                    <p class="my-0">${{ delivery | floatformat:2 }}</p>
                    <p class="my-0"><strong>${{ grand_total | floatformat:2 }}</strong></p>
                </div>
                {% if free_delivery_delta > 0 %}
                    <p class="mb-1 text-danger">
                        You could get free delivery by spending just <strong>${{ free_delivery_delta }}</strong> more!
                    </p>
                {% endif %}
                <a href="{% url 'products' %}" class="btn btn-outline-black rounded-0 btn-lg">
                    <span class="icon">
                        <i class="fas fa-chevron-left"></i>
                    </span>
                    <span class="text-uppercase">Keep Shopping</span>
                </a>
                <a href="{% url 'checkout' %}" class="btn btn-black rounded-0 btn-lg">
                    <span class="text-uppercase">Secure Checkout</span>
                    <span class="icon">
                        <i class="fas fa-lock"></i>
                    </span>
                </a>
            </div>
        </div>
    </div>
    <div class="row">
        <div class="col newsletter">
            <h1 class="text-center"> INSERT NEWS LETTER HERE!</h1>
        </div>
    </div>