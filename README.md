# ENAC DATA CATALOG - CKAN

Ckan is automatically started with ckan.service

To manually (re)start it:

```
make run
```

https://github.com/EPFL-ENAC/ENACDataCatalog based on https://github.com/keitaroinc/docker-ckan

## A bit of history
- The Notion card: https://www.notion.so/enacit4r/ckan-enac-data-catalog-2468bae521b740208ae51c04fed22cc6
- The google drive with a lot of non-structured information about this project

### Extract of the Datasets@ENAC.docx
Probably a list of things we want for the CKAN ENAC DATA CATALOG
- Publicly available Swiss GIS Data
    - https://opendata.swiss/fr/dataset?q=gis ?
    - https://www.geocat.ch/ ? 
- (DEPRECATED) Topographic data from SwissTopo is available from https://geovite.ethz.ch/Data.html
    - Swiss topo: Geovite.ethz.ch (DEPRECATED)
    - Directly accessible through swisstopo: https://www.swisstopo.admin.ch/fr/geodata/maps.html
- Meteorological data ia available from MeteoSwiss, and we have direct access to their databases at ENAC (we’re currently working on streamlining that access pipeline - so let me know if you’re looking for meteo data, and which in particular!)
- Geospatial data repository of the Swiss Confederation: map.geo.admin.ch/
- For more local data, I’d refer for cantons website. For example, Geneva’s database is an excellent resource: https://ge.ch/sitg/
- Environmental Research Data in Switzerland: https://www.envidat.ch/
- Hydro data: https://wiki.epfl.ch/hydrodata (to look into/!\)
- MétéoSuisse epflgeodata.epfl.ch (Infra par Nicolas Dubois, geodata@epfl.ch géré par LASIG, see Geodonnees doc) 
- Données OFS: epflgeodata.epfl.ch (S. Joost)
- Géodonnées du canton de Vaud : https://www.asitvd.ch/ (also S. Joost)
- https://opendata.swiss/en/
- Access to data Marti / Gionata– helpers scripts ?


## Plugins
- https://github.com/EPFL-ENAC/CKAN_ext_oaipmh
    - Important: You need to have a sysadmin user called "harvest" on your CKAN instance!
    - CKAN Data Catalog Plug-in for OAIPMH protocol (for integration with Zenodo and Infoscience)    
- https://github.com/EPFL-ENAC/CKAN_ext_localfolders
    - https://extensions.ckan.org/extension/harvest/
    - extansion of CKAN Harvester plugin that mount
        base_url = '/srv/app/data/harvest/' from /mnt/harvest on the machine


## Scripts / API FEED
- data-catalog-data-loading
    - Created by regis.longchamp@epfl.ch to automate populating ckan metadata via the API
    - https://github.com/EPFL-ENAC/enac-data-catalog-data-loading
    - The repository gathers a bunch of code to reference new data into the ckan data management system.


## New setup
Just run `ansible-playbook -v -i inventory/enac-ckan.epfl.ch.yml  playbooks/deploy-app.yml` in the repo enacit-ansible 
- The certificates are handled by the enacit-ansible repo
    - It should be done and referenced in the enacit-ansible repo
- don't forget to add a deploy key:
```
Authorize cloning from the vm by adding a 'deploy-key' in the github setting of this repository
the 'deploy-key' is the public key of the machine created by the provisioning it is needed when the repo is private
```

### ansible is stuck ?
If ansible is stuck at the gather information stage, you may try running the following command.
```
ANSIBLE_DEBUG=1 ansible-playbook -vvvvv -i inventory/enac-ckan.epfl.ch.yml  playbooks/dump_vars.yml
```

- it usually is only this dataset that pauses problem, so just unmount -l it:
    umount -l /mnt/harvest/meteosuisse/Precipitation/CombiPrecip/data
- you'll need to stop the harvest process before though. remount it and then relaunch the process harvest


## Machine setup

### SSH and certificates
    - have a look at how it was setup: https://github.com/EPFL-ENAC/enacit-srv-lin-sysadmin/tree/develop/prod/enac-ckan#2021-07-27--ssl-certificate--request before enacit-ansible
## Deprecated setup
### Password
- The passwords are stored inside our enac keeweb under the keywords: 'ckan-datacatalog *'
- For the interface login/password are under 'ckan-datacatalog ui credentials'

### mount.py and Makefile
You need to update credentials via Env variable if the ./mount.py allow it or directly on the machine by using the password found in the keeweb

#### Mounting the files
You need to create the file path before mounting the enac drives

