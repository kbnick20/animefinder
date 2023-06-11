from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status as status_code
from user.serializers import TopAnimeSerializer
from user.models import TopAnime

# Create your views here.


class TopAnimeViewSet(viewsets.ViewSet):
    """

    """
    serializer_class = TopAnimeSerializer

    def create(self, request):
        """

        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response("Anime added to the Top list successfully", status=status_code.HTTP_200_OK)

    def list(self, request):
        """

        """
        all_objects = TopAnime.objects.filter()
        serializer = self.serializer_class(all_objects, many=True)
        return Response(serializer.data)

