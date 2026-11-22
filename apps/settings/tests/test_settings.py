from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.settings.models import (
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

User = get_user_model()


class SettingsAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.admin = User.objects.create_superuser(
            username="adminuser",
            email="admin@starline.com",
            password="AdminPassword123!",
        )
        self.topbar = TopbarSetting.objects.create(
            id=1,
            hotline="+8809611177177",
            phone_display="09611-177177",
            ambulance="01844-477701",
            email="info@starlinehospital.com.bd",
        )
        self.nav_item = NavbarItem.objects.create(
            title_bn="হোম",
            title_en="Home",
            href="/",
            order=1,
        )
        self.slide = SliderSlide.objects.create(
            desktop_image="/images/carousel/desktop/carousel-1.jpg",
            title_bn="টেস্ট স্লাইড",
            title_en="Test Slide",
            order=1,
        )
        self.department = Department.objects.create(
            name_en="Cardiology & CCU",
            name_bn="কার্ডিওলজি ও সিসিইউ",
            doctor_count=5,
            order=1,
        )
        self.doctor = Doctor.objects.create(
            name_en="Dr. Test Doctor",
            name_bn="ডা. টেস্ট ডাক্তার",
            specialization_en="Cardiologist",
            specialization_bn="কার্ডিওলজিস্ট",
            image_path="/images/doctors/dr-birendra-nath-bhattacharya.jpg",
            bmdc_number="A-12345",
            order=1,
        )
        self.facility = ClinicalFacility.objects.create(
            title_en="Cardiac Tests & Heart Care",
            title_bn="কার্ডিয়াক পরীক্ষা",
            icon_name="HeartPulse",
            order=1,
        )
        self.package = HealthPackage.objects.create(
            name_en="Basic Health Checkup",
            name_bn="বেসিক হেলথ চেকআপ",
            target_audience_en="General",
            target_audience_bn="সাধারণ",
            original_price=2000,
            discounted_price=1500,
            features_list_en=["CBC", "FBS"],
            features_list_bn=["সিবিসি", "এফবিএস"],
            order=1,
        )

    def test_get_combined_site_settings_public(self):
        response = self.client.get("/api/v1/settings/all/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("topbar", response.data)
        self.assertIn("navbar", response.data)
        self.assertIn("slides", response.data)
        self.assertIn("departments", response.data)
        self.assertIn("doctors", response.data)
        self.assertIn("facilities", response.data)
        self.assertIn("packages", response.data)
        self.assertEqual(response.data["topbar"]["phone_display"], "09611-177177")
        self.assertEqual(len(response.data["navbar"]), 1)
        self.assertEqual(len(response.data["slides"]), 1)
        self.assertEqual(len(response.data["departments"]), 1)
        self.assertEqual(len(response.data["doctors"]), 1)
        self.assertEqual(len(response.data["facilities"]), 1)
        self.assertEqual(len(response.data["packages"]), 1)

    def test_update_topbar_settings_authenticated(self):
        self.client.force_authenticate(user=self.admin)
        payload = {"phone_display": "09611-999999"}
        response = self.client.put("/api/v1/settings/topbar/", payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.topbar.refresh_from_db()
        self.assertEqual(self.topbar.phone_display, "09611-999999")

    def test_create_slider_slide_authenticated(self):
        self.client.force_authenticate(user=self.admin)
        payload = {
            "desktop_image": "/images/carousel/desktop/carousel-2.jpg",
            "title_bn": "নতুন স্লাইড",
            "title_en": "New Slide",
            "order": 2,
        }
        response = self.client.post("/api/v1/settings/slider/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(SliderSlide.objects.filter(title_en="New Slide").exists())

    def test_create_department_authenticated(self):
        self.client.force_authenticate(user=self.admin)
        payload = {
            "name_en": "Neurology",
            "name_bn": "নিউরোমেডিসিন",
            "doctor_count": 3,
            "order": 2,
            "is_active": True,
        }
        response = self.client.post("/api/v1/settings/departments/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Department.objects.filter(name_en="Neurology").exists())

    def test_create_facility_authenticated(self):
        self.client.force_authenticate(user=self.admin)
        payload = {
            "title_en": "Dialysis Unit",
            "title_bn": "ডায়ালাইসিস ইউনিট",
            "icon_name": "Activity",
            "order": 2,
            "is_active": True,
        }
        response = self.client.post("/api/v1/settings/facilities/", payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(ClinicalFacility.objects.filter(title_en="Dialysis Unit").exists())

    def test_create_package_authenticated(self):
        self.client.force_authenticate(user=self.admin)
        payload = {
            "name_en": "Executive Checkup",
            "name_bn": "এক্সিকিউটিভ চেকআপ",
            "target_audience_en": "Corporate",
            "target_audience_bn": "কর্পোরেট",
            "original_price": 5000,
            "discounted_price": 3800,
            "features_list_en": ["ECG", "CBC"],
            "features_list_bn": ["ইসিজি", "সিবিসি"],
            "order": 2,
            "is_active": True,
        }
        response = self.client.post("/api/v1/settings/packages/", payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(HealthPackage.objects.filter(name_en="Executive Checkup").exists())
