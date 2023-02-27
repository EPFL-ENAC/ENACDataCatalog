#! /usr/bin/env sh

echo '/mnt/harvest/meteosuisse/Precipitation/CombiPrecip/data
/mnt/harvest/meteosuisse/RprelimD/data
/mnt/harvest/meteosuisse/Albedo/data
/mnt/harvest/meteosuisse/Clear_Sky_Index/data
/mnt/harvest/meteosuisse/Precipitation/RhiresD/data
/mnt/harvest/meteosuisse/Precipitation/RhiresM/data
/mnt/harvest/meteosuisse/Precipitation/RhiresY/data
/mnt/harvest/meteosuisse/Precipitation/Radar_AQC/data
/mnt/harvest/meteosuisse/Radiation/Clear_Sky_Shortwave/data
/mnt/harvest/meteosuisse/Radiation/Diffuse/data
/mnt/harvest/meteosuisse/Radiation/Direct_Clear_Sky_Shortwave/data
/mnt/harvest/meteosuisse/Radiation/Direct/data
/mnt/harvest/meteosuisse/Radiation/Global/data
/mnt/harvest/meteosuisse/Sunshine_Duration/SrelD/data
/mnt/harvest/meteosuisse/Sunshine_Duration/SrelM/data
/mnt/harvest/meteosuisse/Sunshine_Duration/SrelY/data
/mnt/harvest/meteosuisse/Temperature/TmaxD/data
/mnt/harvest/meteosuisse/Temperature/TmaxM/data
/mnt/harvest/meteosuisse/Temperature/TmaxY/data
/mnt/harvest/meteosuisse/Temperature/TabsD/data
/mnt/harvest/meteosuisse/Temperature/TabsM/data
/mnt/harvest/meteosuisse/Temperature/TabsY/data
/mnt/harvest/meteosuisse/Temperature/TminD/data
/mnt/harvest/meteosuisse/Temperature/TminM/data
/mnt/harvest/meteosuisse/Temperature/TminY/data' | sed 's/\/mnt\/harvest\///' | xargs -I {} mkdir -p {}

