from django.contrib import admin
from import_export.admin import ExportMixin, ImportExportModelAdmin
from .models import Category, Service, ServiceField, ConsultationRequest
from import_export import resources

admin.site.site_header = "Fintrix Administration"
admin.site.site_title = "Fintrix Admin Portal"
admin.site.index_title = "Welcome to Fintrix Admin Panel"

# ==========================
# Resource Classes for Import/Export
# ==========================
class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class ServiceResource(resources.ModelResource):
    class Meta:
        model = Service

class ConsultationRequestResource(resources.ModelResource):
    class Meta:
        model = ConsultationRequest

# ==========================
# Admin Panel Configuration
# ==========================

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource
    list_display = ("name",)
    search_fields = ("name",)


class ServiceFieldInline(admin.TabularInline):
    model = ServiceField
    extra = 1  


@admin.register(Service)
class ServiceAdmin(ImportExportModelAdmin):
    resource_class = ServiceResource
    list_display = ("name", "category", "base_price", "is_active", "is_deleted")
    search_fields = ("name", "category__name")
    list_filter = ("category", "is_active", "is_deleted")
    inlines = [ServiceFieldInline]


@admin.register(ConsultationRequest)
class ConsultationRequestAdmin(ImportExportModelAdmin):
    resource_class = ConsultationRequestResource
    list_display = ("name", "email", "mobile_number", "service", "whatsapp_opt_in", "created_at")
    search_fields = ("name", "email", "mobile_number", "service__name")
    list_filter = ("whatsapp_opt_in", "created_at")
    readonly_fields = ("created_at",)  
