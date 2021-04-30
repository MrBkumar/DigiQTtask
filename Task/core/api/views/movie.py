from rest_framework.views import APIView
from rest_framework.response import Response
from core.api.serializers import MovieDetailsSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from core.models import Movie

# ........................................................................................
# API For Movie detail
# ........................................................................................


class MovieDetailsView(APIView):
    """
    Movie Detail View
    """

    serializer_class = MovieDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        """
        GET method for retrieving the data
        """
        try:
            movie = Movie.objects.get(pk=pk)
            if movie is not None:
                serializer = MovieDetailsSerializer(
                    movie, context={"request": request}
                )
                return Response(
                    {
                        "status": "OK",
                        "message": "Successfully Fetched Movie Details",
                        "data": serializer.data,
                    }
                )

        except Movie.DoesNotExist:
            return Response({"status": "FAIL", "message": "Movie Not Found", "data": []})

# ........................................................................................
# API For Movie sorting
# ........................................................................................


class MovieSortingView(APIView):
    """
    Movie Sorting View
    """

    serializer_class = MovieDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, sort_by, format=None):
        """
        GET method for retrieving the data
        """
        try:
            if sort_by:
                movies = Movie.objects.order_by(sort_by)
                data = []
                for movie in movies:
                    serializer = MovieDetailsSerializer(
                        movie, context={"request": request}
                    )
                    data.append(serializer.data)
                return Response(
                    {
                        "status": "OK",
                        "message": "Successfully Fetched Movie Details",
                        "data": data,
                    }
                )

        except:
            return Response({"status": "FAIL", "message": "Something wrong", "data": []})

# ........................................................................................
# API For Movie search
# ........................................................................................


class MovieSearchView(APIView):
    """
    Movie Serching View
    """

    serializer_class = MovieDetailsSerializer
    permission_classes = (IsAuthenticated,)

    def get(self, request, search_by, format=None):
        """
        GET method for retrieving the data
        """
        try:
            if search_by:
                data = []
                movies = Movie.objects.filter(name__icontains = search_by)
                for movie in movies:
                    serializer = MovieDetailsSerializer(
                        movie, context={"request": request}
                    )
                    data.append(serializer.data)
                return Response(
                    {
                        "status": "OK",
                        "message": "Successfully Fetched Movie Details",
                        "data": data,
                    }
                )

        except Movie.DoesNotExist:
            return Response({"status": "FAIL", "message": "Movie Not Found", "data": []})
