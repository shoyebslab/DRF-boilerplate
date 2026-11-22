import os
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")

import django
django.setup()

from apps.settings.models import TopbarSetting, NavbarItem, SliderSlide


def seed():
    print("Seeding Topbar Setting...")
    topbar, _ = TopbarSetting.objects.get_or_create(id=1)
    topbar.hotline = "+8809611177177"
    topbar.phone_display = "09611-177177"
    topbar.ambulance = "01844-477701"
    topbar.email = "info@starlinehospital.com.bd"
    topbar.address_bn = "মহিপাল, ঢাকা-চট্টগ্রাম মহাসড়ক সংলগ্ন, ফেনী"
    topbar.address_en = "Near Mahipal, Dhaka-Chittagong Highway, Feni, Bangladesh"
    topbar.announcement_bn = "জরুরি বিভাগ ও সার্বক্ষণিক অ্যাম্বুলেন্স সেবা ২৪ ঘণ্টা খোলা"
    topbar.announcement_en = "Emergency Department & Ambulance Services Available 24/7"
    topbar.portal_link = "/login"
    topbar.save()
    print("  - Topbar saved.")

    print("\nSeeding Navbar Items...")
    navbar_items = [
        {"title_bn": "হোম", "title_en": "Home", "href": "/", "order": 1, "is_external": False},
        {"title_bn": "আমাদের সম্পর্কে", "title_en": "About Us", "href": "/about", "order": 2, "is_external": False},
        {"title_bn": "স্বাস্থ্য পরীক্ষা", "title_en": "Health Packages", "href": "/services#packages", "order": 3, "is_external": False},
        {"title_bn": "অভিজ্ঞ চিকিৎসকগণ", "title_en": "Our Doctors", "href": "/services#doctors", "order": 4, "is_external": False},
        {"title_bn": "বিভাগসমূহ", "title_en": "Departments", "href": "/services#departments", "order": 5, "is_external": False},
        {"title_bn": "সেবাসমূহ", "title_en": "Services", "href": "/services", "order": 6, "is_external": False},
        {"title_bn": "অনলাইন রিপোর্ট", "title_en": "Online Report", "href": "https://report.starlinehospital.com.bd", "order": 7, "is_external": True},
        {"title_bn": "যোগাযোগ", "title_en": "Contact", "href": "/contact", "order": 8, "is_external": False},
    ]

    for item in navbar_items:
        nav, created = NavbarItem.objects.update_or_create(
            href=item["href"],
            defaults=item
        )
        print(f"  - [{'Created' if created else 'Updated'}] {nav.title_en} ({nav.title_bn})")

    print("\nSeeding Slider Slides...")
    slides_data = [
        {
            "desktop_image": "/images/carousel/desktop/star-line-specialized-hospital.jpg",
            "mobile_image": "/images/carousel/mobile/star-line-specialized-hospital.jpg",
            "title_bn": "স্টার লাইন স্পেশালাইজড হাসপাতাল",
            "title_en": "Star Line Specialized Hospital",
            "subtitle_bn": "আধুনিক বিশেষায়িত স্বাস্থ্যসেবার বিশ্বস্ত ঠিকানা - ফেনীর মহিপালে আন্তর্জাতিক মানের সেবা",
            "subtitle_en": "Trusted Destination for Advanced Healthcare in Mahipal, Feni",
            "button_text_bn": "অ্যাপয়েন্টমেন্ট নিন",
            "button_text_en": "Book Appointment",
            "button_link": "/contact",
            "order": 1,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/govt-appvd-a-category-hospital.jpg",
            "mobile_image": "/images/carousel/mobile/govt-appvd-a-category-hospital.jpg",
            "title_bn": "সরকারি অনুমোদিত \"এ\" ক্যাটাগরি হাসপাতাল",
            "title_en": "Govt Approved \"A\" Category Hospital",
            "subtitle_bn": "স্বাস্থ্য ও পরিবার কল্যাণ মন্ত্রণালয় কর্তৃক অনুমোদিত সর্বাধুনিক বিশেষায়িত চিকিৎসালয়",
            "subtitle_en": "Recognized and approved high-standard hospital facility in Bangladesh",
            "button_text_bn": "আমাদের সম্পর্কে জানুন",
            "button_text_en": "About Our Facility",
            "button_link": "/about",
            "order": 2,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/carousel-1.jpg",
            "mobile_image": "/images/carousel/mobile/carousel-1.jpg",
            "title_bn": "বিশ্বমানের আধুনিক স্বাস্থ্যসেবা কেন্দ্র",
            "title_en": "Modern Healthcare Facility",
            "subtitle_bn": "অভিজ্ঞ প্রফেসর ও কনসালটেন্ট চিকিৎসকদের নিয়মিত সেবা ও ব্যক্তিগত পরিচর্যা",
            "subtitle_en": "Expert senior consultants, dedicated care, and cutting-edge technology",
            "button_text_bn": "চিকিৎসক তালিকা",
            "button_text_en": "Our Doctors",
            "button_link": "/services#doctors",
            "order": 3,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/carousel-3.jpg",
            "mobile_image": "/images/carousel/mobile/carousel-3.jpg",
            "title_bn": "এনআইসিইউ - নবজাতকের বিশেষ নিবিড় পরিচর্যা কেন্দ্র",
            "title_en": "NICU - Neonatal Intensive Care Unit",
            "subtitle_bn": "নবজাতকের জটিল চিকিৎসার জন্য ২৪ ঘণ্টা বিশেষায়িত পেডিয়াট্রিক ও আইসিইউ টিম",
            "subtitle_en": "Round-the-clock neonatal intensive care by experienced pediatricians",
            "button_text_bn": "সেবাসমূহ দেখুন",
            "button_text_en": "Explore Services",
            "button_link": "/services",
            "order": 4,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/carousel-4.jpg",
            "mobile_image": "/images/carousel/mobile/carousel-4.jpg",
            "title_bn": "২৪/৭ আধুনিক মডেল ফার্মেসী সেবা",
            "title_en": "24/7 Modern Pharmacy Service",
            "subtitle_bn": "১০০% আসল ও সঠিক তাপমাত্রায় সংরক্ষিত দেশি-বিদেশি সকল জীবন রক্ষাকারী ওষুধ",
            "subtitle_en": "Genuine medications stored at strict temperature control 24/7",
            "button_text_bn": "ফার্মেসী যোগাযোগ",
            "button_text_en": "Contact Pharmacy",
            "button_link": "/contact",
            "order": 5,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/carousel-5.jpg",
            "mobile_image": "/images/carousel/mobile/carousel-5.jpg",
            "title_bn": "সর্বাধুনিক ১৬০ স্লাইস সিটিস্ক্যান - রেডিওলোজি বিভাগ",
            "title_en": "160 Slice CT Scan - Radiology & Imaging",
            "subtitle_bn": "দ্রুততম সময়ে অত্যন্ত নিখুঁত ও নির্ভুল হোল-বডি এবং কার্ডিয়াক সিটিস্ক্যান পরীক্ষা",
            "subtitle_en": "Ultra-fast, crystal-clear diagnostic scans with minimal radiation exposure",
            "button_text_bn": "ডায়াগনস্টিক তথ্য",
            "button_text_en": "Diagnostics",
            "button_link": "/services",
            "order": 6,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/carousel-6.jpg",
            "mobile_image": "/images/carousel/mobile/carousel-6.jpg",
            "title_bn": "১.৫ টেসলা এমআরআই মেশিন - রেডিওলোজি বিভাগ",
            "title_en": "1.5 Tesla MRI - Radiology & Imaging",
            "subtitle_bn": "শব্দহীন ও আরামদায়ক পরিবেশে ব্রেন, স্পাইন ও জয়েন্টের উচ্চ রেজোলিউশন স্ক্যান",
            "subtitle_en": "High-field 1.5T MRI providing superior tissue contrast and neuro analysis",
            "button_text_bn": "পরীক্ষার সময়সূচি",
            "button_text_en": "Schedule Test",
            "button_link": "/contact",
            "order": 7,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/carousel-7.jpg",
            "mobile_image": "/images/carousel/mobile/carousel-7.jpg",
            "title_bn": "সিসিইউ - আধুনিক করোনারি কেয়ার ইউনিট",
            "title_en": "CCU - Modern Coronary Care Unit",
            "subtitle_bn": "হৃদরোগে আক্রান্ত রোগীদের জরুরি সেবা ও কেন্দ্রীয় মনিটরিং সুবিধাযুক্ত নিবিড় সেবা",
            "subtitle_en": "Comprehensive critical cardiac care with centralized hemodynamic monitors",
            "button_text_bn": "জরুরি হটলাইন",
            "button_text_en": "Emergency Hotline",
            "button_link": "tel:+8809611177177",
            "order": 8,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/carousel-8.jpg",
            "mobile_image": "/images/carousel/mobile/carousel-8.jpg",
            "title_bn": "নিউরোকেয়ার বিভাগ - ব্রেন ও নার্ভ বিশেষজ্ঞ সেবা",
            "title_en": "Neurocare Center - Advanced Brain & Spine",
            "subtitle_bn": "অভিজ্ঞ নিউরোলজিস্ট ও নিউরোসার্জনদের সমন্বয়ে আন্তর্জাতিক মানের চিকিৎসা",
            "subtitle_en": "Expert brain, spine and nervous system treatment with specialized rehab",
            "button_text_bn": "পরামর্শ নিন",
            "button_text_en": "Consultation",
            "button_link": "/contact",
            "order": 9,
            "is_active": True,
        },
        {
            "desktop_image": "/images/carousel/desktop/carousel-9.jpg",
            "mobile_image": "/images/carousel/mobile/carousel-9.jpg",
            "title_bn": "বিএমডি - বোন মিনারেল ডেনসিটি টেস্ট",
            "title_en": "BMD - Bone Mineral Density Test",
            "subtitle_bn": "হাড়ের ঘনত্ব ও অস্টিওপোরোসিস রোগ নির্ণয়ে ফেনী অঞ্চলের প্রথম সর্বাধুনিক বিএমডি",
            "subtitle_en": "Gold standard DEXA bone densitometry for precise osteoporosis detection",
            "button_text_bn": "প্যাকেজসমূহ দেখুন",
            "button_text_en": "Health Packages",
            "button_link": "/services#packages",
            "order": 10,
            "is_active": True,
        },
    ]

    for s in slides_data:
        slide, created = SliderSlide.objects.update_or_create(
            order=s["order"],
            defaults=s
        )
        print(f"  - [{'Created' if created else 'Updated'}] Slide {slide.order}: {slide.title_en}")

    print("\nSite settings seeding complete!")


if __name__ == "__main__":
    seed()
