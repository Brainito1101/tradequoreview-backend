from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Review
from .serializers import ReviewSerializer

@api_view(['GET'])
def get_reviews_by_section(request):
    section = request.GET.get('section')
    if section:
        reviews = Review.objects.filter(section=section).order_by('-date')
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)
    return Response({'error': 'Section query parameter is required'}, status=400)
