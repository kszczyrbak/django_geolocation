from rest_framework.response import Response
from rest_framework import status


def model_created_response(model):
    return Response({
        "status": "success",
        "data": model,
        "message": "Resource created"
    }, status=status.HTTP_201_CREATED)


def bad_request_response(data, errors=""):
    return Response({
        "status": "fail",
        "data": data,
        "message": "Bad request",
        "error": errors
    }, status=status.HTTP_400_BAD_REQUEST)


def model_already_exists_response(model, errors=""):
    return Response({
        "status": "fail",
        "data": model,
        "message": "Resource already exists",
        "errors": errors
    }, status=status.HTTP_409_CONFLICT)


def server_error_response(model, errors=""):
    return Response({
        "status": "fail",
        "data": model,
        "message": "Internal server error. Please try again later",
        "errors": errors
    }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
