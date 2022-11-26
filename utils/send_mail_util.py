from django.contrib.auth.tokens import PasswordResetTokenGenerator

import six
import threading

#? Chua biet cai nay de lam gi
class EmailThread(threading.Thread):
    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)
    def run(self):
        self.email.send()

#* Sinh ma token - Mot nguoi dung chi co mot ma token duy nhat
class TokenGenerator(PasswordResetTokenGenerator):
    def _make_hash_value(self, user, timestamp):
        return (six.text_type(user.pk)+six.text_type(timestamp)+six.text_type(user.is_email_verified))

generate_token = TokenGenerator()