# Supported APIs

| Path | Method | Description | Supports |
|------|--------|-------------|----------|
| `/v1/apiCollections` | get | List API Collections | ❌ |
| `/v1/apiCollections` | put | Create or update API Collection | ❌ |
| `/v1/apiCollections` | post | Create a APICollection | ❌ |
| `/v1/apiCollections/name/{fqn}` | get | Get a APICollection by fully qualified name | ❌ |
| `/v1/apiCollections/name/{fqn}` | delete | Delete a API Collection by fully qualified name | ❌ |
| `/v1/apiCollections/name/{fqn}` | patch | Update a APICollection by name. | ❌ |
| `/v1/apiCollections/restore` | put | Restore a soft deleted API Collection. | ❌ |
| `/v1/apiCollections/{id}` | get | Get a API Collection by Id | ❌ |
| `/v1/apiCollections/{id}` | delete | Delete a API Collection by Id | ❌ |
| `/v1/apiCollections/{id}` | patch | Update a API Collection by Id | ❌ |
| `/v1/apiCollections/{id}/versions` | get | List API Collection versions | ❌ |
| `/v1/apiCollections/{id}/versions/{version}` | get | Get a version of the APICollection | ❌ |
| `/v1/apiCollections/{id}/vote` | put | Update Vote for a API Collection | ❌ |
| `/v1/apiEndpoints` | get | List API Endpoints | ❌ |
| `/v1/apiEndpoints` | put | Update API Endpoint | ❌ |
| `/v1/apiEndpoints` | post | Create a API Endpoint | ❌ |
| `/v1/apiEndpoints/name/{fqn}` | get | Get a Endpoint by fully qualified name. | ❌ |
| `/v1/apiEndpoints/name/{fqn}` | delete | Delete a APIEndpoint by fully qualified name | ❌ |
| `/v1/apiEndpoints/name/{fqn}` | patch | Update a APIEndpoint using name. | ❌ |
| `/v1/apiEndpoints/restore` | put | Restore a soft deleted APIEndpoint | ❌ |
| `/v1/apiEndpoints/{id}` | get | Get a APIEndpoint by id | ❌ |
| `/v1/apiEndpoints/{id}` | delete | Delete a APIEndpoint by id | ❌ |
| `/v1/apiEndpoints/{id}` | patch | Update a APIEndpoint | ❌ |
| `/v1/apiEndpoints/{id}/followers` | put | Add a follower | ❌ |
| `/v1/apiEndpoints/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/apiEndpoints/{id}/versions` | get | List API Endpoint versions | ❌ |
| `/v1/apiEndpoints/{id}/versions/{version}` | get | Get a version of the APIEndpoint | ❌ |
| `/v1/apiEndpoints/{id}/vote` | put | Update Vote for a APIEndpoint | ❌ |
| `/v1/apps` | get | List installed application | ❌ |
| `/v1/apps` | put | Create Or Update App | ❌ |
| `/v1/apps` | post | Create a Application | ❌ |
| `/v1/apps/configure/{name}` | post | Configure an Application | ❌ |
| `/v1/apps/deploy/{name}` | post | Deploy App to Quartz or Ingestion | ❌ |
| `/v1/apps/marketplace` | get | List application | ❌ |
| `/v1/apps/marketplace` | put | Create Or Update App | ❌ |
| `/v1/apps/marketplace` | post | Create a Application | ❌ |
| `/v1/apps/marketplace/name/{fqn}` | patch | Updates an App by name. | ❌ |
| `/v1/apps/marketplace/name/{name}` | get | Get a App by name | ❌ |
| `/v1/apps/marketplace/name/{name}` | delete | Delete a App by name | ❌ |
| `/v1/apps/marketplace/restore` | put | Restore a soft deleted KPI | ❌ |
| `/v1/apps/marketplace/{id}` | get | Get a app by Id | ❌ |
| `/v1/apps/marketplace/{id}` | delete | Delete a App by Id | ❌ |
| `/v1/apps/marketplace/{id}` | patch | Updates a App | ❌ |
| `/v1/apps/marketplace/{id}/versions` | get | List Installed Application versions | ❌ |
| `/v1/apps/marketplace/{id}/versions/{version}` | get | Get a version of the App | ❌ |
| `/v1/apps/name/{fqn}` | patch | Updates a App by name. | ❌ |
| `/v1/apps/name/{name}` | get | Get a App by name | ❌ |
| `/v1/apps/name/{name}` | delete | Delete a App by name | ❌ |
| `/v1/apps/name/{name}/extension` | get | List App Extension data | ❌ |
| `/v1/apps/name/{name}/logs` | get | Retrieve all logs from last ingestion pipeline run for the application | ❌ |
| `/v1/apps/name/{name}/runs/latest` | get | Get Latest App Run Record | ❌ |
| `/v1/apps/name/{name}/status` | get | List App Run Records | ❌ |
| `/v1/apps/restore` | put | Restore a soft deleted KPI | ❌ |
| `/v1/apps/schedule/{name}` | post | Schedule an Application | ❌ |
| `/v1/apps/stop/{name}` | post | Stop a Application run | ❌ |
| `/v1/apps/trigger/{name}` | post | Trigger an Application run | ❌ |
| `/v1/apps/{id}` | get | Get a app by Id | ❌ |
| `/v1/apps/{id}` | delete | Delete a App by Id | ❌ |
| `/v1/apps/{id}` | patch | Updates a App | ❌ |
| `/v1/apps/{id}/versions` | get | List Installed Application versions | ❌ |
| `/v1/apps/{id}/versions/{version}` | get | Get a version of the App | ❌ |
| `/v1/bots` | get | List bots | ❌ |
| `/v1/bots` | put | Create or update a bot | ❌ |
| `/v1/bots` | post | Create a bot | ❌ |
| `/v1/bots/name/{fqn}` | patch | Update a bot by name. | ❌ |
| `/v1/bots/name/{name}` | get | Get a bot by name | ❌ |
| `/v1/bots/name/{name}` | delete | Delete a bot by name | ❌ |
| `/v1/bots/restore` | put | Restore a soft deleted bot | ❌ |
| `/v1/bots/{id}` | get | Get a bot by Id | ❌ |
| `/v1/bots/{id}` | delete | Delete a bot by Id | ❌ |
| `/v1/bots/{id}` | patch | Update a bot | ❌ |
| `/v1/bots/{id}/versions` | get | List bot versions | ❌ |
| `/v1/bots/{id}/versions/{version}` | get | Get a version of the bot | ❌ |
| `/v1/charts` | get | List charts | ❌ |
| `/v1/charts` | put | Create or update chart | ❌ |
| `/v1/charts` | post | Create a chart | ❌ |
| `/v1/charts/name/{fqn}` | get | Get a chart by fully qualified name | ❌ |
| `/v1/charts/name/{fqn}` | delete | Delete a chart by fully qualified name | ❌ |
| `/v1/charts/name/{fqn}` | patch | Update a chart by name. | ❌ |
| `/v1/charts/restore` | put | Restore a soft deleted chart | ❌ |
| `/v1/charts/{id}` | get | Get a chart by Id | ❌ |
| `/v1/charts/{id}` | delete | Delete a chart by Id | ❌ |
| `/v1/charts/{id}` | patch | Update a chart | ❌ |
| `/v1/charts/{id}/followers` | put | Add a follower | ❌ |
| `/v1/charts/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/charts/{id}/versions` | get | List chart versions | ❌ |
| `/v1/charts/{id}/versions/{version}` | get | Get a version of the chart | ❌ |
| `/v1/charts/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/classifications` | get | List classifications | ❌ |
| `/v1/classifications` | put | Update a classification | ❌ |
| `/v1/classifications` | post | Create a classification | ❌ |
| `/v1/classifications/name/{fqn}` | patch | Update a classification using name. | ❌ |
| `/v1/classifications/name/{name}` | get | Get a classification by name | ❌ |
| `/v1/classifications/name/{name}` | delete | Delete classification by name | ❌ |
| `/v1/classifications/restore` | put | Restore a soft deleted classification | ❌ |
| `/v1/classifications/{id}` | get | Get a classification by id | ❌ |
| `/v1/classifications/{id}` | delete | Delete classification by id | ❌ |
| `/v1/classifications/{id}` | patch | Update a classification | ❌ |
| `/v1/classifications/{id}/versions` | get | List classification versions | ❌ |
| `/v1/classifications/{id}/versions/{version}` | get | Get a version of the classification | ❌ |
| `/v1/containers` | get | List Containers | ❌ |
| `/v1/containers` | put | Create or update a Container | ❌ |
| `/v1/containers` | post | Create a Container | ❌ |
| `/v1/containers/name/{fqn}` | get | Get an Container by name | ❌ |
| `/v1/containers/name/{fqn}` | delete | Delete a Container by fully qualified name | ❌ |
| `/v1/containers/name/{fqn}` | patch | Update a Container using name. | ❌ |
| `/v1/containers/name/{fqn}/children` | get | List children containers | ❌ |
| `/v1/containers/restore` | put | Restore a soft deleted Container. | ❌ |
| `/v1/containers/{id}` | get | Get an Object Store Container | ❌ |
| `/v1/containers/{id}` | delete | Delete a Container | ❌ |
| `/v1/containers/{id}` | patch | Update a Container | ❌ |
| `/v1/containers/{id}/followers` | put | Add a follower | ❌ |
| `/v1/containers/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/containers/{id}/versions` | get | List Container versions | ❌ |
| `/v1/containers/{id}/versions/{version}` | get | Get a version of the Container | ❌ |
| `/v1/containers/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/dashboard/datamodels` | get | List Dashboard Data Models | ❌ |
| `/v1/dashboard/datamodels` | put | Create or update dashboard datamodel | ❌ |
| `/v1/dashboard/datamodels` | post | Create a dashboard datamodel | ❌ |
| `/v1/dashboard/datamodels/name/{fqn}` | get | Get a dashboard datamodel by fully qualified name | ❌ |
| `/v1/dashboard/datamodels/name/{fqn}` | delete | Delete a data model by fully qualified name. | ❌ |
| `/v1/dashboard/datamodels/name/{fqn}` | patch | Update a dashboard datamodel by name. | ❌ |
| `/v1/dashboard/datamodels/restore` | put | Restore a soft deleted data model. | ❌ |
| `/v1/dashboard/datamodels/{id}` | get | Get a dashboard datamodel by Id | ❌ |
| `/v1/dashboard/datamodels/{id}` | delete | Delete a data model by `id`. | ❌ |
| `/v1/dashboard/datamodels/{id}` | patch | Update a dashboard datamodel | ❌ |
| `/v1/dashboard/datamodels/{id}/followers` | put | Add a follower | ❌ |
| `/v1/dashboard/datamodels/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/dashboard/datamodels/{id}/versions` | get | List dashboard datamodel versions | ❌ |
| `/v1/dashboard/datamodels/{id}/versions/{version}` | get | Get a version of the dashboard datamodel | ❌ |
| `/v1/dashboard/datamodels/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/dashboards` | get | List dashboards | ❌ |
| `/v1/dashboards` | put | Create or update a dashboard | ❌ |
| `/v1/dashboards` | post | Create a dashboard | ❌ |
| `/v1/dashboards/name/{fqn}` | get | Get a dashboard by fully qualified name | ❌ |
| `/v1/dashboards/name/{fqn}` | delete | Delete a dashboard by fully qualified name | ❌ |
| `/v1/dashboards/name/{fqn}` | patch | Update a dashboard by name. | ❌ |
| `/v1/dashboards/restore` | put | Restore a soft deleted dashboard | ❌ |
| `/v1/dashboards/{id}` | get | Get a dashboard by Id | ❌ |
| `/v1/dashboards/{id}` | delete | Delete a dashboard by Id | ❌ |
| `/v1/dashboards/{id}` | patch | Update a dashboard | ❌ |
| `/v1/dashboards/{id}/followers` | put | Add a follower | ❌ |
| `/v1/dashboards/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/dashboards/{id}/versions` | get | List dashboard versions | ❌ |
| `/v1/dashboards/{id}/versions/{version}` | get | Get a version of the dashboard | ❌ |
| `/v1/dashboards/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/dataProducts` | get | List dataProducts | ❌ |
| `/v1/dataProducts` | put | Create or update a dataProduct | ❌ |
| `/v1/dataProducts` | post | Create a dataProduct | ❌ |
| `/v1/dataProducts/name/{fqn}` | patch | Update a dataProduct by name. | ❌ |
| `/v1/dataProducts/name/{name}` | get | Get a dataProduct by name | ❌ |
| `/v1/dataProducts/name/{name}` | delete | Delete a dataProduct by name | ❌ |
| `/v1/dataProducts/{id}` | get | Get a dataProduct by Id | ❌ |
| `/v1/dataProducts/{id}` | delete | Delete a dataProduct by Id | ❌ |
| `/v1/dataProducts/{id}` | patch | Update a dataProduct | ❌ |
| `/v1/dataProducts/{id}/versions` | get | List dataProduct versions | ❌ |
| `/v1/dataProducts/{id}/versions/{version}` | get | Get a version of the dataProduct | ❌ |
| `/v1/dataProducts/{name}/assets/add` | put | Bulk Add Assets | ❌ |
| `/v1/dataProducts/{name}/assets/remove` | put | Bulk Remove Assets | ❌ |
| `/v1/dataQuality/testCases` | get | List test cases | ❌ |
| `/v1/dataQuality/testCases` | put | Update test case | ❌ |
| `/v1/dataQuality/testCases` | post | Create a test case | ❌ |
| `/v1/dataQuality/testCases/logicalTestCases` | put | Add test cases to a logical test suite | ❌ |
| `/v1/dataQuality/testCases/logicalTestCases/{testSuiteId}/{id}` | delete | Delete a logical test case by Id from a test suite | ❌ |
| `/v1/dataQuality/testCases/name/{fqn}` | get | Get a test case by fully qualified name | ❌ |
| `/v1/dataQuality/testCases/name/{fqn}` | delete | Delete a test case by fully qualified name | ❌ |
| `/v1/dataQuality/testCases/restore` | put | Restore a soft deleted test case | ❌ |
| `/v1/dataQuality/testCases/search/list` | get | List test cases using search service | ❌ |
| `/v1/dataQuality/testCases/testCaseIncidentStatus` | get | List the test case failure statuses | ❌ |
| `/v1/dataQuality/testCases/testCaseIncidentStatus` | post | Create a new test case failure status | ❌ |
| `/v1/dataQuality/testCases/testCaseIncidentStatus/stateId/{stateId}` | get | Get test case failure statuses for a sequence id | ❌ |
| `/v1/dataQuality/testCases/testCaseIncidentStatus/{id}` | get | Get test case failure status by id | ❌ |
| `/v1/dataQuality/testCases/testCaseIncidentStatus/{id}` | patch | Update an existing test case failure status | ❌ |
| `/v1/dataQuality/testCases/testCaseResults/search/latest` | get | Latest test case results using search service | ❌ |
| `/v1/dataQuality/testCases/testCaseResults/search/list` | get | List test case results using search service | ❌ |
| `/v1/dataQuality/testCases/testCaseResults/{fqn}` | get | List of test case results for a given test case | ❌ |
| `/v1/dataQuality/testCases/testCaseResults/{fqn}` | post | Add test case result data to a testCase | ❌ |
| `/v1/dataQuality/testCases/testCaseResults/{fqn}/{timestamp}` | delete | Delete test case result | ❌ |
| `/v1/dataQuality/testCases/testCaseResults/{fqn}/{timestamp}` | patch | Update a test case result | ❌ |
| `/v1/dataQuality/testCases/{fqn}/testCaseResult` | get | List of test case results | ❌ |
| `/v1/dataQuality/testCases/{fqn}/testCaseResult` | put | Add test case result data | ❌ |
| `/v1/dataQuality/testCases/{fqn}/testCaseResult/{timestamp}` | delete | Delete test case result | ❌ |
| `/v1/dataQuality/testCases/{fqn}/testCaseResult/{timestamp}` | patch | Update a test case result | ❌ |
| `/v1/dataQuality/testCases/{id}` | get | Get a test case by Id | ❌ |
| `/v1/dataQuality/testCases/{id}` | delete | Delete a test case by Id | ❌ |
| `/v1/dataQuality/testCases/{id}` | patch | Update a test case | ❌ |
| `/v1/dataQuality/testCases/{id}/failedRowsSample` | get | Get failed rows sample data | ❌ |
| `/v1/dataQuality/testCases/{id}/failedRowsSample` | put | Add failed rows sample data | ❌ |
| `/v1/dataQuality/testCases/{id}/failedRowsSample` | delete | Delete failed rows sample data | ❌ |
| `/v1/dataQuality/testCases/{id}/inspectionQuery` | put | Add inspection query data | ❌ |
| `/v1/dataQuality/testCases/{id}/versions` | get | List test case versions | ❌ |
| `/v1/dataQuality/testCases/{id}/versions/{version}` | get | Get a version of the test case | ❌ |
| `/v1/dataQuality/testDefinitions` | get | List test definitions | ❌ |
| `/v1/dataQuality/testDefinitions` | put | Update test definition | ❌ |
| `/v1/dataQuality/testDefinitions` | post | Create a test definition | ❌ |
| `/v1/dataQuality/testDefinitions/name/{name}` | get | Get a test definition by name | ❌ |
| `/v1/dataQuality/testDefinitions/name/{name}` | delete | Delete a test definition | ❌ |
| `/v1/dataQuality/testDefinitions/restore` | put | Restore a soft deleted test definition | ❌ |
| `/v1/dataQuality/testDefinitions/{id}` | get | Get a test definition by Id | ❌ |
| `/v1/dataQuality/testDefinitions/{id}` | delete | Delete a test definition | ❌ |
| `/v1/dataQuality/testDefinitions/{id}` | patch | Update a test definition | ❌ |
| `/v1/dataQuality/testDefinitions/{id}/versions` | get | List test definition versions | ❌ |
| `/v1/dataQuality/testDefinitions/{id}/versions/{version}` | get | Get a version of the test definition | ❌ |
| `/v1/dataQuality/testSuites` | get | List test suites | ❌ |
| `/v1/dataQuality/testSuites` | put | Update logical test suite | ❌ |
| `/v1/dataQuality/testSuites` | post | Create a logical test suite | ❌ |
| `/v1/dataQuality/testSuites/basic` | put | Create or Update Basic test suite | ❌ |
| `/v1/dataQuality/testSuites/basic` | post | Create a basic test suite | ❌ |
| `/v1/dataQuality/testSuites/basic/name/{name}` | delete | Delete a test suite | ❌ |
| `/v1/dataQuality/testSuites/basic/{id}` | delete | Delete a test suite | ❌ |
| `/v1/dataQuality/testSuites/dataQualityReport` | get | Get Data Quality Report | ❌ |
| `/v1/dataQuality/testSuites/executable` | put | Create or Update Executable test suite | ❌ |
| `/v1/dataQuality/testSuites/executable` | post | Create an executable test suite | ❌ |
| `/v1/dataQuality/testSuites/executable/name/{name}` | delete | Delete a test suite | ❌ |
| `/v1/dataQuality/testSuites/executable/{id}` | delete | Delete a test suite | ❌ |
| `/v1/dataQuality/testSuites/executionSummary` | get | Get the execution summary of test suites | ❌ |
| `/v1/dataQuality/testSuites/name/{name}` | get | Get a test suite by name | ❌ |
| `/v1/dataQuality/testSuites/name/{name}` | delete | Delete a logical test suite | ❌ |
| `/v1/dataQuality/testSuites/restore` | put | Restore a soft deleted test suite | ❌ |
| `/v1/dataQuality/testSuites/search/list` | get | List test suite using search service | ❌ |
| `/v1/dataQuality/testSuites/{id}` | get | Get a test suite by Id | ❌ |
| `/v1/dataQuality/testSuites/{id}` | delete | Delete a logical test suite | ❌ |
| `/v1/dataQuality/testSuites/{id}` | patch | Update a test suite | ❌ |
| `/v1/dataQuality/testSuites/{id}/versions` | get | List test suite versions | ❌ |
| `/v1/dataQuality/testSuites/{id}/versions/{version}` | get | Get a version of the test suite | ❌ |
| `/v1/databaseSchemas` | get | List database schemas | ❌ |
| `/v1/databaseSchemas` | put | Create or update schema | ❌ |
| `/v1/databaseSchemas` | post | Create a schema | ❌ |
| `/v1/databaseSchemas/entityRelationship` | get | Search Schema Entity Relationship | ❌ |
| `/v1/databaseSchemas/name/{fqn}` | get | Get a schema by fully qualified name | ❌ |
| `/v1/databaseSchemas/name/{fqn}` | delete | Delete a schema by fully qualified name | ❌ |
| `/v1/databaseSchemas/name/{fqn}` | patch | Update a database schema by name. | ❌ |
| `/v1/databaseSchemas/name/{name}/export` | get | Export database schema in CSV format | ❌ |
| `/v1/databaseSchemas/name/{name}/exportAsync` | get | Export database schema in CSV format | ❌ |
| `/v1/databaseSchemas/name/{name}/import` | put | Import tables from CSV to update database schema (no creation allowed) | ❌ |
| `/v1/databaseSchemas/name/{name}/importAsync` | put | Import tables from CSV to update database schema asynchronously (no creation allowed) | ❌ |
| `/v1/databaseSchemas/restore` | put | Restore a soft deleted database schema. | ❌ |
| `/v1/databaseSchemas/{id}` | get | Get a schema by Id | ❌ |
| `/v1/databaseSchemas/{id}` | delete | Delete a schema by Id | ❌ |
| `/v1/databaseSchemas/{id}` | patch | Update a database schema | ❌ |
| `/v1/databaseSchemas/{id}/databaseSchemaProfilerConfig` | get | Get databaseSchema profile config | ❌ |
| `/v1/databaseSchemas/{id}/databaseSchemaProfilerConfig` | put | Add databaseSchema profile config | ❌ |
| `/v1/databaseSchemas/{id}/databaseSchemaProfilerConfig` | delete | Delete database profiler config | ❌ |
| `/v1/databaseSchemas/{id}/versions` | get | List schema versions | ❌ |
| `/v1/databaseSchemas/{id}/versions/{version}` | get | Get a version of the schema | ❌ |
| `/v1/databaseSchemas/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/databases` | get | List databases | ❌ |
| `/v1/databases` | put | Create or update database | ❌ |
| `/v1/databases` | post | Create a database | ❌ |
| `/v1/databases/name/{fqn}` | get | Get a database by fully qualified name | ❌ |
| `/v1/databases/name/{fqn}` | delete | Delete a database by fully qualified name | ❌ |
| `/v1/databases/name/{fqn}` | patch | Update a database by name. | ❌ |
| `/v1/databases/name/{name}/export` | get | Export database in CSV format | ❌ |
| `/v1/databases/name/{name}/exportAsync` | get | Export database in CSV format | ❌ |
| `/v1/databases/name/{name}/import` | put | Import database schemas from CSV to update database schemas (no creation allowed) | ❌ |
| `/v1/databases/name/{name}/importAsync` | put | Import database schemas from CSV asynchronously | ❌ |
| `/v1/databases/restore` | put | Restore a soft deleted Database. | ❌ |
| `/v1/databases/{id}` | get | Get a database by Id | ❌ |
| `/v1/databases/{id}` | delete | Delete a database by Id | ❌ |
| `/v1/databases/{id}` | patch | Update a database | ❌ |
| `/v1/databases/{id}/databaseProfilerConfig` | get | Get database profile config | ❌ |
| `/v1/databases/{id}/databaseProfilerConfig` | put | Add database profile config | ❌ |
| `/v1/databases/{id}/databaseProfilerConfig` | delete | Delete database profiler config | ❌ |
| `/v1/databases/{id}/versions` | get | List database versions | ❌ |
| `/v1/databases/{id}/versions/{version}` | get | Get a version of the database | ❌ |
| `/v1/databases/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/docStore` | get | List Documents | ❌ |
| `/v1/docStore` | put | Update Document | ❌ |
| `/v1/docStore` | post | Create a Document | ❌ |
| `/v1/docStore/name/{fqn}` | patch | Update a Document by name. | ❌ |
| `/v1/docStore/name/{name}` | get | Get a Document by name | ❌ |
| `/v1/docStore/name/{name}` | delete | Delete a Document by name | ❌ |
| `/v1/docStore/resetEmailTemplate` | post | Reset seed data of EmailTemplate type | ❌ |
| `/v1/docStore/validateTemplate/{templateName}` | put | Validate Email Template | ❌ |
| `/v1/docStore/{id}` | get | Get a Document by id | ❌ |
| `/v1/docStore/{id}` | delete | Delete a Document by id | ❌ |
| `/v1/docStore/{id}` | patch | Update a Document. | ❌ |
| `/v1/docStore/{id}/versions` | get | List Document versions | ❌ |
| `/v1/docStore/{id}/versions/{version}` | get | Get a version of the Document | ❌ |
| `/v1/domains` | get | List domains | ❌ |
| `/v1/domains` | put | Create or update a domain | ❌ |
| `/v1/domains` | post | Create a domain | ❌ |
| `/v1/domains/hierarchy` | get | List domains in hierarchical order | ❌ |
| `/v1/domains/name/{fqn}` | patch | Update a domain by name. | ❌ |
| `/v1/domains/name/{name}` | get | Get a domain by name | ❌ |
| `/v1/domains/name/{name}` | delete | Delete a domain by name | ❌ |
| `/v1/domains/{id}` | get | Get a domain by Id | ❌ |
| `/v1/domains/{id}` | delete | Delete a domain by Id | ❌ |
| `/v1/domains/{id}` | patch | Update a domain | ❌ |
| `/v1/domains/{id}/versions` | get | List domain versions | ❌ |
| `/v1/domains/{id}/versions/{version}` | get | Get a version of the domain | ❌ |
| `/v1/domains/{name}/assets/add` | put | Bulk Add Assets | ❌ |
| `/v1/domains/{name}/assets/remove` | put | Bulk Remove Assets | ❌ |
| `/v1/events` | get | Get change events | ❌ |
| `/v1/events/subscriptions` | get | List all available Event Subscriptions | ❌ |
| `/v1/events/subscriptions` | put | Updated an existing or create a new Event Subscription | ❌ |
| `/v1/events/subscriptions` | post | Create a new Event Subscription | ❌ |
| `/v1/events/subscriptions/id/{eventSubscriptionId}/destinations` | get | Get the destinations for a specific Event Subscription | ❌ |
| `/v1/events/subscriptions/id/{id}/failedEvents` | get | Get failed events for a subscription by id | ❌ |
| `/v1/events/subscriptions/id/{id}/listEvents` | get | Retrieve events based on various filters | ❌ |
| `/v1/events/subscriptions/id/{id}/listSuccessfullySentChangeEvents` | get | Get successfully sent change events for an alert | ❌ |
| `/v1/events/subscriptions/id/{subscriptionId}/diagnosticInfo` | get | Get event subscription diagnostic info | ❌ |
| `/v1/events/subscriptions/id/{subscriptionId}/eventsRecord` | get | Get event subscription events record | ❌ |
| `/v1/events/subscriptions/listAllFailedEvents` | get | Get all failed events | ❌ |
| `/v1/events/subscriptions/name/{eventSubscriptionName}` | get | Get an Event Subscription by name | ❌ |
| `/v1/events/subscriptions/name/{eventSubscriptionName}/destinations` | get | Get the destinations for a specific Event Subscription by its name | ❌ |
| `/v1/events/subscriptions/name/{eventSubscriptionName}/failedEvents` | get | Get failed events for a subscription by name | ❌ |
| `/v1/events/subscriptions/name/{eventSubscriptionName}/listSuccessfullySentChangeEvents` | get | Get successfully sent change events for an alert by name | ❌ |
| `/v1/events/subscriptions/name/{eventSubscriptionName}/status/{destinationId}` | get | Get Event Subscription status | ❌ |
| `/v1/events/subscriptions/name/{eventSubscriptionName}/syncOffset` | put | Sync Offset for a specific Event Subscription by its name | ❌ |
| `/v1/events/subscriptions/name/{fqn}` | patch | Update an Event Subscriptions by name. | ❌ |
| `/v1/events/subscriptions/name/{name}` | delete | Delete an Event Subscription by name | ❌ |
| `/v1/events/subscriptions/name/{subscriptionName}/diagnosticInfo` | get | Get event subscription diagnostic info by name | ❌ |
| `/v1/events/subscriptions/name/{subscriptionName}/eventsRecord` | get | Get event subscription events record by name | ❌ |
| `/v1/events/subscriptions/testDestination` | post | Send a test message alert to external destinations. | ❌ |
| `/v1/events/subscriptions/validation/condition/{expression}` | get | Validate a given condition | ❌ |
| `/v1/events/subscriptions/{alertType}/resources` | get | Get list of Event Subscriptions Resources used in filtering Event Subscription | ❌ |
| `/v1/events/subscriptions/{eventSubscriptionId}/status/{destinationId}` | get | Get Event Subscription status by Id | ❌ |
| `/v1/events/subscriptions/{id}` | get | Get a event Subscription by ID | ❌ |
| `/v1/events/subscriptions/{id}` | delete | Delete an Event Subscription by Id | ❌ |
| `/v1/events/subscriptions/{id}` | patch | Update an Event Subscriptions | ❌ |
| `/v1/events/subscriptions/{id}/processedEvents` | get | Check If the Publisher Processed All Events | ❌ |
| `/v1/events/subscriptions/{id}/versions` | get | List Event Subscription versions | ❌ |
| `/v1/events/subscriptions/{id}/versions/{version}` | get | Get a version of the Event Subscription | ❌ |
| `/v1/feed` | get | List threads | ❌ |
| `/v1/feed` | post | Create a thread | ❌ |
| `/v1/feed/count` | get | Count of threads | ❌ |
| `/v1/feed/tasks/{id}` | get | Get a task thread by task Id | ❌ |
| `/v1/feed/tasks/{id}/close` | put | Close a task | ❌ |
| `/v1/feed/tasks/{id}/resolve` | put | Resolve a task | ❌ |
| `/v1/feed/{id}` | get | Get a thread by Id | ❌ |
| `/v1/feed/{id}` | patch | Update a thread by `Id`. | ❌ |
| `/v1/feed/{id}/posts` | get | Get all the posts of a thread | ❌ |
| `/v1/feed/{id}/posts` | post | Add post to a thread | ❌ |
| `/v1/feed/{threadId}` | delete | Delete a thread by Id | ❌ |
| `/v1/feed/{threadId}/posts/{postId}` | delete | Delete a post from its thread | ❌ |
| `/v1/feed/{threadId}/posts/{postId}` | patch | Update post of a thread by `Id`. | ❌ |
| `/v1/glossaries` | get | List glossaries | ❌ |
| `/v1/glossaries` | put | Create or update a glossary | ❌ |
| `/v1/glossaries` | post | Create a glossary | ❌ |
| `/v1/glossaries/documentation/csv` | get | Get CSV documentation | ❌ |
| `/v1/glossaries/name/{fqn}` | patch | Update a glossary using name. | ❌ |
| `/v1/glossaries/name/{name}` | get | Get a glossary by name | ❌ |
| `/v1/glossaries/name/{name}` | delete | Delete a glossary by name | ❌ |
| `/v1/glossaries/name/{name}/export` | get | Export glossary in CSV format | ❌ |
| `/v1/glossaries/name/{name}/exportAsync` | get | Export glossary in CSV format | ❌ |
| `/v1/glossaries/name/{name}/import` | put | Import glossary terms from CSV to create, and update glossary terms | ❌ |
| `/v1/glossaries/name/{name}/importAsync` | put | Import glossary in CSV format asynchronously | ❌ |
| `/v1/glossaries/restore` | put | Restore a soft deleted glossary | ❌ |
| `/v1/glossaries/{id}` | get | Get a glossary by Id | ❌ |
| `/v1/glossaries/{id}` | delete | Delete a glossary by Id | ❌ |
| `/v1/glossaries/{id}` | patch | Update a glossary | ❌ |
| `/v1/glossaries/{id}/versions` | get | List glossary versions | ❌ |
| `/v1/glossaries/{id}/versions/{version}` | get | Get a version of the glossaries | ❌ |
| `/v1/glossaries/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/glossaryTerms` | get | List glossary terms | ❌ |
| `/v1/glossaryTerms` | put | Create or update a glossary term | ❌ |
| `/v1/glossaryTerms` | post | Create a glossary term | ❌ |
| `/v1/glossaryTerms/name/{fqn}` | get | Get a glossary term by fully qualified name | ❌ |
| `/v1/glossaryTerms/name/{fqn}` | delete | Delete a glossary term by fully qualified name | ❌ |
| `/v1/glossaryTerms/name/{fqn}` | patch | Update a glossary term by name. | ❌ |
| `/v1/glossaryTerms/restore` | put | Restore a soft deleted glossary term | ❌ |
| `/v1/glossaryTerms/{id}` | get | Get a glossary term by Id | ❌ |
| `/v1/glossaryTerms/{id}` | delete | Delete a glossary term by Id | ❌ |
| `/v1/glossaryTerms/{id}` | patch | Update a glossary term | ❌ |
| `/v1/glossaryTerms/{id}/assets/add` | put | Bulk Add Glossary Term to Assets | ❌ |
| `/v1/glossaryTerms/{id}/assets/remove` | put | Bulk Remove Glossary Term from Assets | ❌ |
| `/v1/glossaryTerms/{id}/tags/validate` | put | Validate Tags Addition to Glossary Term | ❌ |
| `/v1/glossaryTerms/{id}/versions` | get | List glossary term versions | ❌ |
| `/v1/glossaryTerms/{id}/versions/{version}` | get | Get a version of the glossary term | ❌ |
| `/v1/glossaryTerms/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/governance/workflowDefinitions` | get | List Workflow Definitions | ❌ |
| `/v1/governance/workflowDefinitions` | put | Create or update Workflow Definition | ❌ |
| `/v1/governance/workflowDefinitions` | post | Create a Workflow Definition | ❌ |
| `/v1/governance/workflowDefinitions/name/{fqn}` | get | Get a Workflow Definition by fully qualified name | ❌ |
| `/v1/governance/workflowDefinitions/name/{fqn}` | delete | Delete a Workflow Definition by fully qualified name | ❌ |
| `/v1/governance/workflowDefinitions/name/{fqn}` | patch | Update a Workflow Definition by name. | ❌ |
| `/v1/governance/workflowDefinitions/name/{fqn}/trigger` | post | Start a new instance of a Workflow Definition | ❌ |
| `/v1/governance/workflowDefinitions/restore` | put | Restore a soft deleted Workflow Definition. | ❌ |
| `/v1/governance/workflowDefinitions/{id}` | get | Get a Workflow Definition by Id | ❌ |
| `/v1/governance/workflowDefinitions/{id}` | delete | Delete a Workflow Definition by Id | ❌ |
| `/v1/governance/workflowDefinitions/{id}` | patch | Update a Workflow Definition by Id | ❌ |
| `/v1/governance/workflowDefinitions/{id}/versions` | get | List Workflow Definition versions | ❌ |
| `/v1/governance/workflowDefinitions/{id}/versions/{version}` | get | Get a version of the Workflow Definition | ❌ |
| `/v1/governance/workflowInstanceStates` | get | List the Workflow Instance States | ❌ |
| `/v1/governance/workflowInstanceStates/{id}` | get | Get a Workflow Instance State by id | ❌ |
| `/v1/governance/workflowInstanceStates/{workflowDefinitionName}/{workflowInstanceId}` | get | Get all the Workflow Instance States for a Workflow Instance id | ❌ |
| `/v1/governance/workflowInstances` | get | List the Workflow Instances | ❌ |
| `/v1/lineage` | put | Add a lineage edge | ❌ |
| `/v1/lineage/export` | get | Export lineage | ❌ |
| `/v1/lineage/exportAsync` | get | Export lineage | ❌ |
| `/v1/lineage/getDataQualityLineage` | get | Search Data Quality lineage | ❌ |
| `/v1/lineage/getLineage` | get | Search lineage | ❌ |
| `/v1/lineage/getLineageEdge/{fromId}/{toId}` | get | Get  a lineage edge | ❌ |
| `/v1/lineage/{entityType}/{entityId}/type/{lineageSource}` | delete | Delete a lineage edge by Type | ❌ |
| `/v1/lineage/{entity}/name/{fqn}` | get | Get lineage by fully qualified name | ❌ |
| `/v1/lineage/{entity}/{id}` | get | Get lineage by Id | ❌ |
| `/v1/lineage/{fromEntity}/name/{fromFQN}/{toEntity}/name/{toFQN}` | delete | Delete a lineage edge by FQNs | ❌ |
| `/v1/lineage/{fromEntity}/{fromId}/{toEntity}/{toId}` | delete | Delete a lineage edge | ❌ |
| `/v1/lineage/{fromEntity}/{fromId}/{toEntity}/{toId}` | patch | Patch a lineage edge | ❌ |
| `/v1/metadata/types` | get | List types | ❌ |
| `/v1/metadata/types` | put | Create or update a type | ❌ |
| `/v1/metadata/types` | post | Create a type | ❌ |
| `/v1/metadata/types/customProperties` | get |  | ❌ |
| `/v1/metadata/types/fields/{entityType}` | get |  | ❌ |
| `/v1/metadata/types/name/{fqn}` | patch | Update a type using name. | ❌ |
| `/v1/metadata/types/name/{name}` | get | Get a type by name | ❌ |
| `/v1/metadata/types/name/{name}` | delete | Delete a type by name | ❌ |
| `/v1/metadata/types/{id}` | get | Get a type | ❌ |
| `/v1/metadata/types/{id}` | put | Add or update a Property to an entity | ❌ |
| `/v1/metadata/types/{id}` | delete | Delete a type by id | ❌ |
| `/v1/metadata/types/{id}` | patch | Update a type | ❌ |
| `/v1/metadata/types/{id}/versions` | get | List type versions | ❌ |
| `/v1/metadata/types/{id}/versions/{version}` | get | Get a version of the types | ❌ |
| `/v1/metrics` | get | List metrics | ❌ |
| `/v1/metrics` | put | Create or update a metric | ❌ |
| `/v1/metrics` | post | Create a Metric | ❌ |
| `/v1/metrics/name/{fqn}` | get | Get a Metric by fully qualified name. | ❌ |
| `/v1/metrics/name/{fqn}` | delete | Delete a Metric by fully qualified name | ❌ |
| `/v1/metrics/name/{fqn}` | patch | Update a Metric using name. | ❌ |
| `/v1/metrics/restore` | put | Restore a soft deleted Metric. | ❌ |
| `/v1/metrics/{id}` | get | Get a metric by Id | ❌ |
| `/v1/metrics/{id}` | delete | Delete a Metric by id | ❌ |
| `/v1/metrics/{id}` | patch | Update a Metric | ❌ |
| `/v1/metrics/{id}/followers` | put | Add a follower | ❌ |
| `/v1/metrics/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/metrics/{id}/versions` | get | List Metric versions | ❌ |
| `/v1/metrics/{id}/versions/{version}` | get | Get a version of the Metric | ❌ |
| `/v1/metrics/{id}/vote` | put | Update Vote for a Metric | ❌ |
| `/v1/mlmodels` | get | List ML models | ❌ |
| `/v1/mlmodels` | put | Create or update an ML model | ❌ |
| `/v1/mlmodels` | post | Create an ML model | ❌ |
| `/v1/mlmodels/name/{fqn}` | get | Get an ML model by fully qualified name | ❌ |
| `/v1/mlmodels/name/{fqn}` | delete | Delete a ML model by fully qualified name | ❌ |
| `/v1/mlmodels/name/{fqn}` | patch | Update an ML model by name. | ❌ |
| `/v1/mlmodels/restore` | put | Restore a soft deleted ML model | ❌ |
| `/v1/mlmodels/{id}` | get | Get an ML model by Id | ❌ |
| `/v1/mlmodels/{id}` | delete | Delete an ML model by Id | ❌ |
| `/v1/mlmodels/{id}` | patch | Update an ML model | ❌ |
| `/v1/mlmodels/{id}/followers` | put | Add a follower | ❌ |
| `/v1/mlmodels/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/mlmodels/{id}/versions` | get | List ML model versions | ❌ |
| `/v1/mlmodels/{id}/versions/{version}` | get | Get a version of the ML model | ❌ |
| `/v1/mlmodels/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/permissions` | get | Get permissions for logged in user | ❌ |
| `/v1/permissions/policies` | get | Get permissions for a set of policies | ❌ |
| `/v1/permissions/{resource}` | get | Get permissions a given resource/entity type for logged in user | ❌ |
| `/v1/permissions/{resource}/name/{name}` | get | Get permissions for a given entity name for a logged in user | ❌ |
| `/v1/permissions/{resource}/{id}` | get | Get permissions for a given entity for a logged in user | ❌ |
| `/v1/personas` | get | List personas | ❌ |
| `/v1/personas` | put | Update Persona | ❌ |
| `/v1/personas` | post | Create a Persona | ❌ |
| `/v1/personas/name/{fqn}` | patch | Update a Persona using name. | ❌ |
| `/v1/personas/name/{name}` | get | Get a Persona by name | ❌ |
| `/v1/personas/name/{name}` | delete | Delete a Persona by name | ❌ |
| `/v1/personas/{id}` | get | Get a persona by id | ❌ |
| `/v1/personas/{id}` | delete | Delete a Persona by id | ❌ |
| `/v1/personas/{id}` | patch | Update a Persona | ❌ |
| `/v1/personas/{id}/versions` | get | List Persona versions | ❌ |
| `/v1/personas/{id}/versions/{version}` | get | Get a version of the Persona | ❌ |
| `/v1/pipelines` | get | List pipelines | ❌ |
| `/v1/pipelines` | put | Create or update a pipeline | ❌ |
| `/v1/pipelines` | post | Create a pipeline | ❌ |
| `/v1/pipelines/name/{fqn}` | get | Get a pipeline by fully qualified name | ❌ |
| `/v1/pipelines/name/{fqn}` | delete | Delete a pipeline by fully qualified name | ❌ |
| `/v1/pipelines/name/{fqn}` | patch | Update a pipeline by name. | ❌ |
| `/v1/pipelines/restore` | put | Restore a soft deleted pipeline | ❌ |
| `/v1/pipelines/{fqn}/status` | get | List pipeline status | ❌ |
| `/v1/pipelines/{fqn}/status` | put | Add status data | ❌ |
| `/v1/pipelines/{fqn}/status/{timestamp}` | delete | Delete pipeline status | ❌ |
| `/v1/pipelines/{id}` | get | Get a pipeline by Id | ❌ |
| `/v1/pipelines/{id}` | delete | Delete a pipeline by Id | ❌ |
| `/v1/pipelines/{id}` | patch | Update a pipeline | ❌ |
| `/v1/pipelines/{id}/followers` | put | Add a follower | ❌ |
| `/v1/pipelines/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/pipelines/{id}/versions` | get | List pipeline versions | ❌ |
| `/v1/pipelines/{id}/versions/{version}` | get | Get a version of the pipeline | ❌ |
| `/v1/pipelines/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/policies` | get | List policies | ❌ |
| `/v1/policies` | put | Create or update a policy | ❌ |
| `/v1/policies` | post | Create a policy | ❌ |
| `/v1/policies/functions` | get | Get list of policy functions used in authoring conditions in policy rules. | ❌ |
| `/v1/policies/name/{fqn}` | get | Get a policy by fully qualified name | ❌ |
| `/v1/policies/name/{fqn}` | delete | Delete a policy by fully qualified name | ❌ |
| `/v1/policies/name/{fqn}` | patch | Update a policy by name. | ❌ |
| `/v1/policies/resources` | get | Get list of policy resources used in authoring a policy | ❌ |
| `/v1/policies/restore` | put | Restore a soft deleted policy | ❌ |
| `/v1/policies/validation/condition/{expression}` | get | Validate a given condition | ❌ |
| `/v1/policies/{id}` | get | Get a policy by id | ❌ |
| `/v1/policies/{id}` | delete | Delete a policy by Id | ❌ |
| `/v1/policies/{id}` | patch | Update a policy | ❌ |
| `/v1/policies/{id}/versions` | get | List policy versions | ❌ |
| `/v1/policies/{id}/versions/{version}` | get | Get a version of the policy by Id | ❌ |
| `/v1/queries` | get | Get a list of Queries | ❌ |
| `/v1/queries` | put | Create or update a query | ❌ |
| `/v1/queries` | post | Create a query | ❌ |
| `/v1/queries/name/{fqn}` | get | Get a query by name | ❌ |
| `/v1/queries/name/{fqn}` | delete | Delete a query | ❌ |
| `/v1/queries/name/{fqn}` | patch | Update a query using name. | ❌ |
| `/v1/queries/restore` | put | Restore a soft deleted Query | ❌ |
| `/v1/queries/{id}` | get | Get a query | ❌ |
| `/v1/queries/{id}` | delete | Delete a query | ❌ |
| `/v1/queries/{id}` | patch | Update a query | ❌ |
| `/v1/queries/{id}/followers` | put | Add a follower | ❌ |
| `/v1/queries/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/queries/{id}/usage` | put | Add query usage | ❌ |
| `/v1/queries/{id}/usage` | delete | remove query used in | ❌ |
| `/v1/queries/{id}/usedBy` | put | Populate Used By Field | ❌ |
| `/v1/queries/{id}/users` | put | Add query users | ❌ |
| `/v1/queries/{id}/versions` | get | Get List of all query versions | ❌ |
| `/v1/queries/{id}/versions/{version}` | get | Get a specific version of the query | ❌ |
| `/v1/queries/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/reports` | get | List reports | ❌ |
| `/v1/reports` | put | Create or update a report | ❌ |
| `/v1/reports` | post | Create a report | ❌ |
| `/v1/reports/{id}` | get | Get a report by Id | ❌ |
| `/v1/reports/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/roles` | get | List roles | ❌ |
| `/v1/roles` | put | Update role | ❌ |
| `/v1/roles` | post | Create a role | ❌ |
| `/v1/roles/name/{fqn}` | patch | Update a role using name. | ❌ |
| `/v1/roles/name/{name}` | get | Get a role by name | ❌ |
| `/v1/roles/name/{name}` | delete | Delete a role | ❌ |
| `/v1/roles/restore` | put | Restore a soft deleted role | ❌ |
| `/v1/roles/{id}` | get | Get a role by id | ❌ |
| `/v1/roles/{id}` | delete | Delete a role | ❌ |
| `/v1/roles/{id}` | patch | Update a role | ❌ |
| `/v1/roles/{id}/versions` | get | List role versions | ❌ |
| `/v1/roles/{id}/versions/{version}` | get | Get a version of the role | ❌ |
| `/v1/search/aggregate` | get | Get aggregated fields | ❌ |
| `/v1/search/fieldQuery` | get | Search entities | ❌ |
| `/v1/search/get/{index}/doc/{id}` | get | Search entities in ES index with Id | ❌ |
| `/v1/search/query` | get | Search entities | ✅ |
| `/v1/search/reindex/stream/status` | get | Get Stream Job Latest Status | ❌ |
| `/v1/search/sourceUrl` | get | Search entities | ❌ |
| `/v1/search/suggest` | get | Suggest entities | ❌ |
| `/v1/searchIndexes` | get | List searchIndexes | ❌ |
| `/v1/searchIndexes` | put | Update SearchIndex | ❌ |
| `/v1/searchIndexes` | post | Create a SearchIndex | ❌ |
| `/v1/searchIndexes/name/{fqn}` | get | Get a SearchIndex by fully qualified name | ❌ |
| `/v1/searchIndexes/name/{fqn}` | delete | Delete a SearchIndex by fully qualified name | ❌ |
| `/v1/searchIndexes/name/{fqn}` | patch | Update a SearchIndex using name. | ❌ |
| `/v1/searchIndexes/restore` | put | Restore a soft deleted SearchIndex | ❌ |
| `/v1/searchIndexes/{id}` | get | Get a SearchIndex by id | ❌ |
| `/v1/searchIndexes/{id}` | delete | Delete a SearchIndex by id | ❌ |
| `/v1/searchIndexes/{id}` | patch | Update a SearchIndex | ❌ |
| `/v1/searchIndexes/{id}/followers` | put | Add a follower | ❌ |
| `/v1/searchIndexes/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/searchIndexes/{id}/sampleData` | get | Get sample data | ❌ |
| `/v1/searchIndexes/{id}/sampleData` | put | Add sample data | ❌ |
| `/v1/searchIndexes/{id}/versions` | get | List SearchIndex versions | ❌ |
| `/v1/searchIndexes/{id}/versions/{version}` | get | Get a version of the SearchIndex | ❌ |
| `/v1/searchIndexes/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/services/apiServices` | get | List API services | ❌ |
| `/v1/services/apiServices` | put | Update API service | ❌ |
| `/v1/services/apiServices` | post | Create API service | ❌ |
| `/v1/services/apiServices/name/{fqn}` | delete | Delete an APIService by fully qualified name | ❌ |
| `/v1/services/apiServices/name/{fqn}` | patch | Update an API service using name. | ❌ |
| `/v1/services/apiServices/name/{name}` | get | Get API service by name | ❌ |
| `/v1/services/apiServices/restore` | put | Restore a soft deleted API Service. | ❌ |
| `/v1/services/apiServices/{id}` | get | Get an API service | ❌ |
| `/v1/services/apiServices/{id}` | delete | Delete an API service | ❌ |
| `/v1/services/apiServices/{id}` | patch | Update an API service | ❌ |
| `/v1/services/apiServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/apiServices/{id}/versions` | get | List API service versions | ❌ |
| `/v1/services/apiServices/{id}/versions/{version}` | get | Get a version of the API service | ❌ |
| `/v1/services/dashboardServices` | get | List dashboard services | ❌ |
| `/v1/services/dashboardServices` | put | Update a dashboard service | ❌ |
| `/v1/services/dashboardServices` | post | Create a dashboard service | ❌ |
| `/v1/services/dashboardServices/name/{fqn}` | patch | Update a dashboard service using name. | ❌ |
| `/v1/services/dashboardServices/name/{name}` | get | Get dashboard service by name | ❌ |
| `/v1/services/dashboardServices/name/{name}` | delete | Delete a dashboard service by name | ❌ |
| `/v1/services/dashboardServices/restore` | put | Restore a soft deleted dashboard service | ❌ |
| `/v1/services/dashboardServices/{id}` | get | Get a dashboard service by Id | ❌ |
| `/v1/services/dashboardServices/{id}` | delete | Delete a dashboard service by Id | ❌ |
| `/v1/services/dashboardServices/{id}` | patch | Update a dashboard service | ❌ |
| `/v1/services/dashboardServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/dashboardServices/{id}/versions` | get | List dashboard service versions | ❌ |
| `/v1/services/dashboardServices/{id}/versions/{version}` | get | Get a version of the dashboard service | ❌ |
| `/v1/services/databaseServices` | get | List database services | ❌ |
| `/v1/services/databaseServices` | put | Update database service | ❌ |
| `/v1/services/databaseServices` | post | Create database service | ❌ |
| `/v1/services/databaseServices/name/{fqn}` | patch | Update a database service using name. | ❌ |
| `/v1/services/databaseServices/name/{name}` | get | Get database service by name | ❌ |
| `/v1/services/databaseServices/name/{name}` | delete | Delete a database service by name | ❌ |
| `/v1/services/databaseServices/name/{name}/export` | get | Export database service in CSV format | ❌ |
| `/v1/services/databaseServices/name/{name}/exportAsync` | get | Export database service in CSV format | ❌ |
| `/v1/services/databaseServices/name/{name}/import` | put | Import service from CSV to update database service (no creation allowed) | ❌ |
| `/v1/services/databaseServices/name/{name}/importAsync` | put | Import service from CSV to update database service asynchronously (no creation allowed) | ❌ |
| `/v1/services/databaseServices/restore` | put | Restore a soft deleted database service | ❌ |
| `/v1/services/databaseServices/{id}` | get | Get a database service | ❌ |
| `/v1/services/databaseServices/{id}` | delete | Delete a database service by Id | ❌ |
| `/v1/services/databaseServices/{id}` | patch | Update a database service | ❌ |
| `/v1/services/databaseServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/databaseServices/{id}/versions` | get | List database service versions | ❌ |
| `/v1/services/databaseServices/{id}/versions/{version}` | get | Get a version of the database service | ❌ |
| `/v1/services/ingestionPipelines` | get | List ingestion pipelines for metadata operations | ❌ |
| `/v1/services/ingestionPipelines` | put | Create or update an ingestion pipeline | ❌ |
| `/v1/services/ingestionPipelines` | post | Create an ingestion pipeline | ❌ |
| `/v1/services/ingestionPipelines/bulk/deploy` | post | Bulk deploy a list of Ingestion Pipeline | ❌ |
| `/v1/services/ingestionPipelines/deploy/{id}` | post | Deploy an ingestion pipeline run | ❌ |
| `/v1/services/ingestionPipelines/ip` | get | Check the airflow REST host IP | ❌ |
| `/v1/services/ingestionPipelines/kill/{id}` | post | Mark as failed and kill any not-finished workflow or task for the ingestion pipeline | ❌ |
| `/v1/services/ingestionPipelines/logs/{id}/last` | get | Retrieve all logs from last ingestion pipeline run | ❌ |
| `/v1/services/ingestionPipelines/name/{fqn}` | get | Get an ingestion pipeline by fully qualified name | ❌ |
| `/v1/services/ingestionPipelines/name/{fqn}` | delete | Delete an ingestion pipeline by fully qualified name | ❌ |
| `/v1/services/ingestionPipelines/name/{fqn}` | patch | Update an ingestion pipeline using name. | ❌ |
| `/v1/services/ingestionPipelines/restore` | put | Restore a soft deleted ingestion pipeline | ❌ |
| `/v1/services/ingestionPipelines/status` | get | Check the airflow REST status | ❌ |
| `/v1/services/ingestionPipelines/toggleIngestion/{id}` | post | Set an ingestion pipeline either as enabled or disabled | ❌ |
| `/v1/services/ingestionPipelines/trigger/{id}` | post | Trigger an ingestion pipeline run | ❌ |
| `/v1/services/ingestionPipelines/{fqn}/pipelineStatus` | get | List of pipeline status | ❌ |
| `/v1/services/ingestionPipelines/{fqn}/pipelineStatus` | put | Add pipeline status | ❌ |
| `/v1/services/ingestionPipelines/{fqn}/pipelineStatus/{id}` | get | Get pipeline status | ❌ |
| `/v1/services/ingestionPipelines/{id}` | get | Get an ingestion pipeline by Id | ❌ |
| `/v1/services/ingestionPipelines/{id}` | delete | Delete an ingestion pipeline by Id | ❌ |
| `/v1/services/ingestionPipelines/{id}` | patch | Update an ingestion pipeline | ❌ |
| `/v1/services/ingestionPipelines/{id}/pipelineStatus` | delete | Delete Pipeline Status | ❌ |
| `/v1/services/ingestionPipelines/{id}/versions` | get | List ingestion workflow versions | ❌ |
| `/v1/services/ingestionPipelines/{id}/versions/{version}` | get | Get a version of the ingestion pipeline | ❌ |
| `/v1/services/messagingServices` | get | List messaging services | ❌ |
| `/v1/services/messagingServices` | put | Update messaging service | ❌ |
| `/v1/services/messagingServices` | post | Create a messaging service | ❌ |
| `/v1/services/messagingServices/name/{fqn}` | patch | Update a messaging service using name. | ❌ |
| `/v1/services/messagingServices/name/{name}` | get | Get messaging service by name | ❌ |
| `/v1/services/messagingServices/name/{name}` | delete | Delete a messaging service by name | ❌ |
| `/v1/services/messagingServices/restore` | put | Restore a soft deleted messaging service | ❌ |
| `/v1/services/messagingServices/{id}` | get | Get a messaging service by Id | ❌ |
| `/v1/services/messagingServices/{id}` | delete | Delete a messaging service by Id | ❌ |
| `/v1/services/messagingServices/{id}` | patch | Update a messaging service | ❌ |
| `/v1/services/messagingServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/messagingServices/{id}/versions` | get | List messaging service versions | ❌ |
| `/v1/services/messagingServices/{id}/versions/{version}` | get | Get a version of the messaging service | ❌ |
| `/v1/services/metadataServices` | get | List metadata services | ❌ |
| `/v1/services/metadataServices` | put | Update metadata service | ❌ |
| `/v1/services/metadataServices` | post | Create metadata service | ❌ |
| `/v1/services/metadataServices/name/{fqn}` | patch | Update a metadata service using name. | ❌ |
| `/v1/services/metadataServices/name/{name}` | get | Get a metadata service by name | ❌ |
| `/v1/services/metadataServices/name/{name}` | delete | Delete a metadata service by name | ❌ |
| `/v1/services/metadataServices/restore` | put | Restore a soft deleted metadata service. | ❌ |
| `/v1/services/metadataServices/{id}` | get | Get a metadata service by Id | ❌ |
| `/v1/services/metadataServices/{id}` | delete | Delete a metadata service by Id | ❌ |
| `/v1/services/metadataServices/{id}` | patch | Update a metadata service | ❌ |
| `/v1/services/metadataServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/metadataServices/{id}/versions` | get | List metadata service versions | ❌ |
| `/v1/services/metadataServices/{id}/versions/{version}` | get | Get a version of the metadata service | ❌ |
| `/v1/services/mlmodelServices` | get | List ML model services | ❌ |
| `/v1/services/mlmodelServices` | put | Update ML model service | ❌ |
| `/v1/services/mlmodelServices` | post | Create an ML model service | ❌ |
| `/v1/services/mlmodelServices/name/{fqn}` | patch | Update an ML model service using name. | ❌ |
| `/v1/services/mlmodelServices/name/{name}` | get | Get an ML model service by name | ❌ |
| `/v1/services/mlmodelServices/name/{name}` | delete | Delete an ML model service by name | ❌ |
| `/v1/services/mlmodelServices/restore` | put | Restore a soft deleted ML model service | ❌ |
| `/v1/services/mlmodelServices/{id}` | get | Get an ML model service by Id | ❌ |
| `/v1/services/mlmodelServices/{id}` | delete | Delete an ML model service by Id | ❌ |
| `/v1/services/mlmodelServices/{id}` | patch | Update an ML model service | ❌ |
| `/v1/services/mlmodelServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/mlmodelServices/{id}/versions` | get | List ML model service versions | ❌ |
| `/v1/services/mlmodelServices/{id}/versions/{version}` | get | Get a version of the ML model service | ❌ |
| `/v1/services/pipelineServices` | get | List pipeline services | ❌ |
| `/v1/services/pipelineServices` | put | Update pipeline service | ❌ |
| `/v1/services/pipelineServices` | post | Create a pipeline service | ❌ |
| `/v1/services/pipelineServices/name/{fqn}` | get | Get pipeline service by fully qualified name | ❌ |
| `/v1/services/pipelineServices/name/{fqn}` | delete | Delete a pipeline service by fully qualified name | ❌ |
| `/v1/services/pipelineServices/name/{fqn}` | patch | Update a pipeline service using name. | ❌ |
| `/v1/services/pipelineServices/restore` | put | Restore a soft deleted pipeline service. | ❌ |
| `/v1/services/pipelineServices/{id}` | get | Get a pipeline service by Id | ❌ |
| `/v1/services/pipelineServices/{id}` | delete | Delete a pipeline service by Id | ❌ |
| `/v1/services/pipelineServices/{id}` | patch | Update a pipeline service | ❌ |
| `/v1/services/pipelineServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/pipelineServices/{id}/versions` | get | List pipeline service versions | ❌ |
| `/v1/services/pipelineServices/{id}/versions/{version}` | get | Get a version of the pipeline service | ❌ |
| `/v1/services/searchServices` | get | List search services | ❌ |
| `/v1/services/searchServices` | put | Update search service | ❌ |
| `/v1/services/searchServices` | post | Create search service | ❌ |
| `/v1/services/searchServices/name/{fqn}` | delete | Delete an SearchService by fully qualified name | ❌ |
| `/v1/services/searchServices/name/{fqn}` | patch | Update an search service using name. | ❌ |
| `/v1/services/searchServices/name/{name}` | get | Get search service by name | ❌ |
| `/v1/services/searchServices/restore` | put | Restore a soft deleted SearchService. | ❌ |
| `/v1/services/searchServices/{id}` | get | Get an search service | ❌ |
| `/v1/services/searchServices/{id}` | delete | Delete an search service | ❌ |
| `/v1/services/searchServices/{id}` | patch | Update an search service | ❌ |
| `/v1/services/searchServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/searchServices/{id}/versions` | get | List search service versions | ❌ |
| `/v1/services/searchServices/{id}/versions/{version}` | get | Get a version of the search service | ❌ |
| `/v1/services/storageServices` | get | List storage services | ❌ |
| `/v1/services/storageServices` | put | Update storage service | ❌ |
| `/v1/services/storageServices` | post | Create storage service | ❌ |
| `/v1/services/storageServices/name/{fqn}` | delete | Delete an StorageService by fully qualified name | ❌ |
| `/v1/services/storageServices/name/{name}` | get | Get storage service by name | ❌ |
| `/v1/services/storageServices/restore` | put | Restore a soft deleted StorageService. | ❌ |
| `/v1/services/storageServices/{id}` | get | Get an storage service | ❌ |
| `/v1/services/storageServices/{id}` | delete | Delete an storage service | ❌ |
| `/v1/services/storageServices/{id}` | patch | Update an storage service | ❌ |
| `/v1/services/storageServices/{id}/testConnectionResult` | put | Add test connection result | ❌ |
| `/v1/services/storageServices/{id}/versions` | get | List storage service versions | ❌ |
| `/v1/services/storageServices/{id}/versions/{version}` | get | Get a version of the storage service | ❌ |
| `/v1/storedProcedures` | get | List Stored Procedures | ❌ |
| `/v1/storedProcedures` | put | Create or update Stored Procedure | ❌ |
| `/v1/storedProcedures` | post | Create a Stored Procedure | ❌ |
| `/v1/storedProcedures/name/{fqn}` | get | Get a Stored Procedure by fully qualified name | ❌ |
| `/v1/storedProcedures/name/{fqn}` | delete | Delete a schema by fully qualified name | ❌ |
| `/v1/storedProcedures/name/{fqn}` | patch | Update a Stored Procedure by name. | ❌ |
| `/v1/storedProcedures/restore` | put | Restore a soft deleted stored procedure. | ❌ |
| `/v1/storedProcedures/{id}` | get | Get a stored procedure by Id | ❌ |
| `/v1/storedProcedures/{id}` | delete | Delete a StoredProcedure by Id | ❌ |
| `/v1/storedProcedures/{id}` | patch | Update a Stored Procedure | ❌ |
| `/v1/storedProcedures/{id}/followers` | put | Add a follower | ❌ |
| `/v1/storedProcedures/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/storedProcedures/{id}/versions` | get | List stored procedure versions | ❌ |
| `/v1/storedProcedures/{id}/versions/{version}` | get | Get a version of the Stored Procedure | ❌ |
| `/v1/storedProcedures/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/suggestions` | get | List Suggestions | ❌ |
| `/v1/suggestions` | post | Create a Suggestion | ❌ |
| `/v1/suggestions/accept-all` | put | Accept all Suggestions from a user and an Entity | ❌ |
| `/v1/suggestions/reject-all` | put | Reject all Suggestions from a user and an Entity | ❌ |
| `/v1/suggestions/{entityType}/name/{entityFQN}` | delete | Delete a Suggestions by entityFQN | ❌ |
| `/v1/suggestions/{id}` | get | Get a suggestion by Id | ❌ |
| `/v1/suggestions/{id}` | put | Update a suggestion by `Id`. | ❌ |
| `/v1/suggestions/{id}/accept` | put | Accept a Suggestion | ❌ |
| `/v1/suggestions/{id}/reject` | put | Reject a Suggestion | ❌ |
| `/v1/suggestions/{suggestionId}` | delete | Delete a Suggestion by Id | ❌ |
| `/v1/system/version` | get | Get version of metadata service | ❌ |
| `/v1/tables` | get | List tables | ✅ |
| `/v1/tables` | put | Create or update a table | ❌ |
| `/v1/tables` | post | Create a table | ❌ |
| `/v1/tables/entityRelationship` | get | Search Entity Relationship | ❌ |
| `/v1/tables/name/{fqn}` | get | Get a table by fully qualified name | ✅ |
| `/v1/tables/name/{fqn}` | delete | Delete a table by fully qualified name | ❌ |
| `/v1/tables/name/{fqn}` | patch | Update a table by name. | ❌ |
| `/v1/tables/name/{name}/export` | get | Export table in CSV format | ❌ |
| `/v1/tables/name/{name}/exportAsync` | get | Export table in CSV format | ❌ |
| `/v1/tables/name/{name}/import` | put | Import columns from CSV to update table (no creation allowed) | ❌ |
| `/v1/tables/name/{name}/importAsync` | put | Import columns from CSV to update table asynchronously (no creation allowed) | ❌ |
| `/v1/tables/restore` | put | Restore a soft deleted table | ❌ |
| `/v1/tables/{fqn}/columnProfile` | get | List of column profiles | ❌ |
| `/v1/tables/{fqn}/systemProfile` | get | List of system profiles | ❌ |
| `/v1/tables/{fqn}/tableProfile` | get | List of table profiles | ❌ |
| `/v1/tables/{fqn}/tableProfile/latest` | get | Get the latest table profile | ❌ |
| `/v1/tables/{fqn}/{entityType}/{timestamp}/profile` | delete | Delete table profile data | ❌ |
| `/v1/tables/{id}` | get | Get a table by Id | ❌ |
| `/v1/tables/{id}` | delete | Delete a table by Id | ❌ |
| `/v1/tables/{id}` | patch | Update a table | ❌ |
| `/v1/tables/{id}/customMetric` | put | Add column custom metrics | ❌ |
| `/v1/tables/{id}/customMetric/{columnName}/{customMetricName}` | delete | Delete custom metric from a column | ❌ |
| `/v1/tables/{id}/customMetric/{customMetricName}` | delete | Delete custom metric from a table | ❌ |
| `/v1/tables/{id}/dataModel` | put | Add data modeling information to a table | ❌ |
| `/v1/tables/{id}/followers` | put | Add a follower | ❌ |
| `/v1/tables/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/tables/{id}/joins` | put | Add table join information | ❌ |
| `/v1/tables/{id}/sampleData` | get | Get sample data | ✅ |
| `/v1/tables/{id}/sampleData` | put | Add sample data | ❌ |
| `/v1/tables/{id}/sampleData` | delete | Delete sample data | ❌ |
| `/v1/tables/{id}/tableProfile` | put | Add table profile data | ❌ |
| `/v1/tables/{id}/tableProfilerConfig` | get | Get table profile config | ❌ |
| `/v1/tables/{id}/tableProfilerConfig` | put | Add table profile config | ❌ |
| `/v1/tables/{id}/tableProfilerConfig` | delete | Delete table profiler config | ❌ |
| `/v1/tables/{id}/versions` | get | List table versions | ❌ |
| `/v1/tables/{id}/versions/{version}` | get | Get a version of the table | ❌ |
| `/v1/tables/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/tags` | get | List tags | ❌ |
| `/v1/tags` | put | Create or update a tag | ❌ |
| `/v1/tags` | post | Create a tag | ❌ |
| `/v1/tags/name/{fqn}` | get | Get a tag by fully qualified name | ❌ |
| `/v1/tags/name/{fqn}` | delete | Delete a tag by fully qualified name | ❌ |
| `/v1/tags/name/{fqn}` | patch | Update a tag using name. | ❌ |
| `/v1/tags/restore` | put | Restore a soft deleted tag. | ❌ |
| `/v1/tags/{id}` | get | Get a tag by id | ❌ |
| `/v1/tags/{id}` | delete | Delete a tag by id | ❌ |
| `/v1/tags/{id}` | patch | Update a tag | ❌ |
| `/v1/tags/{id}/assets/add` | put | Bulk Add Classification Tag to Assets | ❌ |
| `/v1/tags/{id}/assets/remove` | put | Bulk Remove Tag from Assets | ❌ |
| `/v1/tags/{id}/versions` | get | List tag versions | ❌ |
| `/v1/tags/{id}/versions/{version}` | get | Get a version of the tags | ❌ |
| `/v1/teams` | get | List teams | ❌ |
| `/v1/teams` | put | Update team | ❌ |
| `/v1/teams` | post | Create a team | ❌ |
| `/v1/teams/documentation/csv` | get | Get CSV documentation for team import/export | ❌ |
| `/v1/teams/hierarchy` | get | List teams with hierarchy | ❌ |
| `/v1/teams/name/{fqn}` | patch | Update a team using name. | ❌ |
| `/v1/teams/name/{name}` | get | Get a team by name | ❌ |
| `/v1/teams/name/{name}` | delete | Delete a team by name | ❌ |
| `/v1/teams/name/{name}/export` | get | Export teams in CSV format | ❌ |
| `/v1/teams/name/{name}/exportAsync` | get | Export teams in CSV format | ❌ |
| `/v1/teams/name/{name}/import` | put | Import from CSV to create, and update teams. | ❌ |
| `/v1/teams/name/{name}/importAsync` | put | Import from CSV to create, and update teams asynchronously. | ❌ |
| `/v1/teams/restore` | put | Restore a soft deleted team | ❌ |
| `/v1/teams/{id}` | get | Get a team by id | ❌ |
| `/v1/teams/{id}` | delete | Delete a team by id | ❌ |
| `/v1/teams/{id}` | patch | Update a team | ❌ |
| `/v1/teams/{id}/versions` | get | List team versions | ❌ |
| `/v1/teams/{id}/versions/{version}` | get | Get a version of the team | ❌ |
| `/v1/teams/{name}/assets/add` | put | Bulk Add Assets | ❌ |
| `/v1/teams/{name}/assets/remove` | put | Bulk Remove Assets | ❌ |
| `/v1/teams/{teamId}/users` | put | Update team users | ❌ |
| `/v1/teams/{teamId}/users/{userId}` | delete | Remove a user from a team | ❌ |
| `/v1/topics` | get | List topics | ❌ |
| `/v1/topics` | put | Update topic | ❌ |
| `/v1/topics` | post | Create a topic | ❌ |
| `/v1/topics/name/{fqn}` | get | Get a topic by fully qualified name | ❌ |
| `/v1/topics/name/{fqn}` | delete | Delete a topic by fully qualified name | ❌ |
| `/v1/topics/name/{fqn}` | patch | Update a topic using name. | ❌ |
| `/v1/topics/restore` | put | Restore a soft deleted topic | ❌ |
| `/v1/topics/{id}` | get | Get a topic by id | ❌ |
| `/v1/topics/{id}` | delete | Delete a topic by id | ❌ |
| `/v1/topics/{id}` | patch | Update a topic | ❌ |
| `/v1/topics/{id}/followers` | put | Add a follower | ❌ |
| `/v1/topics/{id}/followers/{userId}` | delete | Remove a follower | ❌ |
| `/v1/topics/{id}/sampleData` | get | Get sample data | ❌ |
| `/v1/topics/{id}/sampleData` | put | Add sample data | ❌ |
| `/v1/topics/{id}/versions` | get | List topic versions | ❌ |
| `/v1/topics/{id}/versions/{version}` | get | Get a version of the topic | ❌ |
| `/v1/topics/{id}/vote` | put | Update Vote for a Entity | ❌ |
| `/v1/usage/{entity}/name/{fqn}` | get | Get usage by fully qualified name | ❌ |
| `/v1/usage/{entity}/name/{fqn}` | put | Report usage by fully qualified name | ❌ |
| `/v1/usage/{entity}/name/{fqn}` | post | Report usage by fully qualified name | ❌ |
| `/v1/usage/{entity}/{id}` | get | Get usage by id | ❌ |
| `/v1/usage/{entity}/{id}` | put | Report usage | ❌ |
| `/v1/usage/{entity}/{id}` | post | Report usage | ❌ |
| `/v1/users` | get | List users | ❌ |
| `/v1/users` | put | Update user | ❌ |
| `/v1/users` | post | Create a user | ❌ |
| `/v1/users/auth-mechanism/{id}` | get | Get Authentication Mechanism for a Bot User | ❌ |
| `/v1/users/changePassword` | put | Change Password For User | ❌ |
| `/v1/users/checkEmailInUse` | post | Check if a email is already in use | ❌ |
| `/v1/users/checkEmailVerified` | post | Check if a mail is verified | ❌ |
| `/v1/users/documentation/csv` | get | Get CSV documentation for user import/export | ❌ |
| `/v1/users/export` | get | Export users in a team in CSV format | ❌ |
| `/v1/users/exportAsync` | get | Export users in a team in CSV format | ❌ |
| `/v1/users/generatePasswordResetLink` | post | Generate Password Reset Link | ❌ |
| `/v1/users/generateRandomPwd` | get | Generate a random password | ❌ |
| `/v1/users/generateToken/{id}` | put | Generate JWT Token for a Bot User | ❌ |
| `/v1/users/import` | put | Import from CSV to create, and update teams. | ❌ |
| `/v1/users/importAsync` | put | Import from CSV to create, and update teams asynchronously. | ❌ |
| `/v1/users/loggedInUser` | get | Get current logged in user | ❌ |
| `/v1/users/loggedInUser/groupTeams` | get | Get group type of teams for current logged in user | ❌ |
| `/v1/users/login` | post | Login User with email (plain-text) and Password (encoded in base 64) | ❌ |
| `/v1/users/logout` | post | Logout a User(Only called for saml and basic Auth) | ❌ |
| `/v1/users/name/{name}` | get | Get a user by name | ❌ |
| `/v1/users/name/{name}` | delete | Delete a user | ❌ |
| `/v1/users/password/reset` | post | Reset Password For User | ❌ |
| `/v1/users/refresh` | post | Provide access token to User with refresh token | ❌ |
| `/v1/users/registrationConfirmation` | put | Confirm User Email | ❌ |
| `/v1/users/resendRegistrationToken` | put | Resend Registration Token | ❌ |
| `/v1/users/restore` | put | Restore a soft deleted User. | ❌ |
| `/v1/users/revokeToken` | put | Revoke JWT Token for a Bot User | ❌ |
| `/v1/users/security/token` | get | Get personal access token to User | ❌ |
| `/v1/users/security/token` | put | Provide access token to User | ❌ |
| `/v1/users/security/token/revoke` | put | Revoke personal access token to User | ❌ |
| `/v1/users/signup` | post | Register User | ❌ |
| `/v1/users/token/{id}` | get | Get JWT Token for a Bot User | ❌ |
| `/v1/users/{id}` | get | Get a user | ❌ |
| `/v1/users/{id}` | delete | Delete a user | ❌ |
| `/v1/users/{id}` | patch | Update a user | ❌ |
| `/v1/users/{id}/versions` | get | List user versions | ❌ |
| `/v1/users/{id}/versions/{version}` | get | Get a version of the user | ❌ |