from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from estudiante.models import EstudianteModelo
from estudiante.serializers import EstudianteSerializer

class EstudianteApiView(APIView):       # Clase PeersonaApiVista

    def get(self, request):         # metodo get
        serializer = EstudianteSerializer(EstudianteModelo.objects.all(), many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):        # metodo post
        #res = request.data.get('name')
        serializer = EstudianteSerializer(data = request.data)
        serializer.is_valid(raise_exception = True) 
        serializer.save()
        return Response(status=status.HTTP_200_OK, data = serializer.data)

class EstudianteApiViewDetail(APIView):   #Clase PersonaApiVistaDetalles

    def get_object(self, id):       # metodo get_object
        try:
            return EstudianteModelo.objects.get(pk = id) 
        
        except EstudianteModelo.DoesNotExist:
            return None

    def get(self, request, id):     # metodo get
        estudiante = self.get_object(id)
        serializer = EstudianteSerializer(estudiante)
        return Response(status = status.HTTP_200_OK, data = serializer.data)

    def put(self, request, id):     # metodo put
        estudiante = self.get_object(id)
        if(estudiante == None):
            return Response(status = status.HTTP_200_OK, data = {'error':'Nqt found data'})
        serializer = EstudianteSerializer(estudiante, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_200_OK,data = serializer.data)
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id ):   #metodo delete
        estudiante= self.get_object(id)
        estudiante.delete()
        response = {'deleted': True}
        return Response(status = status.HTTP_200_OK, data = response)