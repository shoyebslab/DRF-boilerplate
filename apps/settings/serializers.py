from rest_framework import serializers

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


class TopbarSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopbarSetting
        fields = [
            "id",
            "hotline",
            "phone_display",
            "ambulance",
            "email",
            "address_bn",
            "address_en",
            "announcement_bn",
            "announcement_en",
            "facebook_url",
            "youtube_url",
            "portal_link",
            "updated_at",
        ]


class NavbarItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavbarItem
        fields = [
            "id",
            "title_bn",
            "title_en",
            "href",
            "order",
            "is_active",
            "is_external",
            "is_button",
            "created_at",
            "updated_at",
        ]


class SliderSlideSerializer(serializers.ModelSerializer):
    class Meta:
        model = SliderSlide
        fields = [
            "id",
            "desktop_image",
            "mobile_image",
            "title_bn",
            "title_en",
            "subtitle_bn",
            "subtitle_en",
            "button_text_bn",
            "button_text_en",
            "button_link",
            "order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = [
            "id",
            "name_bn",
            "name_en",
            "subtitle_bn",
            "subtitle_en",
            "description_bn",
            "description_en",
            "icon_name",
            "doctor_count",
            "dept_url",
            "order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [
            "id",
            "name_bn",
            "name_en",
            "specialization_bn",
            "specialization_en",
            "qualification_bn",
            "qualification_en",
            "institute_bn",
            "institute_en",
            "bmdc_number",
            "image_path",
            "department_name",
            "profile_url",
            "order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class ClinicalFacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicalFacility
        fields = [
            "id",
            "title_bn",
            "title_en",
            "subtitle_bn",
            "subtitle_en",
            "description_bn",
            "description_en",
            "icon_name",
            "read_more_url",
            "order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class HealthPackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthPackage
        fields = [
            "id",
            "name_bn",
            "name_en",
            "target_audience_bn",
            "target_audience_en",
            "original_price",
            "discounted_price",
            "is_popular",
            "features_list_bn",
            "features_list_en",
            "details_url",
            "order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class HealthCardNoticeSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthCardNotice
        fields = [
            "id",
            "badge_text_bn",
            "badge_text_en",
            "title_bn",
            "title_en",
            "subtitle_bn",
            "subtitle_en",
            "verify_url",
            "benefits_url",
            "is_active",
            "updated_at",
        ]


class NewsBlogItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsBlogItem
        fields = [
            "id",
            "item_type",
            "category",
            "title_bn",
            "title_en",
            "summary_bn",
            "summary_en",
            "published_date",
            "slug",
            "order",
            "is_active",
            "created_at",
            "updated_at",
        ]


class CombinedSiteSettingsSerializer(serializers.Serializer):
    topbar = TopbarSettingSerializer()
    navbar = NavbarItemSerializer(many=True)
    slides = SliderSlideSerializer(many=True)
    departments = DepartmentSerializer(many=True)
    doctors = DoctorSerializer(many=True)
    facilities = ClinicalFacilitySerializer(many=True)
    packages = HealthPackageSerializer(many=True)
    health_card = HealthCardNoticeSerializer()
    news = NewsBlogItemSerializer(many=True)
    blogs = NewsBlogItemSerializer(many=True)
