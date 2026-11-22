import os
import sys
from pathlib import Path
import django

# Setup django environment
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.development")
django.setup()

from apps.settings.models import (
    Department,
    Doctor,
    ClinicalFacility,
    HealthPackage,
    HealthCardNotice,
    NewsBlogItem,
)

def seed_departments():
    print("Seeding Departments...")
    depts = [
        {
            "name_bn": "অ্যানেস্থেসিওলজি",
            "name_en": "Anesthesiology",
            "subtitle_bn": "নিরাপদ ও আধুনিক অ্যানেস্থেশিয়া সেবায় বিশেষ কেয়ার",
            "subtitle_en": "Safe and modern anesthesia care with dedicated specialists",
            "description_bn": "নিরাপদ ও আধুনিক অ্যানেস্থেশিয়া সেবায় বিশেষায়িত কেয়ার ও অপারেশন পরবর্তী নিবিড় পর্যবেক্ষণ।",
            "description_en": "Safe and modern anesthesia care with advanced perioperative life support.",
            "icon_name": "ShieldAlert",
            "doctor_count": 1,
            "dept_url": "anesthesiology",
            "order": 1,
        },
        {
            "name_bn": "ব্রেস্ট সার্জারি",
            "name_en": "Breast Surgery",
            "subtitle_bn": "স্তনজনিত চিকিৎসায় ও নিবিড় পরিচর্যা সেবা",
            "subtitle_en": "Specialized breast healthcare and surgical oncology",
            "description_bn": "স্তনজনিত সকল রোগের আধুনিক সার্জারি ও নিবিড় পরিচর্যা সেবা।",
            "description_en": "Specialized breast healthcare, mammography, and benign & oncological breast surgery.",
            "icon_name": "HeartHandshake",
            "doctor_count": 4,
            "dept_url": "breast-surgery",
            "order": 2,
        },
        {
            "name_bn": "ক্যান্সার কেয়ার",
            "name_en": "Cancer Care",
            "subtitle_bn": "ক্যান্সার চিকিৎসায় ও নিবিড় পরিচর্যা সেবা",
            "subtitle_en": "Comprehensive oncology screening and supportive therapies",
            "description_bn": "ক্যান্সার রোগ নির্ণয়, কেমোথেরাপি ও উপশমকারী চিকিৎসার সমন্বিত কেয়ার।",
            "description_en": "Comprehensive medical oncology, chemotherapy daycare, and multidisciplinary cancer board.",
            "icon_name": "Cross",
            "doctor_count": 1,
            "dept_url": "cancer-care",
            "order": 3,
        },
        {
            "name_bn": "কার্ডিয়াক ভাস্কুলার সার্জারি",
            "name_en": "Cardiac Vascular Surgery",
            "subtitle_bn": "বক্ষ, কার্ডিওভাস্কুলার ও থোরাসিক রোগের আধুনিক চিকিৎসায় বিশেষজ্ঞ কেয়ার",
            "subtitle_en": "Advanced thoracic and cardiovascular surgical procedures",
            "description_bn": "বক্ষ, কার্ডিওভাস্কুলার ও থোরাসিক রোগের আধুনিক চিকিৎসায় অভিজ্ঞ সার্জনদের তত্ত্বাবধানে সেবা।",
            "description_en": "Cardiovascular and thoracic vascular surgeries performed with international standard protocols.",
            "icon_name": "HeartPulse",
            "doctor_count": 2,
            "dept_url": "cardiac-vascular-surgery",
            "order": 4,
        },
        {
            "name_bn": "কার্ডিওলজি (হৃদরোগ বিভাগ)",
            "name_en": "Cardiology",
            "subtitle_bn": "হৃদরোগ চিকিৎসায় ও নিবিড় পরিচর্যা সেবা",
            "subtitle_en": "Comprehensive non-invasive & clinical cardiac treatment",
            "description_bn": "২৪ ঘণ্টা ক্যাথ ল্যাব, সিসিইউ, ইকোকার্ডিওগ্রাম ও অভিজ্ঞ ইন্টারভেনশনাল কার্ডিওলজিস্ট।",
            "description_en": "Full diagnostic non-invasive cardiac evaluation, 24/7 CCU, and specialized heart failure management.",
            "icon_name": "Heart",
            "doctor_count": 9,
            "dept_url": "cardiology",
            "order": 5,
        },
        {
            "name_bn": "কার্ডিওলজি (ইন্টারভেনশনাল)",
            "name_en": "Cardiology (Interventional)",
            "subtitle_bn": "অত্যাধুনিক প্রযুক্তিতে কম অস্ত্রোপচারে হৃদরোগের নিরাময় সেবা",
            "subtitle_en": "Coronary angiography, angioplasty and stenting care",
            "description_bn": "আধুনিক ক্যাথ ল্যাবে এনজিওগ্রাম, রিং পরানো (এনজিওপ্লাস্টি) ও পেসমেকার প্রতিস্থাপন।",
            "description_en": "State-of-the-art flat-panel Cath Lab providing coronary angiography and primary percutaneous intervention.",
            "icon_name": "Activity",
            "doctor_count": 1,
            "dept_url": "cardiology-interventional",
            "order": 6,
        },
        {
            "name_bn": "চাইল্ড ডেভেলপমেন্ট সেন্টার",
            "name_en": "Child Development",
            "subtitle_bn": "শিশুদের শারীরিক, মানসিক ও সামাজিক বিকাশের জন্য বিশেষজ্ঞ সেবা",
            "subtitle_en": "Pediatric developmental screening and rehabilitation",
            "description_bn": "অটিজম, স্পিচ থেরাপি, অকুপেশনাল থেরাপি ও বিশেষ চাহিদাসম্পন্ন শিশুদের সমন্বিত সেবা।",
            "description_en": "Comprehensive child development therapies, sensory integration, and behavioral assessments.",
            "icon_name": "Baby",
            "doctor_count": 1,
            "dept_url": "child-development",
            "order": 7,
        },
        {
            "name_bn": "ক্লিনিক্যাল হেমাটোলজি",
            "name_en": "Clinical Hematology",
            "subtitle_bn": "রক্ত, রক্তশূন্যতা ও লিম্ফোমা রোগের আধুনিক চিকিৎসা কেন্দ্র",
            "subtitle_en": "Expert hematology and blood disorder diagnostics",
            "description_bn": "রক্তস্বল্পতা, থ্যালাসেমিয়া, ব্লাড ক্যান্সার ও লিম্ফোমা রোগের সর্বাধুনিক চিকিৎসা।",
            "description_en": "Diagnostic bone marrow aspiration, leukemia workup, thalassemia counseling, and blood disorder clinic.",
            "icon_name": "Droplets",
            "doctor_count": 2,
            "dept_url": "clinical-hematology",
            "order": 8,
        },
    ]

    Department.objects.all().delete()
    for d in depts:
        Department.objects.create(**d)
    print(f"  - Created {len(depts)} departments.")

