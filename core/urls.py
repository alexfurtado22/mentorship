from allauth.account.views import SignupView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("mentor/", include("app.urls")),  # Your app's URLs
    path("", SignupView.as_view(), name="account_signup"),
    path("account/signup/", RedirectView.as_view(url="/")),
    path("accounts/", include("allauth.urls")),
]

# Debug Toolbar & Media Files in Development
if settings.DEBUG:
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        path("__reload__/", include("django_browser_reload.urls")),
    ]

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
