from django.conf import settings
from drf_yasg import openapi
from drf_yasg.generators import OpenAPISchemaGenerator
from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny


class APISchemeGenerator(OpenAPISchemaGenerator):
    """
    This class is used to generate the API documentation.
    """

    def get_schema(self, request=None, public=False):
        """
        This method is used to get the schema for the API documentation.

        :param request:
        :param public:
        :return:
        """
        schema = super().get_schema(request, public)
        schema.schemes = ["http"] if settings.DEBUG else ["https"]
        return schema


schema_view = get_schema_view(
    openapi.Info(
        title="Social Media API",
        default_version="v1",
        description="""
        This is the API for the Social Media application.

        How to use:
        1. Click on the "Authorize" button in the upper right corner.

        2. Enter the following in the field that appears:
        <access_token>
        where <access_token> is the access token that you received when you logged in.

        3. Click on the "Authorize" button.

        4. Click on the "Close" button.

        5. Now you can use the API.

        Access token lifetime: {access_time_token} day.
        Refresh token lifetime: {refresh_time_token} day.
        """.format(
            access_time_token=settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].days,
            refresh_time_token=settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].days,
        ),
        terms_of_service="https://www.google.com/policies/terms/"
    ),
    public=True,
    permission_classes=[AllowAny],
    urlconf="SocialNetworkStarnavi.urls",
    generator_class=APISchemeGenerator,
)
