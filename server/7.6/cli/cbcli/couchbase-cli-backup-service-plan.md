[View original HTML](/server/7.6/cli/cbcli/couchbase-cli-backup-service-plan.html)

Manage the backup service plans.

## [](#synopsis)SYNOPSIS

_couchbase-cli backup-service_ [--cluster <url>] [--username <user>]
    [--password <password>] [--client-cert <path>]
    [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--output] plan [--list] [--get]
    [--remove] [--add] [--name <name>] [--description <text>]
    [--services <list>] [--task [<task> …​]]

## [](#description)DESCRIPTION

Manage backup service plans.

## [](#action-options)ACTION OPTIONS

\--list

List the backup plans.

\--get

Get the backup plan by name.

\--remove

Remove a plan by name.

\--add

Add a new plan.

## [](#options)OPTIONS

\--name <name>

plan name.

\--description <text>

An optional description provided when adding a new plan.

\--services <list>

An optional comma separated lists of services to backup when adding a new plan.

\--task \[<task> …​\]

One or more tasks to add to the plan. Tasks are given in JSON format. For more information see the examples below.

## [](#host-formats)HOST FORMATS

When specifying a host for the couchbase-cli command the following formats are expected:

* `couchbase://<addr>` or `couchbases://<addr>`
* `http://<addr>:<port>` or `https://<addr>:<port>`
* `<addr>:<port>`

It is recommended to use the couchbase://<addr> or couchbases://<addr> format for standard installations. The other formats allow an option to take a port number which is needed for non-default installations where the admin port has been set up on a port other that 8091 (or 18091 for https).

## [](#certificate-authentication-mtls-authentication)CERTIFICATE AUTHENTICATION (MTLS AUTHENTICATION)

This tool supports authenticating against a Couchbase Cluster by using certificate based authentication (mTLS authentication). To use certificate based authentication a certificate/key must be supplied, there a currently multiple ways this may be done.

### [](#pem-encoded-certificatekey)PEM ENCODED CERTIFICATE/KEY

An unencrypted PEM encoded certificate/key may be supplied by using: - `--client-cert <path>`\- `--client-key <path>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

The file passed to `--client-key` must contain at most one private key, the key can be in one of the following formats: - PKCS#1 - PKCS#8

Currently, only the following key types are supported: - RSA - DSA

### [](#pem-encoded-certificatepem-or-der-encrypted-pkcs8-key)PEM ENCODED CERTIFICATE/PEM OR DER ENCRYPTED PKCS#8 KEY

An encrypted PKCS#8 formatted key may be provided using: - `--client-cert <path>`\- `--client-key <path>`\- `--client-key-password <password>`

The file passed to `--client-cert` must contain the client certificate, and an optional chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - DSA

### [](#encrypted-pkcs12-certificatekey)ENCRYPTED PKCS#12 CERTIFICATE/KEY

An encrypted PKCS#12 certificate/key may be provided using: - `--client-cert <path>`\- `--client-cert-password <password>`

The file passed to `--client-cert` must contain the client certificate and exactly one private key. It may also contain the chain required to authenticate the client certificate.

Currently, only the following key types are supported: - RSA - DSA

## [](#examples)EXAMPLES

To retrieve a summary of all plans run:

$ couchbase-cli backup-service -c 127.0.0.1:8091 -u Administrator -p password \
  plan --list
  Name     | # Tasks | Services  | Default
  ---------------------------------------------
  _daily   | 3       | all       | True
  custom   | 9       | Data      | False

This will show you the name of all the plans registered with the service as well as how many tasks the plans has and what services are included.

To retrieve more in-depth information of a singular plan you can use the `--get`action argument as shown below.

$ couchbase-cli backup-service -c 127.0.0.1:8091 -u Administrator -p password \
  plan --get --name _daily
Name: _daily
Description: This plan does a backup every hour and merge 6 hours as well as at the end of the week
Services: all
Default: False

Tasks:
Name                 | Schedule                      | Options
-------------------------------------------------------------------
backup_hourly        | backup every hour at 00:00    | N/A
merge_every_6_hours  | merge every 6 hours at 00:30  | Merge from 0 to 0
merge_week           | merge every sunday at 23:40   | Merge from 0 to 7

To retrieve the information in JSON format add `--output json` before the `plan` key word.

To remove a plan use the action argument `--remove` as shown below. Note that only plans that are not being used by an active instance may be removed. To remove a plan that is being used, all the plans that use it must be archived first.

$ couchbase-cli backup-service -c 127.0.0.1:8091 -u Administrator -p password \
  plan --remove --name _daily

To add a plan use the action argument `--add` as seen below.

$ couchbase-cli backup-service -c 127.0.0.1:8091 -u Administrator -p password \
  plan --add --name new-plan --description "Optional description"
  --task '{"name":"t1", "task_type":"BACKUP", "full_backup": true, \
  "schedule":{"frequency": 1, "period": "HOURS", "job_type":"BACKUP"}}'
   --services data

The `--description` is an optional string of up to 140 characters that can be used to describe what the plan does. The `--services` flag defines what services should be backed up by the tasks in the plan, valid services are `[data, gsi, cbas, ft, eventing, views]`. Finally, the `--task` argument accepts JSON task objects. The task objects have the following schema:

{
    "name": "task-name",
    "task_type": "BACKUP", // it can be either BACKUP or MERGE
    "full_backup": true,   // optional field to make backup tasks full
    "merge_options": {     // optional field to configure what data to merge in merge tasks
        "offset_start": 1, // the offset on which to start merging in days
        "offset_end": 1    // the offset on which to end the merge based from the start in days
    },
    "schedule": {
        "frequency": 5,
        "period": "HOURS",    // period can be [MINUTES, HOURS, DAYS, WEEKS, MONDAY-SUNDAY]
        "job_type": "BACKUP", // either BACKUP or MERGE
        "time": "22:00"       // Optional time at which to run the tasks
    }
}

## [](#environment-and-configuration-variables)ENVIRONMENT AND CONFIGURATION VARIABLES

CB\_REST\_USERNAME

Specifies the username to use when executing the command. This environment variable allows you to specify a default argument for the -u/--username argument on the command line.

CB\_REST\_PASSWORD

Specifies the password of the user executing the command. This environment variable allows you to specify a default argument for the -p/--password argument on the command line. It also allows the user to ensure that their password are not cached in their command line history.

CB\_CLIENT\_CERT

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `CB_CLIENT_KEY` as an alternative to the `CB_USERNAME` and `CB_PASSWORD` variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_CERT\_PASSWORD

The password for the certificate provided to the `CB_CLIENT_CERT` variable, when using this variable, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY

The path to the client private key whose public key is contained in the certificate provided to the `CB_CLIENT_CERT` variable. May be supplied with `CB_CLIENT_CERT` as an alternative to the `CB_USERNAME` and `CB_PASSWORD`variables. See the CERTIFICATE AUTHENTICATION section for more information.

CB\_CLIENT\_KEY\_PASSWORD

The password for the key provided to the `CB_CLIENT_KEY` variable, when using this variable, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

## [](#see-also)SEE ALSO

[backup-service](couchbase-cli-backup-service.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite