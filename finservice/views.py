from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Service, ConsultationRequest
from django.views.generic import TemplateView
from .forms import ConsultationForm

# Create your views here.
class HomePageView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.prefetch_related("services").all()  # Load categories with services
        return context
    
    def post(self, request, *args, **kwargs):
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)  # Save the form but don’t commit to DB yet
            if not consultation.city_or_pincode:  # If field is empty, set it to None
                consultation.city_or_pincode = None
            if not consultation.service:  # If no service is selected, allow it to be null
                consultation.service = None
            consultation.save()  # Save to DB
            return redirect("home")  # Redirect to the homepage after saving
        return render(request, self.template_name, {"form": form, "categories": Category.objects.prefetch_related("services").all()})

def service_list(request):
    categories = Category.objects.prefetch_related("services").all()
    return render(request, "finservice/services.html", {"categories": categories})

def service_detail(request, service_id):
    service = get_object_or_404(Service, id=service_id)

    if request.method == "POST":
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.service = service  # Associate the service
            consultation.save()
            return redirect("service_detail", service_id=service_id)  # Redirect after submission
    else:
        form = ConsultationForm()

    return render(request, "finservice/service_detail.html", {"service": service, "form": form})

class ContactPageView(TemplateView):
    template_name = "finservice/contact.html"

    def post(self, request, *args, **kwargs):
        form = ConsultationForm(request.POST)
        if form.is_valid():
            consultation = form.save(commit=False)
            consultation.save()  # Save the form data
            return redirect("contact")  # Redirect to the same page after submission

        # If form is not valid, render the page again with errors
        return render(request, self.template_name, {"form": form})

    def get(self, request, *args, **kwargs):
        form = ConsultationForm()
        return render(request, self.template_name, {"form": form})
    
class AboutPageView(TemplateView):
    template_name = "finservice/about.html"

class PrivacyPageView(TemplateView):
    template_name = "finservice/privacy.html"

class HelpPageView(TemplateView):
    template_name = "finservice/help.html"