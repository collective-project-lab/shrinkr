from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import redirect
from django.http import Http404
from .storage import get_storage
from .serializers import ShortenedURLSerializer, ShortenURLInputSerializer
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

@method_decorator(csrf_exempt, name='dispatch')
class URLShortenerViewSet(viewsets.ViewSet):

    def list(self, request):
        """GET /api/urls/ — list all URLs"""
        storage = get_storage()
        urls = storage.list_all()
        return Response(urls)

    def create(self, request):
        """POST /api/urls/ — shorten a URL"""
        serializer = ShortenURLInputSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        storage = get_storage()
        short_code = storage.save(serializer.validated_data['long_url'])
        short_url = request.build_absolute_uri(f'/{short_code}/')

        return Response(
            {'short_code': short_code, 'short_url': short_url},
            status=status.HTTP_201_CREATED
        )

    def destroy(self, request, pk=None):
        """DELETE /api/urls/{short_code}/ — delete a URL"""
        storage = get_storage()
        deleted = storage.delete(pk)
        if not deleted:
            return Response(
                {'error': 'Short code not found'},
                status=status.HTTP_404_NOT_FOUND
            )
        return Response(status=status.HTTP_204_NO_CONTENT)


def redirect_view(request, short_code):
    """GET /{short_code}/ — redirect to original URL"""
    storage = get_storage()
    long_url = storage.get(short_code)
    if not long_url:
        raise Http404
    return redirect(long_url)