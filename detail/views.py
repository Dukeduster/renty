from rest_framework.views import APIView
from rest_framework import status, generics
from rest_framework.response import Response
from .models import CarRental, Car, Reservation
from .serializers import RentalSerializer, CarSerializer, CarSerializerToSave, CarSearchSerializer
from django.http import Http404
from django.utils.dateparse import parse_datetime, parse_date
from datetime import datetime, date
from django.views.decorators.http import require_http_methods
import firebase_admin
from firebase_admin import credentials, auth



class RentalView(generics.ListAPIView):
    

    def get_queryset(self):
        queryset = CarRental.objects.all()
        return queryset

    def post(self, request):
        serializer = RentalSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@require_http_methods(["GET", "POST"])
def api_getto(request):
    response = JsonResponse(
        # your stuff here
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


class CarView(APIView):
    serializer_class = CarSerializer

    def get(self, request, carid, format=None):
        if carid is not None:
            cars = Car.objects.filter(id=carid)
            serializer = CarSerializer(cars[0], many=False)
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request):
        serializer = CarSerializerToSave(data=request.data)
        if serializer.is_valid():
            serializer.save()
            Response["Access-Control-Allow-Origin"] = "*"
            Response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
            Response["Access-Control-Max-Age"] = "1000"
            Response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReservationView(APIView):
    serializer_class = RentalSerializer
    cred = credentials.Certificate('D:\\udeaprojects\\renty\\renty-python-firebase-adminsdk.json')
    default_app = firebase_admin.initialize_app(cred)
    def get(self, request):
        try:
            token = self.request.query_params.get('tokenId', None)
            if token is not None:
                decoded_token = auth.verify_id_token(token)
                uid = decoded_token['uid']
                data= {
                    "uid": uid
                }
                return Response(data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except ValueError as e:
                data={
                    "error": str(e)
                }
                return Response(data, status=status.HTTP_401_UNAUTHORIZED)
  





class CarSearchView(generics.ListAPIView):
    serializer_class = CarSearchSerializer

    def get_queryset(self):
        queryset = Car.objects.all()
        reservatedCars = Reservation.objects.all()
        # type es una palabra reservada de python
        _type = self.request.query_params.get('type', None)
        pickup = self.request.query_params.get('pickup', None)
        if _type is not None:
            queryset = queryset.filter(category__iexact=_type)
        if pickup is not None:
            queryset = queryset.filter(pickup__iexact=pickup)
        _from = self.request.query_params.get('from', None)
        _from = _parse_date(str(_from))
        to = self.request.query_params.get('to', None)
        to = _parse_date(str(to))
        if _from is None or to is None:
            queryset = Car.objects.none()
        else:
            if _from > to:
                raise Http404
            fromReservations = reservatedCars.filter(
                fromDate__range=(_from, to))
            toReservations = reservatedCars.filter(toDate__range=(_from, to))
            # Union
            reservatedCars = (fromReservations | toReservations).values('car')
            queryset = queryset.exclude(id__in=reservatedCars)
        return queryset


def _parse_date(date):
    parsed_date = parse_date(date)
    return parsed_date

