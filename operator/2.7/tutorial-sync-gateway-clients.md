---
title: Exposing Sync Gateway to Couchbase Lite Clients
editUrl: https://github.com/couchbase/docs-operator/edit/release/2.7/modules/ROOT/pages/tutorial-sync-gateway-clients.adoc
pubDate: 2026-03-20T03:41:54.898Z
link: xref:2.7@operator::tutorial-sync-gateway-clients.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.7/tutorial-sync-gateway-clients.html)

# Exposing Sync Gateway to Couchbase Lite Clients

> Expose Sync Gateway to external Couchbase Lite Clients 

> [!WARNING]
> Tutorials are accurate at the time of writing but rely heavily on third party software. Tutorials are provided to demonstrate how a particular problem may be solved. Use of third party software is not supported by Couchbase. For further help in the event of a problem, contact the relevant software maintainer.

This tutorial defines best practices for exposing Sync Gateway cluster for Couchbase Lite clients to connect to.

In a production deployment, you will likely have more than one Sync Gateway nodes fronted by a [load balancer](../../sync-gateway/current/deploy/load-balancer.md) or a reverse-proxy. Couchbase Lite clients connect to the Layer4 or Layer7 Load Balancer.

In addition, on production environments, it is also [recommended](../../sync-gateway/current/deploy/load-balancer.md#transport-layer-security-https-ssl) that all communication between Couchbase Lite clients and Sync Gateway be secured using TLS.

You have couple of options on how to configure your Kubernetes deployment for TLS. Here are some recommendations

## [](#option-1-ingress-as-tls-termination-point)Option 1: Ingress as TLS Termination Point

When using Sync Gateway behind a load balancer or reverse proxy, we generally recommend that the reverse proxy be the TLS termination point for the Sync Gateway cluster in order to alleviate the load on the Sync Gateway. This is particularly relevant if you have a large number of connected clients. This option would also apply if you need Layer7 or application level load balancing such as support for sticky sessions.

In this option, you cannot use the Kubernetes Load Balancer service. Instead, we recommend the use of [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/#what-is-ingress), which is an abstraction that manages external access to the services in a cluster. It provides out-of-box support for features like external routable URLs to services, load balancing and TLS termination etc.

![sgw ingress](_images/sgw-ingress.png) 

Figure 1\. Image showing deployment of ingress as TLS termination point

### [](#expose-sync-gateway-as-a-service)Expose Sync Gateway as a service

In this section you will deploy a Kubernetes [node port](https://kubernetes.io/docs/concepts/services-networking/service/#type-nodeport) type service to expose Sync Gateway cluster.

* Create a service definition file corresponding to your deployment similar to one below.

```yaml
apiVersion: v1
kind: Service
metadata:
  name: sync-gateway-service
spec:
  ports:
    - port: 4984
      name: apiport
      targetPort: 4984
  type: "NodePort"
  selector:
    app: sync-gateway
```

This specification creates a new Service object named `sync-gateway-service`, which targets TCP port 4984 on any Pod with the `app=sync-gateway` label. Port 4984 is the default public port of Sync Gateway. You can map any incoming `port` to a `targetPort`. For convenience, the `targetPort` is set to the same value as the `port` field.

* Deploy the Sync Gateway node port service. Assuming that the above configuration is in a file named `sync-gateway-nodeport.yaml`, the command would be as follows:  
```console  
$ kubectl apply -f sync-gateway-nodeport.yaml  
```

### [](#deploy-ingress-controller-as-tls-termination-point)Deploy Ingress Controller as TLS Termination Point

Kubernetes [Ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/#what-is-ingress) routes HTTP and HTTPS traffic from the Internet to services in the cluster. It also functions as a load balancer. In our deployment, we will set up an Ingress Controller that will act as TLS termination point for inbound traffic from the Internet

#### [](#prerequisites)Prerequisites

Before you can configure the Ingress controller as the TLS termination point, you need the TLS certs. Creating X.509 certificates is beyond the scope of this documentation. Obtain TLS certificate and Private Key corresponding to your deployment. In the remainder of the instructions, we will refer to the public certificate as `sgw-lb.crt` and the private key as `sgw-lb.key` respectively for an example domain of `cbm.example.com`.

#### [](#create-a-secret-with-the-tls-credentials)Create a Secret with the TLS Credentials

You will use a [Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to pass the certificate to the Ingress Controller

* Create a secret using `kubectl` command as follows:  
```console  
$ kubectl create secret tls sgw-lb-tls-secret --cert sgw-lb.crt --key sgw-lb.key  
```  
The above command creates a secret named `sgw-lb-tls-secret` using the certificate and private key
* Verify that the secret was created using following command:  
```console  
$ kubectl get secrets  
```

If everything works, you should see `sgw-lb-tls-secret` listed in the output

#### [](#create-an-ingress-controller)Create an Ingress Controller

This is an example of an Ingress controller definition that is configured as TLS termination point for Sync Gateway.

```yaml
apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  name: sgw-ingress (1)
spec:
  tls:
  - hosts:
    - cbm.example.com (2)
    secretName: sgw-lb-tls-secret (3)
  rules:
    - host: cbm.example.com
      http:
        paths:
        - path: /
          backend: (4)
            serviceName: sgw-service
            servicePort: 4984
```

| **1** | metadata.name: The name of the controller is sgw-ingress                                                                                                                                                                          |
| ----- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | spec.tls.hosts : Specifies the host for which the rules apply. You will replace this with the DNS address of your deployment                                                                                                      |
| **3** | spec.tls.secretName: The name of the secret that was created in [Create a Secret with the TLS Credentials](#create-a-secret-with-the-tls-credentials) step                                                                        |
| **4** | spec.http.backend: HTTP (and HTTPS) requests to the Ingress that matches the host and path of the rule are sent to the listed backend. In this case, all HTTP(s) requests to the specified domain are directed to the sgw-service |

#### [](#deploy-the-ingress-controller)Deploy the Ingress Controller

* Use `kubectl` to deploy the controller as follows. If the corresponding controller definition is `sync-gateway-ingress-tls.yaml`, the command would be as follows:  
```console  
$ kubectl apply -f sync-gateway-ingress-tls.yaml  
```
* Verify the status of the deployment using following command  
```console  
$ kubectl get ingress  
```
* If things are fine you should see the equivalent of the following output  
```console  
NAME            HOSTS                     ADDRESS         PORTS     AGE  
sgw-ingress   cbm.example.com            35.XXX.YYY.ZZ   80, 443   15h  
```  
The output above indicates that the host `cbm.example.com` is reachable via TLS port (443)

#### [](#try-it-out)Try It Out

That’s it. To verify that the Sync Gateway is accessible , open up https://<your-sync-gateway-hostname> in your browser. You should the equivalent of

```json
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"2.7"},"version":"Couchbase Sync Gateway/2.7.0(127;b4c828d) EE"}
```

### [](#enabling-tls-between-ingress-and-sync-gateway)Enabling TLS between Ingress and Sync Gateway

If you require end-to-end security, it is recommended that you re-encrypt traffic between the controller and Sync Gateway. The details of how you do it are platform specific.

## [](#option-2-end-to-end-tls-with-load-balancer-as-pass-through)Option 2: End-to-end TLS with Load Balancer as Pass-through

This is the simplest configuration. In this case, Sync Gateway will be configured at the TLS termination point and TLS traffic will pass through the Load Balancer.

![sgw e2e tls](_images/sgw-e2e-tls.png) 

Figure 2\. image showing deployment with e2e TLS

> [!NOTE]
> Load balancers only work on Cloud Environments (e.g. AWS, GCP etc). So if you are deploying on premise or using something like [Minikube](https://github.com/kubernetes/minikube) for your test deployment, this option will not work. Please use a [service](https://kubernetes.io/docs/concepts/services-networking/service/) such as node port or ingress instead and follow steps outlined in the [\[Option 1: Ingress as SSL Termination Point\]](#Option 1: Ingress as SSL Termination Point) section of this tutorial.

### [](#prerequisites-2)Prerequisites

* Creating X.509 certificates is beyond the scope of this documentation. You can generate TLS certificate and Private Key for your deployments by following instructions [here](../../sync-gateway/current/deploy/load-balancer.md). Through the remainder of the instructions, we will refer to the public certificate as `sgw-lb-cert.pem` and the private key as `sgw-lb-key.pem` respectively
* Update the Sync Gateway configuration file described in [\[Configuring Sync-Gateway\]](#Configuring Sync-Gateway) section with the relevant properties to specify the certificate and private keys as defined [here](../../sync-gateway/current/deploy/load-balancer.md#transport-layer-security-https-ssl). The updated version of configuration file would look like the following (only relevant configuration is shown)

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: sync-gateway
stringData:
  config.json: |-
    {
      "logging": {
        "console": {
          "enabled": true,
          "log_level": "info",
          "log_keys": [
            "*"
          ]
        }
      },
      "databases": {
        "cb-example": {
          "server": "couchbase://cb-example",
          "bucket": "default",
          "username": "Administrator",
          "password": "password",
          "SSLCert": "/home/sync_gateway/sgw-lb-cert.pem", (1)
          "SSLKey": "/home/sync_gateway/sgw-lb-key.pem" (2)
          ....
        }
      }
      .....
    }
```

| **1** | databases.cb-example.SSLCert : This is the path to Sync Gateway cert       |
| ----- | -------------------------------------------------------------------------- |
| **2** | databases.cb-example.SSLKey : This is the path to Sync Gateway private key |

Create a secret with the updated version of configuration file. Assuming that the configuration file is `sgw-config-tls.yaml`, the command would be :

```console
$ kubectl apply -f sgw-config-tls.yaml
```

### [](#create-secret-with-the-sync-gateway-certs)Create secret with the Sync Gateway certs

You will use a [Kubernetes Secret](https://kubernetes.io/docs/concepts/configuration/secret/) to pass the certs and private key to Sync Gateway on launch. Create a secret using command below:

```console
$ kubectl create secret generic sgw-cert-key --from-file sgw-lb-cert.pem --from-file sgw-lb-key.pem
```

The above command creates a secret named `sgw-cert-key` with the cert and private key files.

### [](#deploying-the-sync-gateway-with-tls-enabled)Deploying the Sync Gateway with TLS Enabled

Create a Deployment controller definition similar to the one described in [\[Deploying Sync Gateway\]](#Deploying Sync Gateway) section. The controller is updated to include the secret corresponding to the TLS certs.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: sync-gateway
spec:
  replicas: 2
  selector:
    matchLabels:
      app: sync-gateway
  template:
    metadata:
      labels:
        app: sync-gateway
    spec:
      containers:
      - name: sync-gateway
        image: couchbase/sync-gateway:2.7.0-enterprise
        volumeMounts:
        - name: config
          mountPath: /etc/sync_gateway
          readOnly: true
        - name: sgw-cert-volume
          mountPath: /home/sync-gateway-certs (1)
          readOnly: true
        env:
        - name: GOMAXPROCS
          value: "1"
        resources:
          requests:
            cpu: 100m
          limits:
            cpu: 100m
      volumes:
      - name: config
        secret:
          secretName: sync-gateway
      - name: sgw-cert-volume
        secret:
          secretName:  sgw-cert-key (2)
```

| **1** | spec.template.spec.containers\[0\].volumeMounts\[0\].mountPath mounts the TLS secret in the relevant location.                                                                                                 |
| ----- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | spec.template.spec.volumes\[0\].secret.secretName references the [Create secret with the Sync Gateway certs](#create-secret-with-the-sync-gateway-certs) Secret that is mounted in the Sync-Gateway container. |

Deploy the Sync Gateway using command below. If the controller definition is in a file named `sync-gateway-tls.yaml`, the command would be as follows

```console
$ kubectl apply -f sync-gateway-tls.yaml
```

### [](#deploying-a-load-balancer)Deploying a Load Balancer

The load balancer will pass through the TLS encrypted traffic.

You will deploy the load balancer using the [Kubernetes Load Balancer](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/). The load balancer service provides an externally accessible IP address and routes traffic to the right ports in the cluster.

Follow these steps to deploy a load balancer in front of the Sync Gateway cluster.

This is an example of a Load Balancer definition fronting a Sync Gateway.

```yaml
kind: Service
apiVersion: v1
metadata:
  name: sgw-load-balancer (1)
spec:
  selector:
    app: sync-gateway (2)
  ports:
  - protocol: TCP
    port: 4984 (3)
    targetPort: 4984
  type: LoadBalancer
```

| **1** | metadata.name: The name of the load balancer is sgw-load-balancer.                                                                                                                                                                                                                                                           |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | spec.selector.app: This value corresponds to the pods targeted by the load balancer. In this case, it targets any pods with the app=sync-gateway label which are the Sync Gateway nodes - this corresponds to what was specified in the deployment yaml file.                                                                |
| **3** | spec.ports\[\].targetPort: The load balancer service targets port 4984 on the Sync Gateway cluster. This is the Sync Gateway port corresponding to the [REST API](../../sync-gateway/current/rest-api/rest-api.md). For security purposes, it is recommended that you do not expose the admin port (4985) over the Internet. |

Deploy the load balancer using following command. If the Load Balancer service definition file is `sync-gateway-load-balancer.yaml`, the command would be as follows:

```console
$ kubectl apply -f sync-gateway-load-balancer.yaml
```

If successful, you will see the equivalent of the following:

```console
service "sgw-load-balancer" created
```

Verify the status of the service creation with the following:

```console
$ kubectl get services
```

If successful, you will see a new service corresponding to the load balancer. In the sample output below, we have the `sgw-load-balancer` service.

```console
NAME                TYPE           CLUSTER-IP     EXTERNAL-IP
cb-example          ClusterIP      None           <none>
cb-example-srv      ClusterIP      None           <none>
cb-example-ui       NodePort       10.3.246.239   <none>
kubernetes          ClusterIP      10.3.240.1     <none>
sgw-load-balancer   LoadBalancer   10.3.253.17    35.184.19.17
```

The `sgw-load-balancer` `EXTERNAL-IP` is the load balancer’s publicly accessible hostname.

Verify the pods that the load balancer is targeting.

```console
$ kubectl describe service sgw-load-balancer
```

You should see the equivalent of the following.

```console
Name:                     sgw-load-balancer
Namespace:                default
Labels:                   <none>
Annotations:              <none>
Selector:                 app=sync-gateway
Type:                     LoadBalancer
IP:                       10.3.253.17
LoadBalancer Ingress:     35.184.19.17
Port:                     <unset>  4984/TCP
TargetPort:               4984/TCP
NodePort:                 <unset>  32397/TCP
Endpoints:                10.0.0.34:4984,10.0.0.35:4984
Session Affinity:         None
External Traffic Policy:  Cluster
Events:
```

Notice the "endpoints" field and confirm that it corresponds to the Sync Gateway nodes. In this example, we have 2 Sync Gateway nodes.

Verify the Sync Gateway cluster is accessible with the following command; where `EXTERNAL-IP` is the load balancer’s publicly accessible address. In your deployment, you will replace "EXTERNAL\_IP" with the DNS hostname corresponding to your Sync Gateway certs.

```console
$ curl  https://EXTERNAL-IP:4984
```

It should return the following.

```json
{"couchdb":"Welcome","vendor":{"name":"Couchbase Sync Gateway","version":"2.7"},"version":"Couchbase Sync Gateway/2.7(17;fea9947)"}
```

You have successfully deployed a Sync Gateway cluster on Kubernetes with end-to-end TLS enabled. The [Manage a Sync Gateway Cluster](tutorial-sync-gateway-manage.md) page contains additional details related to the management of the Sync Gateway cluster.

> [!IMPORTANT]
> Red Hat OCP users will need to modify the provided template to reference an image pull secret. This must grant permission to pull container images from the Red Hat Container Registry.

## [](#further-reading)Further Reading

* [Sync-Gateway Documentation](../../sync-gateway/current/introduction.md)
* [Connecting Sync-Gateway to Couchbase Server](tutorial-sync-gateway.md)
* [Managing Sync-Gateway Nodes](tutorial-sync-gateway-manage.md)