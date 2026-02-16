[View original HTML](/operator/2.8/howto-ui.html)

> Connect to the Couchbase Server user interface. 

The Couchbase user interface (UI) provides a rich environment for cluster management, debugging and application development. Access to the UI varies based on your chosen [network architecture](concept-couchbase-networking.md).

|  | Kubernetes ingress resources are not supported as they are neither fully featured nor generic across platforms. It is highly recommended that one of the methods outlined below be used for correct functionality as no technical support will be provided. |
|  | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#port-forwarding)Port Forwarding

The standard way to connect to a Couchbase UI is through port-forwarding. In order to forward a Couchbase Server pod, list the pods belonging to the cluster you wish to connect to:

```console
$ kubectl get pods -l couchbase_cluster=cb-example (1)
NAME              READY   STATUS    RESTARTS   AGE
cb-example-0000   1/1     Running   0          69m
cb-example-0001   1/1     Running   0          68m
cb-example-0002   1/1     Running   0          68m
```

| **1** | Replace cb-example with the cluster name you require. |
| ----- | ----------------------------------------------------- |

To port forward to a chosen pod use the following command:

```console
$ kubectl port-forward cb-example-0000 8091
Forwarding from 127.0.0.1:8091 -> 8091
Forwarding from [::1]:8091 -> 8091
```

You can then connect to http://localhost:8091 to access the UI.

|  | If you must connect over TLS then forward port 18091 and use the address https://localhost:18091. Ensure your cluster administrator has provided a CA certificate to be installed into your browser’s trust store. If certificate-based authentication is used, then ensure you have installed your client certificate/key into your browser too. As you are connecting to localhost it is also important that your cluster administrator has added the localhost subject alternative address name into the cluster TLS certificate. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |

## [](#dns-based-addressing)DNS Based Addressing

If you are using the [public networking with External DNS](concept-couchbase-networking.md#public-networking-with-external-dns) network configuration then DNS based addressing can be used. When using public networking the Couchbase administrative service is exposed as a load balancer service in order to provide resilient connectivity for clients. This same service provides access to the UI.

The connection string is determined by the [couchbaseclusters.spec.networking.dns.domain](resource/couchbasecluster.md#couchbaseclusters-spec-networking-dns-domain) cluster parameter. The connection string is in the form `https://console._<dns-domain>_`. Given the DNS domain `my-cluster.acme.org`, to connect to the cluster using TLS use the connection string `https://console.my-cluster.acme.org:18091`.

## [](#configuring-an-ingress)Configuring an Ingress

A [Kubernetes ingress](https://kubernetes.io/docs/concepts/services-networking/ingress/) can be used to expose the Couchbase administrative console to a network external to the Kubernetes cluster. Ingresses are not managed by the Operator because the required configuration is not generic. However, the configuration for your specific provider can be summarized as:

* Enable cookie-based client session affinity.

Couchbase administrative console cookies are valid only for the pod you authenticated against. Client affinity ensures the ingress routes all requests for a session to the same pod each time.

An illustrative example for NGINX would look like:

```console
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-ingress
  annotations:
    nginx.ingress.kubernetes.io/affinity: cookie (1)
    nginx.ingress.kubernetes.io/affinity-mode: persistent
spec:
  rules:
  - http: (2)
      paths:
      - path: / (3)
        pathType: Prefix
        backend:
          service:
            name: my-cluster (4)
            port:
              number: 8091 (5)
```

| **1** | The ingress is annotated with affinity — this enables client affinity — and affinity-mode — this ensures each client session is routed to the same backend pod.                                                                                                                                                               |
| ----- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | A rule is created for all virtual hosts using the HTTP service.                                                                                                                                                                                                                                                               |
| **3** | A path of / and a type of Prefix means that any HTTP path will match this rule.                                                                                                                                                                                                                                               |
| **4** | The service name references a service within the namespace the ingress is created in. The Operator will create a headless service by default for every cluster — in order to create DNS entries — and can be used as the backend service for the ingress. The service will be named the same as a Couchbase cluster resource. |
| **5** | The port is the backend port to connect to. In this instance, the ingress is plain text HTTP, so 8091.                                                                                                                                                                                                                        |

|  | Use TLS to secure your ingresses on the public internet, otherwise your login credentials will be visible in plain text and can be snooped by an attacker. Your ingress provider may support backend TLS encryption, providing end-to-end security — use port 18091 on the backend. When using ingresses to access Couchbase, you cannot use client certificate authentication — use a load balancer service to expose the console instead. |
|  | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |

## [](#configuring-an-istio-proxy)Configuring an Istio Proxy

Istio ingress gateway can be used to as a proxy to access the Couchbase Server user interface when installing a cluster into an Istio enabled namespace. An Istio ingress gateway comes with the additional benefits of the Istio ecosystem such as traffic monitoring and tracing. Refer to the [Istio Gateway](https://istio.io/latest/docs/reference/config/networking/gateway/) documentation for an overview of the configuration options available during installation.

To ensure that your Kubernetes cluster is prepared to configure an ingress gateway, check that the `istio-ingressgateway` service has been assigned a public IP address. The `istio-ingressgateway` service is created by default with the installation of the default Istio profile.

```console
$ kubectl get svc -n istio-system
NAME                   TYPE           CLUSTER-IP    EXTERNAL-IP     PORT(S)                                      AGE
istio-ingressgateway   LoadBalancer   10.0.249.57   20.242.186.24   15021:31049/TCP,80:32273/TCP,443:32358/TCP   22h
```

The next step is to set up a DNS A records for the `EXTERNAL-IP` with your DNS registrar service.

Once the external address has been committed to DNS, set up the necessary proxy rules to begin forwarding traffic through Istio into the Couchbase console service.

```console
apiVersion: networking.istio.io/v1alpha3
kind: Gateway
metadata:
  name: api-gateway
spec:
  servers:
    - port:
        number: 443
        name: https-api
        protocol: HTTPS (1)
      hosts:
        - "public.hostname.com" (2)
```

| **1** | HTTPS is highly recommended as this is a public facing interface.   |
| ----- | ------------------------------------------------------------------- |
| **2** | The DNS name assigned to the ingress gateway load balancer service. |

The next step is to create a `VirtualService` resource to define routing destination rules for incoming traffic from the external Gateway:

```yaml
apiVersion: networking.istio.io/v1beta1
kind: VirtualService
metadata:
 name: "virtual-service-couchbase-ui"
spec:
  hosts:
  - "public.hostname.com"
  gateways:
  - api-gateway
  http:
  - match:
    - uri:
        prefix: / (1)
    route:
    - destination:
        host: "cb-example-ui" (2)
        port:
          number: 18091
```

| **1** | Matches traffic targeting public.hostname.com/                                                                                                                                                                               |
| ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **2** | The internal destination service used to resolve the request. The fully qualified domain name of this service should be used if the VirtualService is created in a namespace that is different than the destination service. |

Finally create a destination rule to allow for sticky sessions when ensures that client sessions remain open and associated with a single instance of Couchbase Server.

```yaml
apiVersion: networking.istio.io/v1alpha3
kind: DestinationRule
metadata:
  name: destination-rule-couchbase-ui
spec:
  host: cb-example-ui
  trafficPolicy:
    loadBalancer:
      consistentHash:
        httpCookie:
          name: user (1)
          ttl: 0s
```

| **1** | It is possible to use other session cookies such as source IP if a different policy is desired. |
| ----- | ----------------------------------------------------------------------------------------------- |