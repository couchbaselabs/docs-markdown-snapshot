[View original HTML](/server/current/cli/cbcli/couchbase-cli-setting-compaction.html)

Modifies compaction settings

## [](#synopsis)SYNOPSIS

_couchbase-cli setting-compaction_ [--cluster <url>] [--username <user>] [--password <password>]
    [--client-cert <path>] [--client-cert-password <password>] [--client-key <path>]
    [--client-key-password <password>] [--compaction-db-percentage <num>]
    [--compaction-db-size <mebibytes>] [--compaction-view-percentage <num>]
    [--compaction-view-size <mebibytes>] [--compaction-period-from <HH:MM>]
    [--compaction-period-to <HH:MM>] [--enable-compaction-abort <num>]
    [--enable-compaction-parallel <num>] [--metadata-purge-interval <num>]
    [--gsi-compaction-mode <mode>] [--compaction-gsi-percentage <percent>]
    [--compaction-gsi-interval <list_of_days>]
    [--compaction-gsi-period-from <HH:MM>]
    [--compaction-gsi-period-to <HH:MM>] [--enable-gsi-compaction-abort <1|0>]

## [](#description)DESCRIPTION

This command sets cluster-wide compaction settings for the views and data service.

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

\--compaction-db-percentage <num>

Compacts database files once the fragmentation percentage is greater than the value set for this option. The value must be between 2 and 100.

\--compaction-db-size <mebibytes>

Compacts the database files once the file fragmentation (in MiB) is greater than the value of this option. This option must be set to a value greater than 1.

\--compaction-view-percentage <num>

Compacts view files once the fragmentation percentage is greater than the value set for this option. The value must be between 2 and 100.

\--compaction-view-size: <mebibytes>

Compacts the view files once the file fragmentation (in MiB) is greater than the value of this option. This option must be set to a value greater than 1.

\--compaction-period-from <HH:MM>

This option is unison in conjunction with the --compaction-period-to option and is used to specify a time period where compaction is allowed to run. You could for example specify that compaction should only run between midnight and 5AM each day by setting the compaction from period to "00:00" and the compaction to period to "5:00". When setting the value for this option you must use the format `HH:MM` when `HH` corresponds to the hour and `MM` corresponds to the minute. If this option is not specified then the compaction will run at any time of the day. This option only affects view and database file compaction.

\--compaction-period-to <HH:MM>

This option is unison in conjunction with the --compaction-period-from option and is used to specify a time period where compaction is allowed to run. You could for example specify that compaction should only run between midnight and 5AM each day by setting the compaction from period to "00:00" and the compaction to period to "5:00". When setting the value for this option you must use the format `HH:MM` when `HH` corresponds to the hour and `MM` corresponds to the minute. If this option is not specified then the compaction will run at any time of the day. This option only affects view and database file compaction.

\--enable-compaction-abort <num>

If a compaction from period and compaction to period are specified then this flag tells the server how to respond if a compaction starts during the allowed compaction interval and is still running once after the allowed interval has ended. If this option is set to "1" then the compaction will be aborted. If it is set to "0" then the compaction will be allowed to complete. By default this option is set to "0".

\--enable-compaction-parallel <num>

Specifies whether view and database file compaction can run at the same time. Compaction can be disk intensive operations so it may be beneficial to only allow one type of compaction to run at a time. To allow parallel compaction set the value of this option to "1". To disable parallel compaction set the value of this option to "0". By default this option is set to "0".

\--metadata-purge-interval <days>

Couchbase persists deletes to disk because these deletes may need to be replicated in the future during intra-cluster replication as well as during Cross Data Center Replication. Couchbase cannot however keep these deletes forever because they will cause the database disk size to increase infinitely over time. To combat this issue Couchbase purges old deletes from disk periodically. This flag allow the user to set this interval. By default the purge interval is set to 7 days. This means that we purge deletes from disk that are more than 7 days old. The value of this option must be between 0.04 (1 hour) and 60 (days).

\--gsi-compaction-mode <mode>

Specifies the strategy for compaction in GSI Indexes. This option may be set to either append or circular. The append compaction strategy works by creating a new index file, moving the active data to the new index file, and then removing the old index file. This strategy will cause increased disk usage during compaction, but will cause the new index file to be smaller than the old one and as a result will free up disk space. The circular compaction strategy will append data at first until the index is 65% fragmented. At which point it will start to write data over old blocks in the file that are no longer being used. A full compaction will be triggered once a day on the day set via --compaction-gsi-interval.

\--compaction-gsi-percentage <percent>

Specifies that GSI compaction should be started when the fragmentation in an index file has exceeded this percentage. This parameter only applies if the append compaction mode is used.

\--compaction-gsi-interval <list\_of\_days>

