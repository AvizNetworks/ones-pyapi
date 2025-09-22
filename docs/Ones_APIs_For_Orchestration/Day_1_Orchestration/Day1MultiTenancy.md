# ONES Multi-Tenancy API – Day-1 Operations

This illustration demonstrates the use of ONES Multi-Tenancy APIs for Day-1 operations such as creating tenants, allocating GPUs, retrieving tenant information, and deleting tenants in a SpectrumX fabric.

---

## Importing ONES Multi-Tenancy Client

```py
from restclient.orchestration.client import FMClient
import json
```

## Setting Up connection
```py
conn = FMClient(url = "http://10.x.x.x:<port_number>") 
#usually <port_number> will be 8787
```

# ONES Multi-Tenancy API Reference

## Create a Tenant
```py
fabric_name = "Web_Services_DC"
payload = {
    "tenantName": "Pepsi",
    "description": "Pepsi Tenant for Compute",
    "maxGpusAllowed": 32
}
result = conn.create_tenant(fabric_name, payload)
```

**POST** `/fabrics/{fabricName}/tenants`  

Creates a new tenant in the specified fabric.

### Parameters

| Name       | In   | Type   | Required | Description              |
|------------|------|--------|----------|--------------------------|
| fabricName | path | string | Yes      | Name of the fabric       |

### Example Request Body

```json
{
  "tenantName": "Pepsi",
  "description": "Pepsi",
  "maxGpusAllowed": 32
}
```

### Sample Responses
| Code | Description                                                                                                                                                                                                       |
| ---- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 201  | Tenant created successfully                                                                                                                                                                                       |
| 400  | Invalid input<br>Specified fabric does not exist.<br>Invalid tenant input.<br>Invalid tenant name (must start with a letter, only letters, numbers, underscores `_` or dashes `-`, no spaces/special characters). |
| 409  | Tenant with the same name already exists in this fabric.                                                                                                                                                          |

### Response Example (201):

```py
Tenant created successfully.
```

## Allocate GPUs to a Tenant
```py
fabric_name = "Web_Services_DC"
tenant_name = "Pepsi"
payload = {
    "operation": "ADD",
    "servers": ["hgx-su00-h00", "hgx-su00-h01"]
}
result = conn.update_tenant_gpus(fabric_name, tenant_name, payload)
```

**PATCH** `/fabrics/{fabricName}/tenants/{tenantName}`

Allocates or deallocates GPUs for a tenant.

### Parameters
| Name       | In   | Type   | Required | Description        |
| ---------- | ---- | ------ | -------- | ------------------ |
| fabricName | path | string | Yes      | Name of the fabric |
| tenantName | path | string | Yes      | Name of the tenant |

### Example Request Body

```json
{
  "operation": "ADD",
  "servers": ["hgx-su00-h00", "hgx-su00-h01"]
}
```

### Sample Responses
| Code | Description                                                                                    |
| ---- | ---------------------------------------------------------------------------------------------- |
| 200  | GPU update processed successfully                                                              |
| 400  | Invalid request <br> GPU allocation exceeds tenant's quota. <br> Server list is null or empty. |
| 404  | Server list is null or empty.                                                                  |
| 409  | One or more GPUs are already allocated to another tenant.                                      |

### Response Example (200):
```py
Gpu update processed successfully.
```

## Deallocate GPUs from a Tenant
```py
fabric_name = "Web_Services_DC"
tenant_name = "Pepsi"
payload = {
  "operation": "DELETE",
  "servers": ["hgx-su00-h02", "hgx-su00-h03"]
}
result = conn.update_tenant_gpus(fabric_name, tenant_name, payload)
```
**PATCH** `/fabrics/{fabricName}/tenants/{tenantName}`

Allocates or deallocates GPUs for a tenant.

### Parameters
| Name       | In   | Type   | Required | Description        |
| ---------- | ---- | ------ | -------- | ------------------ |
| fabricName | path | string | Yes      | Name of the fabric |
| tenantName | path | string | Yes      | Name of the tenant |

### Example Request Body

```json
{
  "operation": "DELETE",
  "servers": ["hgx-su00-h02", "hgx-su00-h03"]
}
```

### Sample Responses
| Code | Description                                                                                    |
| ---- | ---------------------------------------------------------------------------------------------- |
| 200  | GPU update processed successfully                                                              |
| 400  | Invalid request <br> GPU allocation exceeds tenant's quota. <br> Server list is null or empty. |
| 404  | Server list is null or empty.                                                                  |
| 409  | One or more GPUs are already allocated to another tenant.                                      |

### Response Example (200):
```py
Gpu update processed successfully.
```


## Delete a Tenant
### Important: All GPUs must be deallocated before deleting a tenant.
```py
fabric_name = "Web_Services_DC"
tenant_name = "Pepsi"
result = conn.delete_tenant(fabric_name, tenant_name)
```

**DELETE** `/fabrics/{fabricName}/tenants/{tenantName}`

Deletes a tenant from the specified fabric.


### Parameters
| Name       | In   | Type   | Required | Description        |
| ---------- | ---- | ------ | -------- | ------------------ |
| fabricName | path | string | Yes      | Name of the fabric |
| tenantName | path | string | Yes      | Name of the tenant |


