from django.db import models

# Create your models here.


class Metrics(models.Model):
    id = models.BigAutoField(primary_key=True, editable=False)
    names = models.CharField(max_length=100)
    surnames = models.CharField(max_length=100)
    age = models.IntegerField()
    weight = models.FloatField()
    heartRate = models.IntegerField(
        help_text="Frecuencia Cardiaca(Heart Rate) medida en BPM(Beats per minute)/Pulsaciones por minuto")
    bloodOxygenSaturation = models.IntegerField(
        help_text="Saturación de Oxígeno en Sangre")

    STRESS_LEVEL = (
        ('low', 'Low'),
        ('moderate', 'Moderate'),
        ('high', 'High'),
        ('extreme', 'Extreme'),
    )

    stresslevel = models.CharField(
        max_length=20, choices=STRESS_LEVEL, default='low', help_text='Nivel de estrés')

    class Meta:
        db_table = "metrics"
