"""
Search Views
"""
import re

from common import constants
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.validators import ValidationError
from common import permissions

from apps.search import schema
from apps.search.gpt import TravelAssistant
from apps.search.serializers import TravelAssistantSerializer


class SearchAPIView(generics.GenericAPIView):
    """
    An API endpoint to facilitate user searches.

    This endpoint processes user search queries, obtains relevant responses
    from ChatGPT, and augments these responses with additional information
    about hotels, attractions, and coupons relevant to the search.

    """

    permission_classes = [
        permissions.IsUser,
    ]
    serializer_class = TravelAssistantSerializer

    @swagger_auto_schema(responses={200: schema.search_api_response})
    def post(self, request, *args, **kwargs):
        """
        Handle the POST request for user searches.

        Processes the user's search query, communicates with ChatGPT to get a
        relevant response, and stitches information about hotels, attractions,
        and coupons into the final response to the user.

        Args:
        - request: The request object containing user data and the search query.
        - *args: Additional arguments.
        - **kwargs: Additional keyword arguments.

        Returns:
        - A response object containing the combined search results.

        Raises:
        - ValidationError: If there's an error during the processing of the search.
        """

        try:
            serializer = self.serializer_class(data=request.data)
            serializer.is_valid(raise_exception=True)
            # Context is a user previous query
            context = {}
            response = TravelAssistant().process_user_query(
                request.data.get("query"), context
            )
            content_str = response
            # Remove excessive indentation
            formatted_content = re.sub(r"\n\s+", "\n", content_str)
            return Response({"result": formatted_content}, status=status.HTTP_200_OK)
        except Exception as ex:
            return Response(
                {"result": constants.standard_question_patterns},
                status=status.HTTP_200_OK,
            )
