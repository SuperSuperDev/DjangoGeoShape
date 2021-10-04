from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
# Create your models here.


class Country(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    adm0_en = models.CharField(max_length=50)
    adm0_th = models.CharField(max_length=50)
    adm0_pcode = models.CharField(
        primary_key=True,
        max_length=50)
    date = models.DateField()
    validon = models.DateField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return f'{self.adm0_pcode} - {self.adm0_en} - {self.adm0_th }'


# Auto-generated `LayerMapping` dictionary for Country model
country_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'adm0_en': 'ADM0_EN',
    'adm0_th': 'ADM0_TH',
    'adm0_pcode': 'ADM0_PCODE',
    'date': 'date',
    'validon': 'validOn',
    'geom': 'MULTIPOLYGON',
}


class Province(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    adm1_en = models.CharField(max_length=50)
    adm1_th = models.CharField(max_length=50)
    adm1_pcode = models.CharField(
        primary_key=True,
        max_length=50
    )
    adm0_en = models.CharField(max_length=50)
    adm0_th = models.CharField(max_length=50)
    adm0_pcode = models.ForeignKey(
        Country,
        related_name='provinces',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    validon = models.DateField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return f'{self.adm1_pcode} - {self.adm1_en} - {self.adm1_th } | {self.adm0_en}'


province_mapping = {
    'adm0_pcode': {'adm0_pcode': 'ADM0_PCODE'},
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'adm1_en': 'ADM1_EN',
    'adm1_th': 'ADM1_TH',
    'adm1_pcode': 'ADM1_PCODE',
    'adm0_en': 'ADM0_EN',
    'adm0_th': 'ADM0_TH',
    'date': 'date',
    'validon': 'validOn',
    'geom': 'MULTIPOLYGON',
}

class District(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    adm2_en = models.CharField(max_length=50)
    adm2_th = models.CharField(max_length=50)
    adm2_pcode = models.CharField(
        primary_key=True,
        max_length=50)
    adm1_en = models.CharField(max_length=50)
    adm1_th = models.CharField(max_length=50)
    adm1_pcode = models.ForeignKey(
        Province,
        related_name='districts',
        on_delete=models.CASCADE
    )
    adm0_en = models.CharField(max_length=50)
    adm0_th = models.CharField(max_length=50)
    adm0_pcode = models.ForeignKey(
        Country,
        related_name='districts',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    validon = models.DateField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return f'{self.adm2_pcode} - {self.adm2_en} - {self.adm2_th } | {self.adm1_en}, {self.adm0_en} '

# Auto-generated `LayerMapping` dictionary for District model
district_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'adm2_en': 'ADM2_EN',
    'adm2_th': 'ADM2_TH',
    'adm2_pcode': 'ADM2_PCODE',
    'adm1_en': 'ADM1_EN',
    'adm1_th': 'ADM1_TH',
    'adm1_pcode': 'ADM1_PCODE',
    'adm0_en': 'ADM0_EN',
    'adm0_th': 'ADM0_TH',
    'adm0_pcode': 'ADM0_PCODE',
    'date': 'date',
    'validon': 'validOn',
    'geom': 'MULTIPOLYGON',
}

class SubDistrict(models.Model):
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    adm3_en = models.CharField(max_length=50)
    adm3_th = models.CharField(max_length=50)
    adm3_pcode = models.CharField(
        primary_key=True,
        max_length=50)
    adm2_en = models.CharField(max_length=50)
    adm2_th = models.CharField(max_length=50)
    adm2_pcode = models.ForeignKey(
        District,
        related_name='subdistricts',
        on_delete=models.CASCADE
    )
    adm1_en = models.CharField(max_length=50)
    adm1_th = models.CharField(max_length=50)
    adm1_pcode = models.ForeignKey(
        Province,
        related_name='subdistricts',
        on_delete=models.CASCADE
    )
    adm0_en = models.CharField(max_length=50)
    adm0_th = models.CharField(max_length=50)
    adm0_pcode = models.ForeignKey(
        Country,
        related_name='subdistricts',
        on_delete=models.CASCADE
    )
    date = models.DateField()
    validon = models.DateField()
    geom = models.MultiPolygonField(srid=4326)

    def __str__(self):
        return f'{self.adm3_pcode} - {self.adm3_en} - {self.adm3_th } | {self.adm2_en}, {self.adm1_en}, {self.adm0_en} '


# Auto-generated `LayerMapping` dictionary for District model
subdistrict_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'adm3_en': 'ADM3_EN',
    'adm3_th': 'ADM3_TH',
    'adm3_pcode': 'ADM3_PCODE',
    'adm2_en': 'ADM2_EN',
    'adm2_th': 'ADM2_TH',
    'adm2_pcode': 'ADM2_PCODE',
    'adm1_en': 'ADM1_EN',
    'adm1_th': 'ADM1_TH',
    'adm1_pcode': 'ADM1_PCODE',
    'adm0_en': 'ADM0_EN',
    'adm0_th': 'ADM0_TH',
    'adm0_pcode': 'ADM0_PCODE',
    'date': 'date',
    'validon': 'validOn',
    'geom': 'MULTIPOLYGON',
}

class POI(models.Model):
    lat = models.DecimalField(max_digits=10, decimal_places=6)
    lng = models.DecimalField(max_digits=10, decimal_places=6)
    loc = models.PointField(geography=True, srid=4326, default=Point(100.52974993962351,13.741090616723785))
    subdistrict = models.ForeignKey(
        SubDistrict,
        related_name='pois',
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    
    def save(self, *args, **kwargs):
        self.subdistrict = SubDistrict.objects.get(geom__contains=self.loc)
        super(POI, self).save(*args, **kwargs)      
    


# class thailandPlaces(models.Model):
#     adm0_en = models.CharField(max_length=50)
#     adm0_th = models.CharField(max_length=50)
#     adm0_pcode = models.CharField(max_length=50)
#     adm1_en = models.CharField(max_length=50)
#     adm1_th = models.CharField(max_length=50)
#     adm1_pcode = models.CharField(max_length=50)
#     adm2_en = models.CharField(max_length=50)
#     adm2_th = models.CharField(max_length=50)
#     adm2_pcode = models.CharField(max_length=50)
#     adm3_en = models.CharField(max_length=50)
#     adm3_th = models.CharField(max_length=50)
#     adm3_pcode = models.CharField(max_length=50)
#     adm3_ref = models.CharField(max_length=50, default="", blank=True, null=True)
#     adm3alt1en = models.CharField(max_length=50, default="", blank=True, null=True)
#     adm3alt2en = models.CharField(max_length=50, default="", blank=True, null=True)
#     adm3alt1th = models.CharField(max_length=50, default="", blank=True, null=True)
#     adm3alt2th = models.CharField(max_length=50, default="", blank=True, null=True)
#     geom = models.MultiPointField(srid=4326)


# # Auto-generated `LayerMapping` dictionary for thailand model
# thailandPlaces_mapping = {
#     'adm0_en': 'ADM0_EN',
#     'adm0_th': 'ADM0_TH',
#     'adm0_pcode': 'ADM0_PCODE',
#     'adm1_en': 'ADM1_EN',
#     'adm1_th': 'ADM1_TH',
#     'adm1_pcode': 'ADM1_PCODE',
#     'adm2_en': 'ADM2_EN',
#     'adm2_th': 'ADM2_TH',
#     'adm2_pcode': 'ADM2_PCODE',
#     'adm3_en': 'ADM3_EN',
#     'adm3_th': 'ADM3_TH',
#     'adm3_pcode': 'ADM3_PCODE',
#     'adm3_ref': 'ADM3_REF',
#     'adm3alt1en': 'ADM3ALT1EN',
#     'adm3alt2en': 'ADM3ALT2EN',
#     'adm3alt1th': 'ADM3ALT1TH',
#     'adm3alt2th': 'ADM3ALT2TH',
#     'geom': 'MULTIPOINT',
# }

# class thailandShapes(models.Model):
#     shape_leng = models.FloatField()
#     admlevel = models.IntegerField()
#     date = models.DateField()
#     validon = models.DateField()
#     validto = models.DateField(null=True, blank=True)
#     geom = models.MultiLineStringField(srid=4326)


# # Auto-generated `LayerMapping` dictionary for thailand model
# thailandShapes_mapping = {
#     'shape_leng': 'Shape_Leng',
#     'admlevel': 'admLevel',
#     'date': 'date',
#     'validon': 'validOn',
#     'validto': 'validTo',
#     'geom': 'MULTILINESTRING',
# }