Specifies that GSI compaction should only run on the specified days. This option takes a comma separated list of days where the name of the day is capitalized. Accepted values are Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, and Sunday. If you only want compaction to run on Monday and Tuesday then the value of this option should be set to "Monday,Tuesday". This parameter only applies if circular compaction mode is used.

\--compaction-gsi-period-from <HH:MM>

This option is unison in conjunction with the --compaction-gsi-period-to option and is used to specify a time period where GSI compaction is allowed to run. You could for example specify that GSI compaction should only run between midnight and 5AM each day by setting the GSI compaction from period to "00:00" and the GSI compaction to period to "5:00". When setting the value for this option you must use the format `HH:MM` when `HH` corresponds to the hour and `MM` corresponds to the minute. If this option is not specified then compaction will run at any time of the day. This parameter only applies if circular compaction mode is used.

\--compaction-gsi-period-to <HH:MM>

This option is unison in conjunction with the --compaction-gsi-period-from option and is used to specify a time period where GSI compaction is allowed to run. You could for example specify that GSI compaction should only run between midnight and 5AM each day by setting the GSI compaction from period to "00:00" and the GSI compaction to period to "5:00". When setting the value for this option you must use the format `HH:MM` when `HH` corresponds to the hour and `MM` corresponds to the minute. If this option is not specified then GSI compaction will run at any time of the day. This parameter only applies if circular compaction mode is used.

\--enable-gsi-compaction-abort <1|0>

If a GSI compaction from period and GSI compaction to period are specified then this flag tells the server how to respond if a compaction starts during the allowed GSI compaction interval and is still running after the allowed interval has ended. If this option is set to "1" then the GSI compaction will be aborted. If it is set to "0" then the GSI compaction will be allowed to complete. By default this option is set to "0". This parameter only applies if circular compaction mode is used.

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

If we want to set our view and database compaction percentage thresholds to 30% each, but also wanted to ensure that our fragmentation didn’t grow above 1GB we would run the following command

$ couchbase-cli setting-compaction -c 192.168.1.5 --username Administrator \
 --password password --compaction-view-size 1024 --compaction-db-size 1024 \
 --compaction-view-percentage 30 --compaction-db-percentage 30

If we want to have the same settings as above, but we wanted compaction to only run at night so that we didn’t run the risk of compaction affecting normal application traffic we would run the following command. Note that in this example we will assume our night time period is midnight to 6AM. We will also enable compaction aborts so that we can ensure compaction is never running outside of this time window.

$ couchbase-cli setting-compaction -c 192.168.1.5 --username Administrator \
 --password password --compaction-view-size 1024 --compaction-db-size 1024 \
 --compaction-view-percentage 30 --compaction-db-percentage 30 \
 --compaction-period-from 00:00 --compaction-period-to 6:00 \
 --enable-compaction-abort 1

If we don’t mind when compaction runs and we have the disk overhead to run both view and database compaction at the same time then we might set up compaction with the settings in the first example, but also enable parallel compaction. This can be done by running the command below.

$ couchbase-cli setting-compaction -c 192.168.1.5 --username Administrator \
 --password password --compaction-view-size 1024 --compaction-db-size 1024 \
 --compaction-view-percentage 30 --compaction-db-percentage 30 \
 --enable-compaction-parallel

If your application heavily uses expirations or you create and delete a lot of documents quickly then you might want to shorten your metadata purge interval in order to ensure that you don’t use too much disk space. If we want our compaction to run when the fragmentation is 30% or 1GB and we want to change the metadata purge interval to 2 days then we would run the following command.

$ couchbase-cli setting-compaction -c 192.168.1.5 --username Administrator \
 --password password --compaction-view-size 1024 --compaction-db-size 1024 \
 --compaction-view-percentage 30 --compaction-db-percentage 30 \
 --meta-data-purge-interval 2

If you need to change the GSI index compaction settings to use the append compaction mode and want GSI compaction only to happen once your file is 50% fragmented specify the following command.

$ couchbase-cli setting-compaction -c 192.168.1.5 --username Administrator \
 --password password --gsi-compaction-mode append \
 --compaction-gsi-percentage 50

If you want to change the GSI index compaction settings to use the circular compaction mode and want GSI compaction only to happen on Tuesdays and Thursdays between midnight and 3AM and don’t want GSI compaction running outside of those time windows even if the compaction started at a valid time specify the following command.

$ couchbase-cli setting-compaction -c 192.168.1.5 --username Administrator \
 --password password --gsi-compaction-mode circular \
 --compaction-gsi-interval Tuesday,Thursday \
 --compaction-gsi-period-from 00:00 \
 --compaction-gsi-period-to 3:00 --enable-gsi-compaction-abort 1

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

[bucket-compact](couchbase-cli-bucket-compact.md)

## [](#couchbase-cli)COUCHBASE-CLI

Part of the [couchbase-cli](couchbase-cli.md) suite