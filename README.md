# Python-AzureDevOps-Containerized
A small Flask API that connects to Mongo Atlas and is deployed using Azure DevOps which builds and pushes an updated Docker Image each commit to Azure Container Registry.

<br>

### Build an run
For continuous deployment and integration - update the azure-pipelines.yml to your credentials.
Replace the following environment variables to run locally:
- MONGO_ATLAS_USERNAME (your Mongo Atlas username)
- MONGO_ATLAS_PASSWORD (your Mongo Atlas password)
- MONGO_ATLAS_CLUSTER (your Mongo Atlas cluster)
- MONGO_ATLAST_DATABASE (your Mongo Atlas database)
