from django.db import models

# Create your models here.

class Student(models.Model):
    student_name = models.CharField(max_length=150)
    student_age = models.IntegerField()
    student_city = models.CharField(max_length=150)
    student_email = models.EmailField()
    student_phone = models.CharField(max_length=20)
    student_subject = models.CharField(max_length=100)
    student_grade = models.CharField(max_length=20)
    student_hobby = models.CharField(max_length=100)
    student_address = models.CharField(max_length=200)
    enrollment_year = models.IntegerField()

class Product(models.Model):
    product_name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField(upload_to='products/')
    category = models.CharField(max_length=100)

class Piece(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    price = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='pieces/', blank=True, null=True)
    is_original = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Sale(models.Model):
    piece = models.ForeignKey(Piece, on_delete=models.CASCADE)
    buyer_name = models.CharField(max_length=200)
    buyer_contact = models.CharField(max_length=200)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    sale_date = models.DateTimeField(auto_now_add=True)
    sale_type = models.CharField(
        max_length=20,
        choices=[('online', 'Online Sale'), ('inquiry', 'Original Inquiry')]
    )

    def __str__(self):
        return f"{self.piece.title} - {self.buyer_name}"