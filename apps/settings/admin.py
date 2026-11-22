from django.contrib import admin

from .models import (
    ClinicalFacility,
    Department,
    Doctor,
    HealthCardNotice,
    HealthPackage,
    NavbarItem,
    NewsBlogItem,
    SliderSlide,
    TopbarSetting,
)


@admin.register(TopbarSetting)
class TopbarSettingAdmin(admin.ModelAdmin):
    list_display = ["phone_display", "ambulance", "email", "updated_at"]


@admin.register(NavbarItem)
class NavbarItemAdmin(admin.ModelAdmin):
    list_display = ["order", "title_en", "title_bn", "href", "is_active", "is_external"]
    list_display_links = ["title_en"]
    list_editable = ["order", "is_active"]
    search_fields = ["title_en", "title_bn", "href"]


@admin.register(SliderSlide)
class SliderSlideAdmin(admin.ModelAdmin):
    list_display = ["order", "title_en", "title_bn", "is_active", "updated_at"]
    list_display_links = ["title_en"]
    list_editable = ["order", "is_active"]
    search_fields = ["title_en", "title_bn"]


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["order", "name_en", "name_bn", "doctor_count", "is_active"]
    list_display_links = ["name_en"]
    list_editable = ["order", "is_active"]
    search_fields = ["name_en", "name_bn"]


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ["order", "name_en", "name_bn", "specialization_en", "is_active"]
    list_display_links = ["name_en"]
    list_editable = ["order", "is_active"]
    search_fields = ["name_en", "name_bn", "specialization_en", "bmdc_number"]


@admin.register(ClinicalFacility)
class ClinicalFacilityAdmin(admin.ModelAdmin):
    list_display = ["order", "title_en", "title_bn", "is_active"]
    list_display_links = ["title_en"]
    list_editable = ["order", "is_active"]
    search_fields = ["title_en", "title_bn"]


@admin.register(HealthPackage)
class HealthPackageAdmin(admin.ModelAdmin):
    list_display = ["order", "name_en", "discounted_price", "original_price", "is_popular", "is_active"]
    list_display_links = ["name_en"]
    list_editable = ["order", "is_active"]
    search_fields = ["name_en", "name_bn"]


@admin.register(HealthCardNotice)
class HealthCardNoticeAdmin(admin.ModelAdmin):
    list_display = ["title_en", "is_active", "updated_at"]


@admin.register(NewsBlogItem)
class NewsBlogItemAdmin(admin.ModelAdmin):
    list_display = ["order", "item_type", "title_en", "category", "published_date", "is_active"]
    list_display_links = ["title_en"]
    list_editable = ["order", "is_active"]
    search_fields = ["title_en", "title_bn", "category"]
