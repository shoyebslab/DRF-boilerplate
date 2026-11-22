from django.db import models


class TopbarSetting(models.Model):
    """
    Website topbar configuration (single record).
    """
    hotline = models.CharField(max_length=50, default="+8809611177177")
    phone_display = models.CharField(max_length=50, default="09611-177177")
    ambulance = models.CharField(max_length=50, default="01844-477701")
    email = models.EmailField(default="info@starlinehospital.com.bd")
    address_bn = models.CharField(
        max_length=255,
        default="মহিপাল, ঢাকা-চট্টগ্রাম মহাসড়ক সংলগ্ন, ফেনী"
    )
    address_en = models.CharField(
        max_length=255,
        default="Near Mahipal, Dhaka-Chittagong Highway, Feni, Bangladesh"
    )
    announcement_bn = models.CharField(
        max_length=255,
        default="জরুরি বিভাগ ও সার্বক্ষণিক অ্যাম্বুলেন্স সেবা ২৪ ঘণ্টা খোলা"
    )
    announcement_en = models.CharField(
        max_length=255,
        default="Emergency Department & Ambulance Services Available 24/7"
    )
    facebook_url = models.URLField(blank=True, default="https://facebook.com")
    youtube_url = models.URLField(blank=True, default="https://youtube.com")
    portal_link = models.CharField(max_length=100, default="/login")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Topbar Setting"
        verbose_name_plural = "Topbar Settings"

    def __str__(self):
        return f"Topbar: {self.phone_display} ({self.email})"

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(id=1)
        return obj


class NavbarItem(models.Model):
    """
    Navigation bar links with multilingual support.
    """
    title_bn = models.CharField(max_length=100)
    title_en = models.CharField(max_length=100)
    href = models.CharField(max_length=255)
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_external = models.BooleanField(default=False)
    is_button = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Navbar Item"
        verbose_name_plural = "Navbar Items"

    def __str__(self):
        return f"{self.order}. {self.title_en} ({self.title_bn}) -> {self.href}"


class SliderSlide(models.Model):
    """
    Hero banner carousel slide.
    """
    desktop_image = models.CharField(
        max_length=255,
        default="/images/carousel/desktop/star-line-specialized-hospital.jpg"
    )
    mobile_image = models.CharField(
        max_length=255,
        blank=True,
        default=""
    )
    title_bn = models.CharField(max_length=200)
    title_en = models.CharField(max_length=200)
    subtitle_bn = models.TextField(blank=True, default="")
    subtitle_en = models.TextField(blank=True, default="")
    button_text_bn = models.CharField(max_length=100, default="বিস্তারিত দেখুন")
    button_text_en = models.CharField(max_length=100, default="Learn More")
    button_link = models.CharField(max_length=255, default="/contact")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Slider Slide"
        verbose_name_plural = "Slider Slides"

    def __str__(self):
        return f"{self.order}. {self.title_en}"


class Department(models.Model):
    """
    Hospital clinical department.
    """
    name_bn = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    subtitle_bn = models.CharField(max_length=255, blank=True, default="")
    subtitle_en = models.CharField(max_length=255, blank=True, default="")
    description_bn = models.TextField(blank=True, default="")
    description_en = models.TextField(blank=True, default="")
    icon_name = models.CharField(max_length=50, default="Building2")
    doctor_count = models.IntegerField(default=1)
    dept_url = models.CharField(max_length=150, blank=True, default="")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Department"
        verbose_name_plural = "Departments"

    def __str__(self):
        return f"{self.name_en} ({self.name_bn})"


class Doctor(models.Model):
    """
    Specialist medical doctor / consultant.
    """
    name_bn = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    specialization_bn = models.CharField(max_length=200)
    specialization_en = models.CharField(max_length=200)
    qualification_bn = models.TextField(blank=True, default="")
    qualification_en = models.TextField(blank=True, default="")
    institute_bn = models.CharField(max_length=200, default="স্টার লাইন স্পেশালাইজড হাসপাতাল")
    institute_en = models.CharField(max_length=200, default="Star Line Specialized Hospital")
    bmdc_number = models.CharField(max_length=50, blank=True, default="")
    image_path = models.CharField(max_length=255, default="/images/doctors/slsh.jpg")
    department_name = models.CharField(max_length=100, blank=True, default="")
    profile_url = models.CharField(max_length=255, blank=True, default="")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

    def __str__(self):
        return f"{self.name_en} - {self.specialization_en}"