def seed_doctors():
    print("Seeding Doctors...")
    docs = [
        {
            "name_bn": "অধ্যাপক ডাঃ বীরেন্দ্র নাথ ভট্টাচার্য্য",
            "name_en": "Prof. Dr. Birendra Nath Bhattacharjee",
            "specialization_bn": "কার্ডিওলজিস্ট, সিনিয়র কনসালট্যান্ট, হার্ট ফেল ও পেসমেকার বিশেষজ্ঞ ও সার্জন",
            "specialization_en": "Cardiologist & Heart Failure Specialist",
            "qualification_bn": "এমবিবিএস, এফসিপিএস (মেডিসিন), পিএইচডি (কার্ডিওলজি), এফএসিপি (ইউএসএ), এফএসিসি",
            "qualification_en": "MBBS, FCPS (Med), PhD (Cardiology), FACP (USA), FACC",
            "institute_bn": "স্টার লাইন স্পেশালাইজড হাসপাতাল",
            "institute_en": "Star Line Specialized Hospital",
            "bmdc_number": "A-18492",
            "image_path": "/images/doctors/dr-birendra-nath-bhattacharya.jpg",
            "department_name": "Cardiology",
            "profile_url": "/doctors/prof-dr-birendra-nath",
            "order": 1,
        },
        {
            "name_bn": "অধ্যাপক ডাঃ মোহাম্মদ খোরশেদ আলম",
            "name_en": "Prof. Dr. Mohammad Khorshed Alam",
            "specialization_bn": "ল্যাপারোস্কপিক, কোলোরেক্টাল, জেনারেল ও প্লাস্টিক সার্জন",
            "specialization_en": "Laparoscopic, Colorectal & General Surgeon",
            "qualification_bn": "এমবিবিএস, এফসিপিএস (সার্জারি), এমএস, এফআইসিএস (ইউএসএ)",
            "qualification_en": "MBBS, FCPS (Surgery), MS, FICS (USA)",
            "institute_bn": "শহীদ সোহরাওয়ার্দী মেডিকেল কলেজ ও হাসপাতাল",
            "institute_en": "Shaheed Suhrawardy Medical College",
            "bmdc_number": "A-21045",
            "image_path": "/images/doctors/dr-md-humayun-kabir-bhuiyan.jpg",
            "department_name": "General Surgery",
            "profile_url": "/doctors/prof-dr-khorshed-alam",
            "order": 2,
        },
        {
            "name_bn": "অধ্যাপিকা ডাঃ তাহমিনা সিদ্দিকা",
            "name_en": "Prof. Dr. Tahmina Siddika",
            "specialization_bn": "স্ত্রী, প্রসূতি, বন্ধ্যাত্ব ও আল্ট্রাসাউন্ড বিশেষজ্ঞ সার্জন",
            "specialization_en": "Gynecologist, Obstetrician & Infertility Specialist",
            "qualification_bn": "এমবিবিএস, এফসিপিএস (অবস ও গাইনি), ডিজিও, এফআইসিএস",
            "qualification_en": "MBBS, FCPS (Obs & Gynae), DGO, FICS",
            "institute_bn": "চট্টগ্রাম মেডিকেল কলেজ ও হাসপাতাল",
            "institute_en": "Chittagong Medical College Hospital",
            "bmdc_number": "A-15490",
            "image_path": "/images/doctors/prof-dr-tahmina-siddika.jpg",
            "department_name": "Gynaecology & Obstetrics",
            "profile_url": "/doctors/prof-dr-tahmina-siddika",
            "order": 3,
        },
        {
            "name_bn": "চৈতী ভট্ট",
            "name_en": "Chaiti Bhattacharjee",
            "specialization_bn": "সিনিয়র অকুপেশনাল ও চাইল্ড ডেভেলপমেন্ট থেরাপিস্ট",
            "specialization_en": "Senior Occupational & Pediatric Therapist",
            "qualification_bn": "বিএসসি (অনার্স) ইন অকুপেশনাল থেরাপি (ডিইউ), পিজিডি ইন অটিজম",
            "qualification_en": "BSc (Hons) in Occupational Therapy (DU), PGD",
            "institute_bn": "স্টার লাইন চাইল্ড ডেভেলপমেন্ট সেন্টার",
            "institute_en": "Star Line Child Development Center",
            "bmdc_number": "CRP-842",
            "image_path": "/images/doctors/chaiti-bhattacharjee.jpg",
            "department_name": "Child Development",
            "profile_url": "/doctors/chaiti-bhattacharjee",
            "order": 4,
        },
        {
            "name_bn": "ডাঃ আর.এম. ফররুখহোদা (জুয়েল)",
            "name_en": "Dr. R.M. Farrukhhoda Jewel",
            "specialization_bn": "নিউরোলজি ও নিউরোমেডিসিন বিশেষজ্ঞ",
            "specialization_en": "Neurology & Neuro-Medicine Specialist",
            "qualification_bn": "এমবিবিএস (ডিইউ), বিসিএস (স্বাস্থ্য), এমডি (নিউরোলজি)",
            "qualification_en": "MBBS (DU), BCS (Health), MD (Neurology)",
            "institute_bn": "জাতীয় নিউরোসায়েন্সেস ইনস্টিটিউট ও হাসপাতাল",
            "institute_en": "National Institute of Neurosciences",
            "bmdc_number": "A-38914",
            "image_path": "/images/doctors/dr-asm-badruddoza-jewel.jpg",
            "department_name": "Neurology",
            "profile_url": "/doctors/dr-farrukhhoda-jewel",
            "order": 5,
        },
        {
            "name_bn": "ডাঃ আশিস আহসান",
            "name_en": "Dr. Asish Ahsan",
            "specialization_bn": "প্লাস্টিক এবং কসমেটিক ও বার্ন সার্জন",
            "specialization_en": "Plastic, Cosmetic & Burn Surgeon",
            "qualification_bn": "এমবিবিএস, এফসিপিএস (প্লাস্টিক সার্জারি)",
            "qualification_en": "MBBS, FCPS (Plastic Surgery)",
            "institute_bn": "ঢাকা মেডিকেল কলেজ ও হাসপাতাল",
            "institute_en": "Dhaka Medical College Hospital",
            "bmdc_number": "A-41209",
            "image_path": "/images/doctors/dr-ashraful-haque.jpg",
            "department_name": "Plastic Surgery",
            "profile_url": "/doctors/dr-asish-ahsan",
            "order": 6,
        },
        {
            "name_bn": "ডাঃ আমিনুল ইসলাম",
            "name_en": "Dr. Aminul Islam",
            "specialization_bn": "নাক-কান-গলা রোগ বিশেষজ্ঞ ও হেড-নেক সার্জন",
            "specialization_en": "ENT & Head-Neck Surgeon",
            "qualification_bn": "এমবিবিএস, এফসিপিএস (ইএনটি), এমএস (ওটোল্যারিঙ্গোলজি)",
            "qualification_en": "MBBS, FCPS (ENT), MS (Otolaryngology)",
            "institute_bn": "স্টার লাইন স্পেশালাইজড হাসপাতাল",
            "institute_en": "Star Line Specialized Hospital",
            "bmdc_number": "A-29402",
            "image_path": "/images/doctors/Dr.Aminul-Islam.jpg",
            "department_name": "ENT & Head-Neck",
            "profile_url": "/doctors/dr-aminul-islam",
            "order": 7,
        },
        {
            "name_bn": "ডাঃ আসাদুল হক",
            "name_en": "Dr. Asadul Haque",
            "specialization_bn": "ইউরোলজি বিশেষজ্ঞ এবং কিডনি ও মূত্রনালী সার্জন",
            "specialization_en": "Urologist & Endourology Surgeon",
            "qualification_bn": "এমবিবিএস, এমএস (ইউরোলজি)",
            "qualification_en": "MBBS, MS (Urology)",
            "institute_bn": "স্যার সলিমুল্লাহ মেডিকেল কলেজ ও মিটফোর্ড হাসপাতাল",
            "institute_en": "Sir Salimullah Medical College Hospital",
            "bmdc_number": "A-33215",
            "image_path": "/images/doctors/Dr-Sujit-Kumar-Saha.jpg",
            "department_name": "Urology",
            "profile_url": "/doctors/dr-asadul-haque",
            "order": 8,
        },
    ]

    Doctor.objects.all().delete()
    for doc in docs:
        Doctor.objects.create(**doc)
    print(f"  - Created {len(docs)} doctors.")

