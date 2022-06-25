from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend

class PhoneAuthBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        if username is None:
            username = kwargs['phone']
            # username = kwargs.get(UserModel.phone)
            # username = UserModel.objects.get(phone=username)
            
        if username is None or password is None:
            return
        try:
            user = UserModel._default_manager.get(phone=username)
        except UserModel.DoesNotExist:
            # Run the default password hasher once to reduce the timing
            # difference between an existing and a nonexistent user (#20760).
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user

# class PhoneAuthBackend(ModelBackend):
    # def authenticate(self, request, username=None, password=None, **kwargs):
    #     UserModel = get_user_model()
    #     try:
    #         user = UserModel.objects.get(phone=username)
    #     except UserModel.DoesNotExist:
    #         return None
    #     else:
    #         if user.check_password(password):
    #             return user
    #     return None