### Sample Responses
| Code | Description                               |
| ---- | ----------------------------------------- |
| 200  | Tenant deleted successfully.              |
| 404  | Tenant does not exist.                    |
| 409  | Tenant has GPUs allocated. Cannot delete. |


### Response Example (200):
```py
Tenant deleted successfully.
```

## List All Tenants
```py
fabric_name = "Web_Services_DC"
result = conn.list_tenants(fabric_name)
```

**GET** `/fabrics/{fabricName}/tenants`

Retrieves all tenants in a given fabric.

### Parameters
| Name       | In   | Type   | Required | Description        |
| ---------- | ---- | ------ | -------- | ------------------ |
| fabricName | path | string | Yes      | Name of the fabric |


### Sample Responses
| Code | Description                               |
| ---- | ----------------------------------------- |
| 200  | List of tenants                           |
| 404  | Invalid input <br> Fabric does not exist. |


### Response Example (200):
```json
{
  "id": 26,
  "description": "Tenant for Customer Pepsi",
  "name": "Tenant-123",
  "maxGpusAllowed": 32,
  "gpusAllocated": 0,
  "vniId": 4026,
  "fabricName": "Test_Fabric",
  "config_status": "1",
  "createdAt": "2025-09-12T06:34:18.782+00:00",
  "updatedAt": "2025-09-12T06:46:04.737+00:00"
}
```


## Get Tenant Details
```py
fabric_name = "Web_Services_DC"
tenant_name = "Pepsi"
result = conn.get_tenant_details(fabric_name, tenant_name)
```

**GET** `/fabrics/{fabricName}/tenants/{tenantName}`

Retrieves details of a specific tenant.

### Parameters
| Name       | In   | Type   | Required | Description        |
| ---------- | ---- | ------ | -------- | ------------------ |
| fabricName | path | string | Yes      | Name of the fabric |
| tenantName | path | string | Yes      | Name of the tenant |



### Sample Responses
| Code | Description                                                           |
| ---- | --------------------------------------------------------------------- |
| 200  | Tenant details retrieved                                              |
| 404  | Invalid input <br> Tenant does not exist. <br> Fabric does not exist. |


### Response Example (200):
```json
{
  "id": 26,
  "description": "Tenant for Customer Pepsi",
  "name": "Tenant-123",
  "maxGpusAllowed": 32,
  "gpusAllocated": 0,
  "vniId": 4026,
  "fabricName": "Test_Fabric",
  "config_status": "1",
  "createdAt": "2025-09-12T06:34:18.782+00:00",
  "updatedAt": "2025-09-12T06:46:04.737+00:00"
}
```

## Tenant Deletion Policy

- A tenant cannot be deleted if any GPUs are currently allocated to it.

- Before initiating the deletion of a tenant, please ensure that all GPUs assigned to the tenant have been fully deallocated.

- If GPU allocations still exist, the deletion request will not be processed.

- The system performs this validation internally and responds with a handled message.

- If attempted, the tenant deletion API will return a warning error message clearly indicating that GPU deallocation is required before deletion.


## Understanding `Get Response` and `config_status` in API Response

Sample Get response
```json
{
    "id": 26,
    "description": "Tenant for Customer Pepsi",
    "name": "Tenant-123", 
    "maxGpusAllowed": 32,
    "gpusAllocated": 0,
    "vniId": 4026,
    "fabricName": "Test_Fabric",
    "config_status": "1",
    "createdAt": "2025-09-12T06:34:18.782+00:00",
    "updatedAt": "2025-09-12T06:46:04.737+00:00"
}
```

| Field          | Description                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------|
| id             | Identifier for the tenant record.                                                             |
| description    | A user-provided description to identify the purpose of the tenant.                            |
| name           | The name assigned to the tenant (must be unique within the system).                           |
| maxGpusAllowed | Maximum number of GPUs allowed for this tenant.                                               |
| gpusAllocated  | Current number of GPUs allocated to the tenant.                                               |
| vniId          | The VNI (Virtual Network Identifier) associated with this tenant.                             |
| fabricName     | The name of the fabric this tenant is associated with. This is required for API operations.   |
| config_status  | Configuration status code for the tenant. See status mapping below.                           |
| createdAt      | Timestamp when the tenant was created.                                                        |
| updatedAt      | Timestamp of the last update to this tenant record.                                           |



The `config_status` field indicates the current configuration state of the tenant within the system. It is represented as a numeric code, mapped as follows:

| config_status | Status       | Description                                                                 |
|---------------|-------------|-----------------------------------------------------------------------------|
| 3             | In Progress | Configuration for the tenant is currently in progress and not yet complete. |
| 2             | Not Started | Configuration process has not started yet.                                  |
| 1             | Pass        | Configuration has been successfully completed.                              |
| 0             | Fail        | Configuration failed due to an error or misconfiguration.                    |


### Notes
- All requests must include a valid fabricName in the API path.

- APIs are exposed over HTTPS (port 8443).

- Hostnames for GPU allocation must match those defined in your environment.

- Make sure ONES version 4.0+ is installed and the fabric is deployed using RA 1.3.

- Ensure GPU deallocation is done before attempting to delete a tenant.
