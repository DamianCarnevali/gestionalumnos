from drf_yasg import openapi
from drf_yasg.inspectors import SwaggerAutoSchema

class CustomAutoSchema(SwaggerAutoSchema):
    def should_filter(self):
        return False
