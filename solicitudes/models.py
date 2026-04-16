from django.db import models

TIPO_SOLICITUD = [
    ('academica', 'Académica'),
    ('administrativa', 'Administrativa'),
    ('tecnica', 'Técnica'),
    ('otra', 'Otra'),
]


class Solicitud(models.Model):
    nombre_solicitante = models.CharField(max_length=150)
    documento_identidad = models.CharField(max_length=50)
    correo_electronico = models.EmailField()
    telefono_contacto = models.BigIntegerField()
    tipo_solicitud = models.CharField(max_length=20, choices=TIPO_SOLICITUD)
    asunto = models.CharField(max_length=200)
    descripcion_detallada = models.TextField()
    fecha_solicitud = models.DateField()
    archivo_adjunto = models.FileField(upload_to='solicitudes/', blank=True, null=True)

    def __str__(self):
        return f"{self.nombre_solicitante} - {self.asunto}"

    class Meta:
        verbose_name = "Solicitud"
        verbose_name_plural = "Solicitudes"
