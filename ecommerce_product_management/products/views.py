from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render

from .forms import LoginForm, ProductForm
from .models import Category, Product


def login_view(request):
    if request.user.is_authenticated:
        return redirect("dashboard")

    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("dashboard")

        form.add_error(None, "Invalid username or password.")

    return render(request, "registration/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("login")


@login_required
def dashboard(request):
    context = {
        "total_products": Product.objects.count(),
        "active_products": Product.objects.filter(status="active").count(),
        "inactive_products": Product.objects.filter(status="inactive").count(),
        "low_stock_products": Product.objects.filter(stock__lte=5).count(),
    }
    return render(request, "products/dashboard.html", context)


@login_required
def product_list(request):
    products = Product.objects.select_related("category").all()

    search = request.GET.get("search", "").strip()
    category_id = request.GET.get("category", "")
    status = request.GET.get("status", "")

    if search:
        products = products.filter(
            Q(name__icontains=search) | Q(sku__icontains=search)
        )

    if category_id:
        products = products.filter(category_id=category_id)

    if status in {"active", "inactive"}:
        products = products.filter(status=status)

    paginator = Paginator(products, 8)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        "page_obj": page_obj,
        "categories": Category.objects.all(),
        "search": search,
        "selected_category": category_id,
        "selected_status": status,
    }
    return render(request, "products/product_list.html", context)


@login_required
def product_create(request):
    form = ProductForm(request.POST or None, request.FILES or None)

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Product added successfully.")
        return redirect("product_list")

    return render(request, "products/product_form.html", {
        "form": form,
        "page_title": "Add Product",
        "button_text": "Add Product",
    })


@login_required
def product_detail(request, pk):
    product = get_object_or_404(
        Product.objects.select_related("category"), pk=pk
    )
    return render(request, "products/product_detail.html", {
        "product": product
    })


@login_required
def product_update(request, pk):
    product = get_object_or_404(Product, pk=pk)
    form = ProductForm(
        request.POST or None,
        request.FILES or None,
        instance=product
    )

    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Product updated successfully.")
        return redirect("product_list")

    return render(request, "products/product_form.html", {
        "form": form,
        "page_title": "Edit Product",
        "button_text": "Save Changes",
        "product": product,
    })


@login_required
def product_delete(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == "POST":
        product.delete()
        messages.success(request, "Product deleted successfully.")
        return redirect("product_list")

    return render(request, "products/product_confirm_delete.html", {
        "product": product
    })
