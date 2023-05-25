# Source: allauth/socialaccount/adapter.py

from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount import app_settings
from allauth.socialaccount.models import SocialAccount
from allauth.account.utils import user_email
from allauth.account import app_settings as account_settings
from allauth.utils import email_address_exists
from users.models import User
from django.contrib.auth import login


class MySocialAccountAdapter(DefaultSocialAccountAdapter):

    def is_auto_signup_allowed(self, request, sociallogin):
        # If email is specified, check for duplicate and if so, no auto signup.
        auto_signup = app_settings.AUTO_SIGNUP
        if auto_signup:
            email = user_email(sociallogin.user)
            # Let's check if auto_signup is really possible...
            if email:
                if account_settings.UNIQUE_EMAIL:
                    if email_address_exists(email):
                        # Oops, another user already has this address.
                        # We cannot simply connect this social account
                        # to the existing user. Reason is that the
                        # email address may not be verified, meaning,
                        # the user may be a hacker that has added your
                        # email address to their account in the hope
                        # that you fall in their trap.  We cannot
                        # check on 'email_address.verified' either,
                        # because 'email_address' is not guaranteed to
                        # be verified.
                        auto_signup = False

                        ################## Added #####################

                        # 1: User who alredy has a local account try to
                        # login wiith a new social account.
                        # 2: Log the user as an existing local account here
                        # first.
                        # 3: Then the user will be redirected to the social
                        # signup page.
                        # 4: They will be redirected to home without signing 
                        # up because they're already "loged in!"

                        # NOTE: The user will not be connected to social 
                        # account in this process.
                        user = User.objects.get(email=email)
                        login(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')

                        # Source allauth/socialaccount/views.py ConnectionsView
                        account_data = []
                        for account in SocialAccount.objects.filter(user=self.request.user):
                            provider_account = account.get_provider_account()
                            account_data.append(
                                {
                                    "id": account.pk,
                                    "provider": account.provider,
                                    "name": provider_account.to_str(),
                                }
                            )

                        ################## Added ####################

                        # FIXME: We redirect to signup form -- user will
                        # see email address conflict only after posting
                        # whereas we detected it here already.
            elif app_settings.EMAIL_REQUIRED:
                # Nope, email is required and we don't have it yet...
                auto_signup = False
        return auto_signup