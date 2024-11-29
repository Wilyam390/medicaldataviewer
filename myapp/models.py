from django.db import models

class SafetyReport(models.Model):
    occur_country = models.CharField(max_length=100, null=True, blank=True)
    active_substance = models.CharField(max_length=255, null=True, blank=True)
    drug_dosage_form = models.CharField(max_length=255, null=True, blank=True)
    drug_dosage_text = models.TextField(null=True, blank=True)
    drug_indication = models.TextField(null=True, blank=True)
    medicinal_product = models.CharField(max_length=255, null=True, blank=True)
    patient_age = models.IntegerField(null=True, blank=True)
    patient_sex = models.IntegerField(null=True, blank=True)  # Allow NULLs
    reporter_country = models.CharField(max_length=100, null=True, blank=True)
    seriousness_death = models.IntegerField(null=True, blank=True)
    seriousness_disabling = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.active_substance} - {self.medicinal_product}"
