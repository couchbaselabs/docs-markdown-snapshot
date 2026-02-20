---
title: "cbq: The Command Line Shell for SQL++"
description: cbq is a comprehensive command line shell for SQL++.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/tools/pages/cbq-shell.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:7.2@server:tools:cbq-shell.adoc[]
---

[View original HTML](/server/7.2/tools/cbq-shell.html)

# cbq: The Command Line Shell for SQL++

> cbq is a comprehensive command line shell for SQL++. It is a powerful, developer friendly tool that enables you to query and update data from Couchbase Server. The cbq shell enables you to perform all the operations that are supported by the Query REST API and more, such as additional scripting functionality. 

The cbq shell executable, `cbq`, is available in the Couchbase Server installation directory.

The cbq shell interface accepts both shell commands as well as SQL++ commands. All the cbq shell commands start with a back-slash (\\). If the command does not start with a back-slash (\\), the cbq shell interprets the command as a SQL++ command.

When starting the cbq shell you can provide a set of command line options. If no options are present then it assumes default values for expected options.

> [!NOTE]
> The cbq shell commands are case insensitive. However, the command line options are case sensitive.

For the complete list of command line options and shell commands, refer to [Table 1](#table%5Fa3h%5Frhz%5Fdw) and [Table 2](#table%5Fhtk%5Fhgc%5Ffw).

The cbq shell enables you to manipulate parameters based on the REST API. See [Parameter Manipulation](#cbq-parameter-manipulation) for details.

## [](#running-the-cbq-shell)Running the cbq Shell

To run `cbq` on the local host:

1. Log in to a Couchbase Server node that has the query service enabled.
2. Open a command window.
3. Change to the Couchbase tools directory.

  * Linux
  * macOS
  * Microsoft Windows  
```console  
$ cd /opt/couchbase/bin  
```  
```console  
$ cd /Applications/Couchbase\ Server.app/Contents/Resources/couchbase-core/bin  
```  
```console  
> cd C:\Program Files\Couchbase\Server\bin  
```
4. Run the following command to connect to the local query node and start the interactive query shell:

  * Linux / macOS
  * Microsoft Windows  
```console  
$ ./cbq  
```  
```console  
> cbq  
```

### [](#executing-a-single-command)Executing a Single Command

You can use the `--script` option to execute a single SQL++ query and exit the shell:

```console
$ ./cbq -u Administrator -p password -e "http://localhost:8091" \
--script="SELECT * FROM \`travel-sample\`.inventory.airline LIMIT 1;"
```

Results

```console
Connected to : http://localhost:8091/. Type Ctrl-D or \QUIT to exit.

Path to history file for the shell : ~/.cbq_history

SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
{
    ...
}
```

### [](#support-for-multi-line-queries)Support for Multi-line Queries

The cbq shell supports multi-line queries by default, enabling you to enter a query over multiple lines. When entering a query, you can hit Enter without specifying a semi-colon (`;`) at the end of the line to move the cursor to the next line. The prompt `>` indicates that the shell is in multi-line mode. For example:

```console
cbq> SELECT *
   > FROM `travel-sample`.inventory.airline
   > LIMIT 1;
```

When you’re done, use a semi-colon `;` to indicate the end of the query, and then press Enter to execute the query.

### [](#handling-comments)Handling Comments

You can add comments in your query by preceding the comment with a `#` or `--`. The cbq shell interprets a line that starts with `#` or `--` as a comment, logs the line into history, and returns a new prompt. No other action is taken.

```console
cbq> SELECT *
   > #This is the first comment
   > FROM `travel-sample`.inventory.airline
   > --This is the second comment
   > LIMIT 1;
```

However, if a comment exists within a statement, it is considered as part of the SQL++ command. If the cbq shell encounters a block comment (enclosed between `/*` ... `*/`) within a statement, it sends the block comment to the query service.

```console
cbq> SELECT * FROM `travel-sample`.inventory.airline /* Block comment */ LIMIT 1;
```

### [](#file-based-operations)File Based Operations

The cbq shell can execute SQL++ and shell commands contained in files using file-based commands and options. See [File Based Operations](#cbq-file-based-ops) for more information.

### [](#history)History

The `cbq` shell stores the history for every session. All the commands executed in a session are stored in history. By default, history is stored in _\~/.cbq\_history_. You can change the name of the file using the SET command to set the predefined parameter `HISTFILE`.

```console
cbq> \SET HISTFILE filename;
```

By default, all the commands are stored in the specified file. You can scroll through history and retrieve the commands from history using the scrolling arrow keys. Once the query is on the command prompt, you can edit it before executing the updated query.

### [](#exit-status)Exit Status

The cbq shell returns the exit status 0 for successful exit with no errors and 1 if an error was encountered before exiting.

### [](#exit-on-error)Exit On Error

When you specify the argument `--exit-on-error`, the cbq shell checks the result returned after executing the query for any error and exits when the first error is encountered.

### [](#help)Help

Help displays the help information for the shell commands and for the general usage of cbq. Use the help option when bringing up the shell to display the information for all available options:

```console
$ ./cbq -h
$ ./cbq --help
```

Use the `\HELP` shell command during a session to display information for specific shell commands. If you specify one or more commands, the shell displays the usage information for the specified commands.

```console
cbq> \HELP command-name;
```

If you do not specify a command, the cbq shell lists all the commands for which syntax help is available.

```console
cbq> \HELP;
```

## [](#available-command-line-options-and-shell-commands)Available Command Line Options and Shell Commands

__Table 1\. Command Line Options for cbq Shell__
| Option                            | Arguments                                                      | Description and Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| --------------------------------- | -------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \-e \--engine                     | string (url)                                                   | The connection string consists of a protocol scheme, followed by a host, and optionally a port number to connect to the query service (8093) or the Couchbase cluster (8091). For more details, refer to [Connecting to the Cluster or Query Node](#cbq-connect-to-cluster). Shell command: [\\CONNECT](#cbq-connect) Default http://localhost:8091 Examples $ ./cbq -e couchbase://localhost $ ./cbq --engine http://localhost:8091 $ ./cbq -e http://localhost:8091 $ ./cbq -e http://\[fd63:6f75:6368:1075:816:3c1d:789b:bc4\]:8091 Result Connected to : http://localhost:8091/. Type Ctrl-D or \\QUIT to exit. Path to history file for the shell : /Users/myuser1/.cbq\_history cbq>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| \-ne \--no-engine                 | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | When specified, the cbq shell does not connect to any query service. You must explicitly connect to a query service using the [\\CONNECT](#cbq-connect) shell command. Default false Example $ ./cbq --no-engine                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \-ncfg \--networkconfig           | string (auto, default, external)                               | Specifies whether to connect to a node’s principal or alternate address. auto — Select the principal address or alternate address automatically, depending on the input IP. default — Use the principal address. external — Use the alternate addresses. Default auto Example $ ./cbq -ncfg default -e http://localhost:8091                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \-q \--quiet                      | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | When specified, disables the startup connection message for the cbq shell. Default false Example $ ./cbq -q -e http://localhost:8091 Result cbq>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \-ad \--advise                    | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | Runs ADVISE on all queries in the specified file, or that are read from standard input, if a file is not provided with the \-file option. Default false Example ./cbq -advise -file queries.txt Result SELECT ADVISOR(\["select \* from collection1 where id = 1;","select \* from collection2 where name is not missing;"\]) {     "requestID": "15ed5c93-e5f6-4193-83fa-6fdc87847552",     "signature": {         "$1": "object"     },     "results": \[     {         "$1": {             "recommended\_indexes": \[                 {                     "index": "CREATE INDEX adv\_id ON \`collection1\`(\`id\`)",                     "statements": \[                         {                             "run\_count": 1,                             "statement": "select \* from collection1 where id = 1;"                         }                     \]                 },                 {                     "index": "CREATE INDEX adv\_name ON \`collection2\`(\`name\`)",                     "statements": \[                         {                             "run\_count": 1,                             "statement": "select \* from collection2 where name is not missing;"                         }                     \]                 }             \]         }     }     \] |
| \-a \--analytics                  | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | Only applicable when connecting to the Analytics Service. When specified, if you are connecting to a cluster, cbq automatically discovers and connects to an Analytics node. This option also switches on [batch mode](#opt-batch). Default false Example $ ./cbq --analytics                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \-b \--batch                      | string (on, off) \[[2](#%5Ffootnotedef%5F2 "View footnote.")\] | This option is available only with the Analytics Service. When specified, cbq sends the queries to server only when you hit EOF or \\ to indicate the end of the batch input. Default off Examples $ ./cbq --batch You can also set the batch mode in the interactive session using the [\\SET](#cbq-set) command: cbq> \\set batch on; cbq> \\set batch off;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| \-t \--timeout                    | string (duration)                                              | Sets the query timeout parameter. Default 0ms Example $ ./cbq -e http://localhost:8091 --timeout="1s"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| \-u \--user                       | string                                                         | Specifies a single user name to log in to Couchbase. When used by itself, without the \-p option to specify the password, you will be prompted for the password. This option requires administration credentials and you cannot switch the credentials during a session. Couchbase recommends using the \-u and \-p option if your password contains special characters such as #, $, %, &, (,), or '. Default none Example $ ./cbq -e http://localhost:8091 -u=Administrator Result Enter Password:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \-p \--password                   | string                                                         | Specifies the password for the given user name. You cannot use this option by itself. It must be used with the -u option to specify the user name. This option requires administration credentials and you cannot switch the credentials during a session. Couchbase recommends using the \-u and \-p option if your password contains special characters such as #, $, %, &, (,), or '. Default none Example $ ./cbq -e http://localhost:8091 -u=Administrator -p=password                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| \-c \--credentials                | string                                                         | Specify the login credentials in the form of username:password. You can specify credentials for different keyspaces by separating them with a comma. Shell command: [\\SET](#cbq-set) \-creds REST API: \-creds parameter Default none Example $ ./cbq -e http://localhost:8091 -c=travel-sample:password,Administrator:password                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \-v \--version                    | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | When specified, provides the version of the cbq shell. To display the query engine version of Couchbase Server (this is not the same as the version of Couchbase Server itself), use one of the following SQL++ queries: select version(); select min\_version(); Shell command: [\\VERSION](#cbq-version) Default false Example $ ./cbq --version Result SHELL VERSION  : 2.0 Use {sqlpp} queries select version(); or select min\_version(); to display server version.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \-h \--help                       | none                                                           | Provides help for the command line options. Shell command: [\\HELP](#cbq-help) Default none Example $ ./cbq --help                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| \-s \-script                      | string                                                         | Provides a single command mode to execute a query from the command line. You can also use multiple \-s options on the command line. If one of the commands is incorrect, an error is displayed for that command and cbq continues to execute the remaining commands. Default none Examples $ ./cbq -u Administrator -p password -s="SELECT \* FROM \\\`travel-sample\\\`.inventory.airline LIMIT 1;" $ ./cbq -s="\\SET v 1" -s="\\SET b 2" -s="\\PUSH b3" -s="\\SET b 5" -s="\\SET" -ne Result Path to history file for the shell : \~/.cbq\_history  \\SET v 1  \\SET b 2  \\PUSH b3  ERROR 139 : Too few input arguments to command.  \\SET b 5  \\SET  Query Parameters :  Named Parameters :  User Defined Session Parameters :  Predefined Session Parameters :  Parameter name : histfile  Value : \[".cbq\_history"\]  Parameter name : batch  Value : \["off"\]  Parameter name : quiet  Value : \[false\]  Parameter name : v  Value : \[1\]  Parameter name : b  Value : \[5\]                                                                                                                                                                                                                                                                                                                                   |
| \-f \--file                       | string (path)                                                  | Provides an input file which contains all the commands to be run. Shell command: [\\SOURCE](#cbq-source) Default none Example $ ./cbq --file="sample.txt"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \-o \--output                     | string (path)                                                  | Specifies an output file where the commands and their results are to be written. If the file doesn’t exist, it is created. If the file already exists, it is overwritten. Shell command: [\\REDIRECT](#cbq-redirect) Default none Example $ ./cbq -u Administrator -p password -o="results.txt" -s="SELECT \* FROM \\\`travel-sample\\\`.inventory.airline LIMIT 1;"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \--pretty                         | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | Specifies whether the output should be formatted with line breaks and indents. This option is set to true by default. To specify that the output should _not_ be formatted with line breaks and indents, you must explicitly set this option to false. Default true Example $ ./cbq -u Administrator -p password --pretty=false -s="SELECT \* FROM \\\`travel-sample\\\`.inventory.airline LIMIT 1;"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \--exit-on-error                  | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | When specified, the cbq shell must exit when it encounters the first error. Default false Example $ ./cbq --exit-on-error -f="sample.txt"                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \--cacert                         | string (path)                                                  | Only applicable when using an encrypted protocol scheme — either _https://_ or _couchbases://_. Specifies the path to the root CA certificate to verify the identity of the server. Default none Example $ ./cbq --cacert ./root/ca.pem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \--cert                           | string (path)                                                  | Only applicable when using an encrypted protocol scheme — either _https://_ or _couchbases://_. Specifies the path to the chain certificate. Default none Example $ ./cbq --cert ./client/client/chain.pem                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| \--key                            | string (path)                                                  | Only applicable when using an encrypted protocol scheme — either _https://_ or _couchbases://_. Specifies the path to the client key file. Default none Examples $ ./cbq --key ./client/client/client.key                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| \--no-ssl-verify or \-skip-verify | boolean \[[1](#%5Ffootnotedef%5F1 "View footnote.")\]          | Only applicable when using an encrypted protocol scheme — either _https://_ or _couchbases://_. When specified, the cbq shell can skip the verification of certificates. Default false Examples $ ./cbq --no-ssl-verify -f="sample.txt" $ ./cbq -skip-verify https://127.0.0.1:18091                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |

__Table 2\. cbq Shell Commands__
| Shell Command  | Arguments                                                 | Description and Examples                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| -------------- | --------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| \\CONNECT      | url                                                       | Connects cbq shell to the specified query engine or Couchbase cluster. The connection string consists of a protocol scheme, followed by a host, and optionally a port number to connect to the query service (8093) or the Couchbase cluster (8091). For more details, refer to [Connecting to the Cluster or Query Node](#cbq-connect-to-cluster). Command Line Option: [\-e](#opt-engine) or [\--engine](#opt-engine) Examples cbq> \\CONNECT http://localhost:8093; cbq> \\CONNECT http://\[fd63:6f75:6368:1075:816:3c1d:789b:bc4\]:8091;                                                                                                                                                                                                                                                                                                                                                                        |
| \\DISCONNECT   | none                                                      | Disconnects the cbq shell from the query service or cluster endpoint. Example cbq> \\DISCONNECT; Result  Couchbase query shell not connected to any endpoint.  Use \\CONNECT command to connect.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| \\EXIT \\QUIT  | none                                                      | Exits cbq shell. Examples cbq> \\EXIT; cbq> \\QUIT;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| \\SET          | parameter value parameter \= prefix : variable name       | Sets the top most value of the stack for the given variable with the specified value. Variables can be of the following types: Query parameters Session variables User-defined Pre-defined and named parameters. When the \\SET command is used without any arguments, it displays the values for all the parameters of the current session. Examples cbq> \\SET -args \[5, "12-14-1987"\]; cbq> \\SET -args \[6,7\];                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \\PUSH         | parameter value                                           | Pushes the specified value on to the given parameter stack. When the \\PUSH command is used without any arguments, it copies the top element of every variable’s stack, and then pushes that copy to the top of the respective variable’s stack. While each variable stack grows by 1, the previous values are preserved. Examples cbq> \\PUSH -args  \[8\]; cbq> \\PUSH; Check variable stack cbq> \\SET; Result  Query Parameters :  Parameter name : args  Value : \[\[6,7\] \[8\] \[8\]\] ...                                                                                                                                                                                                                                                                                                                                                                                                                   |
| \\UNSET        | parameter                                                 | Deletes or resets the entire stack for the specified parameter. Examples cbq> \\UNSET -args; cbq> \\SET; Result  Query Parameters :  ...                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| \\POP          | parameter                                                 | Pops the top most value from the specified parameter’s stack. When the \\POP command is used without any arguments, it pops the top most value of every variable’s stack. Examples cbq> \\POP -args; cbq> \\SET; Result  Query Parameters :  Parameter name : args  Value : \[\[6,7\] \[8\]\]                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| \\ALIAS        | shell-command or n1ql-statement                           | Creates a command alias for the specified cbq shell command or SQL++ statement. You can then execute the alias using \\\\alias-name;. When the \\ALIAS command is used without any arguments, it lists all the available aliases. Examples cbq> \\ALIAS travel-limit1 SELECT \* FROM \`travel-sample\`.inventory.airline LIMIT 1; cbq> \\ALIAS; Result serverversion  select version() travel-limit1  SELECT \* FROM \`travel-sample\`.inventory.airline LIMIT 1 Execute alias cbq> \\\\serverversion; Result {     "requestID": "ef63f01b-f159-437f-a4df-28d6145fa3c2",     "signature": {         "$1": "string"     },     "results": \[         {             "$1": "7.0.0-N1QL"         }     \],     "status": "success",     "metrics": {         "elapsedTime": "14.54962ms",         "executionTime": "13.164635ms",         "resultCount": 1,         "resultSize": 34,         "serviceLoad": 12     } } |
| \\UNALIAS      | alias-name                                                | Deletes the specified alias. Examples cbq> \\UNALIAS travel-limit1; cbq> \\ALIAS; Result serverversion  select version()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| \\ECHO         | args where args can be parameters, aliases, or any input. | If the input is a parameter, this command echoes (displays) the value of the parameter. The parameter must be prefixed according to its type. See [Table 3](#table%5Fltk%5Fc5s%5F5v) for details. If the input is not a parameter, the command echoes the statement as is. If the input is an alias, the command displays the value of an alias command. Examples cbq> \\ECHO -$r; cbq> \\ECHO \\\\serverversion; Result select version()                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| \\VERSION      | none                                                      | Displays the version of the client shell. Command Line Option: [\-v](#opt-version) or [\--version](#opt-version) Example cbq> \\VERSION; Result  SHELL VERSION  : 2.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| \\HELP         | command                                                   | Displays the help information for the specified command. When used without any arguments, it lists all the commands supported by the cbq shell. Command Line Option: [\-h](#opt-help) or [\--help](#opt-help) Example cbq> \\HELP ECHO; Result \\ECHO args ... Echo the input value. args can be a name (a prefixed-parameter), an alias (command alias) or a value (any input statement). Example : \\ECHO -$r ; \\ECHO \\\\tempalias;                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| \\COPYRIGHT    | none                                                      | Displays the copyright, attributions, and distribution terms. Example cbq> \\COPYRIGHT;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| \\SOURCE       | input-file                                                | Reads and executes the commands from a file. Multiple commands in the input file must be separated by ; <newline>. Command Line Option: [\-f](#opt-file) or [\--file](#opt-file) For example, _sample.txt_ contains the following commands: SELECT \* FROM \`travel-sample\`.inventory.airline LIMIT 1; \\ECHO this; #This is a comment; Example cbq> \\SOURCE sample.txt;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| \\REDIRECT     | filename                                                  | Redirects the output of all the commands to the specified file until the cbq shell receives the \\REDIRECT OFF command. By default, the file is created in the directory that you were in when you started the cbq shell. You can specify a different location using relative paths. If the file doesn’t exist, it is created. If the file already exists, it is overwritten. You can append redirected output to an existing file using [File Append Mode](#file-append-mode). Command Line Option: [\-o](#opt-output) or [\--output](#opt-output) Example cbq> \\REDIRECT temp\_out.txt;                                                                                                                                                                                                                                                                                                                          |
| \\REDIRECT OFF | none                                                      | Redirects the output of subsequent commands from a custom file to standard output (os.stdout). Example cbq> \\REDIRECT OFF;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## [](#cbq-connect-to-cluster)Connecting to the Cluster or Query Node

You can connect the cbq shell to Couchbase Server either through the query service or through the cluster endpoint. There are two ways to establish a connection:

* Using an option on startup:

-e <url to query engine or Couchbase cluster>
--engine=<url to query engine or Couchbase cluster>
* Using a shell command:  
```console  
cbq> \CONNECT url;  
```

The `url` may contain up to three components: the protocol scheme, the host, and a port number. The URL is optional and if it is not specified, the default URL `http://localhost:8091` is used. An error is thrown if the URL is invalid.

The cbq shell supports the _http://_, _https://_, _couchbase://_ and _couchbases://_ protocol schemes. The _https://_ and _couchbases://_ protocol schemes are encrypted. For more details, refer to [Using an Encrypted Connection](#cbq-encrypted).

The host may be the IP address or hostname of any node in the cluster, as cbq will automatically discover the query nodes. The cbq shell supports both IPV4 and IPV6 addresses.

The _couchbase://_ and _couchbases://_ protocol schemes support the domain name service (DNS). When using one of these protocol schemes, the host may be a domain name which is resolved using DNS. For example, this enables you to connect to a cluster or node over the internet.

Note that you must use the encrypted _couchbases://_ protocol scheme to connect to a cluster or node deployed in Couchbase Capella.

You may optionally specify the port when using the _http://_ or _https://_ protocol schemes. When connecting to the query service, use the query port 8093, or 18093 for an encrypted connection. When connecting to the cluster, you don’t need to specify the port as the connection uses round robin to find a query service to connect to. If you want to specify a port, use the admin port 8091, or 18091 for an encrypted connection.

You cannot specify the port when using the _couchbase://_ or _couchbases://_ protocol schemes.

You can close the connection with an existing node or cluster without exiting the shell at any given time during the session using the `\DISCONNECT;` command. If the shell is not connected to any endpoint, an error with a message that the shell is not connected to any instance is thrown.

Examples

```console
$ ./cbq -e http://localhost:8091 -u Administrator -p password
Connected to : http://localhost:8091/. Type Ctrl-D or \QUIT to exit.

Path to history file for the shell : ~/.cbq_history

cbq> \DISCONNECT;
Couchbase query shell not connected to any endpoint. Use \CONNECT command to connect.

cbq> \CONNECT http://127.0.0.1:8091;
Connected to : http://127.0.0.1:8091. Type Ctrl-D or \QUIT to exit.

cbq> \EXIT;

$ ./cbq -e http://127.0.0.1:8091 -u Administrator -p password
Connected to : http://127.0.0.1:8091/. Type Ctrl-D or \QUIT to exit.

Path to history file for the shell : ~/.cbq_history
cbq>
```

### [](#bringing-up-an-unconnected-instance)Bringing Up an Unconnected Instance

You can bring up the shell without connecting to any query service or cluster endpoint by using the `-ne` or `--no-engine` option. After starting cbq without any service, you can connect to a specific endpoint using the `CONNECT` command.

Example

```console
$ ./cbq -ne
Path to history file for the shell : ~/.cbq_history

cbq> \CONNECT http://Administrator:password@localhost;
Connected to : http://Administrator:password@localhost:8091. Type Ctrl-D or \QUIT to exit.
```

### [](#exiting-the-cbq-shell)Exiting the cbq Shell

You can exit the cbq shell by pressing Ctrl+D or by using one of the following commands:

```console
cbq> \EXIT;
cbq> \QUIT;
```

When you run the exit command, the cbq shell first saves the history, closes existing connections, saves the current session in a session file, resets all environment variables, and then closes the shell liner interface.

Example

```console
$ ./cbq -u Administrator -p password
Connected to : http://localhost:8091/. Type Ctrl-D or \QUIT to exit.
Path to history file for the shell : ~/.cbq_history

cbq> SELECT name FROM `travel-sample`.inventory.airline LIMIT 1;
{
    "requestID": "59d1c699-11a2-47c6-b4d0-4a7de1d15a3c",
    "signature": {
        "name": "json"
    },
    "results": [
    {
        "name": "40-Mile Air"
    }
    ],
    "status": "success",
    "metrics": {
        "elapsedTime": "13.514441ms",
        "executionTime": "13.355058ms",
        "resultCount": 1,
        "resultSize": 37,
        "serviceLoad": 12
    }
}

cbq> \EXIT;
$
```

## [](#accessing-a-secure-keyspace)Accessing a Secure Keyspace

If your keyspace has a password, you can pass the keyspace name and keyspace password like so:

```console
$ ./cbq -engine="http://<keyspacename>:<keyspacepassword>@localhost:8091/"
```

For the 'travel-sample' keyspace, if you add a password to it of _w1fg2Uhj89_ (as by default it has none), the command to start `cbq` would look like this:

```console
$ ./cbq -engine="http://travel-sample:w1fg2Uhj89@localhost:8091/"
```

> [!NOTE]
> These commands execute successfully only if you have loaded sample bucket 'travel-sample' either at install or from the Settings menu in the web UI.

If you want to access all of the keyspaces in the same cbq session, you would pass in the Administrator username and password instead of the keyspace level.

```console
$ ./cbq -engine="http://Administrator:password@localhost:8091/"
```

## [](#cbq-single-cred)Providing Single User Credentials

You can pass a single user name credential to the cbq shell on startup using the command line options:

-u=username
--user=username

The shell then prompts you for a password. You can also provide a single password credential using the `-p` option. You cannot use this option by itself. It must be used with the `-u` option to specify the user name that the password is associated with.

-p=password
--password=password

Example

```console
$ ./cbq -u=Administrator
Enter Password:
Connected to : http://localhost:8091/. Type Ctrl-D or \QUIT to exit.

$ ./cbq -e http://localhost:8091 -u=Administrator -p=password
Connected to : http://localhost:8091/. Type Ctrl-D or \QUIT to exit.
cbq>
```

For information on passing the user name and password credentials using other mechanisms, see [Passing Credentials Using the SET Shell Command](#pass-cred-shell-cmd) and [Passing Credentials Using REST API](#pass-cred-rest-api).

## [](#cbq-multiple-creds)Providing Multiple Credentials for Authorization

The cbq shell supports self-signed certificates for encrypting communication between clusters.

Using the cbq shell, you can set the credentials for different users on startup or by using the SET shell commands to set the credentials query parameter. You can also use this to provide authentication credentials for multiple SASL buckets per session. Depending on the type of credential being set, there are multiple possible values for the credentials query parameter.

To set the credentials for different users on startup, use one of the following options:

-c=list-of-creds
--credentials=list-of-creds

The `list-of-creds` can take either one or multiple credentials. The credentials consist of an identity and a password separated by a colon `:`. To specify multiple credentials, append all the user names and passwords to the same credentials array. For example:

-c=travel-sample:pwd1,beer-sample:pwd2

For information on passing a single user name credential to the cbq shell, see [Providing Single User Credentials](#cbq-single-cred).

### [](#pass-cred-shell-cmd)Passing Credentials Using the SET Shell Command

You can provide the credential types using the SET command.

> [!NOTE]
> The credentials are set for the shell session and not on a per query basis. You can use the SET, PUSH, POP and UNSET commands to reset the credentials during a session.

To pass authentication credentials per query, set the query parameter to a new value using the SET shell command before executing the query.

You can also switch between users and change credentials during a session. To do so, set the `-creds` query parameter for the session using the following command:

```console
cbq> \SET -creds travel-sample:b1, session:s1;
```

### [](#pass-cred-rest-api)Passing Credentials Using Query REST API

You can use query REST API to pass credentials from clients.

For SASL buckets, you can pass the credentials as:

```json
[  {
     "user":"travel-sample",
     "pass":"password"
   }  ]
```

If you are using the Administrator credentials:

```json
[  {
        "user":"Administrator",
        "pass":"password"
   }  ]
```

For multiple SASL protected buckets, you can pass an array of authentication credentials:

```json
[  {
        "user":"beer-sample",
        "pass":"password1"
        },
        {
        "user":"travel-sample",
        "pass":"password2"
   }  ]
```

### [](#displaying-the-credentials)Displaying the Credentials

You can display the credentials for the current session using the [ECHO](#cbq-echo) shell command. This command displays only the user names (and not the passwords).

```console
cbq> \ECHO -creds;

Administrator:*
```

You can also display a full list of variables using the SET command specified without any arguments.

```console
cbq> \SET;
Query Parameters ::
Parameter name : timeout Value  ["3ms" "4s"]

Named Parameters ::
Parameter name : r Value  [9.5 9.5]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]
```

## [](#cbq-encrypted)Using an Encrypted Connection

You can connect to the cluster or node with an encrypted protocol scheme — that is, either _https://_ or _couchbases://_. To do this, you can provide the root CA certificate, the chain certificate, and the client key file using the [\--cacert](#opt-cacert), [\--cert](#opt-cert), and [\--key](#opt-key) options. You can use the [\--no-ssl-verify](#opt-skip-verify) option to skip the verification of certificates.

When connecting to a cluster or node with an encrypted protocol scheme, the default ports are 18091 and 18093\. You need not specify the port when connecting to the cluster.

You can use the encrypted _couchbases://_ protocol scheme with a domain name to connect to a node or cluster deployed in Couchbase Capella. For more details, refer to [Connecting to the Cluster or Query Node](#cbq-connect-to-cluster).

## [](#cbq-parameter-manipulation)Parameter Manipulation

The cbq shell categorizes parameters into the following types:

* Named Parameters
* REST API Parameters
* Session or Pre-defined Parameters
* User-defined Parameters

### [](#parameter-configuration)Parameter Configuration

When using parameters, you can set a stack of values for each parameter. You can either push a new value onto the stack using the PUSH command, or set the current value for a parameter using the SET command. The SET command always modifies the top of a variable’s stack while the PUSH command adds to the stack. When you use PUSH with no arguments, it copies the top element of every parameter’s (except the predefined parameters) stack and pushes that copy to the top of its respective stack. As a result, each stack grows by 1, but the values are preserved. You can then use the SET command to modify the top value.

To unset the values from a parameter’s stack, you can use the UNSET command to remove all the values from the stack and delete the corresponding parameter stack. However, if you want to delete a single value from the settings, use the POP command. When you use the POP command with no arguments, it pops the one value from the top of each parameter’s stack.

### [](#setting-variable-values)Setting Variable Values

Each variable has a separate stack associated with it and the `prefix` `name` argument helps distinguish between the stacks.

The SET command always modifies the top value of a variable. You can use the SET command to set different kinds of parameters: query parameter, predefined session variables, user-defined session variables and named parameters.

```console
cbq> \SET <prefix><name> value;
```

where `name` is the name of the parameter, `value` is the value to be set, and `prefix` is one of the following depending on the parameter type. The cbq shell uses the prefix to differentiate between the different types of parameters.

__Table 3\. Prefixes for Parameters__
| Prefix    | Parameter Type                         |
| --------- | -------------------------------------- |
| \-        | Query parameter                        |
| \-$       | Named parameters                       |
| No prefix | Predefined (built-in) session variable |
| $         | User defined session variable          |

> [!NOTE]
> Positional parameters are set using the `-args` query parameter.

You can use the cbq shell to set all the REST API settings by specifying the settings as query parameters prefixed by `-`. As a best practice, we recommend that you save the initial set of basic parameters and their default values using the `\PUSH` command (with no arguments).

Examples

```console
cbq> \SET -$airport "SJC";
cbq> \PUSH -args ["LAX", 6];
cbq> \SET;
Query Parameters ::
Parameter name : args Value  [["LAX",6]]

Named Parameters ::
Parameter name : airport Value  ["SJC"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

cbq> \PUSH -$airport "SFO";
cbq> \PUSH;
cbq> \SET;
Query Parameters ::
Parameter name : args Value  [["LAX",6] ["LAX",6]]

Named Parameters ::
Parameter name : airport Value  ["SJC" "SFO" "SFO"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

cbq> \SET -args ["SFO", 8];
cbq> \SET;
Query Parameters ::
Parameter name : args Value  [["LAX",6] ["SFO",8]]

Named Parameters ::
Parameter name : airport Value  ["SJC" "SFO" "SFO"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

cbq> \POP;
cbq> \SET;
Query Parameters ::
Parameter name : args Value  [["LAX",6]]

Named Parameters ::
Parameter name : airport Value  ["SJC" "SFO"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

cbq> \POP -$airport;
cbq> \SET;
Query Parameters ::
Parameter name : args Value  [["LAX",6]]

Named Parameters ::
Parameter name : airport Value  ["SJC"]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]

cbq> \UNSET -$airport;
cbq> \SET;
Query Parameters ::
Parameter name : args Value  [["LAX",6]]

Named Parameters ::

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]
```

To display all the parameters defined in a session, use the SET command with no arguments.

```console
cbq> \SET;
Query Parameters ::
Parameter name : timeout Value  ["100m"]

Named Parameters ::
Parameter name : r Value  [9.5]

User Defined Session Parameters ::

Predefined Session Parameters ::
Parameter name : histfile Value  [".cbq_history"]
```

The following table lists the available predefined session variables.

__Table 4\. Predefined Session Variables__
| Variable Name | Possible Values | Description                                                                                                                               |
| ------------- | --------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| HISTFILE      | Valid file name | Specifies the file name to store the command history. By default the file is saved in the user’s home directory. Default: _.cbq\_history_ |

### [](#handling-named-parameters)Handling Named Parameters

Use the \\SET command to define named parameters. For each named parameter, prefix the variable name with `-$`. The following example creates named parameters `r` and `date` with values 9.5 and "1-1-2016" respectively.

```console
cbq> \SET -$r 9.5;
cbq> \SET -$date "1-1-2016";
```

### [](#handling-positional-parameters)Handling Positional Parameters

Use the SET shell command with the `-args` query parameter to define positional parameters:

```console
cbq> \SET -args value;
```

The `value` contains the different values that correspond to positions within the query. For example,

```console
cbq> \SET -args [ 9.5, "1-1-2016"];
```

### [](#resetting-variable-values)Resetting Variable Values

You can reset the value of a variable by either popping it or deleting it altogether. To pop the top of a parameter’s stack use:

```console
cbq> \POP <prefix><name>;
```

To pop the top of every parameter’s stack once, use the POP command without any arguments:

```console
cbq> \POP;
```

To pop all the values of a parameter’s stack and then delete the parameter, use:

```console
cbq> \UNSET <prefix><name>;
```

## [](#cbq-shell-cmd-echo)Using ECHO to Display Values of Parameters and More

The ECHO command displays the current values of the parameters set for a session. You can use it to display any input string or command aliases that have been created using the ALIAS shell command. To display parameters, you must include their prefixes. If not, the shell considers the parameters as generic statements and displays the parameter as is.

```console
cbq> \ECHO input ... ;
```

where `input` can be a parameter with prefix (`<prefix><parameter-name>`), an alias (`\\command-alias`), a SQL++ statement, or a string.

Examples

```console
cbq> \ECHO hello;
hello

cbq> \ECHO \\travel-alias1;
SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;

cbq> \ECHO -$r;
9.5
```

## [](#cbq-shell-cmd-alias)Command Alias

Using the ALIAS shell command, you can define and store aliases for commands. This is useful when you have lengthy queries that need to be executed often. Run the following command to define an alias:

```console
cbq> \ALIAS command-alias command;
```

Example

```console
cbq> \ALIAS travel-alias1 SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
```

To run the command alias, use `\\command-alias`.

Example

```console
cbq> \\travel-alias1;

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
    ...
}
```

To list all the existing aliases, use:

```console
cbq> \ALIAS;
```

Example

```console
cbq> \ALIAS;
serverversion  select version()
travel-alias1  SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
```

You can delete a defined alias using the \\UNLIAS command.

```console
cbq> \UNALIAS alias-name ... ;
```

```console
cbq> \UNALIAS serverversion travel-alias1;

/* Check existing aliases */
cbq> \ALIAS;
 ERROR 141 : Alias does not exist :
```

This command can take multiple arguments and deletes the defined alias for every input name.

## [](#cbq-prepared-stmts)Executing Prepared Statements

You can use the shell command to execute prepared statements. As a pre-requisite, you must first prepare a statement using the SQL++ [PREPARE](../n1ql/n1ql-language-reference/prepare.md) statement. To execute prepared statements, follow these steps:

1. Set the named and positional parameters that are present in the prepared statement.
2. Prepare using the SQL++ PREPARE statement. This can be either prepared statement or a named prepared statement. If you do not specify a name for the prepared statement (`PREPARE query;`), a unique name is assigned. You can use this auto-assigned name when executing the prepared statement. If you specify a name (PREPARE `name` FROM `query`;), you can use this name to run the prepared statement.
3. Execute the prepared statement using the shell command:  
EXECUTE name-of-prepared-stmt;

## [](#canceling-a-query)Canceling a Query

You can cancel a running query by using the Ctrl+C keys.

### [](#connection-timeout-parameter)Connection Timeout Parameter

You can use the timeout parameter to limit the running time of a query. This parameter specifies the time to wait before returning an error when executing a query.

--t=value
--timeout=value

Timeout can be specified in the following units: `ns` for nanoseconds, `μs` for microseconds, `ms` for milliseconds, `s` for seconds, `m` for minutes, and `h` for hours. Examples of valid values include "0.5s", "10ms", or "1m".

You can also the SET shell command to set this parameter. An error is thrown if the timeout is invalid.

```console
$ ./cbq --timeout="2s"

$ ./cbq -q
cbq> \SET -TIMEOUT 1ms;
```

## [](#cbq-file-based-ops)File Based Operations

Using the file based commands and options, the cbq shell can execute SQL++ and shell commands contained in files. There are two ways to accomplish this:

* Using an option on startup:

-f=input-file
--file=input-file  
The cbq shell executes the commands present in the input file, prints them to stdout (or to a file if using redirects), and exits.
* Using a shell command:  
cbq> \SOURCE input-file;  
Runs the commands present in the input file and prints the result to stdout.

Consider the input file, _sample.txt_, containing the following commands:

CREATE PRIMARY INDEX ON `travel-sample`.inventory.airline USING GSI;
SELECT * from `travel-sample`.inventory.airline LIMIT 2;
SELECT callsign from `travel-sample`.inventory.airline LIMIT 3;
\HELP;

To execute the commands contained in _sample.txt_ using the -f option, run `$./cbq -f=sample.txt`

Results

```console
 Connected to : http://localhost:8091/. Type Ctrl-D or \QUIT to exit.

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

To execute the commands contained in _sample.txt_ using the shell command, run `cbq> \SOURCE sample.txt;`

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

You can redirect all the output for a session or part of a session to a specified file by using the following option:

-o filename
--output=filename

To redirect a specific set of commands during a session, you must specify the commands between `\REDIRECT` and `\REDIRECT OFF` as shown:

```console
cbq> \REDIRECT filename;
command-1; command-2;, ..., command-n;
cbq> \REDIRECT OFF;
```

All the commands specified after `\REDIRECT` and before `\REDIRECT OFF` are saved into the specified output file.

If the file doesn’t exist, it is created. If the file already exists, it is overwritten. You can append redirected output to an existing file using [File Append Mode](#file-append-mode).

Example

```console
cbq> \REDIRECT temp_output.txt;
cbq> CREATE PRIMARY INDEX ON `travel-sample`.inventory.airline USING GSI;
cbq> SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
cbq> \HELP;
cbq> \REDIRECT OFF;
```

You can specify multiple `\REDIRECT` commands. When you do so, the output file changes to the specified files and switches back to `stdout` only when you specify `\REDIRECT OFF`.

### [](#file-append-mode)File Append Mode

You can use _file append mode_ to specify that cbq should append redirected output to the end of an existing file, rather than overwriting the existing file.

To use file append mode, include a plus sign `+` at the start of the output path or filename.

Example

```console
cbq> \REDIRECT +temp_output.txt;
cbq> SELECT * FROM `travel-sample`.inventory.airline LIMIT 1;
cbq> \REDIRECT OFF;
```

Every time you start appending to the output file, a timestamp is added to the end of the output file, followed by any redirected commands and results.

-- <2021-07-30T14:48:43.661+01:00> : opened in append mode

SELECT * FROM `travel-sample`.inventory.airline LIMIT 1
...

Note that file append mode is only available with the `\REDIRECT` command within a shell session. It is not available for the `-o` or `--output` command line option. When you use the `-o` or `--output` command line option, the specified output file is always overwritten.

## [](#cbq-server-shell-info)Server and Shell Information

The cbq shell provides commands that convey information about the shell or cluster endpoints.

### [](#version)Version

You can find the version of the client (shell) by using either the command line option to display the current version of the shell and exit, or as a shell command to print the version of the shell during the shell session.

Example Using the Command-line Option

```console
$ ./cbq -v
SHELL VERSION  : 2.0

Use {sqlpp} queries select version(); or select min_version(); to display server version.

$ ./cbq --version
SHELL VERSION  : 2.0

Use {sqlpp} queries select version(); or select min_version(); to display server version.
```

Example Using the Shell Command

```console
cbq> \VERSION;
SHELL VERSION : 2.0
```

To display the version of the query service, use the SQL++ commands `SELECT version();` and `SELECT min_version();`.

### [](#copyright)Copyright

You can view the copyright, attributions, and distribution terms of the command line query tool using the `\COPYRIGHT;` command.

```console
cbq> \COPYRIGHT;
Copyright (c) 2016 Couchbase, Inc. Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License. You may obtain a copy of the
License at http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software distributed under the
License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
either express or implied. See the License for the specific language governing permissions
and limitations under the License.
cbq>
```

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

Source: _https://github.com/peterh/liner_

---

[1](#%5Ffootnoteref%5F1). Invoking a boolean option with no value sets the value to `true`. 

[2](#%5Ffootnoteref%5F2). Invoking this option with no value sets the value to `on`.