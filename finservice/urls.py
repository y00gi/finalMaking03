from django.urls import path
from .views import HomePageView, service_list, service_detail, ContactPageView, AboutPageView, PrivacyPageView, HelpPageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("services/", service_list, name="services"),
    path("services/<int:service_id>/", service_detail, name="service_detail"),
    path("contact/", ContactPageView.as_view(), name="contact"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("privacy/", PrivacyPageView.as_view(), name="privacy"),
    path("help/", HelpPageView.as_view(), name="help"),
    ]