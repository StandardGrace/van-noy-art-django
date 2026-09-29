Project Name
============
Van Noys Visuals

Project Description
====================
Van Noys Visuals is a Django and MySQL web application built as a course
final project, extending a series of earlier staged Django assignments
(project setup, templating, models, product catalogue) into a working
demo for an artist storefront concept.

The site presents a public gallery where visitors can browse artwork —
prints and digital pieces available for direct purchase, and originals
available by inquiry — alongside a small content-management layer where
staff can log in to upload new pieces and track sales. Two staff roles
are supported: an Owner account that can view sales records, and an
Employee account that can upload artwork but cannot view sales, enforced
through Django's built-in Groups and permissions system.

Technologies
============
- Python
- Django
- MySQL
- HTML
- CSS
- JavaScript

How to Run
==========
1. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

2. Create a MySQL database named `student_management` (or update `NAME`
   in `core/settings.py` to match your own).

3. In `core/settings.py`, both `PASSWORD` (under `DATABASES`) and
   `SECRET_KEY` have been left blank and need to be filled in before
   running:
   - Set `PASSWORD` to your own local MySQL password.
   - Generate a new `SECRET_KEY`:
     ```
     python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
     ```
     Paste the output in as the value of `SECRET_KEY`.

4. Apply migrations:
   ```
   python manage.py migrate
   ```

5. Create a superuser account:
   ```
   python manage.py createsuperuser
   ```

6. Run the development server:
   ```
   python manage.py runserver
   ```

7. Visit `http://127.0.0.1:8000/` in a browser.

### Testing the Owner vs. Employee permission split

The superuser account above bypasses all permission checks, so it won't
show this distinction on its own. To see it in action:

1. In Django Admin, under Groups, create:
   - **Owner** — grant "Can view sale"
   - **Employee** — grant nothing
2. Create two regular (non-superuser) accounts, check "Staff status" on
   both, and assign one to each group.
3. Log in as each — both reach Upload Piece; only the Owner-group
   account reaches Sales.

### Adding sample content

Gallery and Home will be empty until at least one Piece exists. Add one
via `/upload/` while logged in as staff, or directly through Django
Admin.

Features
========
- Home page featuring the most recently uploaded artwork piece
- About and Contact pages
- User registration, login, and logout, built on Django's authentication system
- Public artwork gallery with an animated, expandable detail view per piece
- Staff-only page for uploading new artwork, with image upload support
- Sales tracking page with role-based visibility (Owner vs. Employee, via Django Groups and permissions)
- Responsive, mobile-first layout with a collapsible navigation menu
- Product catalogue, carried over from an earlier assignment in the same project
- Django Admin support for managing pieces, sales, and user accounts

Author
======
Patrick Grace