from rest_framework.views import exception_handler
from rest_framework.response import Response

def GetException(exc):
    response = exception_handler(exc, None)
    if response:
        return Response(response.reason_phrase, response.status_code)
    else:
        print(f"- Internal Error! \n {exc} \n")
        return Response(str(exc), 500)
