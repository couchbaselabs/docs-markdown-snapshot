[View original HTML](/server/7.6/cli/cbcli/couchbase-cli-setting-audit.html)

Modifies audit log settings (EE only)

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-audit_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--list-filterable-events] [--get-settings]
    [--set] [--audit-enabled <1|0>] [--audit-log-path <path>]
    [--audit-log-rotate-interval <seconds>] [--audit-log-rotate-size <bytes>]
    [--disabled-users <user-list>] [--disable-events <event-list>] [--prune-age]

Some of these options are only available in Couchbase Server 6.5.1 and later. Refer to [OPTIONS](#options) for details.

## [](#description)DESCRIPTION

Auditing is used to observe the action of users in the cluster. It is usually turned on for security purposes to ensure that those without permission to access information do not access it. By default auditing is disabled in Couchbase. The setting-audit command can be used to enable and disable auditing, set the auditing log path, and change the auditing log rotation interval; in Couchbase Server 6.5.1 and later, the command can also be used to retrieve the current auditing configuration, retrieve the auditable events and descriptions, and disable auditing for certain users and events.

## [](#options)OPTIONS

\-c

\--cluster

Specifies the hostname of a node in the cluster. See the HOST FORMATS section for more information on specifying a hostname.

\-u

\--username <username>

Specifies the username of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error.

\-p

\--password <password>

Specifies the password of the user executing the command. If you do not have a user account with permission to execute the command then it will fail with an unauthorized error. If this argument is specified, but no password is given then the command will prompt the user for a password through non-echoed stdin. You may also specify your password by using the environment variable CB\_REST\_PASSWORD.

\--client-cert <path>

The path to a client certificate used to authenticate when connecting to a cluster. May be supplied with `--client-key` as an alternative to the `--username` and `--password` flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-cert-password <password>

The password for the certificate provided to the `--client-cert` flag, when using this flag, the certificate/key pair is expected to be in the PKCS#12 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key <path>

The path to the client private key whose public key is contained in the certificate provided to the `--client-cert` flag. May be supplied with `--client-cert` as an alternative to the `--username` and `--password`flags. See the CERTIFICATE AUTHENTICATION section for more information.

\--client-key-password <password>

The password for the key provided to the `--client-key` flag, when using this flag, the key is expected to be in the PKCS#8 format. See the CERTIFICATE AUTHENTICATION section for more information.

\--list-filterable-events

(Couchbase Server 6.5.1 and later.) Returns a table or a JSON list (if --output json used) with all the event IDs with there descriptions.

\--get-settings

(Couchbase Server 6.5.1 and later.) Returns the current audit settings including which events are disabled and which are enabled.

\--set

(Couchbase Server 6.5.1 and later.) Sets the cluster audit settings.

\--audit-enabled <num>

Specifies whether or not auditing is enabled. To enabled auditing set this option to "1". To disable auditing set this option to "0".

\--audit-log-path <path>

Specifies the auditing log path. This should be a path to a folder where the auditing log is kept. The folder must exist on all servers in the cluster.

\--audit-log-rotate-interval <seconds>

Specifies the audit log rotate interval. This is the interval in which the current audit log will be replaced with a new empty audit log file. The log file is rotated to ensure that the audit log does not consume too much disk space. The minimum audit log rotate interval is 15 minutes (900 seconds).

\--audit-log-rotate-size <bytes>

Specifies the audit log rotate size. This is the size at which the current audit log will be replaced with a new empty audit log file. The log file is rotated to ensure that the audit log does not consume too much disk space. The minimum audit log rotate size is 0 bytes and maximum is 524,288,000 (500MiB). When it is set to 0 the log will not be rotated based on size.

\--disabled-users <user-list>

(Couchbase Server 6.5.1 and later.) A comma separated list of users to ignore events from. Local RBAC usernames should be postfixed with `/local`, external LDAP users should be postfixed with `/external`.

\--disable-events <events-list>

(Couchbase Server 6.5.1 and later.) A comma separated list of events IDs to disable auditing for (e.g 8243,8255,8257). To retrieve information of what event ID maps to what event use the --list-filterable-events to retrieve a list of IDs with descriptions.

\--prune-age <seconds>

Specifies the age of the audit logs to prune. The minimum prune age is 0 seconds, which disables pruning. The maximum value for this setting is 35791394 (4085 years).

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

(Unless otherwise specified, the examples below are only applicable to Couchbase Server 6.5.1 and later.)

To get the current audit settings run the command below.

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --get-settings

If auditing is disabled the expected output will be of the form (all the commands can return json if `--output json` is provided):

Audit enabled: False
UUID: 44726500
Log path: /opt/couchbase/var/lib/couchbase/logs
Rotate interval: 86400
Rotate size: 20971520
Disabled users: []

To retrieve the list of events that can be audited use the command:

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --list-filterable-events

ID    | Module         | Name                                           | Description
-------------------------------------------------------------------------------------
36865 | analytics      | Service configuration change                   | A successful service configuration change was made.
36866 | analytics      | Node configuration change                      | A successful node configuration change was made.
32768 | eventing       | Create Function                                | Eventing function definition was created or updated
....
40961 | view_engine    | Delete Design Doc                              | Design Doc is Deleted
40962 | view_engine    | Query DDoc Meta Data                           | Design Doc Meta Data Query Request
40963 | view_engine    | View Query                                     | View Query Request
40964 | view_engine    | Update Design Doc                              | Design Doc is Updated

To enable auditing on a cluster and set the audit log to the default logs folder on a Linux installation with a log rotate interval of 7 days, run the command below.

_Couchbase Server 6.5:_

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --audit-enabled 1 --audit-log-rotate-interval 604800 \
 --audit-log-path /opt/couchbase/var/lib/couchbase/logs

_Couchbase Server 6.5.1 and later:_

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --set --audit-enabled 1 --audit-log-rotate-interval 604800 \
 --audit-log-path /opt/couchbase/var/lib/couchbase/logs

To enable auditing on a cluster and set the audit log to the default logs folder on a Linux installation with a log rotate size of 20MiB, run the command below.

_Couchbase Server 6.5:_

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --audit-enabled 1 --audit-log-rotate-size 20971520 \
 --audit-log-path /opt/couchbase/var/lib/couchbase/logs

_Couchbase Server 6.5.1 and later:_

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --set --audit-enabled 1 --audit-log-rotate-size 20971520 \
 --audit-log-path /opt/couchbase/var/lib/couchbase/logs

To enable auditing on a cluster, set the audit log to the default logs folder on a Linux installation with a log rotate size of 20MiB, disable auditing for users backup and restore, and disable auditing for event 40964 and 40963, run the command below.

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --set --audit-enabled 1 --audit-log-rotate-size 20971520 \
 --audit-log-path /opt/couchbase/var/lib/couchbase/logs \
 --disabled-users user1/local,user2/external --disable-events 40964,40963

To disable auditing run the following command.

_Couchbase Server 6.5:_

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --audit-enabled 0

_Couchbase Server 6.5.1 and later:_

$ couchbase-cli setting-audit -c 192.168.1.5:8091 --username Administrator \
 --password password --set --audit-enabled 0

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

[admin-role-manage](couchbase-cli-user-manage.md), [ssl-manage](couchbase-cli-ssl-manage.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite