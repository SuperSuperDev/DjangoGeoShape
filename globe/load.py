import os
from pathlib import Path
from django.contrib.gis.utils import LayerMapping
from .models import Country, Province, District, SubDistrict

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

country_shapefile = Path(__file__).resolve().parent / 'data/tha_adm_rtsd_itos_20190221_SHP_PART_1' / 'tha_admbnda_adm0_rtsd_20190221.shp'

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

province_shapefile = Path(__file__).resolve().parent / 'data/tha_adm_rtsd_itos_20190221_SHP_PART_1' / 'tha_admbnda_adm1_rtsd_20190221.shp'

district_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'adm2_en': 'ADM2_EN',
    'adm2_th': 'ADM2_TH',
    'adm2_pcode': 'ADM2_PCODE',
    'adm1_en': 'ADM1_EN',
    'adm1_th': 'ADM1_TH',
    'adm1_pcode': {'adm1_pcode': 'ADM1_PCODE'},
    'adm0_en': 'ADM0_EN',
    'adm0_th': 'ADM0_TH',
    'adm0_pcode': {'adm0_pcode': 'ADM0_PCODE'},
    'date': 'date',
    'validon': 'validOn',
    'geom': 'MULTIPOLYGON',
}

district_shapefile = Path(__file__).resolve().parent / 'data/tha_adm_rtsd_itos_20190221_SHP_PART_1' / 'tha_admbnda_adm2_rtsd_20190221.shp'

subdistrict_mapping = {
    'shape_leng': 'Shape_Leng',
    'shape_area': 'Shape_Area',
    'adm3_en': 'ADM3_EN',
    'adm3_th': 'ADM3_TH',
    'adm3_pcode': 'ADM3_PCODE',
    'adm2_en': 'ADM2_EN',
    'adm2_th': 'ADM2_TH',
    'adm2_pcode': {'adm2_pcode': 'ADM2_PCODE'},
    'adm1_en': 'ADM1_EN',
    'adm1_th': 'ADM1_TH',
    'adm1_pcode': {'adm1_pcode': 'ADM1_PCODE'},
    'adm0_en': 'ADM0_EN',
    'adm0_th': 'ADM0_TH',
    'adm0_pcode': {'adm0_pcode': 'ADM0_PCODE'},
    'date': 'date',
    'validon': 'validOn',
    'geom': 'MULTIPOLYGON',
}

subdistrict_shapefile = Path(__file__).resolve().parent / 'data/tha_adm_rtsd_itos_20190221_SHP_PART_2' / 'tha_admbnda_adm3_rtsd_20190221.shp'

def run(verbose=True):
    layermap = LayerMapping(Country, country_shapefile, country_mapping, transform=False, encoding='utf-8')
    layermap.save(strict=True, verbose=verbose)
    lmprov = LayerMapping(Province, province_shapefile, province_mapping, transform=False, encoding='utf-8')
    lmprov.save(strict=True, verbose=verbose)
    lmdist = LayerMapping(District, district_shapefile, district_mapping, transform=False, encoding='utf-8')
    lmdist.save(strict=True, verbose=verbose)
    lmsubdist = LayerMapping(SubDistrict, subdistrict_shapefile, subdistrict_mapping, transform=False, encoding='utf-8')
    lmsubdist.save(strict=True, verbose=verbose)
    print('starting lms mapping')
    # lms = LayerMapping(thailandShapes, thailandShapes_shp, thailandShapes_mapping, transform=False)
    # print('saving lms mapping')
    # lms.save(strict=True, verbose=verbose)
    # print('starting lmp mapping')
    # lmp = LayerMapping(thailandPlaces, thailandPlaces_shp, thailandPlaces_mapping, transform=False)
    # print('saving lmp mapping')
    # lmp.save(strict=True, verbose=verbose)


