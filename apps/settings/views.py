from drf_spectacular.utils import extend_schema
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

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
from .serializers import (
    ClinicalFacilitySerializer,
    CombinedSiteSettingsSerializer,
    DepartmentSerializer,
    DoctorSerializer,
    HealthCardNoticeSerializer,
    HealthPackageSerializer,
    NavbarItemSerializer,
    NewsBlogItemSerializer,
    SliderSlideSerializer,
    TopbarSettingSerializer,
)


class CombinedSiteSettingsView(APIView):
    """
    Returns all public website settings and homepage content in a single fast response.
    """
    permission_classes = [AllowAny]

    @extend_schema(
        summary="Get Combined Site Settings & Homepage Content",
        description="Returns Topbar, Navbar, Hero Slides, Departments, Doctors, Clinical Services, Packages, and News.",
        responses={200: CombinedSiteSettingsSerializer},
    )
    def get(self, request):
        topbar = TopbarSetting.get_solo()
        navbar = NavbarItem.objects.filter(is_active=True).order_by("order", "id")
        slides = SliderSlide.objects.filter(is_active=True).order_by("order", "id")
        departments = Department.objects.filter(is_active=True).order_by("order", "id")[:8]
        doctors = Doctor.objects.filter(is_active=True).order_by("order", "id")[:8]
        facilities = ClinicalFacility.objects.filter(is_active=True).order_by("order", "id")[:6]
        packages = HealthPackage.objects.filter(is_active=True).order_by("order", "id")[:4]
        health_card = HealthCardNotice.get_solo()
        blogs = NewsBlogItem.objects.filter(item_type="blog", is_active=True).order_by("order", "-id")[:3]
        news = NewsBlogItem.objects.filter(item_type="news", is_active=True).order_by("order", "-id")[:3]

        data = {
            "topbar": TopbarSettingSerializer(topbar).data,
            "navbar": NavbarItemSerializer(navbar, many=True).data,
            "slides": SliderSlideSerializer(slides, many=True).data,
            "departments": DepartmentSerializer(departments, many=True).data,
            "doctors": DoctorSerializer(doctors, many=True).data,
            "facilities": ClinicalFacilitySerializer(facilities, many=True).data,
            "packages": HealthPackageSerializer(packages, many=True).data,
            "health_card": HealthCardNoticeSerializer(health_card).data,
            "blogs": NewsBlogItemSerializer(blogs, many=True).data,
            "news": NewsBlogItemSerializer(news, many=True).data,
        }
        return Response(data, status=status.HTTP_200_OK)


class TopbarSettingView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        topbar = TopbarSetting.get_solo()
        return Response(TopbarSettingSerializer(topbar).data, status=status.HTTP_200_OK)

    def put(self, request):
        topbar = TopbarSetting.get_solo()
        serializer = TopbarSettingSerializer(topbar, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request):
        return self.put(request)


class NavbarItemListCreateView(generics.ListCreateAPIView):
    queryset = NavbarItem.objects.all().order_by("order", "id")
    serializer_class = NavbarItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class NavbarItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NavbarItem.objects.all()
    serializer_class = NavbarItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class SliderSlideListCreateView(generics.ListCreateAPIView):
    queryset = SliderSlide.objects.all().order_by("order", "id")
    serializer_class = SliderSlideSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class SliderSlideDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SliderSlide.objects.all()
    serializer_class = SliderSlideSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class DepartmentListCreateView(generics.ListCreateAPIView):
    queryset = Department.objects.all().order_by("order", "id")
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class DepartmentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all().order_by("order", "id")
    serializer_class = DoctorSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class DoctorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class ClinicalFacilityListCreateView(generics.ListCreateAPIView):
    queryset = ClinicalFacility.objects.all().order_by("order", "id")
    serializer_class = ClinicalFacilitySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class ClinicalFacilityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ClinicalFacility.objects.all()
    serializer_class = ClinicalFacilitySerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class HealthPackageListCreateView(generics.ListCreateAPIView):
    queryset = HealthPackage.objects.all().order_by("order", "id")
    serializer_class = HealthPackageSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class HealthPackageDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HealthPackage.objects.all()
    serializer_class = HealthPackageSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class HealthCardNoticeView(APIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    def get(self, request):
        obj = HealthCardNotice.get_solo()
        return Response(HealthCardNoticeSerializer(obj).data, status=status.HTTP_200_OK)

    def put(self, request):
        obj = HealthCardNotice.get_solo()
        serializer = HealthCardNoticeSerializer(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)


class NewsBlogItemListCreateView(generics.ListCreateAPIView):
    queryset = NewsBlogItem.objects.all().order_by("order", "-id")
    serializer_class = NewsBlogItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]


class NewsBlogItemDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = NewsBlogItem.objects.all()
    serializer_class = NewsBlogItemSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]
