---
title: "cbq: The Command Line Shell for SQL++"
description: cbq is a comprehensive command line shell for SQL++.
editUrl: https://github.com/couchbaselabs/docs-devex/edit/release/8.0/modules/n1ql/pages/n1ql-intro/cbq.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/current/n1ql/n1ql-intro/cbq.html)

# cbq: The Command Line Shell for SQL++

> cbq is a comprehensive command line shell for SQL++. It is a powerful, developer friendly tool that enables you to query and update data from Couchbase Server. The cbq shell enables you to perform all the operations that are supported by the Query Workbench and more, such as additional scripting functionality. 

The cbq shell executable, `cbq`, is available in the Couchbase Server installation directory. It is also available in the [Couchbase Server tools](../../cli/cli-intro.md#server-tools-packages) package beginning with version 7.6.2.

## [](#examples-on-this-page)Examples on this Page

The examples on this page use the `travel-sample` dataset, which is supplied with Couchbase Server. For instructions on how to install the sample data, see [Sample Buckets](../../manage/manage-settings/install-sample-buckets.md).

* Linux
* macOS
* Microsoft Windows
* Shell Command

In the command line examples:

* `$BASE_URL` is the URL of any node in the Couchbase cluster.
* `$USER` is the user name to connect to Couchbase Server.
* `$PASSWORD` is the password to connect to Couchbase Server.

In the command line examples:

* `$BASE_URL` is the URL of any node in the Couchbase cluster.
* `$USER` is the user name to connect to Couchbase Server.
* `$PASSWORD` is the password to connect to Couchbase Server.

In the command line examples:

* `%BASE_URL%` is the URL of any node in the Couchbase cluster.
* `%USER%` is the user name to connect to Couchbase Server.
* `%PASSWORD%` is the password to connect to Couchbase Server.

In the shell command examples:

* `<BASE_URL>` is the URL of any node in the Couchbase cluster.
* `<USER>` is the user name to connect to Couchbase Server.
* `<PASSWORD>` is the password to connect to Couchbase Server.

## [](#running-the-cbq-shell)Running the cbq Shell

When starting the cbq shell you can provide a set of command line options. If no options are present then cbq assumes default values for expected options.

To run `cbq`:

1. Open a command window.
2. Change to the directory where the Couchbase command line tools are installed.

  * Linux
  * macOS
  * Microsoft Windows  
```sh  
cd /opt/couchbase/bin  
```  
```sh  
cd /Applications/Couchbase\ Server.app/Contents/Resources/couchbase-core/bin  
```  
```cmd  
cd C:\Program Files\Couchbase\Server\bin  
```
3. Run the following command to connect to the node or cluster and start the interactive query shell:

  * Linux
  * macOS
  * Microsoft Windows  
```sh  
./cbq -u $USER -p $PASSWORD -e $BASE_URL  
```  
```sh  
./cbq -u $USER -p $PASSWORD -e $BASE_URL  
```  
```cmd  
cbq -u %USER% -p %PASSWORD% -e %BASE_URL%  
```

For more information about connecting to a node or cluster, see [Connecting to the Cluster or Query Node](#cbq-connect-to-cluster), [Providing Credentials](#cbq-single-cred), and [Using an Encrypted Connection](#cbq-encrypted).

For the complete list of command line options, see [Table 3](#table%5Fa3h%5Frhz%5Fdw).

### [](#executing-a-single-command)Executing a Single Command

When you start the cbq shell, the cbq shell prompt is displayed.

```console
cbq>
```

The cbq shell interface accepts accepts shell commands as well as SQL++ commands. All the cbq shell commands start with a backslash (`\`). If the command does not start with a backslash (`\`), the cbq shell interprets the command as a SQL++ command.

* To execute a SQL++ query at the cbq prompt, type the query. At the end of the query, type a semicolon `;` and press Enter.
* To execute a cbq command at the cbq prompt, type the command name starting with a backslash `\`. At the end of the command, type a semicolon `;` and press Enter.

The cbq shell enables you to manipulate query parameters. See [Parameter Manipulation](#cbq-parameter-manipulation) for details.

For the complete list of shell commands, see [Table 4](#table%5Fhtk%5Fhgc%5Ffw).

### [](#support-for-multi-line-queries)Support for Multi-line Queries

The cbq shell supports multi-line queries by default, enabling you to enter a query over multiple lines. When entering a query, you can hit Enter without specifying a semicolon (`;`) at the end of the line to move the cursor to the next line. The prompt `>` indicates that the shell is in multi-line mode. For example:

```console
cbq> SELECT *
   > FROM `travel-sample`.inventory.airline
   > LIMIT 1;
```

When you’re done, use a semicolon `;` to indicate the end of the query, and then press Enter to execute the query.

### [](#handling-comments)Handling Comments

You can add comments in your query by preceding the comment with a `#` or `--`. The cbq shell interprets a line that starts with `#` or `--` as a comment, logs the line into history, and returns a new prompt. No other action is taken.

```sqlpp
SELECT *
#This is the first comment
FROM `travel-sample`.inventory.airline
--This is the second comment
LIMIT 1;
```

However, if a comment exists within a statement, it is considered as part of the SQL++ command. If the cbq shell encounters a block comment (enclosed between `/*` ... `*/`) within a statement, it sends the block comment to the query service.

```sqlpp
SELECT * FROM `travel-sample`.inventory.airline /* Block comment */ LIMIT 1;
```

### [](#file-based-operations)File Based Operations

The cbq shell can execute SQL++ and shell commands contained in files using file-based commands and options. See [File Based Operations](#cbq-file-based-ops) for more information.

### [](#history)History

The `cbq` shell stores the history for every session. All the commands executed in a session are stored in history. By default, history is stored in `~/.cbq_history`. You can change the name of the file using the SET command to set the predefined parameter `histfile`. See [Parameter Manipulation](#cbq-parameter-manipulation) for more information.

By default, all the commands are stored in the specified file. You can scroll through history and retrieve the commands from history using the scrolling arrow keys. Once the query is on the command prompt, you can edit it before executing the updated query.

### [](#help)Help

Help displays the help information for the shell commands and for the general usage of cbq.

* Command Line Option
* Shell Command

Use the `-h` or `--help` command line option when bringing up the shell to display the information for all available options.

---

Example

```sh
./cbq -h
```

Use the `\HELP` shell command during a session to display information for specific shell commands. If you specify one or more commands, the shell displays the usage information for the specified commands.

If you do not specify a command, the cbq shell lists all the commands for which syntax help is available.

---

Example

```sqlpp
\HELP;
```

## [](#cbq-connect-to-cluster)Connecting to the Cluster or Query Node

You can connect the cbq shell to Couchbase Server through any of the nodes in the cluster.

* Command Line Option
* Shell Command

To establish a connection on startup, use the `-e` or `--engine` command line option, optionally followed by a URL.

---

Example

```sh
./cbq -e $BASE_URL -u $USER -p $PASSWORD
```

Result

Connected to : http://<HOST>:8091/. Type Ctrl-D or \QUIT to exit.

Path to history file for the shell : ~/.cbq_history

To establish a connection during a session, use the `\CONNECT` shell command, optionally followed by a URL.

---

Example

```sqlpp
\CONNECT <BASE_URL>;
```

Result

Connected to : http://<HOST>:8091. Type Ctrl-D or \QUIT to exit.

The URL may contain up to three components: the protocol scheme, the host, and a port number. The URL is optional and if it is not specified, the default URL `http://localhost:8091` is used. An error is thrown if the URL is invalid.

The cbq shell supports the `http://`, `https://`, `couchbase://` and `couchbases://` protocol schemes. The `https://` and `couchbases://` protocol schemes are encrypted. For more details, refer to [Using an Encrypted Connection](#cbq-encrypted).

The host may be the IP address or hostname of any node in the cluster, as cbq will automatically discover the query nodes. The cbq shell supports both IPV4 and IPV6 addresses. For example: `localhost`, `node1`, `127.0.0.1`, or `[fd63:6f75:6368:1075:816:3c1d:789b:bc4]`.

The `couchbase://` and `couchbases://` protocol schemes support the domain name service (DNS). When using one of these protocol schemes, the host may be a domain name which is resolved using DNS. For example, this enables you to connect to a cluster or node over the internet.

You may optionally specify the port when using the `http://` or `https://` protocol schemes. When connecting to the query service, use the query port 8093, or 18093 for an encrypted connection. When connecting to the cluster, you don’t need to specify the port as the connection uses round robin to find a query service to connect to. If you want to specify a port, use the admin port 8091, or 18091 for an encrypted connection.

You cannot specify the port when using the `couchbase://` or `couchbases://` protocol schemes.

### [](#disconnecting)Disconnecting

You can close the connection with a node or cluster during the session without exiting the shell using the `\DISCONNECT` command. If the shell is not connected to any endpoint, an error with a message that the shell is not connected to any instance is thrown.

Example

```sqlpp
\DISCONNECT;
```

Result

Couchbase query shell not connected to any endpoint. Use \CONNECT command to connect.

### [](#bringing-up-an-unconnected-instance)Bringing Up an Unconnected Instance

You can bring up the shell without connecting to any query service or cluster node by using the `-ne` or `--no-engine` option. After starting cbq without any connection, you can connect to a node using the `\CONNECT` command.

Example

```sh
./cbq -ne
```

Result

Path to history file for the shell : ~/.cbq_history

### [](#exiting-the-cbq-shell)Exiting the cbq Shell

You can exit the cbq shell by pressing Ctrl+D or by using the `\EXIT` or `\QUIT` command.

The cbq shell first saves the history, closes existing connections, saves the current session in a session file, resets all environment variables, and then closes the shell liner interface.

Example

```sqlpp
\EXIT;
```

Result

```console
$
```

## [](#cbq-single-cred)Providing Credentials

You can pass a single user name credential to the cbq shell on startup using the `-u` or `--username` command line option, followed by the user name. The shell then prompts you for a password.

Example

```sh
./cbq -e $BASE_URL -u $USER
```

Result

Enter Password:
Connected to : http://<HOST>:8091/. Type Ctrl-D or \QUIT to exit.

You can also provide a single password credential using the `-p` or `--password` command line option, followed by the password. You cannot use this option by itself. It must be used with the `-u` option to specify the user name that the password is associated with.

Example

```sh
./cbq --e $BASE_URL -u $USER -p $PASSWORD
```

Result

Connected to : http://<HOST>:8091/. Type Ctrl-D or \QUIT to exit.

### [](#accessing-a-secure-keyspace)Providing Credentials in the Connection String

You can pass the username and password by inserting them into the connection string. This method is not recommended when starting cbq, as you must quote or URL-encode any special characters in the username or password. However, this method may be useful for specifying the username and password when connecting to the cluster or node within a cbq session.

To pass credentials in the connection string:

1. Add the username immediately after the protocol scheme.
2. After the username, add a colon `:` followed by the password.
3. After the password, add an at sign `@` followed by the rest of the connection string.

* Command Line Option
* Shell Command

To pass credentials on startup, use the `-e` or `--engine` command line option, and specify the username and password in the URL.

---

In this example, `$HOST` and `$PORT` are the parts of the cluster or node URL following the protocol scheme.

Example

```sh
./cbq -engine="http://$USER:$PASSWORD@$HOST:$PORT/"
```

To pass credentials during a session, use the `\CONNECT` shell command, and specify the username and password in the URL.

---

In this example, `<HOST>` and `<PORT>` are the parts of the cluster or node URL following the protocol scheme.

Example

```sqlpp
\CONNECT http://<USER>:<PASSWORD>@<HOST>:<PORT>/;
```

### [](#cbq-multiple-creds)Providing Multiple Credentials for Authorization

When starting the cbq shell, you can set the credentials using a single command line option, as an alternative to specifying the username and password separately. This method is not recommended, as you must quote or escape any special characters in the username or password.

You can also use the `\SET` or `\PUSH` shell command to set the credentials query parameter within a session. This enables you to change credentials before executing a query, for example to switch to a database user with access to another keyspace. Note that the credentials are set for the remainder of the shell session and not just on a per query basis.

The list of credentials can contain one or multiple credentials. Each credential consists of an identity and a password separated by a colon `:`. To specify multiple credentials, append all the user names and passwords to the same credentials array.

* Command Line Option
* Shell Command

To set the credentials on startup, use the `-c` or `--credentials` command line option, followed by the list of credentials.

---

In this example, `$USER2` and `$PASSWORD2` are alternative credentials with access to a second keyspace.

Example

```sh
./cbq e $BASE_URL -c=$USER:$PASSWORD,$USER2:$PASSWORD2
```

To change credentials during a session, use the `\SET` shell command to specify the `-creds` query parameter, followed by the list of credentials.

---

In this example, `<USER2>` and `<PASSWORD2>` are alternative credentials with access to a second keyspace.

Example

```sqlpp
\SET -creds <USER>:<PASSWORD>, <USER2>:<PASSWORD2>;
```

For more information about using multiple credentials, see [Query Service REST API](../../n1ql-rest-query/index.md#creds) and [Request with Authentication — Request Parameter](../n1ql-rest-api/exauthrequest.md).

### [](#displaying-the-credentials)Displaying the Credentials

You can display the credentials for the current session using the [\\ECHO](#cbq-echo) shell command. This command displays only the user names (and not the passwords).

Example

```sqlpp
\ECHO -creds;
```

Result

<USER>:*

You can also display a full list of variables using the [\\SET](#cbq-set) command specified without any arguments.

Example

```sqlpp
\SET;
```

Result

 Query Parameters :
 Parameter name : creds
 Value : [ "<USER>:*" ]


 Named Parameters :

 User Defined Session Parameters :

 Predefined Session Parameters :
 Parameter name : histfile
 Value : [".cbq_history"]

 Parameter name : batch
 Value : ["off"]

 Parameter name : quiet
 Value : [false]

## [](#cbq-encrypted)Using an Encrypted Connection

The cbq shell supports self-signed certificates for encrypting communication between clusters.

You can connect to the cluster or node with an encrypted protocol scheme — that is, either `https://` or `couchbases://`. To do this, you can provide the root CA certificate, the chain certificate, and the client key file using the [\--cacert](#opt-cacert), [\--cert](#opt-cert), and [\--key](#opt-key) options. You can use the [\--no-ssl-verify](#opt-skip-verify) option to skip the verification of certificates.

When connecting to a cluster or node with an encrypted protocol scheme, the default ports are 18091 and 18093\. You cannot specify the port when using the `couchbases://` protocol scheme.

For more details, refer to [Connecting to the Cluster or Query Node](#cbq-connect-to-cluster).

## [](#cbq-parameter-manipulation)Parameter Manipulation

The cbq shell categorizes parameters into the following types:

* Query parameters
* Named parameters
* User-defined session variables
* Pre-defined session variables

### [](#parameter-configuration)Parameter Configuration

When using parameters, you can set a stack of values for each parameter. You can either push a new value onto the stack using the `\PUSH` command, or set the current value for a parameter using the `\SET` command. The `\SET` command always modifies the top of a variable’s stack while the `\PUSH` command adds to the stack. When you use `\PUSH` with no arguments, it copies the top element of every parameter’s stack (except the predefined parameters) and pushes that copy to the top of its respective stack. As a result, each stack grows by 1, but the values are preserved. You can then use the `\SET` command to modify the top value.

To unset the values from a parameter’s stack, you can use the `\UNSET` command to remove all the values from the stack and delete the corresponding parameter stack. However, if you want to delete a single value from the settings, use the `\POP` command. When you use the `\POP` command with no arguments, it pops the one value from the top of each parameter’s stack.

To display all the parameters defined in a session, use the `\SET` command with no arguments.

### [](#setting-variable-values)Setting Variable Values

To set the value of a parameter, use the `\SET` or `\PUSH` shell command, followed by a parameter name and parameter value.

The parameter name may have a prefix, depending on the type of parameter: query parameter, named parameter, user-defined session variable, or predefined session variable. The cbq shell uses the prefix to differentiate between the different types of parameters.

__Table 1\. Prefixes for Parameters__
| Prefix     | Parameter Type                         |
| ---------- | -------------------------------------- |
| \-         | Query parameter                        |
| \-$ or \-@ | Named parameters                       |
| $          | User defined session variable          |
| No prefix  | Predefined (built-in) session variable |

> [!NOTE]
> Positional parameters are set using the `-args` query parameter.

For more details about the available query parameters (prefixed by `-`), see [Request-Level Parameters](../n1ql-manage/query-settings.md#section%5Fnnj%5Fsjk%5Fk1b). As a best practice, save the initial set of basic parameters and their default values using the `\PUSH` command (with no arguments).

The following example sets the `airport` named parameter, pushes two positional parameters to the `args` query parameter stack, and then displays all parameters.

Example

```sqlpp
\SET -$airport "SJC";
\PUSH -args ["LAX", 6];
\SET;
```

Result

Query Parameters ::
Parameter name : args Value  [["LAX",6]]

Named Parameters ::
Parameter name : airport Value  ["SJC"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

The following example pushes a new value to the `airport` named parameter stack, duplicates the top value in each stack except the predefined session parameters, and then displays all parameters.

Example

```sqlpp
\PUSH -$airport "SFO";
\PUSH;
\SET;
```

Result

Query Parameters ::
Parameter name : args Value  [["LAX",6] ["LAX",6]]

Named Parameters ::
Parameter name : airport Value  ["SJC" "SFO" "SFO"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

The following example sets the top level of the `airport` named parameter stack to a new value, and then displays all parameters.

Example

```sqlpp
\SET -args ["SFO", 8];
\SET;
```

Result

Query Parameters ::
Parameter name : args Value  [["LAX",6] ["SFO",8]]

Named Parameters ::
Parameter name : airport Value  ["SJC" "SFO" "SFO"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

### [](#handling-named-parameters)Handling Named Parameters

To define named parameters, use the `\SET` or `\PUSH` command. For each named parameter, prefix the variable name with `-$` or `-@`.

For more details about named parameters, see [Named Parameters and Positional Parameters](../n1ql-manage/query-settings.md#section%5Fsrh%5Ftlm%5Fn1b).

The following example creates named parameters `r` and `date` with values `9.5` and `"1-1-2016"` respectively.

Example

```sqlpp
\SET -$r 9.5;
\SET -@date "1-1-2016";
```

### [](#handling-positional-parameters)Handling Positional Parameters

To define positional parameters, use the `\SET` or `\PUSH` command with the `-args` query parameter, followed by an array containing the different values that correspond to positions within the query.

For more details about positional parameters, see [Named Parameters and Positional Parameters](../n1ql-manage/query-settings.md#section%5Fsrh%5Ftlm%5Fn1b).

Example

```sqlpp
\SET -args [ 9.5, "1-1-2016"];
```

### [](#handling-predefined-session-variables)Handling Predefined Session Variables

The following table lists the available predefined session variables.

__Table 2\. Predefined Session Variables__
| Variable Name | Possible Values      | Description                                                                                                                                                                                       |
| ------------- | -------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| histfile      | Valid file name      | Specifies the file name to store the command history. By default the file is saved in the user’s home directory. Default: .cbq\_history                                                           |
| batch         | String ("on", "off") | This variable is available only with the Analytics Service. When specified, cbq sends the queries to Analytics only when you hit EOF or \\ to indicate the end of the batch input. Default: "off" |
| quiet         | Boolean              | When specified, disables the startup connection message for the cbq shell. Default: false                                                                                                         |

### [](#resetting-variable-values)Resetting Variable Values

You can reset the value of a variable by either popping it or deleting it altogether.

To pop the top of every parameter’s stack once, use the `\POP` command without any arguments.

Example

```sqlpp
\POP;
\SET;
```

Result

Query Parameters ::
Parameter name : args Value  [["LAX",6]]

Named Parameters ::
Parameter name : airport Value  ["SJC" "SFO"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

To pop the top value from a single parameter’s stack, use the `\POP` command, followed by the parameter prefix and parameter name.

Example

```sqlpp
\POP -$airport;
\SET;
```

Result

Query Parameters ::
Parameter name : args Value  [["LAX",6]]

Named Parameters ::
Parameter name : airport Value  ["SJC"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

To pop all the values of a parameter’s stack and then delete the parameter, use the `\UNSET` command, followed by the parameter prefix and parameter name.

Example

```sqlpp
\UNSET -$airport;
\SET;
```

Result

Query Parameters ::
Parameter name : args Value  [["LAX",6]]

Named Parameters ::

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

## [](#cbq-shell-cmd-echo)Using ECHO to Display Values of Parameters and More

The ECHO command displays the current values of the parameters set for a session. You can use it to display any input string or command aliases that have been created using the ALIAS shell command.

### [](#echo-a-string-or-statement)Echo a String or Statement

To echo a string or a SQL++ statement, use the `\ECHO` command, followed by the string or statement.

Example

```sqlpp
\ECHO hello;
```

Result

hello

### [](#echo-an-alias)Echo an Alias

To echo a command alias, use the `\ECHO` command, followed by two backslashes and the command alias name.

Example

```sqlpp
\ECHO \\travel-alias1;
```

Result

```sqlpp
SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
```

### [](#echo-a-parameter)Echo a Parameter

To echo a parameter, use the `\ECHO` command, followed by the parameter prefix and parameter name.

If you do not include the parameter prefix, the shell considers the parameter as a generic statement and displays the parameter as is.

Example

```sqlpp
\ECHO -$r;
```

Result

9.5

## [](#cbq-shell-cmd-alias)Command Alias

Using the ALIAS shell command, you can define and store aliases for commands. This is useful when you have lengthy queries that need to be executed often.

### [](#create-command-aliases)Create Command Aliases

To define an alias, use the `\ALIAS` command, followed by the command alias name and the query.

Example

```sqlpp
\ALIAS travel-alias1 SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
```

### [](#run-command-aliases)Run Command Aliases

To run the command alias, type two backslashes `\\`, followed by the command alias name.

Example

```sqlpp
\\travel-alias1;
```

Result

```json
{
    "requestID": "b25c84d6-7b7b-440a-a286-5027e6ecbbb5",
    "signature": {
        "*": "*"
    },
    "results": [
    {
        "airline": {
            "callsign": "MILE-AIR",
            "country": "United States",
            "iata": "Q5",
            "icao": "MLA",
            "id": 10,
            "name": "40-Mile Air",
            "type": "airline"
        }
    }
    ],
    "status": "success",
    // ...
}
```

### [](#list-command-aliases)List Command Aliases

To list all the existing aliases, use the `\ALIAS` command without options.

Example

```sqlpp
\ALIAS;
```

Result

serverversion  select version()
travel-alias1  SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;

### [](#delete-command-aliases)Delete Command Aliases

You can delete a defined alias using the `\UNLIAS` command, followed by the alias name. This command can take multiple arguments and deletes the defined alias for every input name.

Example

```sqlpp
\UNALIAS serverversion travel-alias1;
```

Check aliases

```sqlpp
\ALIAS;
```

Result

 ERROR 141 : Alias does not exist :

## [](#cbq-prepared-stmts)Executing Prepared Statements

You can use the shell command to execute prepared statements. As a pre-requisite, you must first prepare a statement. To prepare and execute a statement, follow these steps:

1. Set the named and positional parameters that are present in the prepared statement.
2. Prepare a statement using the SQL++ [PREPARE](../n1ql-language-reference/prepare.md) statement. If you do not specify a name for the prepared statement, a unique name is assigned. You can use this auto-assigned name when executing the prepared statement. If you specify a name, you can use this name to run the prepared statement.
3. Execute the prepared statement using the SQL++ [EXECUTE](../n1ql-language-reference/execute.md) statement.

## [](#canceling-a-query)Canceling a Query

You can cancel a running query by using the Ctrl+C keys.

### [](#connection-timeout-parameter)Connection Timeout Parameter

You can use the timeout parameter to limit the running time of a query. This parameter specifies the time to wait before returning an error when executing a query.

Timeout can be specified in the following units: `ns` for nanoseconds, `μs` for microseconds, `ms` for milliseconds, `s` for seconds, `m` for minutes, and `h` for hours. Examples of valid values include `"0.5s"`, `"10ms"`, or `"1m"`. An error is thrown if the timeout is invalid.

* Command Line Option
* Shell Command

Use the `-t` or `--timeout` command line option, followed by the length of the timeout.

---

Example

```sh
./cbq -e $BASE_URL -u $USER -p $PASSWORD --timeout="2s"
```

Use the `\SET` shell command to set the `TIMEOUT` parameter, followed by the length of the timeout.

---

Example

```sqlpp
\SET -TIMEOUT 1ms;
```

## [](#cbq-file-based-ops)File Based Operations

Using the file based commands and options, the cbq shell can execute SQL++ and shell commands contained in files. There are two ways to accomplish this.

* Command Line Option
* Shell Command

Use the `-f` or `--file` command line option, followed by the input file.

The cbq shell executes the commands present in the input file, prints them to stdout (or to a file if using redirects), and exits.

---

Consider the input file, `sample.txt`, containing the following commands.

sample.txt

```sqlpp
CREATE PRIMARY INDEX ON `travel-sample`.inventory.airline USING GSI;
SELECT * from `travel-sample`.inventory.airline LIMIT 2;
SELECT callsign from `travel-sample`.inventory.airline LIMIT 3;
\HELP;
```

Example

```sh
./cbq -e $BASE_URL -u $USER -p $PASSWORD -f=sample.txt
```

Results

```console
 Connected to : http://<HOST>:8091/. Type Ctrl-D or \QUIT to exit.

 Path to history file for the shell : ~/.cbq_history
CREATE PRIMARY INDEX ON `travel-sample`.inventory.airline USING GSI;
{ ...
  "results": [ ],
  ...
}
SELECT * from `travel-sample`.inventory.airline LIMIT 2;
{ ...
  "results": [ ],
  ...
}
SELECT callsign from `travel-sample`.inventory.airline LIMIT 3;
{ ...
  "results": [ ],
  ...
}
\HELP;
Help information for all shell commands.
...
$
```

Use the `\SOURCE` shell command, followed by the input file.

The cbq shell executes the commands present in the input file and prints them to stdout, or to a file if using redirects.

---

Consider the input file, `sample.txt`, containing the following commands.

sample.txt

```sqlpp
CREATE PRIMARY INDEX ON `travel-sample`.inventory.airline USING GSI;
SELECT * from `travel-sample`.inventory.airline LIMIT 2;
SELECT callsign from `travel-sample`.inventory.airline LIMIT 3;
\HELP;
```

Example

```sqlpp
\SOURCE sample.txt;
```

Results

```console
CREATE PRIMARY INDEX ON `travel-sample`.inventory.airline USING GSI;
{ ...
  "results": [ ],
 ...
}
SELECT * from `travel-sample`.inventory.airline LIMIT 2;
{ ...
  "results": [ ],
  ...
}
SELECT callsign from `travel-sample`.inventory.airline LIMIT 3;
{ ...
  "results": [ ],
  ...
}
\HELP;
Help information for all shell commands.
...
cbq>
```

### [](#redirecting-results-to-a-file)Redirecting Results to a File

You can redirect all the output for a session or part of a session to a specified output file. If the file doesn’t exist, it is created. If the file already exists, it is overwritten.

* Command Line Option
* Shell Command

Use the `-o` or `--output` command line option, followed by the output file.

---

Example

```sh
./cbq -e $BASE_URL -u $USER -p $PASSWORD -o temp_output.txt
```

To start redirecting commands during a session, use `\REDIRECT` followed by the output file. To stop redirecting commands, use `\REDIRECT OFF`. All the commands specified after `\REDIRECT` and before `\REDIRECT OFF` are saved into the specified output file.

You can specify multiple `\REDIRECT` commands. When you do so, the output file changes to the specified files and switches back to `stdout` only when you specify `\REDIRECT OFF`.

You can append redirected output to an existing file using [File Append Mode](#file-append-mode).

---

Example

```sqlpp
\REDIRECT temp_output.txt;
CREATE PRIMARY INDEX ON `travel-sample`.inventory.airline USING GSI;
SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
\HELP;
\REDIRECT OFF;
```

### [](#file-append-mode)File Append Mode

You can use file append mode to specify that cbq should append redirected output to the end of an existing file, rather than overwriting the existing file.

Note that file append mode is only available with the `\REDIRECT` command within a shell session. It is not available for the `-o` or `--output` command line option. When you use the `-o` or `--output` command line option, the specified output file is always overwritten.

To use file append mode, include a plus sign `+` at the start of the output path or filename.

Example

```sqlpp
\REDIRECT +temp_output.txt;
SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
\REDIRECT OFF;
```

Every time you start appending to the output file, a timestamp is added to the end of the output file, followed by any redirected commands and results.

-- <2021-07-30T14:48:43.661+01:00> : opened in append mode

SELECT * FROM `travel-sample`.inventory.airline LIMIT 1
...

## [](#cbq-server-shell-info)Server and Shell Information

The cbq shell provides commands that convey information about the shell or cluster endpoints.

### [](#version)Version

You can find the version of the client (shell) by using either the command line option to display the current version of the shell and exit, or as a shell command to print the version of the shell during the shell session.

To display the version of the query service, use the [VERSION()](../n1ql-language-reference/metafun.md#version) function in SQL++.

* Command Line Option
* Shell Command

Use the `-v` or `--version` command line option.

---

Example

```sh
./cbq -v
```

Result

GO VERSION : go1.22.2
SHELL VERSION : 7.6.2-3721

Use N1QL queries select version(); or select min_version(); to display server version.

Use the `\VERSION` shell command.

---

Example

```sqlpp
\VERSION;
```

Result

GO VERSION : go1.22.2
SHELL VERSION : 7.6.2-3721

Use N1QL queries select version(); or select min_version(); to display server version.

### [](#copyright)Copyright

You can view the copyright, attributions, and distribution terms of the command line query tool using the `\COPYRIGHT` shell command.

Example

```sqlpp
\COPYRIGHT;
```

Result

Copyright (c) 2016 Couchbase, Inc. Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the
License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific language governing permissions
and limitations under the License.

## [](#exiting-the-cbq-shell-2)Exiting the cbq Shell

You can exit the cbq shell by pressing Ctrl+D or by using the `\EXIT` or `\QUIT` command.

The cbq shell first saves the history, closes existing connections, saves the current session in a session file, resets all environment variables, and then closes the shell liner interface.

Example

```sqlpp
\EXIT;
```

Result

```console
$
```

## [](#executing-a-script)Executing a Script

You can use the `--script` option to start cbq, execute a single SQL++ query, and exit the shell.

Example

```sh
./cbq -u $USER -p $PASSWORD -e $BASE_URL \
--script="SELECT * FROM \`travel-sample\`.inventory.airline LIMIT 1;"
```

Results

Connected to : http://<HOST>:8091/. Type Ctrl-D or \QUIT to exit.

Path to history file for the shell : ~/.cbq_history

SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
{
    ...
}

### [](#exit-on-error)Exit On Error

When you specify the argument `--exit-on-error`, the cbq shell checks the result returned after executing the query for any error and exits when the first error is encountered.

### [](#exit-status)Exit Status

The cbq shell returns the exit status 0 for successful exit with no errors and 1 if an error was encountered before exiting.

## [](#available-command-line-options-and-shell-commands)Available Command Line Options and Shell Commands

> [!NOTE]
> The [command line options](#table%5Fa3h%5Frhz%5Fdw) are case sensitive. The [cbq shell commands](#table%5Fhtk%5Fhgc%5Ffw) are case insensitive.

__Table 3\. Command Line Options for cbq Shell__
| Option                            | Arguments                                                      | Description and Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-e \--engine                     | string (url)                                                   | The connection string consists of a protocol scheme, followed by a host, and optionally a port number to connect to the query service (8093) or the Couchbase cluster (8091). For more details, refer to [Connecting to the Cluster or Query Node](#cbq-connect-to-cluster). Shell command: [\\CONNECT](#cbq-connect) Default http://localhost:8091 Examples ./cbq --engine $BASE\_URL \\ \-u $USER -p $PASSWORD ./cbq -e $BASE\_URL \\ \-u $USER -p $PASSWORD Result Connected to : http://<HOST>:8091/. Type Ctrl-D or \\QUIT to exit. Path to history file for the shell : /Users/myuser1/.cbq\_history                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| \-ne \--no-engine                 | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | When specified, the cbq shell does not connect to any query service. You must explicitly connect to a query service using the [\\CONNECT](#cbq-connect) shell command. Default false Example ./cbq --no-engine                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \-ncfg \--networkconfig           | string (auto, default, external)                               | Specifies whether to connect to a node’s principal or alternate address. auto — Select the principal address or alternate address automatically, depending on the input IP. default — Use the principal address. external — Use the alternate addresses. Default auto Example ./cbq -ncfg default \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| \-q \--quiet                      | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | When specified, disables the startup connection message for the cbq shell. Default false Example ./cbq -q \\ \-e $BASE\_URL -u $USER -p $PASSWORD Result cbq>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| \-ad \--advise                    | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | Runs ADVISE on all queries in the specified file, or that are read from standard input, if a file is not provided with the \-file option. Default false Example ./cbq -advise -file queries.txt \\ \-e $BASE\_URL -u $USER -p $PASSWORD queries.txt SELECT ADVISOR(\["select \* from collection1 where id = 1;",                 "select \* from collection2 where name is not missing;"\]) Result {     "requestID": "15ed5c93-e5f6-4193-83fa-6fdc87847552",     "signature": {         "$1": "object"     },     "results": \[     {         "$1": {             "recommended\_indexes": \[                 {                     "index": "CREATE INDEX adv\_id ON \`collection1\`(\`id\`)",                     "statements": \[                         {                             "run\_count": 1,                             "statement": "select \* from collection1 where id = 1;"                         }                     \]                 },                 {                     "index": "CREATE INDEX adv\_name ON \`collection2\`(\`name\`)",                     "statements": \[                         {                             "run\_count": 1,                             "statement": "select \* from collection2 where name is not missing;"                         }                     \]                 }             \]         }     }     \] } |
| \-a \--analytics                  | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | Only applicable when connecting to the Analytics Service. If specified, when you connect to a cluster, cbq automatically discovers and connects to an Analytics node. This option also switches on [batch mode](#opt-batch). Default false Example ./cbq --analytics \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \-b \--batch                      | string (on, off) \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] | This option is available only with the Analytics Service. When specified, cbq sends the queries to Analytics only when you hit EOF or \\ to indicate the end of the batch input. Default off Examples ./cbq --batch \\ \-e $BASE\_URL -u $USER -p $PASSWORD You can also set the batch mode in the interactive session using the [\\SET](#cbq-set) command: \\set batch on; \\set batch off;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \-qc \--query\_context            | string                                                         | Sets the query context parameter. For more information, see [Query Context](queriesandresults.md#query-context). Shell command: [\\SET](#cbq-set) \-query\_context Default none Example ./cbq -qc "travel-sample.inventory" \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \-t \--timeout                    | string (duration)                                              | Sets the query timeout parameter. For more information, see [timeout](../n1ql-manage/query-settings.md#timeout%5Freq). Shell command: [\\SET](#cbq-set) \-timeout Default 0ms Example ./cbq --timeout="1s" \\ \-e $BASE\_URL -u $USER -p $PASSWORD For further examples, see [Connection Timeout Parameter](#connection-timeout-parameter).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \-u \--user                       | string                                                         | Specifies a single user name to log in to Couchbase. When used by itself, without the \-p option to specify the password, you will be prompted for the password. This option requires administration credentials and you cannot switch the credentials during a session. Couchbase recommends using the \-u and \-p option if your password contains special characters such as #, $, %, &, (,), or '. Default none Example ./cbq -u $USER \\ \-e $BASE\_URL Result Enter Password:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \-p \--password                   | string                                                         | Specifies the password for the given user name. You cannot use this option by itself. It must be used with the -u option to specify the user name. This option requires administration credentials and you cannot switch the credentials during a session. Couchbase recommends using the \-u and \-p option if your password contains special characters such as #, $, %, &, (,), or '. Default none Example ./cbq -u $USER -p $PASSWORD \\ \-e $BASE\_URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \-c \--credentials                | string                                                         | Specify the login credentials in the form of username:password. You can specify credentials for different keyspaces by separating them with a comma. Shell command: [\\SET](#cbq-set) \-creds REST API: \-creds parameter Default none Example ./cbq -c=$USER:$PASSWORD,$USER2:$PASSWORD2 \\ \-e $BASE\_URL                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \-v \--version                    | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | When specified, provides the version of the cbq shell. To display the version of the query engine (this is not the same as the version of Couchbase Server itself), use one of the following SQL++ queries: select version(); select min\_version(); Shell command: [\\VERSION](#cbq-version) Default false Example ./cbq --version Result GO VERSION : go1.21.6 SHELL VERSION : 7.6.0-2176 Use N1QL queries select version(); or select min\_version(); to display server version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \-h \--help                       | none                                                           | Provides help for the command line options. Shell command: [\\HELP](#cbq-help) Default none Example ./cbq --help                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \-s \-script                      | string                                                         | Provides a single command mode to execute a query from the command line. You can also use multiple \-s options on the command line. If one of the commands is incorrect, an error is displayed for that command and cbq continues to execute the remaining commands. Default none Examples ./cbq -s="SELECT \* FROM \\\`travel-sample\\\`.inventory.airline LIMIT 1;" \\ \-e $BASE\_URL -u $USER -p $PASSWORD ./cbq -s="\\SET v 1" -s="\\SET b 2" -s="\\PUSH b3" \\ \-s="\\SET b 5" -s="\\SET" -ne Result Path to history file for the shell : \~/.cbq\_history  \\SET v 1  \\SET b 2  \\PUSH b3  ERROR 139 : Too few input arguments to command.  \\SET b 5  \\SET  Query Parameters :  Named Parameters :  User Defined Session Parameters :  Predefined Session Parameters :  Parameter name : histfile  Value : \[".cbq\_history"\]  Parameter name : batch  Value : \["off"\]  Parameter name : quiet  Value : \[false\]  Parameter name : v  Value : \[1\]  Parameter name : b  Value : \[5\]                                                                                                                                                                                                                                                                                                                                                                                               |
| \-f \--file                       | string (path)                                                  | Provides an input file which contains all the commands to be run. Shell command: [\\SOURCE](#cbq-source) Default none Example ./cbq --file="sample.txt" \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| \-o \--output                     | string (path)                                                  | Specifies an output file where the commands and their results are to be written. If the file doesn’t exist, it is created. If the file already exists, it is overwritten. Shell command: [\\REDIRECT](#cbq-redirect) Default none Example ./cbq -o="results.txt" -s="SELECT \* FROM \\\`travel-sample\\\`.inventory.airline LIMIT 1;" \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| \--pretty                         | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | Specifies whether the output should be formatted with line breaks and indents. This option is set to true by default. To specify that the output should _not_ be formatted with line breaks and indents, you must explicitly set this option to false. Default true Example ./cbq --pretty=false -s="SELECT \* FROM \\\`travel-sample\\\`.inventory.airline LIMIT 1;" \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| \--exit-on-error                  | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | When specified, the cbq shell must exit when it encounters the first error. Default false Example ./cbq --exit-on-error -f="sample.txt" \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| \--cacert                         | string (path)                                                  | Only applicable when using an encrypted protocol scheme — either https:// or couchbases://. Specifies the path to the root CA certificate to verify the identity of the server. Default none Example ./cbq --cacert ./root/ca.pem \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| \--cert                           | string (path)                                                  | Only applicable when using an encrypted protocol scheme — either https:// or couchbases://. Specifies the path to the chain certificate. Default none Example ./cbq --cert ./client/client/chain.pem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \--key                            | string (path)                                                  | Only applicable when using an encrypted protocol scheme — either https:// or couchbases://. Specifies the path to the client key file. Default none Examples ./cbq --key ./client/client/client.key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \--no-ssl-verify or \-skip-verify | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | Only applicable when using an encrypted protocol scheme — either https:// or couchbases://. When specified, the cbq shell can skip the verification of certificates. Default false Examples ./cbq --no-ssl-verify -f="sample.txt" \\ \-e $BASE\_URL -u $USER -p $PASSWORD ./cbq -skip-verify \\ \-e $BASE\_URL -u $USER -p $PASSWORD                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |

__Table 4\. cbq Shell Commands__
| Shell Command  | Arguments                                                 | Description and Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| -------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \\CONNECT      | url                                                       | Connects cbq shell to the specified query engine or Couchbase cluster. The connection string consists of a protocol scheme, followed by a host, and optionally a port number to connect to the query service (8093) or the Couchbase cluster (8091). For more details, refer to [Connecting to the Cluster or Query Node](#cbq-connect-to-cluster). Command Line Option: [\-e](#opt-engine) or [\--engine](#opt-engine) Examples \\CONNECT <BASE\_URL>;                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \\DISCONNECT   | none                                                      | Disconnects the cbq shell from the query service or cluster endpoint. Example \\DISCONNECT; Result  Couchbase query shell not connected to any endpoint.  Use \\CONNECT command to connect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \\EXIT \\QUIT  | none                                                      | Exits cbq shell. Examples \\EXIT; \\QUIT;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| \\SET          | parameter value parameter \= prefix : variable name       | Sets the top most value of the stack for the given variable with the specified value. Variables can be of the following types: Query parameters Session variables User-defined Pre-defined and named parameters. When the \\SET command is used without any arguments, it displays the values for all the parameters of the current session. Examples \\SET -args \[5, "12-14-1987"\]; \\SET -args \[6,7\];                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \\PUSH         | parameter value                                           | Pushes the specified value on to the given parameter stack. When the \\PUSH command is used without any arguments, it copies the top element of every variable’s stack, and then pushes that copy to the top of the respective variable’s stack. While each variable stack grows by 1, the previous values are preserved. Examples \\PUSH -args  \[8\]; \\PUSH; Check variable stack \\SET; Result  Query Parameters :  Parameter name : args  Value : \[\[6,7\] \[8\] \[8\]\] ...                                                                                                                                                                                                                                                                                                                                                                                                                   |
| \\UNSET        | parameter                                                 | Deletes or resets the entire stack for the specified parameter. Examples \\UNSET -args; \\SET; Result  Query Parameters :  ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \\POP          | parameter                                                 | Pops the top most value from the specified parameter’s stack. When the \\POP command is used without any arguments, it pops the top most value of every variable’s stack. Examples \\POP -args; \\SET; Result  Query Parameters :  Parameter name : args  Value : \[\[6,7\] \[8\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \\ALIAS        | shell-command or n1ql-statement                           | Creates a command alias for the specified cbq shell command or SQL++ statement. You can then execute the alias using \\\\alias-name;. When the \\ALIAS command is used without any arguments, it lists all the available aliases. Examples \\ALIAS travel-limit1 SELECT \* FROM \`travel-sample\`.inventory.airline LIMIT 1; \\ALIAS; Result serverversion  select version() travel-limit1  SELECT \* FROM \`travel-sample\`.inventory.airline LIMIT 1 Execute alias \\\\serverversion; Result {     "requestID": "ef63f01b-f159-437f-a4df-28d6145fa3c2",     "signature": {         "$1": "string"     },     "results": \[         {             "$1": "7.0.0-N1QL"         }     \],     "status": "success",     "metrics": {         "elapsedTime": "14.54962ms",         "executionTime": "13.164635ms",         "resultCount": 1,         "resultSize": 34,         "serviceLoad": 12     } } |
| \\UNALIAS      | alias-name                                                | Deletes the specified alias. Examples \\UNALIAS travel-limit1; \\ALIAS; Result serverversion  select version()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \\ECHO         | args where args can be parameters, aliases, or any input. | If the input is a parameter, this command echoes (displays) the value of the parameter. The parameter must be prefixed according to its type. See [Table 1](#table%5Fltk%5Fc5s%5F5v) for details. If the input is not a parameter, the command echoes the statement as is. If the input is an alias, the command displays the value of an alias command. Examples \\ECHO -$r; \\ECHO \\\\serverversion; Result select version()                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \\VERSION      | none                                                      | Displays the version of the client shell. Command Line Option: [\-v](#opt-version) or [\--version](#opt-version) Example \\VERSION; Result GO VERSION : go1.21.6 SHELL VERSION : 7.6.0-2176 Use N1QL queries select version(); or select min\_version(); to display server version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \\HELP         | command                                                   | Displays the help information for the specified command. When used without any arguments, it lists all the commands supported by the cbq shell. Command Line Option: [\-h](#opt-help) or [\--help](#opt-help) Example \\HELP ECHO; Result \\ECHO args ... Echo the input value. args can be a name (a prefixed-parameter), an alias (command alias) or a value (any input statement). Example : \\ECHO -$r ; \\ECHO \\\\tempalias;                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| \\COPYRIGHT    | none                                                      | Displays the copyright, attributions, and distribution terms. Example \\COPYRIGHT;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| \\SOURCE       | input-file                                                | Reads and executes the commands from a file. Multiple commands in the input file must be separated by ; and a new line. Command Line Option: [\-f](#opt-file) or [\--file](#opt-file) For example, sample.txt contains the following commands: sample.txt SELECT \* FROM \`travel-sample\`.inventory.airline LIMIT 1; \\ECHO this; #This is a comment; Example \\SOURCE sample.txt;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \\REDIRECT     | filename                                                  | Redirects the output of all the commands to the specified file until the cbq shell receives the \\REDIRECT OFF command. By default, the file is created in the directory that you were in when you started the cbq shell. You can specify a different location using relative paths. If the file doesn’t exist, it is created. If the file already exists, it is overwritten. You can append redirected output to an existing file using [File Append Mode](#file-append-mode). Command Line Option: [\-o](#opt-output) or [\--output](#opt-output) Example \\REDIRECT temp\_out.txt;                                                                                                                                                                                                                                                                                                                |
| \\REDIRECT OFF | none                                                      | Redirects the output of subsequent commands from a custom file to standard output (os.stdout). Example \\REDIRECT OFF;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |

## [](#shortcut-keys-for-cbq-shell)Shortcut Keys for cbq Shell

The following table lists the shortcut keys used by the `cbq` shell.

__Table 5\. Shortcut Keys for cbq Shell__
| Keystroke         | Action                                                     |
| ----------------- | ---------------------------------------------------------- |
| Ctrl+A, Home      | Move cursor to beginning of line                           |
| Ctrl+E, End       | Move cursor to end of line                                 |
| Ctrl+B, Left      | Move cursor one character left                             |
| Ctrl+F, Right     | Move cursor one character right                            |
| Ctrl+Left         | Move cursor to previous word                               |
| Ctrl+Right        | Move cursor to next word                                   |
| Ctrl+D, Del       | (if line is not empty) Delete character under cursor       |
| Ctrl+D            | (if line is empty) End of File - usually quits application |
| Ctrl+C            | Reset input (create new empty prompt)                      |
| Ctrl+L            | Clear screen (line is unmodified)                          |
| Ctrl+T            | Transpose previous character with current character        |
| Ctrl+H, BackSpace | Delete character before cursor                             |
| Ctrl+W            | Delete word leading up to cursor                           |
| Ctrl+K            | Delete from cursor to end of line                          |
| Ctrl+U            | Delete from start of line to cursor                        |
| Ctrl+P, Up        | Previous match from history                                |
| Ctrl+N, Down      | Next match from history                                    |
| Ctrl+R            | Reverse Search history (Ctrl+S forward, Ctrl+G cancel)     |
| Ctrl+Y            | Paste from Yank buffer (Alt+Y to paste next yank instead)  |
| Tab               | Next completion                                            |
| Shift+Tab         | (after Tab) Previous completion                            |

Source: <https://github.com/peterh/liner>

---

[1](#%5Ffootnoteref%5F1). Invoking a boolean option with no value sets the value to `true`. 

[2](#%5Ffootnoteref%5F2). Invoking this option with no value sets the value to `on`.