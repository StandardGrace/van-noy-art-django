from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Student, Product, Piece, Sale

# Display the home page, featuring the most recently added piece
def home(request):
    latest_piece = Piece.objects.order_by("-created_at").first()
    return render(request, "pages/home.html", {"latest_piece": latest_piece})

# Display the about us page
def about(request):
    return render(request, "pages/about.html")

# Display the contact us page
def contact(request):
    return render(request, "pages/contact.html")

# Display the student registration form and save submitted data
def add_student(request):
    if request.method == "POST":
        # Extract form data from request.POST and create a Student object
        student = Student(
            student_name=request.POST.get("student_name"),
            student_age=request.POST.get("student_age"),
            student_city=request.POST.get("student_city"),
            student_email=request.POST.get("student_email"),
            student_phone=request.POST.get("student_phone"),
            student_subject=request.POST.get("student_subject"),
            student_grade=request.POST.get("student_grade"),
            student_hobby=request.POST.get("student_hobby"),
            student_address=request.POST.get("student_address"),
            enrollment_year=request.POST.get("enrollment_year"),
        )
        student.save()
        return redirect("student_list")

    return render(request, "pages/student_form.html")

# Retrieve all students from the database and display them
def student_list(request):
    students = Student.objects.all()
    return render(request, "pages/student_list.html", {"students": students})

# Retrieve all products from the database and display them to site visitors
def product_list(request):
    products = Product.objects.all()
    return render(request, "pages/product_list.html", {"products": products})

# Retrieve all pieces from the database and display them to site visitors
def gallery(request):
    pieces = Piece.objects.all().order_by("-created_at")
    return render(request, "pages/gallery.html", {"pieces": pieces})

# Display the piece upload form and save submitted data (staff only)
@login_required
def upload_piece(request):
    if not request.user.is_staff:
        messages.error(request, "You do not have permission to upload pieces.")
        return redirect("gallery")

    if request.method == "POST":
        piece = Piece(
            title=request.POST.get("title"),
            content=request.POST.get("content"),
            author=request.user.username,
            price=request.POST.get("price") or None,
            image=request.FILES.get("image"),
            is_original=request.POST.get("is_original") == "on",
        )
        piece.save()
        return redirect("gallery")

    return render(request, "pages/piece_form.html")

# Display sales records (visible only to users with the view_sale permission)
@login_required
def sales(request):
    if not request.user.has_perm('pages.view_sale'):
        messages.error(request, "You do not have permission to view sales.")
        return redirect("gallery")

    sale_records = Sale.objects.all().order_by("-sale_date")
    return render(request, "pages/sales.html", {"sales": sale_records})

# Display the registration form and create a new user account
def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "pages/register.html", {"form": form})


# Display the login form and authenticate the user
def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, "pages/login.html")


# Log the current user out and end their session
def logout_user(request):
    logout(request)
    return redirect("login")