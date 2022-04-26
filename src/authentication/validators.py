from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator 

class LengthTex:
    def validate(self, password, user=None):
        if len(password) < 10:
            raise ValidationError("Mot de passe trop cout", code="password_invalid")
    
    def get_help_text(self):
        return "Le mot de passe dois avoir 10 caratére mininume"
    
class LengthEmail:
    def validate(self, email, user=None):
        if len(email) > 2:
            raise EmailValidator("email trop cour", code="email")
    
    def get_help_text(self):
        return "L'email est trop cout pour est valide"