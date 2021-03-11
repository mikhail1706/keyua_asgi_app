from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .serializers import UpdateCitySerializer


class UpdateCityApiView(APIView):
    def post(self, request, city_id):
        ser = UpdateCitySerializer(data=request.data)
        if ser.is_valid():
            users = ser.validated_data.get('users')
            temperature = ser.validated_data.get('temperature')
            channel = get_channel_layer()

            for user_id in users:
                route = f'group_with_user_{user_id}'
                async_to_sync(channel.group_send)(route, {
                    'city_id': city_id,
                    'temperature': temperature,
                    'type': 'update_city'})

            return Response({'msg': f'City information has been updated'}, status=HTTP_200_OK)

        return Response(ser.errors, status=HTTP_400_BAD_REQUEST)




