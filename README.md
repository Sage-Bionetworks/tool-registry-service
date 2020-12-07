# Tool Registry

[![GitHub Release](https://img.shields.io/github/release/Sage-Bionetworks/tool-registry.svg?include_prereleases&color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/tool-registry/releases)
[![GitHub CI](https://img.shields.io/github/workflow/status/Sage-Bionetworks/tool-registry/ci.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/tool-registry)
[![GitHub License](https://img.shields.io/github/license/Sage-Bionetworks/tool-registry.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&logo=github)](https://github.com/Sage-Bionetworks/tool-registry)
[![Docker Pulls](https://img.shields.io/docker/pulls/sagebionetworks/tool-registry.svg?color=94398d&labelColor=555555&logoColor=ffffff&style=for-the-badge&label=pulls&logo=docker)](https://hub.docker.com/repository/docker/sagebionetworks/tool-registry)

Tool Registry API service

## Specification

- Implements the [Tool Registry OpenAPI specification]

## Deploying using Docker

1. Create the file that contains the future environment variables

       cp .env.sample .env

2. Export the variables defined in *.env* to environment variables

       export $(grep -v '^#' .env | xargs -d '\n')

3. Start the Data Node API service

       docker-compose up

4. Go to the API service documentation page <http://localhost:8080/api/v1/ui/>
   to check that the API service is successfully running.

## Development environment

1. Create the file that contains the future environment variables

       cp .env.sample .env

2. Export the variables defined in *.env* to environment variables

       export $(grep -v '^#' .env | xargs -d '\n')

3. Start the MongoDB instance defined in `docker-compose.yml`

       docker-compose up db

4. We recommend using a Conda environment to install and run the Tool Registry
   API service.

       conda create --name tool-registry python=3.8.5
       conda activate tool-registry

5. Install the dependancies and start the Tool Registry

       cd server
       pip install -r requirements.txt
       python -m openapi_server

6. Go to the API service documentation page <http://localhost:8080/api/v1/ui/>
   to check that the API service is successfully running.

<!-- Definitions -->

[Tool Registry OpenAPI specification]: https://github.com/Sage-Bionetworks/tool-registry-schemas