```bash
mkdir -p /mnt/harvest/meteosuisse/;
# if you are in /opt/ENACDataCatalog else you should find a way to copy/move the meteosuisse data templates (json/md/pdf/png..)
rsync -chavzP --stats meteosuisse/* /mnt/harvest/meteosuisse/

```

```bash
## example of script to generate the directory in /mnt/harvest for example
## DO NOT COPY PASTE BEFORE READING
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
```

umount script

```bash
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
    /mnt/harvest/meteosuisse/Temperature/TminY/data' | xargs -I {} umount -l {}
```
#### Firewall
- To be allowed to mount the drives you'll need to create the /mnt directories
    - If you have errors by running python3 /opt/.../mount.py you may save the error output by doing so: `python3 mount.py 2> test.txt` and then create the directory by running something like: `cat test.txt  | grep /mnt | awk '{print $4}' | sed 's/://gi' | ^Crgs -I {} mkdir -p {}`; it should be faster than creating all those directories by hand
- And be allowed in the firewall to access the enacit drives (ask an enac admin to allow your machine to access those enacit vm)
- Verify that you have port 8443 open in the firewall for apache2 and 80/443 for the service web (usually done via enacit-ansible repo)
    - https://github.com/EPFL-ENAC/enacit-ansible/blob/main/inventory/enac-ckan.epfl.ch.yml#L12
- Allow Samba / maybe not useful check with an admin


#### TEQUILA

- Since circa 2022, we need to ask 1234@epfl.ch for access to tequila server from a server
```
# If when you do a wget on this url you have a 403, then you should ask access for your new machine
root@enacvm0096:~# wget -O - https://tequila.epfl.ch/cgi-bin/tequila/createrequest?urlaccess=test [https://tequila.epfl.ch/cgi-bin/tequila/createrequest?urlaccess=test]
--2022-07-05 14:13:06--  https://tequila.epfl.ch/cgi-bin/tequila/createrequest?urlaccess=test [https://tequila.epfl.ch/cgi-bin/tequila/createrequest?urlaccess=test]
Resolving tequila.epfl.ch [http://tequila.epfl.ch] (tequila.epfl.ch [http://tequila.epfl.ch])... 128.178.222.94
Connecting to tequila.epfl.ch [http://tequila.epfl.ch] (tequila.epfl.ch [http://tequila.epfl.ch])|128.178.222.94|:443... connected.
HTTP request sent, awaiting response... 403 You are not allowed to authenticate on this Tequila server
2022-07-05 14:13:06 ERROR 403: You are not allowed to authenticate on this Tequila server.
```

## Harvest datasets from meteosuisse and  infoscience
- Go to https://enac-ckan.epfl.ch/harvest
- Create two harvest source
1) metosuisse
url: meteosuisse
Title: MétéoSuisse data (url: enac-ckan.epfl.ch/harvest/enac-ckan-epfl-ch-harvest-meteosuisse)
Description:
source type: LocalFolders
Update frequency: daily
Configuration:
Organization: meteosuisse (you'll need to create the organization prior to the harvest)


2) infoscience
url: https://infoscience.epfl.ch/oai2d
Title: Infoscience_ENAC_Datasets (url: enac-ckan.epfl.ch/harvest/infoscience_enac_datasets)
Description:
source type: OAI-PMH  Harvester
Update frequency: daily
Configuration:
```
{
 "set": "ENAC_datasets",
 "metadata_prefix": "oai_dc"
}
```
Organization: infoscience (you'll need to create the organization prior to the harvest)

### Side note
- Sometimes the harvest job gets stuck for meteosuisse (due to samba stalling or something else)
- You'll have to rebuild the docker ckan if you want to update the templates in /meteosuisse
- Usually if you run a newly build ckan docker image, you'll need to stop and start the harvest to avoid bad templates to be fed.

## TODO
Side note: not sure if it's still necessary (it was present in and old TODO.md)
Please remove side note when we're sure. And transform those in github ISSUE at least.

- [ ] Dockerise the apache with tequila process present if we really need the swiss topo files : https://github.com/EPFL-ENAC/enacit-srv-lin-sysadmin/tree/develop/prod/enac-ckan#2021-08-23--tequila
    - cf this commit to see how the apache server was accessed by the plugin: 
        https://github.com/EPFL-ENAC/CKAN_ext_localfolders/commit/64f6d6fe9a04e51a33e02e8d7d1742db7a8c1303
- [ ] For information the swiss topo files were access via: https://epflgeodata.epfl.ch/ before geovite existed, and it needed epfl tequila login. But now the data is open at https://www.swisstopo.admin.ch/fr/geodata/maps.html a priori, so it's maybe not needed anymore.
- [ ] Activate group and other option in the oaipmh harvester
- [ ] OAI-PMH : Remove the need to have a 'harvest' user

