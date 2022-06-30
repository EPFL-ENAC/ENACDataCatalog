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

## Machine setup

### SSH and certificates
- Right now the certificates were copied by hand from enacvm0046.xaas.epfl.ch:/etc/ssl to enacvm0096.xaas.epfl.ch:/etc/ssl
    - It should be done and referenced in the enacit-ansible repo
    - have a look at how it was setup: https://github.com/EPFL-ENAC/enacit-srv-lin-sysadmin/tree/develop/prod/enac-ckan#2021-07-27--ssl-certificate--request

### Password
- The passwords are stored inside our enac keeweb under the keywords: 'ckan-datacatalog *'
- For the interface login/password are under 'ckan-datacatalog ui credentials'

### mount.py and Makefile
You need to update credentials via Env variable if the ./mount.py allow it or directly on the machine by using the password found in the keeweb

#### Firewall
- To be allowed to mount the drives you'll need to create the /mnt directories
    - If you have errors by running python3 /opt/.../mount.py you may save the error output by doing so: `python3 mount.py 2> test.txt` and then create the directory by running something like: `cat test.txt  | grep /mnt | awk '{print $4}' | sed 's/://gi' | ^Crgs -I {} mkdir -p {}`; it should be faster than creating all those directories by hand
- And be allowed in the firewall to access the enacit drives (ask an enac admin to allow your machine to access those enacit vm)


## TODO
Side note: not sure if it's still necessary (it was present in and old TODO.md)
Please remove side note when we're sure. And transform those in github ISSUE at least.

- [ ] Dockerise the apache with tequila process present if we really need the swiss topo files : https://github.com/EPFL-ENAC/enacit-srv-lin-sysadmin/tree/develop/prod/enac-ckan#2021-08-23--tequila
    - cf this commit to see how the apache server was accessed by the plugin: 
        https://github.com/EPFL-ENAC/CKAN_ext_localfolders/commit/64f6d6fe9a04e51a33e02e8d7d1742db7a8c1303
    - For information the swiss topo files were access via: https://epflgeodata.epfl.ch/ before geovite existed, and it needed epfl tequila login. But now the data is open at https://www.swisstopo.admin.ch/fr/geodata/maps.html a priori, so it's maybe not needed anymore.
- [ ] Activate group and other option in the oaipmh harvester
- [ ] OAI-PMH : Remove the need to have a 'harvest' user

