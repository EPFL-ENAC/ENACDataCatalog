###################
### Extensions ####
###################
FROM ghcr.io/keitaroinc/ckan:2.9.2 as extbuild

# Locations and tags, please use specific tags or revisions
ENV HARVEST_GIT_URL=https://github.com/ckan/ckanext-harvest
ENV HARVEST_GIT_BRANCH=v1.3.1

# Switch to the root user
USER root

# Install necessary packages to build extensions
RUN apk add \
        gcc \
        g++ \
        libffi-dev \
        openssl-dev \
        python3-dev \
        rust \
        cargo \
        openldap-dev

# Fetch and build the custom CKAN extensions
RUN pip wheel --wheel-dir=/wheels git+${HARVEST_GIT_URL}@${HARVEST_GIT_BRANCH}#egg=ckanext-harvest
RUN pip wheel --wheel-dir=/wheels -r https://raw.githubusercontent.com/ckan/ckanext-harvest/${HARVEST_GIT_BRANCH}/pip-requirements.txt
RUN curl -o /wheels/harvest.txt https://raw.githubusercontent.com/ckan/ckanext-harvest/${HARVEST_GIT_BRANCH}/pip-requirements.txt

RUN pip wheel --wheel-dir=/wheels git+https://github.com/NaturalHistoryMuseum/ckanext-ldap#egg=ckanext-ldap
#RUN pip wheel --wheel-dir=/wheels git+https://github.com/ckan/ckanext-spatial#egg=ckanext-spatial

ARG CACHEBUST=92
RUN pip wheel --wheel-dir=/wheels git+https://github.com/EPFL-ENAC/CKAN_ext_localfolders#egg=ckanext-localfolders

USER ckan

############
### MAIN ###
############
FROM ghcr.io/keitaroinc/ckan:2.9.2

ENV CKAN__PLUGINS envvars image_view text_view recline_view datastore datapusher harvest ckan_harvester ldap oaipmh_harvester localfolders_harvester enac_theme
#spatial_metadata spatial_query

# Switch to the root user
USER root

COPY --from=extbuild /wheels /srv/app/ext_wheels

# Install and enable the custom extensions

RUN pip install -e git+https://github.com/EPFL-ENAC/CKAN_ext_oaipmh#egg=ckanext-oaipmh --src /srv/app/src
RUN pip install -r /srv/app/src/ckanext-oaipmh/requirements.txt

RUN pip install --no-index --find-links=/srv/app/ext_wheels ckanext-harvest && \
    pip install --no-index --find-links=/srv/app/ext_wheels -r /srv/app/ext_wheels/harvest.txt && \
    pip install --no-index --find-links=/srv/app/ext_wheels ckanext-ldap && \
    #pip install --no-index --find-links=/srv/app/ext_wheels ckanext-spatial && \
    pip install --no-index --find-links=/srv/app/ext_wheels ckanext-localfolders && \
    # Configure plugins
    ckan config-tool "${APP_DIR}/production.ini" "ckan.plugins = ${CKAN__PLUGINS}" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckanext.ldap.uri = ldaps://ldap.epfl.ch" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckanext.ldap.base_dn = o=epfl,c=ch" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckanext.ldap.username = displayName" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckanext.ldap.email = mail" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckanext.ldap.search.filter = uid={login}" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckanext.ldap.ckan_fallback = true" && \

    ckan config-tool "${APP_DIR}/production.ini" "ckan.site_title = ENAC data catalogue" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckan.site_description = Unified data catalogue for the ENAC faculty" && \

    ckan config-tool "${APP_DIR}/production.ini" "ckan.harvest.log_scope = 0" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckan.harvest.log_timeframe = 10" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckan.harvest.log_level = info" && \
    ckan config-tool "${APP_DIR}/production.ini" "ckan.site_logo = https://inside.epfl.ch/wp/5.5/wp-content/themes/wp-theme-2018/assets/svg/epfl-logo.svg" && \

    chown -R ckan:ckan /srv/app

# Remove wheels
RUN rm -rf /srv/app/ext_wheels

# Add harvest afterinit script
COPY ./afterinit.d/00_harvest.sh ${APP_DIR}/docker-afterinit.d/00_harvest.sh

ARG CACHEBUST=3
COPY ./ckan/ckanext-enac_theme/ ${APP_DIR}/src/ckan/ckanext-enac_theme/
RUN cd /${APP_DIR}/src/ckan/ckanext-enac_theme/ && python setup.py develop

#COPY ./ckan/home_layout.html ${APP_DIR}/src/ckan/ckan/templates/home/layout1.html

# Switch to the ckan user
USER ckan
