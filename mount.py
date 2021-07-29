import os

enac_username = "enac-ckan"
enac_password = ""

geodata_username = "geodata-admin"
geodata_password = ""

def connect_enac1files():
  source = "//enac1files.epfl.ch/proj-meteosuisse"
  target = "/mnt/harvest/meteosuisse/Precipitation/CombiPrecip/data"
  os.system(f"mount -v -t cifs \"{source}\" -o username={enac_username},password={enac_password},domain=intranet,iocharset=utf8,sec=ntlmv2,vers=1.0 \"{target}\" ")

def connect_enac2netsvc1():
  source = "//enac2netsvc1.epfl.ch/meteosuisse/"
  target = "/mnt/harvest/meteosuisse/RprelimD/data"
  os.system(f"mount -v -t cifs \"{source}\" -o username={enac_username},password={enac_password},domain=intranet,iocharset=utf8,sec=ntlmv2 \"{target}\" ")

def connect_geodata(source, target):
  source = "//enacit1vm02.epfl.ch/geodata/MeteoSwiss/" + source + "/"
  target = "/mnt/harvest/meteosuisse/" + target + "/data/" 
  os.system(f"mount -v -t cifs \"{source}\" -o username={geodata_username},password={geodata_password},domain=intranet,iocharset=utf8,sec=ntlmv2 \"{target}\" ")

connect_enac1files()
connect_enac2netsvc1()

connect_geodata("Albedo/Hourly_Data", "Albedo")
connect_geodata("Clear_Sky_Index", "Clear_Sky_Index")

connect_geodata("Precipitation/Daily_Data",    "Precipitation/RhiresD")
connect_geodata("Precipitation/Monthly_Data",   "Precipitation/RhiresM")
connect_geodata("Precipitation/Yearly_Data",   "Precipitation/RhiresY")
connect_geodata("Precipitation/Radar_Data/AQC", "Precipitation/Radar_AQC")

connect_geodata("Radiation/Clear_Sky_Shortwave_Radiation/Hourly_Data", "Radiation/Clear_Sky_Shortwave")
connect_geodata("Radiation/Diffuse_Radiation/Daily_Data",              "Radiation/Diffuse")
connect_geodata("Radiation/Direct_Clear_Sky_Shortwave_Radiation",      "Radiation/Direct_Clear_Sky_Shortwave")
connect_geodata("Radiation/Direct_Radiation",                          "Radiation/Direct")
connect_geodata("Radiation/Global_Radiation",                          "Radiation/Global")

connect_geodata("Relative_Sunshine_Duration/Daily_Data",   "Sunshine_Duration/SrelD")
connect_geodata("Relative_Sunshine_Duration/Monthly_Data", "Sunshine_Duration/SrelM")
connect_geodata("Relative_Sunshine_Duration/Yearly_Data",  "Sunshine_Duration/SrelY")

connect_geodata("Temperature/Maximum_Temperature/Daily_Data",   "Temperature/TmaxD")
connect_geodata("Temperature/Maximum_Temperature/Monthly_Data", "Temperature/TmaxM")
connect_geodata("Temperature/Maximum_Temperature/Yearly_Data",  "Temperature/TmaxY")
connect_geodata("Temperature/Mean_Temperature/Daily_Data",      "Temperature/TabsD")
connect_geodata("Temperature/Mean_Temperature/Monthly_Data",    "Temperature/TabsM")
connect_geodata("Temperature/Mean_Temperature/Yearly_Data",     "Temperature/TabsY")
connect_geodata("Temperature/Minimum_Temperature/Daily_Data",   "Temperature/TminD")
connect_geodata("Temperature/Minimum_Temperature/Monthly_Data", "Temperature/TminM")
connect_geodata("Temperature/Minimum_Temperature/Yearly_Data",  "Temperature/TminY")
