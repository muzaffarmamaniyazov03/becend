from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

from .serializers import *
from .models import *


class ManagementAPIView(APIView):
    def get(self, request, format=None):
        managements = Management.objects.filter(publish=True)
        serializer = ManagementSerializer(managements, many=True)
        return Response(serializer.data)


class RegionalAPIView(APIView):
    def get(self, request, format=None):
        regionals = Regional.objects.filter(publish=True)
        serializer = RegionalSerializer(regionals, many=True)
        return Response(serializer.data)


class GuideAPIView(APIView):
    def get(self, request, format=None):
        guides = Guide.objects.filter(publish=True)
        serializer = GuideSerializer(guides, many=True)
        return Response(serializer.data)


class AboutAPIView(APIView):
    def get(self, request, format=None):
        abouts = About.objects.all()
        serializer = AboutSerializer(abouts, many=True)
        return Response(serializer.data)


class OrganizationAPIView(APIView):
    def get(self, request, format=None):
        organizations = Organization.objects.filter(publish=True)
        serializer = OrganizationSerializer(organizations, many=True)
        return Response(serializer.data)


class DirectorAPIView(APIView):
    def get(self, request, pk, format=None):
        organization = Organization.objects.get(pk=pk)
        director = Director.objects.get(organization=organization)
        serializer = DirectorSerializer(director)
        return Response(serializer.data)


class NewsAPIView(APIView):
    def get(self, request, format=None):
        news = News.objects.filter(publish=True)
        serializer = NewsSerializer(news, many=True)
        return Response(serializer.data)


class NewsByPagination(APIView):
    def get(self, request, format=None):
        try:
            count_qs = News.objects.filter(publish=True).count()
            offset = int(request.GET.get('offset'))
            limit = int(request.GET.get('limit'))
            qs = News.objects.filter(publish=True)[offset:offset + limit]
            serializer = NewsSerializer(qs, many=True)
            return Response({'result': serializer.data, 'count': count_qs})
        except:
            offset = request.GET.get('offset')
            limit = request.GET.get('limit')
            qs = News.objects.filter(publish=True)[int(offset):int(limit)]
            serializer = NewsSerializer(qs, many=True)
            return JsonResponse(serializer.errors, status=400)


class DocumentsAPIView(APIView):
    def get(self, request, format=None):
        documents = Documents.objects.filter(publish=True)
        serializer = DocumentsSerializer(documents, many=True)
        return Response(serializer.data)


class OpenDataAPIView(APIView):
    def get(self, request, format=None):
        open_data = OpenData.objects.filter(publish=True)
        serializer = DocumentsSerializer(open_data, many=True)
        return Response(serializer.data)