class ClinicalFacility(models.Model):
    """
    Diagnostic and clinical facility service.
    """
    title_bn = models.CharField(max_length=150)
    title_en = models.CharField(max_length=150)
    subtitle_bn = models.CharField(max_length=255, blank=True, default="")
    subtitle_en = models.CharField(max_length=255, blank=True, default="")
    description_bn = models.TextField(blank=True, default="")
    description_en = models.TextField(blank=True, default="")
    icon_name = models.CharField(max_length=50, default="Activity")
    read_more_url = models.CharField(max_length=255, default="/services")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Clinical Facility"
        verbose_name_plural = "Clinical Facilities"

    def __str__(self):
        return f"{self.title_en} ({self.title_bn})"


class HealthPackage(models.Model):
    """
    Preventive health checkup package.
    """
    name_bn = models.CharField(max_length=150)
    name_en = models.CharField(max_length=150)
    target_audience_bn = models.CharField(max_length=100, default="পুরুষ, মহিলা | প্রাপ্তবয়স্ক")
    target_audience_en = models.CharField(max_length=100, default="Male, Female | Adult")
    original_price = models.IntegerField(default=6000)
    discounted_price = models.IntegerField(default=5500)
    is_popular = models.BooleanField(default=True)
    features_list_bn = models.JSONField(default=list, blank=True)
    features_list_en = models.JSONField(default=list, blank=True)
    details_url = models.CharField(max_length=255, default="/services#packages")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "id"]
        verbose_name = "Health Package"
        verbose_name_plural = "Health Packages"

    def __str__(self):
        return f"{self.name_en} (৳{self.discounted_price})"


class HealthCardNotice(models.Model):
    """
    Star Line Health Care Card Facility banner.
    """
    badge_text_bn = models.CharField(max_length=100, default="বিশেষ ছাড় ও সুবিধা")
    badge_text_en = models.CharField(max_length=100, default="Special Discounts & Privileges")
    title_bn = models.CharField(max_length=200, default="স্টার লাইন হেলথ কেয়ার কার্ড সুবিধা")
    title_en = models.CharField(max_length=200, default="Star Line Health Care Card Facility")
    subtitle_bn = models.TextField(
        default="আমাদের অফিশিয়াল হেলথ কার্ডে ডায়াগনস্টিক টেস্ট, রোগী ভর্তি এবং ওপিডি সেবায় বিশেষ ছাড় উপভোগ করুন।"
    )
    subtitle_en = models.TextField(
        default="Enjoy valuable discounts on diagnostic tests, hospital admissions, and OPD services with our official Health Care Card."
    )
    verify_url = models.CharField(max_length=255, default="/contact#card-verification")
    benefits_url = models.CharField(max_length=255, default="/about#card-facility")
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Health Card Notice"
        verbose_name_plural = "Health Card Notices"

    @classmethod
    def get_solo(cls):
        obj, _ = cls.objects.get_or_create(id=1)
        return obj


class NewsBlogItem(models.Model):
    """
    Health awareness blog post or hospital news & event.
    """
    ITEM_TYPES = [
        ("blog", "Health Awareness Blog"),
        ("news", "Hospital News & Event"),
    ]
    item_type = models.CharField(max_length=10, choices=ITEM_TYPES, default="blog")
    category = models.CharField(max_length=50, default="Health")
    title_bn = models.CharField(max_length=255)
    title_en = models.CharField(max_length=255)
    summary_bn = models.TextField(blank=True, default="")
    summary_en = models.TextField(blank=True, default="")
    published_date = models.CharField(max_length=30, default="2026-11-20")
    slug = models.SlugField(max_length=200, blank=True, default="")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["order", "-id"]
        verbose_name = "News & Blog Item"
        verbose_name_plural = "News & Blog Items"

    def __str__(self):
        return f"[{self.item_type}] {self.title_en}"