def seed_facilities():
    print("Seeding Clinical Facilities...")
    facilities = [
        {
            "title_bn": "কার্ডিয়াক টেস্টসমূহ",
            "title_en": "Cardiac Tests",
            "subtitle_bn": "অত্যাধুনিক প্রযুক্তিতে নির্ভরযোগ্য কার্ডিয়াক ডায়াগনস্টিক",
            "subtitle_en": "Advanced and Accurate Cardiac Diagnostic Tests",
            "description_bn": "স্টার লাইন স্পেশালাইজড হাসপাতালে কার্ডিয়াক টেস্ট বিভাগে হৃদরোগ নির্ণয়ে আধুনিক ও নির্ভুল পরীক্ষা প্রদান করে। ডিজিটাল ইসিজি, ইকোকার্ডিওগ্রাফি এবং ইটিটি পরীক্ষা অভিজ্ঞ কার্ডিওলজিস্টদের সরাসরি তত্ত্বাবধানে সম্পন্ন হয়।",
            "description_en": "Accurate non-invasive cardiac evaluation including digital 12-lead ECG, 4D Color Doppler Echocardiography, and Treadmill ETT testing supervised by senior consultants.",
            "icon_name": "HeartPulse",
            "read_more_url": "/services#cardiac-tests",
            "order": 1,
        },
        {
            "title_bn": "ডায়াগনস্টিক সেবা",
            "title_en": "Diagnosis Services",
            "subtitle_bn": "আধুনিক প্রযুক্তির নির্ভুল ও দ্রুততম রোগ নির্ণয়",
            "subtitle_en": "Accurate and Fast Diagnosis with Advanced Technology",
            "description_bn": "স্টার লাইন স্পেশালাইজড হাসপাতালে ডায়াগনস্টিক সেবা বিভাগে রোগ নির্ণয়ে আধুনিক ও দ্রুততম সময়ে সেবা প্রদান করে। ডিজিটাল এক্স-রে, আল্ট্রাসনোগ্রাফি ও হিস্টোপ্যাথলজি পরীক্ষার নির্ভরযোগ্য ঠিকানা।",
            "description_en": "Fast and precise diagnostic modalities featuring high-frequency digital X-Ray, high-resolution Color Doppler USG, and specialized histopathology.",
            "icon_name": "Scan",
            "read_more_url": "/services#diagnosis-services",
            "order": 2,
        },
        {
            "title_bn": "জরুরি ও ভর্তি সেবা",
            "title_en": "Emergency & Admission Services",
            "subtitle_bn": "২৪/৭ সার্বক্ষণিক জরুরি কেয়ার ও নিরাপদ ভর্তি সুবিধা",
            "subtitle_en": "24/7 Advanced Emergency Care and Safe Admission Facilities",
            "description_bn": "স্টার লাইন স্পেশালাইজড হাসপাতালে জরুরি ও ভর্তি সেবা বিভাগে রোগীদের জন্য ২৪/৭ সার্বক্ষণিক জরুরি চিকিৎসা সেবা, ডেডিকেটেড ট্রমা টিম ও আইসিইউ অন-কল সুবিধা প্রস্তুত রয়েছে।",
            "description_en": "Round-the-clock emergency desk, immediate critical triage, emergency resuscitation, and streamlined VIP and general inpatient admissions.",
            "icon_name": "Siren",
            "read_more_url": "/services#emergency-admission",
            "order": 3,
        },
        {
            "title_bn": "ফাংশনাল ইমেজিং",
            "title_en": "Functional Imaging",
            "subtitle_bn": "নির্ভুল ও স্পষ্ট উচ্চক্ষমতাসম্পন্ন ইমেজিং সেবা",
            "subtitle_en": "Functional and Accurate Diagnostic Tests",
            "description_bn": "স্টার লাইন স্পেশালাইজড হাসপাতালে ফাংশনাল টেস্ট বিভাগে হৃদরোগ, স্নায়ু ও অঙ্গপ্রত্যঙ্গের কর্মক্ষমতা যাচাইয়ে আধুনিক প্রযুক্তি ব্যবহার করা হয়।",
            "description_en": "Comprehensive physiological organ imaging and hemodynamic assessments ensuring deep clinical insight.",
            "icon_name": "Activity",
            "read_more_url": "/services#functional-imaging",
            "order": 4,
        },
        {
            "title_bn": "আধুনিক ল্যাবরেটরি",
            "title_en": "Modern Laboratory",
            "subtitle_bn": "স্বয়ংক্রিয় অ্যানালাইজার ও আন্তর্জাতিক মানের রিপোর্ট",
            "subtitle_en": "Advanced Technology with Accurate Diagnostic Results",
            "description_bn": "স্টার লাইন স্পেশালাইজড হাসপাতালে আধুনিক ল্যাবরেটরি বিভাগে উন্নত প্রযুক্তি, আন্তর্জাতিক মানের যন্ত্রপাতি এবং দক্ষ বায়োকেমিস্ট ও মাইক্রোবায়োলজিস্টদের দ্বারা পরীক্ষা সম্পন্ন হয়।",
            "description_en": "Fully automated clinical biochemistry, immunoassay, hematology, and microbiological culturing guaranteeing clinical reproducibility.",
            "icon_name": "FlaskConical",
            "read_more_url": "/services#laboratory",
            "order": 5,
        },
        {
            "title_bn": "নিউরো ডায়াগনস্টিকস",
            "title_en": "Neuro Diagnostics",
            "subtitle_bn": "মস্তিষ্ক ও স্নায়ুরোগ নির্ণয়ে সর্বাধুনিক প্রযুক্তি",
            "subtitle_en": "Advanced and Accurate Diagnostic of Neurological Disorders",
            "description_bn": "নিউরো ডায়াগনস্টিক বিভাগে মস্তিষ্ক, স্নায়ু ও মাংসপেশীর রোগের রোগ নির্ণয়ের জন্য আধুনিক ডিজিটাল ইইজি (EEG), ইএমজি (EMG) ও নার্ভ কন্ডাকশন স্টাডি সুবিধা রয়েছে।",
            "description_en": "Specialized electroencephalography (EEG), electromyography (EMG), and nerve conduction velocity (NCV) diagnostics for comprehensive neurological evaluation.",
            "icon_name": "Brain",
            "read_more_url": "/services#neuro-diagnostics",
            "order": 6,
        },
    ]

    ClinicalFacility.objects.all().delete()
    for f in facilities:
        ClinicalFacility.objects.create(**f)
    print(f"  - Created {len(facilities)} facilities.")

