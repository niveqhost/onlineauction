from django.contrib.auth import get_user_model

def create_admin_user():
    try:
        username = "admin"
        email = "admin@admin.gmail.com"
        password = "admin123"
        User = get_user_model()
        user = User.objects.create_user(username, email, password)
        user.check_password(password)
        user.is_active = 1
        user.is_staff = 1
        user.is_superuser = 1
        user.is_email_verified = 1
        user.save()
        print("Create admin user ... OK")
    except Exception as ex:
        print("CREATE ADMIN USER ERROR: ", ex)

def create_user():
    try:
        username = "seller1"
        email = "seller1@.gmail.com"
        password = "seller1_sell"
        User = get_user_model()
        user = User.objects.create_user(username, email, password)
        user.check_password(password)
        user.is_active = 0
        user.is_staff = 0
        user.is_superuser = 0
        user.save()
        print("Create user ... OK")
    except Exception as ex:
        print("CREATE USER ERROR: ", ex)

create_admin_user()




