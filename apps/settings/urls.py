from django.urls import path

from .views import (
    ClinicalFacilityDetailView,
    ClinicalFacilityListCreateView,
    CombinedSiteSettingsView,
    DepartmentDetailView,
    DepartmentListCreateView,
    DoctorDetailView,
    DoctorListCreateView,
    HealthCardNoticeView,
    HealthPackageDetailView,
    HealthPackageListCreateView,
    NavbarItemDetailView,
    NavbarItemListCreateView,
    NewsBlogItemDetailView,
    NewsBlogItemListCreateView,
    SliderSlideDetailView,
    SliderSlideListCreateView,
    TopbarSettingView,
)

urlpatterns = [
    # Single combined query for fast frontend hydration
    path("all/", CombinedSiteSettingsView.as_view(), name="settings-all"),

    # Topbar Settings
    path("topbar/", TopbarSettingView.as_view(), name="settings-topbar"),

    # Navbar Items
    path("navbar/", NavbarItemListCreateView.as_view(), name="settings-navbar-list"),
    path("navbar/<int:pk>/", NavbarItemDetailView.as_view(), name="settings-navbar-detail"),

    # Slider / Carousel Slides
    path("slider/", SliderSlideListCreateView.as_view(), name="settings-slider-list"),
    path("slider/<int:pk>/", SliderSlideDetailView.as_view(), name="settings-slider-detail"),

    # Departments
    path("departments/", DepartmentListCreateView.as_view(), name="settings-departments-list"),
    path("departments/<int:pk>/", DepartmentDetailView.as_view(), name="settings-departments-detail"),

    # Doctors
    path("doctors/", DoctorListCreateView.as_view(), name="settings-doctors-list"),
    path("doctors/<int:pk>/", DoctorDetailView.as_view(), name="settings-doctors-detail"),

    # Clinical Facilities / Services
    path("facilities/", ClinicalFacilityListCreateView.as_view(), name="settings-facilities-list"),
    path("facilities/<int:pk>/", ClinicalFacilityDetailView.as_view(), name="settings-facilities-detail"),

    # Health Packages
    path("packages/", HealthPackageListCreateView.as_view(), name="settings-packages-list"),
    path("packages/<int:pk>/", HealthPackageDetailView.as_view(), name="settings-packages-detail"),

    # Health Card Facility
    path("health-card/", HealthCardNoticeView.as_view(), name="settings-health-card"),

    # News & Blogs
    path("news-blogs/", NewsBlogItemListCreateView.as_view(), name="settings-news-blogs-list"),
    path("news-blogs/<int:pk>/", NewsBlogItemDetailView.as_view(), name="settings-news-blogs-detail"),
]