def seed_packages():
    print("Seeding Health Packages...")
    packages = [
        {
            "name_bn": "বেসিক হেলথ চেক-আপ",
            "name_en": "Basic Health Check-up",
            "target_audience_bn": "পুরুষ, মহিলা | প্রাপ্তবয়স্ক",
            "target_audience_en": "Male, Female | Adult",
            "original_price": 6000,
            "discounted_price": 5500,
            "is_popular": True,
            "features_list_bn": [
                "কমপ্লিট ব্লাড কাউন্ট (CBC + ESR)",
                "ফাস্টিং ব্লাড সুগার (FBS)",
                "লিপিড প্রোফাইল (রক্তে চর্বির মাত্রা)",
                "সিরাম ক্রিয়েটিনিন (কিডনি পরীক্ষা)",
                "এসজিপিটি (SGPT - লিভার পরীক্ষা)",
                "ইউরিন আর/ই (Urine R/E)",
                "ডিজিটাল চেস্ট এক্স-রে",
                "১২-লিড ইসিজি (ECG)",
            ],
            "features_list_en": [
                "Complete Blood Count (CBC + ESR)",
                "Fasting Blood Sugar (FBS)",
                "Lipid Profile (Cholesterol Panel)",
                "Serum Creatinine (Kidney Function)",
                "SGPT / ALT (Liver Function)",
                "Urine Routine Examination",
                "Digital Chest X-Ray",
                "12-Lead Resting ECG",
            ],
            "order": 1,
        },
        {
            "name_bn": "এক্সিকিউটিভ হেলথ চেক-আপ (পুরুষ)",
            "name_en": "Executive Health Check-up (Male)",
            "target_audience_bn": "পুরুষ | বয়স ৪০ বছর পর্যন্ত",
            "target_audience_en": "Male | Up to 40 Years",
            "original_price": 6700,
            "discounted_price": 5600,
            "is_popular": True,
            "features_list_bn": [
                "সিবিসি এবং পেরিফেরাল ব্লাড ফিল্ম",
                "এইচবিএওয়ানসি (HbA1c - ৩ মাসের সুগার)",
                "সম্পূর্ণ লিপিড প্রোফাইল",
                "সিরাম ইউরিক অ্যাসিড ও ইলেক্ট্রোলাইট",
                "লিভার ফাংশন টেস্ট (LFT)",
                "সিরাম ক্রিয়েটিনিন ও ইউরিয়া",
                "ইউএসজি হোল অ্যাবডোমেন",
                "কার্ডিয়াক ইসিজি ও পরামর্শ",
            ],
            "features_list_en": [
                "CBC with Peripheral Blood Film",
                "HbA1c (3-Month Glycemic Average)",
                "Complete Fasting Lipid Profile",
                "Serum Uric Acid & Electrolytes",
                "Liver Function Panel (LFT)",
                "Kidney Function (Creatinine & Urea)",
                "USG Whole Abdomen with PVR",
                "Cardiology Consultation & ECG",
            ],
            "order": 2,
        },
        {
            "name_bn": "এক্সিকিউটিভ হেলথ চেক-আপ (মহিলা)",
            "name_en": "Executive Health Check-up (Female)",
            "target_audience_bn": "মহিলা | বয়স ৪০ বছর পর্যন্ত",
            "target_audience_en": "Female | Up to 40 Years",
            "original_price": 10000,
            "discounted_price": 8700,
            "is_popular": True,
            "features_list_bn": [
                "সিবিসি ও আয়রন প্রোফাইল",
                "থাইরয়েড ফাংশন টেস্ট (TSH, FT4)",
                "এইচবিএওয়ানসি ও ফাস্টিং সুগার",
                "সিরাম ক্যালসিয়াম ও ভিটামিন ডি",
                "ইউএসজি পেলভিস ও হোল অ্যাবডোমেন",
                "প্যাপ স্মিয়ার ও ব্রেস্ট স্ক্রীনিং",
                "কিডনি ও লিভার ফাংশন টেস্ট",
                "গাইনি বিশেষজ্ঞের সাথে কনসালটেশন",
            ],
            "features_list_en": [
                "CBC with Total Iron Profile",
                "Thyroid Function (TSH, Free T4)",
                "HbA1c & Fasting Glucose",
                "Serum Calcium & Vitamin D3",
                "USG Pelvis & Whole Abdomen",
                "Pap Smear & Clinical Breast Exam",
                "Renal & Hepatic Profiles",
                "Gynecologist Consultation",
            ],
            "order": 3,
        },
        {
            "name_bn": "এক্সিকিউটিভ হেলথ চেক-আপ (পুরুষ - সিনিয়র)",
            "name_en": "Executive Health Check-up (Male)",
            "target_audience_bn": "পুরুষ | বয়স ৪০ বছরের ঊর্ধ্বে",
            "target_audience_en": "Male | Above 40 Years",
            "original_price": 10500,
            "discounted_price": 9000,
            "is_popular": True,
            "features_list_bn": [
                "সম্পূর্ণ মেটাবলিক ও কার্ডিয়াক প্যানেল",
                "পিএসএ (PSA - প্রোস্টেট স্ক্রীনিং)",
                "এইচবিএওয়ানসি ও লিপিড প্রোফাইল",
                "ইকোকার্ডিওগ্রাফি (Echo 4D)",
                "ইউএসজি হোল অ্যাবডোমেন ও প্রোস্টেট",
                "সিরাম ইলেক্ট্রোলাইট ও ক্রিয়েটিনিন",
                "ডিজিটাল চেস্ট এক্স-রে ও ইসিজি",
                "সিনিয়র মেডিসিন কনসালট্যান্ট রিভিউ",
            ],
            "features_list_en": [
                "Comprehensive Metabolic Profile",
                "PSA (Prostate Specific Antigen)",
                "HbA1c & Advanced Lipid Subfractions",
                "2D/4D Color Doppler Echocardiogram",
                "USG Whole Abdomen & Prostate",
                "Serum Electrolytes & Renal Panel",
                "Digital Chest X-Ray & ECG",
                "Senior Consultant Clinical Review",
            ],
            "order": 4,
        },
    ]

    HealthPackage.objects.all().delete()
    for pkg in packages:
        HealthPackage.objects.create(**pkg)
    print(f"  - Created {len(packages)} packages.")

def seed_health_card():
    print("Seeding Health Card Notice...")
    card, _ = HealthCardNotice.objects.get_or_create(id=1)
    card.badge_text_bn = "বিশেষ ছাড় ও স্বাস্থ্য সুবিধা"
    card.badge_text_en = "Special Discounts & Privileges"
    card.title_bn = "স্টার লাইন হেলথ কেয়ার কার্ড সুবিধা"
    card.title_en = "Star Line Health Care Card Facility"
    card.subtitle_bn = "আমাদের অফিশিয়াল হেলথ কার্ডে ডায়াগনস্টিক টেস্ট, রোগী ভর্তি এবং ওপিডি সেবায় বিশেষ ছাড় ও অগ্রাধিকার সেবা উপভোগ করুন।"
    card.subtitle_en = "Enjoy valuable discounts on diagnostic tests, hospital admissions, and OPD services with our official Health Care Card."
    card.verify_url = "/contact#card-verification"
    card.benefits_url = "/about#card-facility"
    card.is_active = True
    card.save()
    print("  - Health card notice saved.")

def seed_news_and_blogs():
    print("Seeding News and Blogs...")
    articles = [
        # Health Awareness Blogs
        {
            "item_type": "blog",
            "category": "health checkup",
            "title_bn": "নিয়মিত স্বাস্থ্য পরীক্ষা: রোগ প্রতিরোধের প্রথম ধাপ",
            "title_en": "Regular Body Checkup: Prevention Before Disease",
            "summary_bn": "লক্ষণ প্রকাশের আগেই রোগ নির্ণয় ও সুস্থ দীর্ঘায়ু নিশ্চিত করতে নিয়মিত হেলথ চেকআপের গুরুত্ব অপরিসীম।",
            "summary_en": "Prevention starts before symptoms appear. Regular body checkups can detect diabetes, high blood pressure, and silent metabolic risks early.",
            "published_date": "2026-10-29",
            "slug": "regular-body-checkup-prevention-before-disease",
            "order": 1,
        },
        {
            "item_type": "blog",
            "category": "health awareness",
            "title_bn": "জ্বর কি ডেঙ্গু হতে পারে? সতর্ক লক্ষণ ও চিকিৎসা",
            "title_en": "Fever? It Could be Dengue: Warning Signs, Tests and When to See a Doctor",
            "summary_bn": "তীব্র জ্বর, মাথাব্যথা ও চোখের পেছনে ব্যথায় দ্রুত এনএস১ অ্যান্টিজেন ও সিবিসি প্লাটিলেট পরীক্ষা করানো জরুরি।",
            "summary_en": "Do not ignore fever, headache and body aches. Learn the warning signs of dengue, the tests you need, and when to seek 24/7 emergency support.",
            "published_date": "2026-10-25",
            "slug": "fever-could-be-dengue-warning-signs-tests",
            "order": 2,
        },
        {
            "item_type": "blog",
            "category": "health awareness",
            "title_bn": "ব্রেন স্ট্রোক না হার্ট অ্যাটাক: কারণ ও জরুরি চিকিৎসা",
            "title_en": "Brain Stroke or Heart Attack: Causes, Warning Signs and Why Timely Treatment Matters",
            "summary_bn": "গোল্ডেন আওয়ারের মধ্যে বিশেষজ্ঞ হাসপাতালে পৌঁছানো রোগীর জীবন বাঁচানোর সবচেয়ে মোক্ষম সুযোগ।",
            "summary_en": "Brain stroke and heart attack are medical emergencies. Learn the causes, warning signs, and why quick medical intervention saves lives.",
            "published_date": "2026-10-23",
            "slug": "brain-stroke-or-heart-attack-warning-signs",
            "order": 3,
        },

        # Hospital News & Events
        {
            "item_type": "news",
            "category": "doctor-profile",
            "title_bn": "মেডিসিন ও ক্রিটিক্যাল কেয়ার বিশেষজ্ঞ ডাঃ রিয়াজ উদ্দিন চৌধুরী - ফেনী",
            "title_en": "Medicine & Critical Care Specialist Dr. Riaz Uddin Chowdhury - Feni",
            "summary_bn": "ডাঃ রিয়াজ উদ্দিন চৌধুরী (এমবিবিএস, এমসিপিএস, এফসিপিএস) প্রতিদিন সকাল ১১টা থেকে দুপুর ১২টা পর্যন্ত চেম্বারে রোগী দেখছেন।",
            "summary_en": "Dr. Riaz Uddin Chowdhury (MBBS, MCPS, FCPS), Senior Medicine Consultant, holds a daily 11 AM-12 PM chamber at Star Line Hospital.",
            "published_date": "2026-08-29",
            "slug": "dr-riaz-uddin-chowdhury-chamber-schedule",
            "order": 1,
        },
        {
            "item_type": "news",
            "category": "doctor-profile",
            "title_bn": "গ্যাস্ট্রো ও লিভার বিশেষজ্ঞ ডাঃ মোঃ আশিকুর রহমান - স্টার লাইন হাসপাতাল",
            "title_en": "Gastro & Liver Specialist Dr. Md. Ashikur Rahman - Star Line Hospital",
            "summary_bn": "ডাঃ মোঃ আশিকুর রহমান (এমবিবিএস, বিসিএস, এমডি-গ্যাস্ট্রোএন্টারোলজি) নিয়মিত পরিপাকতন্ত্র ও লিভারের রোগীদের পরামর্শ দিচ্ছেন।",
            "summary_en": "Dr. Md. Ashikur Rahman (MBBS, BCS Health, MD Gastroenterology), sees patients at Star Line Specialized Hospital.",
            "published_date": "2026-10-02",
            "slug": "dr-ashikur-rahman-gastro-liver-clinic",
            "order": 2,
        },
        {
            "item_type": "news",
            "category": "hospital-news",
            "title_bn": "স্টার লাইন হাসপাতালে যুক্ত হলো ১৬০ স্লাইস আধুনিক কার্ডিয়াক সিটি স্ক্যান",
            "title_en": "Star Line Hospital Launches 160-Slice Ultra-Fast Cardiac CT Scan Facility",
            "summary_bn": "ফেনী ও বৃহত্তর নোয়াখালী অঞ্চলের প্রথম উচ্চক্ষমতাসম্পন্ন ১৬০ স্লাইস সিটি স্ক্যানে মাত্র ৫ সেকেন্ডে হার্ট ও ভাস্কুলার অ্যাসেসমেন্ট সম্ভব।",
            "summary_en": "First high-performance 160-slice cardiac CT in Feni region providing ultra-low dose radiation scans in less than 5 seconds.",
            "published_date": "2026-11-21",
            "slug": "160-slice-cardiac-ct-scan-launch",
            "order": 3,
        },
    ]

    NewsBlogItem.objects.all().delete()
    for art in articles:
        NewsBlogItem.objects.create(**art)
    print(f"  - Created {len(articles)} news and blog articles.")

if __name__ == "__main__":
    print("=== SEEDING STARLINE HOSPITAL COMPLETE HOMEPAGE CONTENT ===")
    seed_departments()
    seed_doctors()
    seed_facilities()
    seed_packages()
    seed_health_card()
    seed_news_and_blogs()
    print("=== HOMEPAGE CONTENT SEEDING COMPLETE! ===")
