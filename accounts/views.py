from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import TemplateView, FormView, UpdateView
from accounts.forms import UserRegistrationForm, UserUpdateForm
from django.contrib.auth import get_user_model, login
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from accounts.token import account_activation_token

User = get_user_model()


class ProfileView(TemplateView):
    template_name = 'accounts/profile.html'


class UserRegistrationView(FormView):
    template_name = 'registration/registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        user = form.save(commit=False)
        user.email = form.cleaned_data['email']
        user.set_password(form.cleaned_data['password'])
        user.is_active = False
        user.is_leader = True
        user.save()
        current_site = get_current_site(self.request)
        subject = 'Activate your account'
        message = render_to_string('registration/account_activation_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': account_activation_token.make_token(user),
        })
        user.email_user(subject=subject, message=message)
        return super().form_valid(form)


class UserUpdateView(UpdateView):
    template_name = 'accounts/update.html'
    form_class = UserUpdateForm
    model = User
    success_url = reverse_lazy('accounts:profile')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        return redirect(reverse_lazy('accounts:login'))
    else:
        return render(request, 'registration/activation_invalid.html')
