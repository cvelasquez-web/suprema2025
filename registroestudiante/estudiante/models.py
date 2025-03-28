from django.db import models


from django.core.validators import RegexValidator
# Create your models here.
class EstudianteModelo(models.Model):
    codCarrera = models.CharField(max_length=255)
    codAnio = models.CharField(max_length=255)
    codAlumno = models.CharField(max_length=255)
    priNombre = models.CharField(max_length=255)
    segNombre = models.CharField(max_length=255)
    priApellido = models.CharField(max_length=255)
    segApellido = models.CharField(max_length=255)
    #telefono = models.CharField(max_length=20)  # Mejor opción
    telefono = models.CharField(
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?1?\d{9,15}$',
                message="Formato: '+999999999'. Máx. 15 dígitos."
            )
        ]
    )
    #telefono = models.BigIntegerField()
    correo = models.CharField(max_length=255)
    fechaNac = models.CharField(max_length=255)
    fecha_Creado = models.DateTimeField(auto_now_add=True)
    fecha_actualizado = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "estudiante"
        ordering =['-fecha_Creado']