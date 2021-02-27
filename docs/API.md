# API Version 1 (not yet accepted)

## Worker
> /api/v1/worker

### Post
Set json body to the host name of the machine that runs the application.

If the host does not yet exist in the repository, it will be created according
to and will receive its configuration in return for a request to the json format.
a log will be created to warn of the arrival of a new worker

If it already exists, it will receive the current configuration of other workers
a log will be created to warn of his return.

Content sample for json body
```json
{
    "hostname": "d1e6ee19f59f"
}
```


## Config
> /api/v1/config

### Get
Returns the configuration to the json format

Content sample of return
```json
{
    "plugins": ["pluginA", "pluginB"],
    "skipPrivate": true,
    "timeout": 10
}
```


## Addr
> /api/v1/addr

### Get
Returns an ip in this order : 
 - rescan priority from 10 for highest to 0
 - never scanned
 - oldest scan

A log will be created to warn that the ip has been get by a worker, so it will be locked
for the other workers.

### Post
Put to the body json an ip, or an ip with cidr the list of ip will be automatically
created and typed in its version (v4, v6) a log will be created with the list of ip's
that will have been added
> more than one ip list can be added before the request in json

Content sample for json body
```json
{
    "ip": ["127.0.0.1/24"]
}
```

### Update
Send the scan result to the database and create a log to release the ip with the time.

It will receive the current version of the configuration to make sure that the worker is up to date.

Content sample for json body
```json
{
    "ip": "127.0.0.1",
    "worker": "d1e6ee19f59f",
    "result": {
      "pluginA": true,
      "pluginB": false
    }
}
```
