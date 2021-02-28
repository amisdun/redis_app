from rest_framework.views import APIView
from rest_framework.response import Response
import redis
import json

class Communicate(APIView):

    redis_client = redis.StrictRedis(host='redis', port=6379)

    def get(self, request):
        response = {}

        try:
            #connectin to redis client
            sub = self.redis_client.pubsub()

            #subscribing to a channel for incoming message
            sub.subscribe('communication')

            #checking for available message
            print(sub.listen())
            for message in sub.listen():
                if message:
                    if message['type'] == 'message':
                        print(message)
                        status = 200
                        return Response(message['data'], status=status)

        except Exception as e:
            response['error'] = "An error has occured {}".format(e)
            status = 500

        return Response(response, status=status)


    def post(self, request):
        response = {}

        message = request.data.get('message','')

        if message:
            try:
                self.redis_client.publish('communication', message)

                response['resppnse'] = "Message published to the communcation channel"
                status = 200

            except Exception as e:
                response['error'] = "An error has occured {}".format(e)
                status = 500
        else:
            response['error'] = "No message provided, should have message key!!!"
            status = 409

        return Response(response, status=status)

