---
title: Manual
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/mobile-travel-sample/edit/master/content/modules/mobile-travel-tutorial/pages/swift/installation/manual.adoc
  xref: xref:tutorials:mobile-travel-tutorial:swift/installation/manual.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/tutorials/mobile-travel-tutorial/swift/installation/manual.html)

# Manual

## [](#pre-requisites)Pre-requisites

**Windows Users** : If you are developing on Windows, use a Windows 10 machine. Also, note that you should also have **administrative privileges on the Windows box** so you can authorize the installation and running of the required executables.

* Visual C++ 2017 (**only Windows Users**): Install the Microsoft Visual C++ Compiler for Python Downloadable from [here](https://www.microsoft.com/en-us/download/details.aspx?id=44266).
* Python 3.4+: downloadable from [python.org](https://www.python.org/downloads/). This should come packaged with pip3

**Windows Users** : If you are developing on Windows, make sure that Python is included in your system's PATH environment variable. You can follow instructions [here](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/)to set your PATH variable.
* Git: downloadable from [git-scm.org](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git).

Try it out

1. Verify the python installation

  * Run the following command from your terminal.  
  ```bash  
  bash python --version  
  ```  
  You should see the version of python displayed.
  * Confirm that pip3 is installed. pip is package management software for Python.  
  ```bash  
  pip3  
  ```  
  You should see the command line options.
2. Verify git installation

  * Run the following command from your terminal.  
  ```bash  
  bash git --version  
  ```  
  You should see the version of git installed.

## [](#workshop-repo)Workshop Repo

* Clone the "master" branch of the workshop source from GitHub. We are doing a shallow pull with `depth` as 1 to speed the cloning process.  
```bash  
git clone -b master --depth 1 https://github.com/couchbaselabs/mobile-travel-sample.git  
```

## [](#couchbase-server)Couchbase Server

In this lesson, you will install and launch v7.1.x of Couchbase Server.

Screenshots below apply to Couchbase Server 7.1.1 and there will be some variation with CBS 7.0.x. However, equivalent functionality is available in earlier versions of server. Refer to documentation for compatible server versions.

**Apple M1 Users:** Install and launch v7.1.1 or later

If there is a later version available, you can download it as well bearing in mind that the instructions have been validated with the version that is specified in instructions below.

Couchbase Server 7.1.1

* [Download and install](https://www.couchbase.com/downloads) v7.1.1 of Couchbase Server. Follow the instructions specified in the appropriate platform specific [install guide](../../../../server/current/install/install-intro.md) to install the same.
* On the setup wizard, create an Administrator account with the user _Administrator_ and password as _password_.  
![createadminuser v7 1](../../_images/createadminuser-v7-1.png)
* As you follow the download instructions and setup wizard, make sure you keep all the services (data, query, and index) selected.  
![cbs services](../../_images/cbs-services.png)
* Install the sample bucket named _travel-sample_ because it contains the data used in this tutorial. You can add the bucket from the "Sample Buckets" tab in the "Settings" menu in the admin console.  
![sample bucket v7 1](../../_images/sample_bucket-v7-1.png)
* Create an RBAC user named **admin** with password **password** and **Application Access** to the travel-sample bucket. You can do this from the "Security" menu. These credentials will be used by the Sync Gateway to access the documents in this bucket.  
![add rbac v7 1](../../_images/add_rbac-v7-1.png)  
![RBAC user v7 1](../../_images/RBAC_user-v7-1.png)
* Create a Full text search index on travel-sample bucket called 'hotels'. You can do this from the "Search" menu. Just go with default index settings.  
![add fts](../../_images/add_fts.png)  
![fts](../../_images/fts.png)

Try it out

1. Launch Couchbase Server (if not already runnning)
2. Log into the "Admin Console" (`<http://localhost:8091>`) with appropriate Administrator credentials you created during installation
3. Select the "Buckets" option from the menu on the left
4. Verify that you have around 63,000 documents in your travel-sample bucket

## [](#sync-gateway)Sync Gateway

In this section, you will install and launch version 3.0.3 of Sync Gateway.

* Download Sync Gateway 3.0.3 from [here](https://www.couchbase.com/download) for your platform
* The Sync Gateway will have to be launched with the config file named `sync-gateway-config-travelsample-manual.json` that you should have downloaded as per the instructions in the [Workshop Repo](#workshop-repo) section. The config file will be located in `/path/to/mobile-travel-sample`.
* Open the `sync-gateway-config-travelsample-manual.json` and confirm that the RBAC user credentials configured on the Couchbase Server are used by Sync Gateway for accessing the bucket  
```json  
"username": "admin",  
"password": "password",  
```
* Launch the Sync Gateway.

**macOS**  
```bash  
$ cd /path/to/couchbase-sync-gateway/bin  
$ ./sync_gateway /path/to/mobile-travel-sample/sync-gateway-config-travelsample-manual.json  
```

**Windows**  
By default, the Sync Gateway service will install with _serviceconfig.json_ as the configuration file at **C:\\Program%20Files\\Couchbase\\Sync%20Gateway\\serviceconfig.json**.  
The Sync Gateway will have to be launched with the config file named `sync-gateway-config-travelsample-manual.json` that you should have downloaded as per the instructions in the [Workshop Repo](#workshop-repo) section. The config file will be located in `C:/path/to/mobile-travel-sample`.  
Open the sync-gateway-config-travelsample-manual.json and confirm that the RBAC user credentials configured on the Couchbase Server are used by Sync Gateway for accessing the bucket.  
```json  
"username": "admin",  
"password": "password",  
```
* Stop the Sync Gateway service (since it would be launched with the default version of config file). To stop the service, you can use the Services application (Control Panel -→ Admin Tools -→ Services).
* Replace the _serviceconfig.json_ file with the `sync-gateway-config-travelsample-manual.json`  
```bash  
copy c:/path/to/mobile-travel-sample/sync-gateway-config-travelsample-manual.json "C:\Program Files\Couchbase\Sync Gateway\serviceconfig.json"  
```
* Start the Sync Gateway service with the new version of _serviceconfig.json_ file. To start the service, you can use the Services application (Control Panel -→ Admin Tools -→ Services).

Try it out

1. Access this URL `<http://127.0.0.1:4984>` in your browser
2. Verify that you get JSON response _similar_ to one below `{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"3.0"},"version":"Couchbase Sync Gateway/3.0.0(460;26daced) EE"}`

## [](#python-travel-sample-web-backend)Python Travel Sample Web Backend

### [](#clone-repository)Clone repository

#### [](#apple-m1-users)Apple M1 Users:

* Clone the `mobile-travel-sample-m1` branch of Travel Sample Python web app repo  
```bash  
git clone -b mobile-travel-sample-m1  https://github.com/couchbaselabs/try-cb-python.git  
cd try-cb-python  
```

#### [](#other-platforms)Other platforms:

* Clone the `mobile-travel-sample-tutorial` branch of Travel Sample Python web app repo  
```bash  
git clone -b mobile-travel-sample-tutorial  https://github.com/couchbaselabs/try-cb-python.git  
cd try-cb-python  
```

### [](#install-python)Install Python

#### [](#windows-users-only)Windows Users Only

* Verify the pip installation.  
If you are developing on Windows, **pip.exe** will be found in the "Scripts" sub directory under the Python installation directory.  
Add the path to the "Scripts" folder to the system's PATH environment variable.  
You can follow instructions [here](https://www.pythoncentral.io/add-python-to-path-python-is-not-recognized-as-an-internal-or-external-command/)to set your PATH variable.  
Verify that pip is recognized by typing the following in the cmd terminal. You should see the help menu.  
```bash  
pip3  
```

#### [](#others)Others

* We will run the Travel Web App in a Python [virtual environment](https://virtualenv.pypa.io/en/stable/). First, check if `virtualenv` is installed on your system.  
```bash  
$ virtualenv --version  
```
* If `virtualenv` is not installed , you can use `apt-get` or `pip3` to install it.  
```bash  
$ sudo pip3 install virtualenv  
```
* Specify the folder for your virtual environment.  
```bash  
$ virtualenv .  
```
* Activate your environment. You should see a prompt as shown below.  
```bash  
$ source bin/activate  
(try-cb-python) $  
```

### [](#install-dependencies-run-app)Install dependencies & run app

The application uses several Python libraries that need to be installed, these are listed in **requirements.txt** and can be automatically loaded using the pip3 command.

```bash
pip3 install -r requirements.txt
```

* Update **travel.py** to reflect the username and password that you have used when installing Couchbase Server. This defaults to "Administrator" and "password".  
```python  
DEFAULT_USER = "Administrator"  
PASSWORD = 'password'  
```
* Now launch the Travel Web App  
```bash  
$ python travel.py  
$ Running on http://127.0.0.1:8080/ (Press CTRL+C to quit)  
```  
You may see an alert similar to one below requesting access to run the app.  
Make sure you select the "Allow access" option.  
Try it out

  1. Open <http://127.0.0.1:8080/> in your web browser
  2. Verify that you see the login screen of the Travel Sample Web App similar to the screenshot shown below

![try cb login 2](../../_images/try-cb-login-2.png) 

Figure 1\. Travel Sample Login Screen