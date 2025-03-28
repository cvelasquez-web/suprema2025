from rest_framework.serializers import ModelSerializer
from estudiante.models import EstudianteModelo

class EstudianteSerializer(ModelSerializer):
    class Meta:
        model = EstudianteModelo
        fields =['id', 'codCarrera','codAnio', 'codAlumno','priNombre','segNombre','priApellido','segApellido','telefono','correo','fechaNac']
        #fields = '__alls__'