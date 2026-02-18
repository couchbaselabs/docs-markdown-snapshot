---
title: CouchbaseCluster Resource
editUrl: https://github.com/couchbase/couchbase-operator/edit/2.9.x/docs/user/modules/ROOT/pages/resource/couchbasecluster.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/operator/current/resource/couchbasecluster.html)

# CouchbaseCluster Resource

The CouchbaseCluster resource represents a Couchbase cluster. It allows configuration of cluster topology, networking, storage and security options.

The following is an example resource, depicting the overall structure and any defaults (consult the field reference for valid values for "empty" values, such as empty strings etc.):

```yaml
apiVersion: v2
kind: CouchbaseCluster
metadata:
  name: ""
spec:
  antiAffinity: false
  autoResourceAllocation:
    cpuLimits: 4
    cpuRequests: 2
    enabled: false
    overheadMemory: ""
    overheadPercent: 0
  autoscaleStabilizationPeriod: ""
  backup:
    annotations:
    image: couchbase/operator-backup:1.4.1
    imagePullSecrets:
    - name: ""
    labels:
    managed: false
    nodeSelector: {}
    objectEndpoint:
      secret: ""
      url: ""
      useVirtualPath: false
    resources: {}
    s3Secret: ""
    selector: {}
    serviceAccountName: couchbase-backup
    tolerations:
    - effect: ""
      key: ""
      operator: ""
      tolerationSeconds: 0
      value: ""
    useIAMRole: false
  buckets:
    enableBucketMigrationRoutines: false
    managed: false
    selector:
      matchExpressions:
      - key: ""
        operator: ""
        values:
        - ""
      matchLabels:
    synchronize: false
  cluster:
    allowFailoverEphemeralNoReplicas: false
    analytics:
      numReplicas: 0
    analyticsServiceMemoryQuota: 1Gi
    appTelemetry:
      enabled: false
      maxScrapeClientsPerNode: 1024
      scrapeIntervalSeconds: 60
    autoCompaction:
      databaseFragmentationThreshold:
        percent: 30
        size: ""
      magmaFragmentationPercentage: 0
      parallelCompaction: false
      timeWindow:
        abortCompactionOutsideWindow: false
        end: ""
        start: ""
      tombstonePurgeInterval: 72h
      viewFragmentationThreshold:
        percent: 30
        size: ""
    autoFailoverMaxCount: 1
    autoFailoverOnDataDiskIssues: false
    autoFailoverOnDataDiskIssuesTimePeriod: 120s
    autoFailoverServerGroup: false
    autoFailoverTimeout: 120s
    clusterName: ""
    data:
      auxIOThreads: 0
      diskUsageLimit:
        enabled: false
        percent: 85
      minReplicasCount: 0
      nonIOThreads: 0
      readerThreads: ""
      tcpKeepAliveIdle: 0
      tcpKeepAliveInterval: 0
      tcpKeepAliveProbes: 0
      tcpUserTimeout: 0
      writerThreads: ""
    dataServiceMemoryQuota: 256Mi
    eventingServiceMemoryQuota: 256Mi
    indexServiceMemoryQuota: 256Mi
    indexStorageSetting: memory_optimized
    indexer:
      deferBuild: false
      enablePageBloomFilter: false
      enableShardAffinity: false
      logLevel: info
      maxRollbackPoints: 2
      memorySnapshotInterval: 200ms
      numReplica: 0
      redistributeIndexes: false
      stableSnapshotInterval: 5s
      storageMode: memory_optimized
      threads: 0
    query:
      backfillEnabled: True
      cboEnabled: True
      cleanupClientAttemptsEnabled: True
      cleanupLostAttemptsEnabled: True
      cleanupWindow: 60s
      completedLimit: 4000
      completedMaxPlanSize: 262144
      completedStreamSize: 0
      completedThreshold: 1s
      completedTrackingAllRequests: false
      completedTrackingEnabled: false
      completedTrackingThreshold: ""
      logLevel: info
      maxParallelism: 1
      memoryQuota: 0
      nodeQuotaValPercent: 67
      numActiveTransactionRecords: 1024
      numCpus: 0
      pipelineBatch: 16
      pipelineCap: 512
      preparedLimit: 16384
      scanCap: 512
      temporarySpace: 5Gi
      temporarySpaceUnlimited: false
      timeout: ""
      txTimeout: 0ms
      useReplica: false
    queryServiceMemoryQuota: ""
    searchServiceMemoryQuota: 256Mi
  enableOnlineVolumeExpansion: false
  enablePreviewScaling: false
  envImagePrecedence: false
  hibernate: false
  hibernationStrategy: ""
  image: ""
  logging:
    audit:
      disabledEvents:
      - 0
      disabledUsers:
      - ""
      enabled: false
      garbageCollection:
        sidecar:
          age: 1h
          enabled: false
          image: busybox:1.33.1
          interval: 20m
          resources: {}
      rotation:
        interval: 15m
        pruneAge: 0
        size: 20Mi
    logRetentionCount: 0
    logRetentionTime: ""
    server:
      configurationName: fluent-bit-config
      enabled: false
      manageConfiguration: True
      sidecar:
        configurationMountPath: /fluent-bit/config/
        image: couchbase/fluent-bit:1.2.9
        resources: {}
        tls:
          mountPath: /fluent-bit/certs/
          secretNames:
          - ""
  migration:
    maxConcurrentMigrations: 1
    migrationOrderOverride:
      migrationOrderOverrideStrategy: ""
      nodeOrder:
      - ""
      serverClassOrder:
      - ""
      serverGroupOrder:
      - ""
    numUnmanagedNodes: 0
    stabilizationPeriod: ""
    unmanagedClusterHost: ""
  mirWatchdog:
    enabled: false
    interval: ""
    skipReconciliation: false
  monitoring:
    prometheus:
      authorizationSecret: ""
      enabled: false
      image: ""
      refreshRate: 60
      resources: {}
  networking:
    addressFamily: ""
    adminConsoleServiceTemplate: {}
    adminConsoleServiceType: NodePort
    adminConsoleServices:
    - ""
    allowExternallyUnreachablePods: false
    cloudNativeGateway:
      image: ""
      logLevel: info
      serviceTemplate: {}
      terminationGracePeriodSeconds: 75
      tls:
        serverSecretName: ""
    disableUIOverHTTP: false
    disableUIOverHTTPS: false
    dns:
      domain: ""
    exposeAdminConsole: false
    exposedFeatureServiceTemplate: {}
    exposedFeatureServiceType: NodePort
    exposedFeatureTrafficPolicy: ""
    exposedFeatures:
    - ""
    improvedHostNetwork: false
    initPodsWithNodeHostname: false
    loadBalancerSourceRanges:
    - ""
    networkPlatform: ""
    serviceAnnotations:
    tls:
      allowPlainTextCertReload: false
      cipherSuites:
      - ""
      clientCertificatePaths:
      - delimiter: ""
        path: ""
        prefix: ""
      clientCertificatePolicy: ""
      nodeToNodeEncryption: ""
      passphrase:
        rest:
          addressFamily: inet
          headers:
          timeout: 5000
          url: ""
          verifyPeer: True
        script:
          secret: ""
      rootCAs:
      - ""
      secretSource:
        clientSecretName: ""
        serverSecretName: ""
      static:
        operatorSecret: ""
        serverSecret: ""
      tlsMinimumVersion: TLS1.2
      validateBareHostnames: True
    waitForAddressReachable: 10m
    waitForAddressReachableDelay: 2m
  onlineVolumeExpansionTimeoutInMins: 0
  paused: false
  perServiceClassPDB: false
  platform: ""
  recoveryPolicy: ""
  rollingUpgrade:
    maxUpgradable: 0
    maxUpgradablePercent: ""
  security:
    adminSecret: ""
    encryptionAtRest:
      audit:
        enabled: false
        keyLifetime: 8760h
        keyName: ""
        rotationInterval: 720h
      configuration:
        enabled: false
        keyLifetime: 8760h
        keyName: ""
        rotationInterval: 720h
      log:
        enabled: false
        keyLifetime: 8760h
        keyName: ""
        rotationInterval: 720h
      managed: false
      selector:
        matchExpressions:
        - key: ""
          operator: ""
          values:
          - ""
        matchLabels:
    ldap:
      authenticationEnabled: True
      authorizationEnabled: false
      bindDN: ""
      bindSecret: ""
      cacert: ""
      cacheValueLifetime: 30000
      encryption: ""
      groupsQuery: ""
      hosts:
      - ""
      middleboxCompMode: True
      nestedGroupsEnabled: false
      nestedGroupsMaxDepth: 10
      port: 389
      serverCertValidation: false
      tlsSecret: ""
      userDNMapping:
        query: ""
        template: ""
    passwordPolicy:
      enforceDigits: false
      enforceLowercase: false
      enforceSpecialChars: false
      enforceUppercase: false
      minLength: 0
      passwordResetOnPolicyChangeExemptUsers:
      - ""
      requirePasswordResetOnPolicyChange: false
    podSecurityContext:
      fsGroup: 0
      fsGroupChangePolicy: ""
      runAsGroup: 0
      runAsNonRoot: false
      runAsUser: 0
      seLinuxOptions:
        level: ""
        role: ""
        type: ""
        user: ""
      seccompProfile:
        localhostProfile: ""
        type: ""
      supplementalGroups:
      - 0
      sysctls:
      - name: ""
        value: ""
      windowsOptions:
        gmsaCredentialSpec: ""
        gmsaCredentialSpecName: ""
        hostProcess: false
        runAsUserName: ""
    rbac:
      managed: false
      selector: {}
    securityContext:
      allowPrivilegeEscalation: false
      capabilities:
        add:
        - ""
        drop:
        - ""
      privileged: false
      procMount: ""
      readOnlyRootFilesystem: false
      runAsGroup: 0
      runAsNonRoot: false
      runAsUser: 0
      seLinuxOptions:
        level: ""
        role: ""
        type: ""
        user: ""
      seccompProfile:
        localhostProfile: ""
        type: ""
      windowsOptions:
        gmsaCredentialSpec: ""
        gmsaCredentialSpecName: ""
        hostProcess: false
        runAsUserName: ""
    uiSessionTimeout: 0
  securityContext: {}
  serverGroups:
  - ""
  servers:
  - autoscaleEnabled: false
    env: []
    envFrom: []
    image: ""
    name: ""
    pod: {}
    resources: {}
    serverGroups:
    - ""
    services:
    - ""
    size: 0
    volumeMounts:
      analytics:
      - ""
      data: ""
      default: ""
      index: ""
      logs: ""
  softwareUpdateNotifications: false
  upgrade:
    previousVersionPodCount: 0
    rollingUpgrade:
      maxUpgradable: 0
      maxUpgradablePercent: ""
    stabilizationPeriod: ""
    upgradeOrder:
    - ""
    upgradeOrderType: Nodes
    upgradeProcess: SwapRebalance
    upgradeStrategy: RollingUpgrade
  upgradeProcess: ""
  upgradeStrategy: ""
  volumeClaimTemplates: []
  xdcr:
    globalSettings:
      checkpointInterval: 0
      collectionsOSOMode: false
      compressionType: ""
      conflictLogging:
        enabled: false
        logCollection:
          bucket: ""
          collection: ""
          scope: ""
        loggingRules:
          customCollectionRules:
          - collection: ""
            logCollection:
              bucket: ""
              collection: ""
              scope: ""
            scope: ""
          defaultCollectionRules:
          - collection: ""
            scope: ""
          noLoggingRules:
          - collection: ""
            scope: ""
      desiredLatency: 0
      docBatchSizeKb: 0
      failureRestartInterval: 0
      filterBinary: false
      filterBypassExpiry: false
      filterBypassUncommittedTxn: false
      filterDeletion: false
      filterExpiration: false
      goGC: 0
      goMaxProcs: 0
      hlvPruningWindowSec: 0
      jsFunctionTimeoutMs: 0
      logLevel: ""
      mergeFunctionMapping:
      mobile: ""
      networkUsageLimit: 0
      optimisticReplicationThreshold: 0
      priority: ""
      retryOnRemoteAuthErr: false
      retryOnRemoteAuthErrMaxWaitSec: 0
      sourceNozzlePerNode: 0
      statsInterval: 0
      targetNozzlePerNode: 0
      workerBatchSize: 0
    managed: false
    remoteClusters:
    - authenticationSecret: ""
      hostname: ""
      name: ""
      replications:
        selector: {}
      tls:
        secret: ""
      uuid: ""
status:
  allocations:
  - allocatedMemory: ""
    allocatedMemoryPercent: 0
    analyticsServiceAllocation: ""
    dataServiceAllocation: ""
    eventingServiceAllocation: ""
    indexServiceAllocation: ""
    name: ""
    requestedMemory: ""
    searchServiceAllocation: ""
    unusedMemory: ""
    unusedMemoryPercent: 0
  autoscalers:
  - ""
  buckets:
  - compressionMode: ""
    conflictResolution: ""
    enableFlush: false
    enableIndexReplica: false
    evictionPolicy: ""
    ioPriority: ""
    memoryQuota: 0
    name: ""
    numVBuckets: 0
    password: ""
    replicas: 0
    storageBackend: ""
    type: ""
  clusterId: ""
  conditions:
  - lastTransitionTime: ""
    lastUpdateTime: ""
    message: ""
    reason: ""
    status: ""
    type: ""
  controlPaused: false
  currentVersion: ""
  groups:
  - ""
  lastUpdateTime: ""
  members:
    ready:
    - ""
    unready:
    - ""
  rebalanceAttempts: 0
  size: 0
  users:
  - ""
```

## [](#couchbaseclusters-apiversion)couchbaseclusters.apiVersion

### [](#constraints)Constraints

**Type**: `string`

### [](#description)Description

APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources>.

## [](#couchbaseclusters-kind)couchbaseclusters.kind

### [](#constraints-2)Constraints

**Type**: `string`

### [](#description-2)Description

Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds>.

## [](#couchbaseclusters-metadata)couchbaseclusters.metadata

### [](#constraints-3)Constraints

**Required**

**Type**: `object`

### [](#description-3)Description

Standard object metadata as defined for all Kubernetes types.

For additional details see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/).

### [](#couchbaseclusters-metadata-name)couchbaseclusters.metadata.name

#### [](#constraints-4)Constraints

**Type**: `string`

#### [](#description-4)Description

The name of a resource. This must be unique for the kind of resource within the namespace.

All resources must have a name. The name may be omitted and `metadata.generateName` used instead to generate a unique resource name.

For additional details on resource names, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/names/).

### [](#couchbaseclusters-metadata-namespace)couchbaseclusters.metadata.namespace

#### [](#constraints-5)Constraints

**Type**: `string`

#### [](#description-5)Description

The namespace the resource resides in. All resources reside in a namespace.

The namespace is optional and may be specified in YAML configuration to override the namespace supplied by `kubectl`.

For additional details on namespaces, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).

### [](#couchbaseclusters-metadata-labels)couchbaseclusters.metadata.labels

#### [](#constraints-6)Constraints

**Type**: `map[string]string`

#### [](#description-6)Description

Labels allow resources to be labeled with key/value pairs of data. Labels are indexed and allow resources to be selected based upon specified labels.

Labels are relevant for certain types when using [label selection](../concept-label-selection.md) within your resources.

For additional details on labels and selectors, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/labels/).

### [](#couchbaseclusters-metadata-annotations)couchbaseclusters.metadata.annotations

#### [](#constraints-7)Constraints

**Type**: `map[string]string`

#### [](#description-7)Description

Annotations allow resources to be annotated with key/value pairs of data. Annotations are arbitrary, and not indexed, so cannot be used to select resources, however may be used to add context or accounting to your resources.

For additional details on annotations, see the [Kubernetes reference documentation](https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations/).

## [](#couchbaseclusters-spec)couchbaseclusters.spec

### [](#constraints-8)Constraints

**Required**

**Type**: `object`

### [](#description-8)Description

ClusterSpec is the specification for a CouchbaseCluster resources, and allows the cluster to be customized.

### [](#couchbaseclusters-spec-antiaffinity)couchbaseclusters.spec.antiAffinity

#### [](#constraints-9)Constraints

**Type**: `boolean`

#### [](#description-9)Description

AntiAffinity forces the Operator to schedule different Couchbase server pods on different Kubernetes nodes. Anti-affinity reduces the likelihood of unrecoverable failure in the event of a node issue. Use of anti-affinity is highly recommended for production clusters.

### [](#couchbaseclusters-spec-autoresourceallocation)couchbaseclusters.spec.autoResourceAllocation

#### [](#constraints-10)Constraints

**Type**: `object`

#### [](#description-10)Description

AutoResourceAllocation populates pod resource requests based on the services running on that pod. When enabled, this feature will calculate the memory request as the total of service allocations defined in `spec.cluster`, plus an overhead defined by `spec.autoResourceAllocation.overheadPercent`.Changing individual allocations for a service will cause a cluster upgrade as allocations are modified in the underlying pods. This field also allows default pod CPU requests and limits to be applied. All resource allocations can be overridden by explicitly configuring them in the `spec.servers.resources` field.

### [](#couchbaseclusters-spec-autoresourceallocation-cpulimits)couchbaseclusters.spec.autoResourceAllocation.cpuLimits

#### [](#constraints-11)Constraints

**Type**: `string`

**Default**: `4`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-11)Description

CPULimits automatically populates the CPU limits across all Couchbase server pods. This field defaults to "4" CPUs. Explicitly specifying the CPU limit for a particular server class will override this value. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-autoresourceallocation-cpurequests)couchbaseclusters.spec.autoResourceAllocation.cpuRequests

#### [](#constraints-12)Constraints

**Type**: `string`

**Default**: `2`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-12)Description

CPURequests automatically populates the CPU requests across all Couchbase server pods. The default value of "2", is the minimum recommended number of CPUs required to run Couchbase Server. Explicitly specifying the CPU request for a particular server class will override this value. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-autoresourceallocation-enabled)couchbaseclusters.spec.autoResourceAllocation.enabled

#### [](#constraints-13)Constraints

**Type**: `boolean`

#### [](#description-13)Description

Enabled defines whether auto-resource allocation is enabled.

### [](#couchbaseclusters-spec-autoresourceallocation-overheadmemory)couchbaseclusters.spec.autoResourceAllocation.overheadMemory

#### [](#constraints-14)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-14)Description

OverheadMemory defines a static amount of memory above that required for individual services on a pod. This will override `overheadPercent` if both are specified.

### [](#couchbaseclusters-spec-autoresourceallocation-overheadpercent)couchbaseclusters.spec.autoResourceAllocation.overheadPercent

#### [](#constraints-15)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-15)Description

OverheadPercent defines the amount of memory above that required for individual services on a pod. For Couchbase Server this should be approximately 25%.

### [](#couchbaseclusters-spec-autoscalestabilizationperiod)couchbaseclusters.spec.autoscaleStabilizationPeriod

#### [](#constraints-16)Constraints

**Type**: `string`

#### [](#description-16)Description

AutoscaleStabilizationPeriod defines how long after a rebalance the corresponding HorizontalPodAutoscaler should remain in maintenance mode. During maintenance mode all autoscaling is disabled since every HorizontalPodAutoscaler associated with the cluster becomes inactive. Since certain metrics can be unpredictable when Couchbase is rebalancing or upgrading, setting a stabilization period helps to prevent scaling recommendations from the HorizontalPodAutoscaler for a provided period of time. Values must be a valid Kubernetes duration of 0s or higher: <https://golang.org/pkg/time/#ParseDuration>A value of 0, puts the cluster in maintenance mode during rebalance but immediately exits this mode once the rebalance has completed. When undefined, the HPA is never put into maintenance mode during rebalance.

### [](#couchbaseclusters-spec-backup)couchbaseclusters.spec.backup

#### [](#constraints-17)Constraints

**Type**: `object`

#### [](#description-17)Description

Backup defines whether the Operator should manage automated backups, and how to lookup backup resources.

### [](#couchbaseclusters-spec-backup-annotations)couchbaseclusters.spec.backup.annotations

#### [](#constraints-18)Constraints

**Type**: `map[string]string`

#### [](#description-18)Description

Annotations defines additional annotations to appear on the backup/restore pods.

### [](#couchbaseclusters-spec-backup-image)couchbaseclusters.spec.backup.image

#### [](#constraints-19)Constraints

**Required**

**Type**: `string`

**Default**: `couchbase/operator-backup:1.4.1`

#### [](#description-19)Description

The Backup Image to run on backup pods.

### [](#couchbaseclusters-spec-backup-imagepullsecrets)couchbaseclusters.spec.backup.imagePullSecrets

#### [](#constraints-20)Constraints

**Type**: `[]object`

#### [](#description-20)Description

ImagePullSecrets allow you to use an image from private repositories and non-dockerhub ones.

### [](#couchbaseclusters-spec-backup-imagepullsecrets-name)couchbaseclusters.spec.backup.imagePullSecrets.name

#### [](#constraints-21)Constraints

**Type**: `string`

#### [](#description-21)Description

Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names>.

### [](#couchbaseclusters-spec-backup-labels)couchbaseclusters.spec.backup.labels

#### [](#constraints-22)Constraints

**Type**: `map[string]string`

#### [](#description-22)Description

Labels defines additional labels to appear on the backup/restore pods.

### [](#couchbaseclusters-spec-backup-managed)couchbaseclusters.spec.backup.managed

#### [](#constraints-23)Constraints

**Type**: `boolean`

#### [](#description-23)Description

Managed defines whether backups are managed by us or the clients.

### [](#couchbaseclusters-spec-backup-nodeselector)couchbaseclusters.spec.backup.nodeSelector

#### [](#constraints-24)Constraints

**Type**: `map[string]string`

#### [](#description-24)Description

NodeSelector defines which nodes to constrain the pods that run any backup and restore operations to.

### [](#couchbaseclusters-spec-backup-objectendpoint)couchbaseclusters.spec.backup.objectEndpoint

#### [](#constraints-25)Constraints

**Type**: `object`

#### [](#description-25)Description

Deprecated: by CouchbaseBackup.spec.objectStore.Endpoint ObjectEndpoint contains the configuration for connecting to a custom S3 compliant object store.

### [](#couchbaseclusters-spec-backup-objectendpoint-secret)couchbaseclusters.spec.backup.objectEndpoint.secret

#### [](#constraints-26)Constraints

**Type**: `string`

#### [](#description-26)Description

The name of the secret, in this namespace, that contains the CA certificate for verification of a TLS endpoint The secret must have the key with the name "tls.crt".

### [](#couchbaseclusters-spec-backup-objectendpoint-url)couchbaseclusters.spec.backup.objectEndpoint.url

#### [](#constraints-27)Constraints

**Type**: `string`

#### [](#description-27)Description

The host/address of the custom object endpoint.

### [](#couchbaseclusters-spec-backup-objectendpoint-usevirtualpath)couchbaseclusters.spec.backup.objectEndpoint.useVirtualPath

#### [](#constraints-28)Constraints

**Type**: `boolean`

#### [](#description-28)Description

UseVirtualPath will force the AWS SDK to use the new virtual style paths which are often required by S3 compatible object stores.

### [](#couchbaseclusters-spec-backup-resources)couchbaseclusters.spec.backup.resources

#### [](#constraints-29)Constraints

**Type**: `object`

#### [](#description-29)Description

Resources is the resource requirements for the backup and restore containers. Will be populated by defaults if not specified.

### [](#couchbaseclusters-spec-backup-s3secret)couchbaseclusters.spec.backup.s3Secret

#### [](#constraints-30)Constraints

**Type**: `string`

#### [](#description-30)Description

Deprecated: by CouchbaseBackup.spec.objectStore.secret S3Secret contains the key region and optionally access-key-id and secret-access-key for operating backups in S3\. This field must be popluated when the `spec.s3bucket` field is specified for a backup or restore resource.

### [](#couchbaseclusters-spec-backup-selector)couchbaseclusters.spec.backup.selector

#### [](#constraints-31)Constraints

**Type**: `object`

#### [](#description-31)Description

Selector allows CouchbaseBackup and CouchbaseBackupRestore resources to be filtered based on labels.

### [](#couchbaseclusters-spec-backup-serviceaccountname)couchbaseclusters.spec.backup.serviceAccountName

#### [](#constraints-32)Constraints

**Type**: `string`

**Default**: `couchbase-backup`

#### [](#description-32)Description

The Service Account to run backup (and restore) pods under. Without this backup pods will not be able to update status.

### [](#couchbaseclusters-spec-backup-tolerations)couchbaseclusters.spec.backup.tolerations

#### [](#constraints-33)Constraints

**Type**: `[]object`

#### [](#description-33)Description

Tolerations specifies all backup and restore pod tolerations.

### [](#couchbaseclusters-spec-backup-tolerations-effect)couchbaseclusters.spec.backup.tolerations.effect

#### [](#constraints-34)Constraints

**Type**: `string`

#### [](#description-34)Description

Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.

### [](#couchbaseclusters-spec-backup-tolerations-key)couchbaseclusters.spec.backup.tolerations.key

#### [](#constraints-35)Constraints

**Type**: `string`

#### [](#description-35)Description

Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.

### [](#couchbaseclusters-spec-backup-tolerations-operator)couchbaseclusters.spec.backup.tolerations.operator

#### [](#constraints-36)Constraints

**Type**: `string`

#### [](#description-36)Description

Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.

### [](#couchbaseclusters-spec-backup-tolerations-tolerationseconds)couchbaseclusters.spec.backup.tolerations.tolerationSeconds

#### [](#constraints-37)Constraints

**Type**: `integer`

#### [](#description-37)Description

TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.

### [](#couchbaseclusters-spec-backup-tolerations-value)couchbaseclusters.spec.backup.tolerations.value

#### [](#constraints-38)Constraints

**Type**: `string`

#### [](#description-38)Description

Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.

### [](#couchbaseclusters-spec-backup-useiamrole)couchbaseclusters.spec.backup.useIAMRole

#### [](#constraints-39)Constraints

**Type**: `boolean`

#### [](#description-39)Description

Deprecated: by CouchbaseBackup.spec.objectStore.useIAM UseIAMRole enables backup to fetch EC2 instance metadata. This allows the AWS SDK to use the EC2’s IAM Role for S3 access. UseIAMRole will ignore credentials in s3Secret.

### [](#couchbaseclusters-spec-buckets)couchbaseclusters.spec.buckets

#### [](#constraints-40)Constraints

**Type**: `object`

#### [](#description-40)Description

Buckets defines whether the Operator should manage buckets, and how to lookup bucket resources.

### [](#couchbaseclusters-spec-buckets-enablebucketmigrationroutines)couchbaseclusters.spec.buckets.enableBucketMigrationRoutines

#### [](#constraints-41)Constraints

**Type**: `boolean`

#### [](#description-41)Description

Used to define whether managed bucket storage backend migration routines should be enabled. This value defaults to false.

### [](#couchbaseclusters-spec-buckets-managed)couchbaseclusters.spec.buckets.managed

#### [](#constraints-42)Constraints

**Type**: `boolean`

#### [](#description-42)Description

Managed defines whether buckets are managed by the Operator (true), or user managed (false). When Operator managed, all buckets must be defined with either CouchbaseBucket or CouchbaseEphemeralBucket resources. Manual addition of buckets will be reverted by the Operator. When user managed, the Operator will not interrogate buckets at all. This field defaults to false.

### [](#couchbaseclusters-spec-buckets-selector)couchbaseclusters.spec.buckets.selector

#### [](#constraints-43)Constraints

**Type**: `object`

#### [](#description-43)Description

Selector is a label selector used to list buckets in the namespace that are managed by the Operator.

### [](#couchbaseclusters-spec-buckets-selector-matchexpressions)couchbaseclusters.spec.buckets.selector.matchExpressions

#### [](#constraints-44)Constraints

**Type**: `[]object`

#### [](#description-44)Description

matchExpressions is a list of label selector requirements. The requirements are ANDed.

### [](#couchbaseclusters-spec-buckets-selector-matchexpressions-key)couchbaseclusters.spec.buckets.selector.matchExpressions.key

#### [](#constraints-45)Constraints

**Required**

**Type**: `string`

#### [](#description-45)Description

key is the label key that the selector applies to.

### [](#couchbaseclusters-spec-buckets-selector-matchexpressions-operator)couchbaseclusters.spec.buckets.selector.matchExpressions.operator

#### [](#constraints-46)Constraints

**Required**

**Type**: `string`

#### [](#description-46)Description

operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.

### [](#couchbaseclusters-spec-buckets-selector-matchexpressions-values)couchbaseclusters.spec.buckets.selector.matchExpressions.values

#### [](#constraints-47)Constraints

**Type**: `[]string`

#### [](#description-47)Description

values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

### [](#couchbaseclusters-spec-buckets-selector-matchlabels)couchbaseclusters.spec.buckets.selector.matchLabels

#### [](#constraints-48)Constraints

**Type**: `map[string]string`

#### [](#description-48)Description

matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

### [](#couchbaseclusters-spec-buckets-synchronize)couchbaseclusters.spec.buckets.synchronize

#### [](#constraints-49)Constraints

**Type**: `boolean`

#### [](#description-49)Description

Synchronize allows unmanaged buckets, scopes, and collections to be synchronized as Kubernetes resources by the Operator. This feature is intended for development only and should not be used for production workloads. The synchronization workflow starts with `spec.buckets.managed` being set to false, the user can manually create buckets, scopes, and collections using the Couchbase UI, or other tooling. When you wish to commit to Kubernetes resources, you must specify a unique label selector in the `spec.buckets.selector` field, and this field is set to true. The Operator will create Kubernetes resources for you, and upon completion set the cluster’s `Synchronized`status condition. Synchronizing will not create a Kubernetes resource for the Couchbase Server maintained \_system scope. You may then safely set `spec.buckets.managed` to true and the Operator will manage these resources as per usual. To update an already managed data topology, you must first set it to unmanaged, make any changes, and delete any old resources, then follow the standard synchronization workflow. The Operator can not, and will not, ever delete, or make modifications to resource specifications that are intended to be user managed, or managed by a life cycle management tool. These actions must be instigated by an end user. For a more complete experience, refer to the documentation for the `cao save` and `cao restore` CLI commands.

### [](#couchbaseclusters-spec-cluster)couchbaseclusters.spec.cluster

#### [](#constraints-50)Constraints

**Type**: `object`

**Default**: `{}`

#### [](#description-50)Description

ClusterSettings define Couchbase cluster-wide settings such as memory allocation, failover characteristics and index settings.

### [](#couchbaseclusters-spec-cluster-allowfailoverephemeralnoreplicas)couchbaseclusters.spec.cluster.allowFailoverEphemeralNoReplicas

#### [](#constraints-51)Constraints

**Type**: `boolean`

#### [](#description-51)Description

AllowFailoverEphemeralNoReplicas allows failover of ephemeral buckets with no replicas. This is only supported on Couchbase Server 8.0+.

### [](#couchbaseclusters-spec-cluster-analytics)couchbaseclusters.spec.cluster.analytics

#### [](#constraints-52)Constraints

**Type**: `object`

#### [](#description-52)Description

Analytics allows the analytics service to be configured.

### [](#couchbaseclusters-spec-cluster-analytics-numreplicas)couchbaseclusters.spec.cluster.analytics.numReplicas

#### [](#constraints-53)Constraints

**Type**: `integer`

**Minimum**: `0`

**Maximum**: `3`

#### [](#description-53)Description

NumReplicas specifies the number of replicas for Analytics. Changing the value in this field when the Analytics service is enabled will trigger a rebalance of the cluster.

### [](#couchbaseclusters-spec-cluster-analyticsservicememoryquota)couchbaseclusters.spec.cluster.analyticsServiceMemoryQuota

#### [](#constraints-54)Constraints

**Type**: `string`

**Default**: `1Gi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-54)Description

AnalyticsServiceMemQuota is the amount of memory that should be allocated to the analytics service. This value is per-pod, and only applicable to pods belonging to server classes running the analytics service. This field must be a quantity greater than or equal to 1Gi. This field defaults to 1Gi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-cluster-apptelemetry)couchbaseclusters.spec.cluster.appTelemetry

#### [](#constraints-55)Constraints

**Type**: `object`

#### [](#description-55)Description

AppTelemetry allows the configuration of application telemetry. This is only supported on Couchbase Server 8.0+.

### [](#couchbaseclusters-spec-cluster-apptelemetry-enabled)couchbaseclusters.spec.cluster.appTelemetry.enabled

#### [](#constraints-56)Constraints

**Required**

**Type**: `boolean`

**Default**: `False`

#### [](#description-56)Description

Enabled controls whether application telemetry is enabled.

### [](#couchbaseclusters-spec-cluster-apptelemetry-maxscrapeclientspernode)couchbaseclusters.spec.cluster.appTelemetry.maxScrapeClientsPerNode

#### [](#constraints-57)Constraints

**Type**: `integer`

**Default**: `1024`

**Minimum**: `1`

**Maximum**: `1024`

#### [](#description-57)Description

MaxScrapeClientsPerNode sets the maximum number of scrape clients per node. Must be between 1 and 1024.

### [](#couchbaseclusters-spec-cluster-apptelemetry-scrapeintervalseconds)couchbaseclusters.spec.cluster.appTelemetry.scrapeIntervalSeconds

#### [](#constraints-58)Constraints

**Type**: `integer`

**Default**: `60`

**Minimum**: `60`

**Maximum**: `600`

#### [](#description-58)Description

ScrapeIntervalSeconds sets the scrape interval in seconds. Must be between 60 and 600.

### [](#couchbaseclusters-spec-cluster-autocompaction)couchbaseclusters.spec.cluster.autoCompaction

#### [](#constraints-59)Constraints

**Type**: `object`

**Default**: `{}`

#### [](#description-59)Description

AutoCompaction allows the configuration of auto-compaction, including on what conditions disk space is reclaimed and when it is allowed to run. Cluster level settings will be used as the default when creating new buckets and any changes to the settings will be applied to all existing buckets that have not had their auto-compaction settings individually modified.

### [](#couchbaseclusters-spec-cluster-autocompaction-databasefragmentationthreshold)couchbaseclusters.spec.cluster.autoCompaction.databaseFragmentationThreshold

#### [](#constraints-60)Constraints

**Type**: `object`

**Default**: `{}`

#### [](#description-60)Description

DatabaseFragmentationThreshold defines the default database fragmentation level to determine the point when compaction is triggered for buckets with a couchstore storage backend.

### [](#couchbaseclusters-spec-cluster-autocompaction-databasefragmentationthreshold-percent)couchbaseclusters.spec.cluster.autoCompaction.databaseFragmentationThreshold.percent

#### [](#constraints-61)Constraints

**Type**: `integer`

**Default**: `30`

**Minimum**: `2`

**Maximum**: `100`

#### [](#description-61)Description

Percent is the percentage of disk fragmentation after which to decompaction will be triggered. This field must be in the range 2-100, defaulting to 30.

### [](#couchbaseclusters-spec-cluster-autocompaction-databasefragmentationthreshold-size)couchbaseclusters.spec.cluster.autoCompaction.databaseFragmentationThreshold.size

#### [](#constraints-62)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-62)Description

Size is the amount of disk framentation, that once exceeded, will trigger decompaction. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-cluster-autocompaction-magmafragmentationpercentage)couchbaseclusters.spec.cluster.autoCompaction.magmaFragmentationPercentage

#### [](#constraints-63)Constraints

**Type**: `integer`

**Minimum**: `10`

**Maximum**: `100`

#### [](#description-63)Description

MagmaFragmentationThresholdPercentage defines the default database fragmentation level to determine point when database compaction is triggered for buckets with a magma storage backend. This field must be in the range 10-100\. This field is ignored for Couchstore buckets.

### [](#couchbaseclusters-spec-cluster-autocompaction-parallelcompaction)couchbaseclusters.spec.cluster.autoCompaction.parallelCompaction

#### [](#constraints-64)Constraints

**Type**: `boolean`

#### [](#description-64)Description

ParallelCompaction controls whether database and view compactions can happen in parallel.

### [](#couchbaseclusters-spec-cluster-autocompaction-timewindow)couchbaseclusters.spec.cluster.autoCompaction.timeWindow

#### [](#constraints-65)Constraints

**Type**: `object`

#### [](#description-65)Description

TimeWindow allows restriction of when compaction can occur.

### [](#couchbaseclusters-spec-cluster-autocompaction-timewindow-abortcompactionoutsidewindow)couchbaseclusters.spec.cluster.autoCompaction.timeWindow.abortCompactionOutsideWindow

#### [](#constraints-66)Constraints

**Type**: `boolean`

#### [](#description-66)Description

AbortCompactionOutsideWindow stops compaction processes when the process moves outside the window, defaulting to false.

### [](#couchbaseclusters-spec-cluster-autocompaction-timewindow-end)couchbaseclusters.spec.cluster.autoCompaction.timeWindow.end

#### [](#constraints-67)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$`

#### [](#description-67)Description

End is a wallclock time, in the form HH:MM, when a compaction should stop.

### [](#couchbaseclusters-spec-cluster-autocompaction-timewindow-start)couchbaseclusters.spec.cluster.autoCompaction.timeWindow.start

#### [](#constraints-68)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(2[0-3]|[01]?[0-9]):([0-5]?[0-9])$`

#### [](#description-68)Description

Start is a wallclock time, in the form HH:MM, when a compaction is permitted to start.

### [](#couchbaseclusters-spec-cluster-autocompaction-tombstonepurgeinterval)couchbaseclusters.spec.cluster.autoCompaction.tombstonePurgeInterval

#### [](#constraints-69)Constraints

**Type**: `string`

**Default**: `72h`

#### [](#description-69)Description

TombstonePurgeInterval controls how long to wait before purging tombstones. This field must be in the range 1h-1440h, defaulting to 72h. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbaseclusters-spec-cluster-autocompaction-viewfragmentationthreshold)couchbaseclusters.spec.cluster.autoCompaction.viewFragmentationThreshold

#### [](#constraints-70)Constraints

**Type**: `object`

**Default**: `{}`

#### [](#description-70)Description

ViewFragmentationThreshold defines triggers for when view compaction should start.

### [](#couchbaseclusters-spec-cluster-autocompaction-viewfragmentationthreshold-percent)couchbaseclusters.spec.cluster.autoCompaction.viewFragmentationThreshold.percent

#### [](#constraints-71)Constraints

**Type**: `integer`

**Default**: `30`

**Minimum**: `2`

**Maximum**: `100`

#### [](#description-71)Description

Percent is the percentage of disk fragmentation after which to decompaction will be triggered. This field must be in the range 2-100, defaulting to 30.

### [](#couchbaseclusters-spec-cluster-autocompaction-viewfragmentationthreshold-size)couchbaseclusters.spec.cluster.autoCompaction.viewFragmentationThreshold.size

#### [](#constraints-72)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-72)Description

Size is the amount of disk framentation, that once exceeded, will trigger decompaction. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-cluster-autofailovermaxcount)couchbaseclusters.spec.cluster.autoFailoverMaxCount

#### [](#constraints-73)Constraints

**Type**: `integer`

**Default**: `1`

**Minimum**: `1`

#### [](#description-73)Description

AutoFailoverMaxCount is the maximum number of automatic failovers Couchbase server will allow before not allowing any more. This field must be between 1-3 for server versions prior to 7.1.0 default is 1.

### [](#couchbaseclusters-spec-cluster-autofailoverondatadiskissues)couchbaseclusters.spec.cluster.autoFailoverOnDataDiskIssues

#### [](#constraints-74)Constraints

**Type**: `boolean`

#### [](#description-74)Description

AutoFailoverOnDataDiskIssues defines whether Couchbase server should failover a pod if a disk issue was detected.

### [](#couchbaseclusters-spec-cluster-autofailoverondatadiskissuestimeperiod)couchbaseclusters.spec.cluster.autoFailoverOnDataDiskIssuesTimePeriod

#### [](#constraints-75)Constraints

**Type**: `string`

**Default**: `120s`

#### [](#description-75)Description

AutoFailoverOnDataDiskIssuesTimePeriod defines how long to wait for transient errors before failing over a faulty disk. This field must be in the range 5-3600s, defaulting to 120s. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbaseclusters-spec-cluster-autofailoverservergroup)couchbaseclusters.spec.cluster.autoFailoverServerGroup

#### [](#constraints-76)Constraints

**Type**: `boolean`

#### [](#description-76)Description

AutoFailoverServerGroup whether to enable failing over a server group. This field is ignored in server versions 7.1+ as it has been removed from the Couchbase API.

### [](#couchbaseclusters-spec-cluster-autofailovertimeout)couchbaseclusters.spec.cluster.autoFailoverTimeout

#### [](#constraints-77)Constraints

**Type**: `string`

**Default**: `120s`

#### [](#description-77)Description

AutoFailoverTimeout defines how long Couchbase server will wait between a pod being witnessed as down, until when it will failover the pod. Couchbase server will only failover pods if it deems it safe to do so, and not result in data loss. This field must be in the range 5-3600s, defaulting to 120s. More info: <https://golang.org/pkg/time/#ParseDuration>.

### [](#couchbaseclusters-spec-cluster-clustername)couchbaseclusters.spec.cluster.clusterName

#### [](#constraints-78)Constraints

**Type**: `string`

#### [](#description-78)Description

ClusterName defines the name of the cluster, as displayed in the Couchbase UI. By default, the cluster name is that specified in the CouchbaseCluster resource’s metadata.

### [](#couchbaseclusters-spec-cluster-data)couchbaseclusters.spec.cluster.data

#### [](#constraints-79)Constraints

**Type**: `object`

#### [](#description-79)Description

Data allows the data service to be configured.

### [](#couchbaseclusters-spec-cluster-data-auxiothreads)couchbaseclusters.spec.cluster.data.auxIOThreads

#### [](#constraints-80)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `64`

#### [](#description-80)Description

AuxIOThreads allows the number of threads used by the data service, per pod, to be altered. This indicates the number of threads that are to be used in the AuxIO thread pool to run auxiliary I/O tasks. This value must be between 1 and 64 threads and is only supported on CB versions 7.1.0+. and should only be increased where there are sufficient CPU resources allocated for their use. If not specified, this defaults to the default value set by Couchbase Server.

### [](#couchbaseclusters-spec-cluster-data-diskusagelimit)couchbaseclusters.spec.cluster.data.diskUsageLimit

#### [](#constraints-81)Constraints

**Type**: `object`

#### [](#description-81)Description

DiskUsageLimit allows a threshold to be set to limit the amount of disk space that can be used by buckets. If the disk usage limit is reached, Couchbase server will prevent data writes to buckets. Setting this value reserves disk space for recovery operations like performing rebalances to add a new node. This field is only supported on Couchbase server versions 8.0 and later.

### [](#couchbaseclusters-spec-cluster-data-diskusagelimit-enabled)couchbaseclusters.spec.cluster.data.diskUsageLimit.enabled

#### [](#constraints-82)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-82)Description

Enabled specifies whether the disk usage limit is enabled, defaulting to false.

### [](#couchbaseclusters-spec-cluster-data-diskusagelimit-percent)couchbaseclusters.spec.cluster.data.diskUsageLimit.percent

#### [](#constraints-83)Constraints

**Type**: `integer`

**Default**: `85`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-83)Description

Percent is the percentage of disk space that can be used before bucket writes are prevented. This field must be in the range 1-100, defaulting to 85.

### [](#couchbaseclusters-spec-cluster-data-minreplicascount)couchbaseclusters.spec.cluster.data.minReplicasCount

#### [](#constraints-84)Constraints

**Type**: `integer`

**Default**: `0`

**Minimum**: `0`

**Maximum**: `3`

#### [](#description-84)Description

MinReplicasCount allows the minimum number of replicas required for buckets to be set. New buckets cannot be created with less than this minimum. This field must be between 0 and 3, defaulting to 0.

### [](#couchbaseclusters-spec-cluster-data-noniothreads)couchbaseclusters.spec.cluster.data.nonIOThreads

#### [](#constraints-85)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `64`

#### [](#description-85)Description

NonIOThreads allows the number of threads used by the data service, per pod, to be altered. This indicates the number of threads that are to be used in the NonIO thread pool to run in memory tasks. This value must be between 1 and 64 threads and is only supported on CB versions 7.1.0+. and should only be increased where there are sufficient CPU resources allocated for their use. If not specified, this defaults to the default value set by Couchbase Server.

### [](#couchbaseclusters-spec-cluster-data-readerthreads)couchbaseclusters.spec.cluster.data.readerThreads

#### [](#constraints-86)Constraints

**Type**: `integer or string`

#### [](#description-86)Description

ReaderThreads allows the number of threads used by the data service, per pod, to be altered. This can either be fixed to a number between 1 and 64, or to one of default(pre 8.0.0) / balanced(post 8.0.0) or disk\_io\_optimized. For server versions below 7.1.0, the minimum fixed value is 4\. Increasing the fixed value should only be done where there are sufficient CPU resources. When using the default/balanced and disk\_io\_optimized options, CB server will automatically determine the number of threads to use. If not specified, this defaults to default/balanced.

### [](#couchbaseclusters-spec-cluster-data-tcpkeepaliveidle)couchbaseclusters.spec.cluster.data.tcpKeepAliveIdle

#### [](#constraints-87)Constraints

**Type**: `integer`

#### [](#description-87)Description

TCPKeepAliveIdle is the number of seconds before the first TCP probe is sent. This field is only supported on Couchbase server versions 8.0.0 and later.

### [](#couchbaseclusters-spec-cluster-data-tcpkeepaliveinterval)couchbaseclusters.spec.cluster.data.tcpKeepAliveInterval

#### [](#constraints-88)Constraints

**Type**: `integer`

#### [](#description-88)Description

TCPKeepAliveInterval is the number of seconds between TCP probes. This field is only supported on Couchbase server versions 8.0.0 and later.

### [](#couchbaseclusters-spec-cluster-data-tcpkeepaliveprobes)couchbaseclusters.spec.cluster.data.tcpKeepAliveProbes

#### [](#constraints-89)Constraints

**Type**: `integer`

#### [](#description-89)Description

TCPKeepAliveProbes is the number of TCP probes missing before the connection is considered dead. This field is only supported on Couchbase server versions 8.0.0 and later.

### [](#couchbaseclusters-spec-cluster-data-tcpusertimeout)couchbaseclusters.spec.cluster.data.tcpUserTimeout

#### [](#constraints-90)Constraints

**Type**: `integer`

#### [](#description-90)Description

TCPUserTimeout is the number of seconds data is stuck in the send buffer before the connection gets torn down. This field is only supported on Couchbase server versions 8.0.0 and later.

### [](#couchbaseclusters-spec-cluster-data-writerthreads)couchbaseclusters.spec.cluster.data.writerThreads

#### [](#constraints-91)Constraints

**Type**: `integer or string`

#### [](#description-91)Description

WriterThreads allows the number of threads used by the data service, per pod, to be altered. This can either be fixed to a number between 1 and 64, or to one of "default" (pre 8.0.0) / "balanced" (post 8.0.0) or "disk\_io\_optimized". For server versions below 7.1.0, the minimum fixed value is 4\. Increasing the fixed value should only be done where there are sufficient CPU resources. When using the default/balanced and disk\_io\_optimized options, CB server will automatically determine the number of threads to use. If not specified, this defaults to default/balanced.

### [](#couchbaseclusters-spec-cluster-dataservicememoryquota)couchbaseclusters.spec.cluster.dataServiceMemoryQuota

#### [](#constraints-92)Constraints

**Type**: `string`

**Default**: `256Mi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-92)Description

DataServiceMemQuota is the amount of memory that should be allocated to the data service. This value is per-pod, and only applicable to pods belonging to server classes running the data service. This field must be a quantity greater than or equal to 256Mi. This field defaults to 256Mi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-cluster-eventingservicememoryquota)couchbaseclusters.spec.cluster.eventingServiceMemoryQuota

#### [](#constraints-93)Constraints

**Type**: `string`

**Default**: `256Mi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-93)Description

EventingServiceMemQuota is the amount of memory that should be allocated to the eventing service. This value is per-pod, and only applicable to pods belonging to server classes running the eventing service. This field must be a quantity greater than or equal to 256Mi. This field defaults to 256Mi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-cluster-indexservicememoryquota)couchbaseclusters.spec.cluster.indexServiceMemoryQuota

#### [](#constraints-94)Constraints

**Type**: `string`

**Default**: `256Mi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-94)Description

IndexServiceMemQuota is the amount of memory that should be allocated to the index service. This value is per-pod, and only applicable to pods belonging to server classes running the index service. This field must be a quantity greater than or equal to 256Mi. This field defaults to 256Mi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-cluster-indexstoragesetting)couchbaseclusters.spec.cluster.indexStorageSetting

#### [](#constraints-95)Constraints

**Type**: `string`

**Default**: `memory_optimized`

**Enumerations**: `memory_optimized, plasma`

#### [](#description-95)Description

**DEPRECATED** \- by indexer.

The index storage mode to use for secondary indexing. This field must be one of "memory\_optimized" or "plasma", defaulting to "memory\_optimized". This field is immutable and cannot be changed unless there are no server classes running the index service in the cluster.

### [](#couchbaseclusters-spec-cluster-indexer)couchbaseclusters.spec.cluster.indexer

#### [](#constraints-96)Constraints

**Type**: `object`

#### [](#description-96)Description

Indexer allows the indexer to be configured.

### [](#couchbaseclusters-spec-cluster-indexer-deferbuild)couchbaseclusters.spec.cluster.indexer.deferBuild

#### [](#constraints-97)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-97)Description

DeferBuild allows the indexer to defer building indexes. This field is only supported on CB versions 8.0.0+.

### [](#couchbaseclusters-spec-cluster-indexer-enablepagebloomfilter)couchbaseclusters.spec.cluster.indexer.enablePageBloomFilter

#### [](#constraints-98)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-98)Description

EnablePageBloomFilter gives Couchbase Server guidance whether bloom filters should be used when item lookups occur. These help to indicate during a lookup that an item is not on disk, and therefore prevent unnecessary on-disk searches. This field is only supported on CB versions 7.1.0+.

### [](#couchbaseclusters-spec-cluster-indexer-enableshardaffinity)couchbaseclusters.spec.cluster.indexer.enableShardAffinity

#### [](#constraints-99)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-99)Description

EnableShardAffinity when false Index Servers rebuild any index that are newly assigned to them during a rebalance. When set to true, Couchbase Server moves a reassigned index’s files between Index Servers. This field is only supported on CB versions 7.6.0+.

### [](#couchbaseclusters-spec-cluster-indexer-loglevel)couchbaseclusters.spec.cluster.indexer.logLevel

#### [](#constraints-100)Constraints

**Type**: `string`

**Default**: `info`

**Enumerations**: `silent, fatal, error, warn, info, verbose, timing, debug, trace`

#### [](#description-100)Description

LogLevel controls the verbosity of indexer logs. This field must be one of "silent", "fatal", "error", "warn", "info", "verbose", "timing", "debug" or "trace", defaulting to "info".

### [](#couchbaseclusters-spec-cluster-indexer-maxrollbackpoints)couchbaseclusters.spec.cluster.indexer.maxRollbackPoints

#### [](#constraints-101)Constraints

**Type**: `integer`

**Default**: `2`

**Minimum**: `1`

#### [](#description-101)Description

MaxRollbackPoints controls the number of checkpoints that can be rolled back to. The default is 2, with a minimum of 1.

### [](#couchbaseclusters-spec-cluster-indexer-memorysnapshotinterval)couchbaseclusters.spec.cluster.indexer.memorySnapshotInterval

#### [](#constraints-102)Constraints

**Type**: `string`

**Default**: `200ms`

#### [](#description-102)Description

MemorySnapshotInterval controls when memory indexes should be snapshotted. This defaults to 200ms, and must be greater than or equal to 1ms.

### [](#couchbaseclusters-spec-cluster-indexer-numreplica)couchbaseclusters.spec.cluster.indexer.numReplica

#### [](#constraints-103)Constraints

**Type**: `integer`

**Default**: `0`

**Minimum**: `0`

**Maximum**: `16`

#### [](#description-103)Description

NumberOfReplica specifies number of secondary index replicas to be created by the Index Service whenever CREATE INDEX is invoked, which ensures high availability and high performance. Note, if nodes and num\_replica are both specified in the WITH clause, the specified number of nodes must be one greater than num\_replica This field must be between 0 and 16, defaulting to 0, which means no index replicas to be created by default.

### [](#couchbaseclusters-spec-cluster-indexer-redistributeindexes)couchbaseclusters.spec.cluster.indexer.redistributeIndexes

#### [](#constraints-104)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-104)Description

RedistributeIndexes when true, Couchbase Server redistributes indexes when rebalance occurs, in order to optimize performance. If false (the default), such redistribution does not occur.

### [](#couchbaseclusters-spec-cluster-indexer-stablesnapshotinterval)couchbaseclusters.spec.cluster.indexer.stableSnapshotInterval

#### [](#constraints-105)Constraints

**Type**: `string`

**Default**: `5s`

#### [](#description-105)Description

StableSnapshotInterval controls when disk indexes should be snapshotted. This defaults to 5s, and must be greater than or equal to 1ms.

### [](#couchbaseclusters-spec-cluster-indexer-storagemode)couchbaseclusters.spec.cluster.indexer.storageMode

#### [](#constraints-106)Constraints

**Type**: `string`

**Default**: `memory_optimized`

**Enumerations**: `memory_optimized, plasma`

#### [](#description-106)Description

StorageMode controls the underlying storage engine for indexes. Once set it can only be modified if there are no nodes in the cluster running the index service. The field must be one of "memory\_optimized" or "plasma", defaulting to "memory\_optimized".

### [](#couchbaseclusters-spec-cluster-indexer-threads)couchbaseclusters.spec.cluster.indexer.threads

#### [](#constraints-107)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-107)Description

Threads controls the number of processor threads to use for indexing. A value of 0 means 1 per CPU. This attribute must be greater than or equal to 0, defaulting to 0.

### [](#couchbaseclusters-spec-cluster-query)couchbaseclusters.spec.cluster.query

#### [](#constraints-108)Constraints

**Type**: `object`

#### [](#description-108)Description

Query allows the query service to be configured.

### [](#couchbaseclusters-spec-cluster-query-backfillenabled)couchbaseclusters.spec.cluster.query.backfillEnabled

#### [](#constraints-109)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-109)Description

BackfillEnabled allows the query service to backfill.

### [](#couchbaseclusters-spec-cluster-query-cboenabled)couchbaseclusters.spec.cluster.query.cboEnabled

#### [](#constraints-110)Constraints

**Required**

**Type**: `boolean`

**Default**: `True`

#### [](#description-110)Description

CBOEnabled specifies whether the cost-based optimizer is enabled. Defaults to true.

### [](#couchbaseclusters-spec-cluster-query-cleanupclientattemptsenabled)couchbaseclusters.spec.cluster.query.cleanupClientAttemptsEnabled

#### [](#constraints-111)Constraints

**Required**

**Type**: `boolean`

**Default**: `True`

#### [](#description-111)Description

CleanupClientAttemptsEnabled specifies whether the Query service preferentially aims to clean up just transactions that it has created, leaving transactions for the distributed cleanup process only when it is forced to. Defaults to true.

### [](#couchbaseclusters-spec-cluster-query-cleanuplostattemptsenabled)couchbaseclusters.spec.cluster.query.cleanupLostAttemptsEnabled

#### [](#constraints-112)Constraints

**Required**

**Type**: `boolean`

**Default**: `True`

#### [](#description-112)Description

CleanupLostAttemptsEnabled specifies the Query service takes part in the distributed cleanup process, and cleans up expired transactions created by any client. Defaults to true.

### [](#couchbaseclusters-spec-cluster-query-cleanupwindow)couchbaseclusters.spec.cluster.query.cleanupWindow

#### [](#constraints-113)Constraints

**Required**

**Type**: `string`

**Default**: `60s`

#### [](#description-113)Description

CleanupWindow specifies how frequently the Query service checks its subset of active transaction records for cleanup. Defaults to 60s.

### [](#couchbaseclusters-spec-cluster-query-completedlimit)couchbaseclusters.spec.cluster.query.completedLimit

#### [](#constraints-114)Constraints

**Required**

**Type**: `integer`

**Default**: `4000`

#### [](#description-114)Description

CompletedLimit sets the number of requests to be logged in the completed requests catalog. As new completed requests are added, old ones are removed.

### [](#couchbaseclusters-spec-cluster-query-completedmaxplansize)couchbaseclusters.spec.cluster.query.completedMaxPlanSize

#### [](#constraints-115)Constraints

**Required**

**Type**: `string`

**Default**: `262144`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-115)Description

CompletedMaxPlanSize limits the size of query execution plans that can be logged in the completed requests catalog. Queries with plans larger than this are not logged. This field is only supported on CB versions 7.6.0+. Defaults to 262144, maximum value is 20840448, and minimum value is 0.

### [](#couchbaseclusters-spec-cluster-query-completedstreamsize)couchbaseclusters.spec.cluster.query.completedStreamSize

#### [](#constraints-116)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-116)Description

CompletedStreamSize controls how much data about completed N1QL queries is saved to disk for analysis. When set to a value greater than 0 (measured in MiB), Couchbase saves information about completed queries to GZIP-compressed files with prefix local\_request\_log. This field is only supported on CB versions 8.0.0+. Defaults to 0 (disabled), minimum value is 0.

### [](#couchbaseclusters-spec-cluster-query-completedthreshold)couchbaseclusters.spec.cluster.query.completedThreshold

#### [](#constraints-117)Constraints

**Type**: `string`

**Default**: `1s`

#### [](#description-117)Description

CompletedThreshold sets the minimum request duration after which requests are added to the completed requests catalog. This field accepts a duration string (e.g. "1s", "500ms") which is converted to milliseconds internally. Valid values are "-1" (disable logging), "0" (log all requests), or a positive duration. The maximum value is 2147483647ms (approximately 24.8 days). This field defaults to 1s.

### [](#couchbaseclusters-spec-cluster-query-completedtrackingallrequests)couchbaseclusters.spec.cluster.query.completedTrackingAllRequests

#### [](#constraints-118)Constraints

**Type**: `boolean`

#### [](#description-118)Description

**DEPRECATED** \- by spec.cluster.query.completedThreshold.

Set completedThreshold to "0" to log all requests. CompletedTrackingAllRequests allows all requests to be tracked regardless of their time. This field requires `completedTrackingEnabled` to be true.

### [](#couchbaseclusters-spec-cluster-query-completedtrackingenabled)couchbaseclusters.spec.cluster.query.completedTrackingEnabled

#### [](#constraints-119)Constraints

**Type**: `boolean`

#### [](#description-119)Description

**DEPRECATED** \- by spec.cluster.query.completedThreshold.

Set completedThreshold to "-1" to disable request tracking. CompletedTrackingEnabled allows completed requests to be tracked in the requests catalog.

### [](#couchbaseclusters-spec-cluster-query-completedtrackingthreshold)couchbaseclusters.spec.cluster.query.completedTrackingThreshold

#### [](#constraints-120)Constraints

**Type**: `string`

#### [](#description-120)Description

**DEPRECATED** \- by spec.cluster.query.completedThreshold.

CompletedTrackingThreshold is a trigger for queries to be logged in the completed requests catalog. All completed queries lasting longer than this threshold are logged in the completed requests catalog. This field requires `completedTrackingEnabled`to be set to true and `completedTrackingAllRequests` to be false to have any effect.

### [](#couchbaseclusters-spec-cluster-query-loglevel)couchbaseclusters.spec.cluster.query.logLevel

#### [](#constraints-121)Constraints

**Type**: `string`

**Default**: `info`

**Enumerations**: `debug, trace, info, warn, error, severe, none`

#### [](#description-121)Description

LogLevel controls the verbosity of query logs. This field must be one of "debug", "trace", "info", "warn", "error", "severe", or "none", defaulting to "info".

### [](#couchbaseclusters-spec-cluster-query-maxparallelism)couchbaseclusters.spec.cluster.query.maxParallelism

#### [](#constraints-122)Constraints

**Required**

**Type**: `integer`

**Default**: `1`

#### [](#description-122)Description

MaxParallelism specifies the maximum parallelism for queries on all Query nodes in the cluster. If the value is zero, negative, or larger than the number of allowed cored the maximum parallelism is restricted to the number of allowed cores. Defaults to 1.

### [](#couchbaseclusters-spec-cluster-query-memoryquota)couchbaseclusters.spec.cluster.query.memoryQuota

#### [](#constraints-123)Constraints

**Type**: `string`

**Default**: `0`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-123)Description

MemoryQuota specifies the maximum amount of memory a request may use on any Query node in the cluster. This parameter enforces a ceiling on the memory used for the tracked documents required for processing a request. It does not take into account any other memory that might be used to process a request, such as the stack, the operators, or some intermediate values. Defaults to 0.

### [](#couchbaseclusters-spec-cluster-query-nodequotavalpercent)couchbaseclusters.spec.cluster.query.nodeQuotaValPercent

#### [](#constraints-124)Constraints

**Required**

**Type**: `integer`

**Default**: `67`

**Minimum**: `0`

**Maximum**: `100`

#### [](#description-124)Description

NodeQuotaValPercent sets the percentage of the `useReplica` that is dedicated to tracked value content memory across all active requests for every Query node in the cluster. This field is only supported on CB versions 7.6.0+. Defaults to 67.

### [](#couchbaseclusters-spec-cluster-query-numactivetransactionrecords)couchbaseclusters.spec.cluster.query.numActiveTransactionRecords

#### [](#constraints-125)Constraints

**Required**

**Type**: `integer`

**Default**: `1024`

**Minimum**: `1`

#### [](#description-125)Description

NumActiveTransactionRecords specifies the total number of active transaction records for all Query nodes in the cluster. Default to 1024 and has a minimum of 1.

### [](#couchbaseclusters-spec-cluster-query-numcpus)couchbaseclusters.spec.cluster.query.numCpus

#### [](#constraints-126)Constraints

**Required**

**Type**: `integer`

**Default**: `0`

**Minimum**: `0`

#### [](#description-126)Description

NumCpus is the number of CPUs the Query service can use on any Query node in the cluster. When set to 0 (the default), the Query service can use all available CPUs, up to the limits described below. The number of CPUs can never be greater than the number of logical CPUs. In Community Edition, the number of allowed CPUs cannot be greater than 4\. In Enterprise Edition, there is no limit to the number of allowed CPUs. This field is only supported on CB versions 7.6.0+. NOTE: This change requires a restart of the Query service to take effect which can be done by rescheduling nodes that are running the query service. Defaults to 0.

### [](#couchbaseclusters-spec-cluster-query-pipelinebatch)couchbaseclusters.spec.cluster.query.pipelineBatch

#### [](#constraints-127)Constraints

**Required**

**Type**: `integer`

**Default**: `16`

#### [](#description-127)Description

PipelineBatch controls the number of items execution operators can batch for Fetch from the KV. Defaults to 16.

### [](#couchbaseclusters-spec-cluster-query-pipelinecap)couchbaseclusters.spec.cluster.query.pipelineCap

#### [](#constraints-128)Constraints

**Required**

**Type**: `integer`

**Default**: `512`

#### [](#description-128)Description

PipelineCap controls the maximum number of items each execution operator can buffer between various operators. Defaults to 512.

### [](#couchbaseclusters-spec-cluster-query-preparedlimit)couchbaseclusters.spec.cluster.query.preparedLimit

#### [](#constraints-129)Constraints

**Required**

**Type**: `integer`

**Default**: `16384`

#### [](#description-129)Description

PreparedLimit is the maximum number of prepared statements in the cache. When this cache reaches the limit, the least recently used prepared statements will be discarded as new prepared statements are created.

### [](#couchbaseclusters-spec-cluster-query-scancap)couchbaseclusters.spec.cluster.query.scanCap

#### [](#constraints-130)Constraints

**Required**

**Type**: `integer`

**Default**: `512`

#### [](#description-130)Description

ScapCan sets the maximum buffered channel size between the indexer client and the query service for index scans. Defaults to 512.

### [](#couchbaseclusters-spec-cluster-query-temporaryspace)couchbaseclusters.spec.cluster.query.temporarySpace

#### [](#constraints-131)Constraints

**Type**: `string`

**Default**: `5Gi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-131)Description

TemporarySpace allows the temporary storage used by the query service backfill, per-pod, to be modified. This field requires `backfillEnabled` to be set to true in order to have any effect. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-cluster-query-temporaryspaceunlimited)couchbaseclusters.spec.cluster.query.temporarySpaceUnlimited

#### [](#constraints-132)Constraints

**Type**: `boolean`

#### [](#description-132)Description

TemporarySpaceUnlimited allows the temporary storage used by the query service backfill, per-pod, to be unconstrained. This field requires `backfillEnabled` to be set to true in order to have any effect. This field overrides `temporarySpace`.

### [](#couchbaseclusters-spec-cluster-query-timeout)couchbaseclusters.spec.cluster.query.timeout

#### [](#constraints-133)Constraints

**Type**: `string`

#### [](#description-133)Description

Timeout is the maximum time to spend on the request before timing out. If this field is not set then there will be no timeout.

### [](#couchbaseclusters-spec-cluster-query-txtimeout)couchbaseclusters.spec.cluster.query.txTimeout

#### [](#constraints-134)Constraints

**Type**: `string`

**Default**: `0ms`

#### [](#description-134)Description

TxTimeout is the maximum time to spend on a transaction before timing out. This setting only applies to requests containing the BEGIN TRANSACTION statement, or to requests where the tximplicit parameter is set. For all other requests, it is ignored. Defaults to 0ms (no timeout).

### [](#couchbaseclusters-spec-cluster-query-usereplica)couchbaseclusters.spec.cluster.query.useReplica

#### [](#constraints-135)Constraints

**Type**: `boolean`

#### [](#description-135)Description

UseReplica specifies whether a query can fetch data from a replica vBucket if active vBuckets are inaccessible. If set to true then read from replica is enabled for all queries, but can be disabled at request level. If set to false read from replica is disabled for all queries and cannot be overridden at request level. If this field is unset then it is enabled/disabled at the request level. This field is only supported on CB versions 7.6.0+.

### [](#couchbaseclusters-spec-cluster-queryservicememoryquota)couchbaseclusters.spec.cluster.queryServiceMemoryQuota

#### [](#constraints-136)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-136)Description

QueryServiceMemQuota is used when the spec.autoResourceAllocation feature is enabled, and is used to define the amount of memory reserved by the query service for use with Kubernetes resource scheduling. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>In CB Server 7.6.0+ QueryServiceMemQuota also sets a soft memory limit for every Query node in the cluster. The garbage collector tries to keep below this target. It is not a hard, absolute limit, and memory usage may exceed this value.

### [](#couchbaseclusters-spec-cluster-searchservicememoryquota)couchbaseclusters.spec.cluster.searchServiceMemoryQuota

#### [](#constraints-137)Constraints

**Type**: `string`

**Default**: `256Mi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-137)Description

SearchServiceMemQuota is the amount of memory that should be allocated to the search service. This value is per-pod, and only applicable to pods belonging to server classes running the search service. This field must be a quantity greater than or equal to 256Mi. This field defaults to 256Mi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-enableonlinevolumeexpansion)couchbaseclusters.spec.enableOnlineVolumeExpansion

#### [](#constraints-138)Constraints

**Type**: `boolean`

#### [](#description-138)Description

EnableOnlineVolumeExpansion enables online expansion of Persistent Volumes. You can only expand a PVC if its storage class’s "allowVolumeExpansion" field is set to true. Additionally, Kubernetes feature "ExpandInUsePersistentVolumes" must be enabled in order to expand the volumes which are actively bound to Pods. Volumes can only be expanded and not reduced to a smaller size. See: <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#resizing-an-in-use-persistentvolumeclaim>

If "EnableOnlineVolumeExpansion" is enabled for use within an environment that does not actually support online volume and file system expansion then the cluster will fallback to rolling upgrade procedure to create a new set of Pods for use with resized Volumes. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes/#expanding-persistent-volumes-claims>.

### [](#couchbaseclusters-spec-enablepreviewscaling)couchbaseclusters.spec.enablePreviewScaling

#### [](#constraints-139)Constraints

**Type**: `boolean`

#### [](#description-139)Description

**DEPRECATED** \- This option only exists for backwards compatibility and no longer restricts autoscaling to ephemeral services.

EnablePreviewScaling enables autoscaling for stateful services and buckets.

### [](#couchbaseclusters-spec-envimageprecedence)couchbaseclusters.spec.envImagePrecedence

#### [](#constraints-140)Constraints

**Type**: `boolean`

#### [](#description-140)Description

EnvImagePrecedence gives precedence over the default container image name in `spec.Image` to an image name provided through Operator environment variables. For more info on using Operator environment variables: <https://docs.couchbase.com/operator/current/reference-operator-configuration.html>.

### [](#couchbaseclusters-spec-hibernate)couchbaseclusters.spec.hibernate

#### [](#constraints-141)Constraints

**Type**: `boolean`

#### [](#description-141)Description

Hibernate is whether to hibernate the cluster.

### [](#couchbaseclusters-spec-hibernationstrategy)couchbaseclusters.spec.hibernationStrategy

#### [](#constraints-142)Constraints

**Type**: `string`

**Enumerations**: `Immediate`

#### [](#description-142)Description

HibernationStrategy defines how to hibernate the cluster. When Immediate the Operator will immediately delete all pods and take no further action until the hibernate field is set to false.

### [](#couchbaseclusters-spec-image)couchbaseclusters.spec.image

#### [](#constraints-143)Constraints

**Required**

**Type**: `string`

**Pattern (Regular Expression)**: `^(.*?(:\d+)?/)?.\*?/.*?(:.\*?\d+\.\d+\.\d+.\*|@sha256:[0-9a-f]{64})$`

#### [](#description-143)Description

Image is the container image name that will be used to launch Couchbase server instances. Updating this field will cause an automatic upgrade of the cluster. Explicitly specifying the image for a server class will override this value for the server class.

### [](#couchbaseclusters-spec-logging)couchbaseclusters.spec.logging

#### [](#constraints-144)Constraints

**Type**: `object`

#### [](#description-144)Description

Logging defines Operator logging options.

### [](#couchbaseclusters-spec-logging-audit)couchbaseclusters.spec.logging.audit

#### [](#constraints-145)Constraints

**Type**: `object`

#### [](#description-145)Description

Used to manage the audit configuration directly.

### [](#couchbaseclusters-spec-logging-audit-disabledevents)couchbaseclusters.spec.logging.audit.disabledEvents

#### [](#constraints-146)Constraints

**Type**: `[]integer`

#### [](#description-146)Description

The list of event ids to disable for auditing purposes. This is passed to the REST API with no verification by the operator. Refer to the documentation for details: <https://docs.couchbase.com/server/current/audit-event-reference/audit-event-reference.html>.

### [](#couchbaseclusters-spec-logging-audit-disabledusers)couchbaseclusters.spec.logging.audit.disabledUsers

#### [](#constraints-147)Constraints

**Type**: `[]string`

**Pattern (Regular Expression)**: `^.+/(local|external)$`

#### [](#description-147)Description

The list of users to ignore for auditing purposes. This is passed to the REST API with minimal validation it meets an acceptable regex pattern. Refer to the documentation for full details on how to configure this: <https://docs.couchbase.com/server/current/manage/manage-security/manage-auditing.html#ignoring-events-by-user>.

### [](#couchbaseclusters-spec-logging-audit-enabled)couchbaseclusters.spec.logging.audit.enabled

#### [](#constraints-148)Constraints

**Type**: `boolean`

#### [](#description-148)Description

Enabled is a boolean that enables the audit capabilities.

### [](#couchbaseclusters-spec-logging-audit-garbagecollection)couchbaseclusters.spec.logging.audit.garbageCollection

#### [](#constraints-149)Constraints

**Type**: `object`

#### [](#description-149)Description

Handle all optional garbage collection (GC) configuration for the audit functionality. This is not part of the audit REST API, it is intended to handle GC automatically for the audit logs. By default the Couchbase Server rotates the audit logs but does not clean up the rotated logs. This is left as an operation for the cluster administrator to manage, the operator allows for us to automate this: <https://docs.couchbase.com/server/current/manage/manage-security/manage-auditing.html>.

### [](#couchbaseclusters-spec-logging-audit-garbagecollection-sidecar)couchbaseclusters.spec.logging.audit.garbageCollection.sidecar

#### [](#constraints-150)Constraints

**Type**: `object`

#### [](#description-150)Description

**DEPRECATED** \- by spec.logging.audit.rotation for Couchbase Server 7.2.4+ Provide the sidecar configuration required (if so desired) to automatically clean up audit logs.

### [](#couchbaseclusters-spec-logging-audit-garbagecollection-sidecar-age)couchbaseclusters.spec.logging.audit.garbageCollection.sidecar.age

#### [](#constraints-151)Constraints

**Type**: `string`

**Default**: `1h`

#### [](#description-151)Description

The minimum age of rotated log files to remove, defaults to one hour.

### [](#couchbaseclusters-spec-logging-audit-garbagecollection-sidecar-enabled)couchbaseclusters.spec.logging.audit.garbageCollection.sidecar.enabled

#### [](#constraints-152)Constraints

**Type**: `boolean`

#### [](#description-152)Description

Enable this sidecar by setting to true, defaults to being disabled.

### [](#couchbaseclusters-spec-logging-audit-garbagecollection-sidecar-image)couchbaseclusters.spec.logging.audit.garbageCollection.sidecar.image

#### [](#constraints-153)Constraints

**Type**: `string`

**Default**: `busybox:1.33.1`

#### [](#description-153)Description

Image is the image to be used to run the audit sidecar helper. No validation is carried out as this can be any arbitrary repo and tag.

### [](#couchbaseclusters-spec-logging-audit-garbagecollection-sidecar-interval)couchbaseclusters.spec.logging.audit.garbageCollection.sidecar.interval

#### [](#constraints-154)Constraints

**Type**: `string`

**Default**: `20m`

#### [](#description-154)Description

The interval at which to check for rotated log files to remove, defaults to 20 minutes.

### [](#couchbaseclusters-spec-logging-audit-garbagecollection-sidecar-resources)couchbaseclusters.spec.logging.audit.garbageCollection.sidecar.resources

#### [](#constraints-155)Constraints

**Type**: `object`

#### [](#description-155)Description

Resources is the resource requirements for the cleanup container. Will be populated by Kubernetes defaults if not specified.

### [](#couchbaseclusters-spec-logging-audit-rotation)couchbaseclusters.spec.logging.audit.rotation

#### [](#constraints-156)Constraints

**Type**: `object`

#### [](#description-156)Description

The interval to optionally rotate the audit log. This is passed to the REST API, see here for details: <https://docs.couchbase.com/server/current/manage/manage-security/manage-auditing.html>.

### [](#couchbaseclusters-spec-logging-audit-rotation-interval)couchbaseclusters.spec.logging.audit.rotation.interval

#### [](#constraints-157)Constraints

**Type**: `string`

**Default**: `15m`

#### [](#description-157)Description

The interval at which to rotate log files, defaults to 15 minutes.

### [](#couchbaseclusters-spec-logging-audit-rotation-pruneage)couchbaseclusters.spec.logging.audit.rotation.pruneAge

#### [](#constraints-158)Constraints

**Type**: `string`

**Default**: `0`

#### [](#description-158)Description

How long Couchbase Server keeps rotated audit logs. If set to 0 (the default) then audit logs won’t be pruned. Has a maximum of 35791394 seconds.

### [](#couchbaseclusters-spec-logging-audit-rotation-size)couchbaseclusters.spec.logging.audit.rotation.size

#### [](#constraints-159)Constraints

**Type**: `string`

**Default**: `20Mi`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-159)Description

Size allows the specification of a rotation size for the log, defaults to 20Mi. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-spec-logging-logretentioncount)couchbaseclusters.spec.logging.logRetentionCount

#### [](#constraints-160)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-160)Description

LogRetentionCount gives the number of persistent log PVCs to keep.

### [](#couchbaseclusters-spec-logging-logretentiontime)couchbaseclusters.spec.logging.logRetentionTime

#### [](#constraints-161)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^\d+(ns|us|ms|s|m|h)$`

#### [](#description-161)Description

LogRetentionTime gives the time to keep persistent log PVCs alive for.

### [](#couchbaseclusters-spec-logging-server)couchbaseclusters.spec.logging.server

#### [](#constraints-162)Constraints

**Type**: `object`

#### [](#description-162)Description

Specification of all logging configuration required to manage the sidecar containers in each pod.

### [](#couchbaseclusters-spec-logging-server-configurationname)couchbaseclusters.spec.logging.server.configurationName

#### [](#constraints-163)Constraints

**Type**: `string`

**Default**: `fluent-bit-config`

#### [](#description-163)Description

ConfigurationName is the name of the Secret to use holding the logging configuration in the namespace. A Secret is used to ensure we can safely store credentials but this can be populated from plaintext if acceptable too. If it does not exist then one will be created with defaults in the namespace so it can be easily updated whilst running. Note that if running multiple clusters in the same kubernetes namespace then you should use a separate Secret for each, otherwise the first cluster will take ownership (if created) and the Secret will be cleaned up when that cluster is removed. If running clusters in separate namespaces then they will be separate Secrets anyway.

### [](#couchbaseclusters-spec-logging-server-enabled)couchbaseclusters.spec.logging.server.enabled

#### [](#constraints-164)Constraints

**Type**: `boolean`

#### [](#description-164)Description

Enabled is a boolean that enables the logging sidecar container.

### [](#couchbaseclusters-spec-logging-server-manageconfiguration)couchbaseclusters.spec.logging.server.manageConfiguration

#### [](#constraints-165)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-165)Description

A boolean which indicates whether the operator should manage the configuration or not. If omitted then this defaults to true which means the operator will attempt to reconcile it to default values. To use a custom configuration make sure to set this to false. Note that the ownership of any Secret is not changed so if a Secret is created externally it can be updated by the operator but it’s ownership stays the same so it will be cleaned up when it’s owner is.

### [](#couchbaseclusters-spec-logging-server-sidecar)couchbaseclusters.spec.logging.server.sidecar

#### [](#constraints-166)Constraints

**Type**: `object`

**Default**: `{}`

#### [](#description-166)Description

Any specific logging sidecar container configuration.

### [](#couchbaseclusters-spec-logging-server-sidecar-configurationmountpath)couchbaseclusters.spec.logging.server.sidecar.configurationMountPath

#### [](#constraints-167)Constraints

**Type**: `string`

**Default**: `/fluent-bit/config/`

#### [](#description-167)Description

ConfigurationMountPath is the location to mount the ConfigurationName Secret into the image. If another log shipping image is used that needs a different mount then modify this. Note that the configuration file must be called 'fluent-bit.conf' at the root of this path, there is no provision for overriding the name of the config file passed as the COUCHBASE\_LOGS\_CONFIG\_FILE environment variable.

### [](#couchbaseclusters-spec-logging-server-sidecar-image)couchbaseclusters.spec.logging.server.sidecar.image

#### [](#constraints-168)Constraints

**Type**: `string`

**Default**: `couchbase/fluent-bit:1.2.9`

#### [](#description-168)Description

Image is the image to be used to deal with logging as a sidecar. No validation is carried out as this can be any arbitrary repo and tag. It will default to the latest supported version of Fluent Bit.

### [](#couchbaseclusters-spec-logging-server-sidecar-resources)couchbaseclusters.spec.logging.server.sidecar.resources

#### [](#constraints-169)Constraints

**Type**: `object`

#### [](#description-169)Description

Resources is the resource requirements for the sidecar container. Will be populated by Kubernetes defaults if not specified.

### [](#couchbaseclusters-spec-logging-server-sidecar-tls)couchbaseclusters.spec.logging.server.sidecar.tls

#### [](#constraints-170)Constraints

**Type**: `object`

#### [](#description-170)Description

TLS configures mounting kubernetes TLS secrets into the logging sidecar. The operator will (in a later release) mount each secret under <mountPath>/<secretName>/ and the files within the secret will retain their keys as filenames. This field is accepted by the CRD but not currently implemented. Functionality (mounting) is planned for Operator version 2.9.1.

### [](#couchbaseclusters-spec-logging-server-sidecar-tls-mountpath)couchbaseclusters.spec.logging.server.sidecar.tls.mountPath

#### [](#constraints-171)Constraints

**Type**: `string`

**Default**: `/fluent-bit/certs/`

#### [](#description-171)Description

MountPath is the parent directory into which each secret will be mounted as a sub-directory named after the secret. For example, a secret named `fluent-bit-ca` mounted with MountPath `/fluent-bit/certs/` will expose files under `/fluent-bit/certs/fluent-bit-ca/`.

### [](#couchbaseclusters-spec-logging-server-sidecar-tls-secretnames)couchbaseclusters.spec.logging.server.sidecar.tls.secretNames

#### [](#constraints-172)Constraints

**Type**: `[]string`

#### [](#description-172)Description

SecretNames is the list of Kubernetes Secret names (typically of type kubernetes.io/tls) to mount into the sidecar. Filenames inside each mounted directory will match the keys in the Secret’s data map.

### [](#couchbaseclusters-spec-migration)couchbaseclusters.spec.migration

#### [](#constraints-173)Constraints

**Type**: `object`

#### [](#description-173)Description

Migration defines the specification for a CouchbaseCluster assimilation of an unmanaged cluster to a managed Kubernetes cluster.

### [](#couchbaseclusters-spec-migration-maxconcurrentmigrations)couchbaseclusters.spec.migration.maxConcurrentMigrations

#### [](#constraints-174)Constraints

**Type**: `integer`

**Default**: `1`

**Minimum**: `1`

#### [](#description-174)Description

MaxConcurrentMigrations is the maximum number of nodes migrations the operator will run concurrently.

### [](#couchbaseclusters-spec-migration-migrationorderoverride)couchbaseclusters.spec.migration.migrationOrderOverride

#### [](#constraints-175)Constraints

**Type**: `object`

#### [](#description-175)Description

MigrationOrderOverride defines the strategy for migration order. If not set then the operator will choose nodes at random.

### [](#couchbaseclusters-spec-migration-migrationorderoverride-migrationorderoverridestrategy)couchbaseclusters.spec.migration.migrationOrderOverride.migrationOrderOverrideStrategy

#### [](#constraints-176)Constraints

**Type**: `string`

**Enumerations**: `ByServerGroup, ByServerClass, ByNode`

#### [](#description-176)Description

MigrationOrderOverrideStrategy defines the strategy for migration order. When not set, the operator will choose nodes at random. When ByServerGroup is set, the operator will migrate nodes in the order of the server groups defined in spec.migration.migrationOrderOverride.serverGroupOrder. If spec.migration.migrationOrderOverride.serverGroupOrder is not set, the operator will migrate the server groups in alphabetical order. When ByServerClass is set, the operator will migrate nodes in the order of the server classes defined in spec.migration.migrationOrderOverride.serverClassOrder. If spec.migration.migrationOrderOverride.serverClassOrder is not set, the operator will migrate the server classes in the order of the server classes defined in spec.servers. When ByNode is set, the operator will migrate nodes in the order of the nodes defined in spec.migration.migrationOrderOverride.nodeOrder. If spec.migration.migrationOrderOverride.nodeOrder is not set, the operator will migrate the nodes in alphabetical order.

### [](#couchbaseclusters-spec-migration-migrationorderoverride-nodeorder)couchbaseclusters.spec.migration.migrationOrderOverride.nodeOrder

#### [](#constraints-177)Constraints

**Type**: `[]string`

#### [](#description-177)Description

NodeOrder defines the order of nodes for migration.

### [](#couchbaseclusters-spec-migration-migrationorderoverride-serverclassorder)couchbaseclusters.spec.migration.migrationOrderOverride.serverClassOrder

#### [](#constraints-178)Constraints

**Type**: `[]string`

#### [](#description-178)Description

ServerClassOrder defines the order of server classes for migration.

### [](#couchbaseclusters-spec-migration-migrationorderoverride-servergrouporder)couchbaseclusters.spec.migration.migrationOrderOverride.serverGroupOrder

#### [](#constraints-179)Constraints

**Type**: `[]string`

#### [](#description-179)Description

ServerGroupOrder defines the order of server groups for migration.

### [](#couchbaseclusters-spec-migration-numunmanagednodes)couchbaseclusters.spec.migration.numUnmanagedNodes

#### [](#constraints-180)Constraints

**Type**: `integer`

#### [](#description-180)Description

NumUnmanagedNodes is the number of nodes the operator will leave in the cluster unmigrated. This is useful for controlling how much of the cluster to migrate over at a time. If not specified the operator will migrate all nodes. e.g. if the unmanaged cluster has 10 nodes and NumUnmanagedNodes is set to 2, then the operator will migrate 8 nodes to Kubernetes and leave 2 nodes.

### [](#couchbaseclusters-spec-migration-stabilizationperiod)couchbaseclusters.spec.migration.stabilizationPeriod

#### [](#constraints-181)Constraints

**Type**: `string`

#### [](#description-181)Description

StabilizationPeriod is the time the operator will wait after a migration before starting the next migration. If not specified the operator will start the next migration immediately.

### [](#couchbaseclusters-spec-migration-unmanagedclusterhost)couchbaseclusters.spec.migration.unmanagedClusterHost

#### [](#constraints-182)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^((([a-zA-Z0-9](-?[a-zA-Z0-9])\*)\.)+[a-zA-Z]{2,})|((25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})\.){3}(25[0-5]|2[0-4][0-9]|[0-1]?[0-9]{1,2})|(([0-9A-Fa-f]{1,4}:){1,7}[0-9A-Fa-f]{1,4})$`

#### [](#description-182)Description

UnmanagedClusterHost is a host of the unmanaged Couchbase cluster to be migrated. This is the host that the operator will connect to to start the migration process.

### [](#couchbaseclusters-spec-mirwatchdog)couchbaseclusters.spec.mirWatchdog

#### [](#constraints-183)Constraints

**Type**: `object`

#### [](#description-183)Description

MirWatchdog runs a series of out-of-band checks on the cluster outside the reconciliation loop to detect conditions that require manual intervention by a user. These checks include but are not limited to cluster login authentication failures, multiple consecutive rebalance failures, down nodes that cannot be recovered, and TLS certificate expiration. When enabled, if the operator detects that manual intervention is needed in order to continue to reconcile the cluster, it will add a cluster condition, emit a Kubernetes Event, and increment a gauge metric to support external alerting. Once the operator determines that manual intervention is no longer needed, it will clear the cluster condition, emit a Kubernetes Event, and decrement the gauge metric. By default this is disabled. DEVELOPER\_PREVIEW: This feature is in developer preview and should not be used in production clusters.

### [](#couchbaseclusters-spec-mirwatchdog-enabled)couchbaseclusters.spec.mirWatchdog.enabled

#### [](#constraints-184)Constraints

**Type**: `boolean`

#### [](#description-184)Description

Enabled controls whether the additional out-of-band checks are enabled for the cluster. This defaults to false. DEVELOPER\_PREVIEW: This feature is in developer preview and should not be used in production clusters.

### [](#couchbaseclusters-spec-mirwatchdog-interval)couchbaseclusters.spec.mirWatchdog.interval

#### [](#constraints-185)Constraints

**Type**: `string`

#### [](#description-185)Description

Interval controls the interval at which the additional out-of-band checks will be performed. The default interval is 20 seconds. DEVELOPER\_PREVIEW: This feature is in developer preview and should not be used in production clusters.

### [](#couchbaseclusters-spec-mirwatchdog-skipreconciliation)couchbaseclusters.spec.mirWatchdog.skipReconciliation

#### [](#constraints-186)Constraints

**Type**: `boolean`

#### [](#description-186)Description

SkipReconciliation controls whether the operator will skip reconciliation when we are in the ManualInterventionRequired state and this condition is set. Once we leave the state the operator will resume reconciliation. This defaults to false and should only be used when additional alerting is in place. DEVELOPER\_PREVIEW: This feature is in developer preview and should not be used in production clusters.

### [](#couchbaseclusters-spec-monitoring)couchbaseclusters.spec.monitoring

#### [](#constraints-187)Constraints

**Type**: `object`

#### [](#description-187)Description

**DEPRECATED** \- By Couchbase Server metrics endpoint on version 7.0+ Monitoring defines any Operator managed integration into 3rd party monitoring infrastructure.

### [](#couchbaseclusters-spec-monitoring-prometheus)couchbaseclusters.spec.monitoring.prometheus

#### [](#constraints-188)Constraints

**Type**: `object`

#### [](#description-188)Description

**DEPRECATED** \- By Couchbase Server metrics endpoint on version 7.0+ Prometheus provides integration with Prometheus monitoring.

### [](#couchbaseclusters-spec-monitoring-prometheus-authorizationsecret)couchbaseclusters.spec.monitoring.prometheus.authorizationSecret

#### [](#constraints-189)Constraints

**Type**: `string`

#### [](#description-189)Description

AuthorizationSecret is the name of a Kubernetes secret that contains a bearer token to authorize GET requests to the metrics endpoint.

### [](#couchbaseclusters-spec-monitoring-prometheus-enabled)couchbaseclusters.spec.monitoring.prometheus.enabled

#### [](#constraints-190)Constraints

**Type**: `boolean`

#### [](#description-190)Description

Enabled is a boolean that enables/disables the metrics sidecar container. This must be set to true, when image is provided.

### [](#couchbaseclusters-spec-monitoring-prometheus-image)couchbaseclusters.spec.monitoring.prometheus.image

#### [](#constraints-191)Constraints

**Required**

**Type**: `string`

#### [](#description-191)Description

Image is the metrics image to be used to collect metrics. No validation is carried out as this can be any arbitrary repo and tag. enabled must be set to true, when image is provided.

### [](#couchbaseclusters-spec-monitoring-prometheus-refreshrate)couchbaseclusters.spec.monitoring.prometheus.refreshRate

#### [](#constraints-192)Constraints

**Type**: `integer`

**Default**: `60`

**Minimum**: `1`

**Maximum**: `600`

#### [](#description-192)Description

RefreshRate is the frequency in which cached statistics are updated in seconds. Shorter intervals will add additional resource overhead to clusters running Couchbase Server 7.0+ Default is 60 seconds, Maximum value is 600 seconds, and minimum value is 1 second.

### [](#couchbaseclusters-spec-monitoring-prometheus-resources)couchbaseclusters.spec.monitoring.prometheus.resources

#### [](#constraints-193)Constraints

**Type**: `object`

#### [](#description-193)Description

Resources is the resource requirements for the metrics container. Will be populated by Kubernetes defaults if not specified.

### [](#couchbaseclusters-spec-networking)couchbaseclusters.spec.networking

#### [](#constraints-194)Constraints

**Type**: `object`

#### [](#description-194)Description

Networking defines Couchbase cluster networking options such as network topology, TLS and DDNS settings.

### [](#couchbaseclusters-spec-networking-addressfamily)couchbaseclusters.spec.networking.addressFamily

#### [](#constraints-195)Constraints

**Type**: `string`

**Enumerations**: `IPv4, IPv6, IPv4Priority, IPv6Priority, IPv6Only, IPv4Only`

#### [](#description-195)Description

AddressFamily allows the manual selection of the address family to use. Setting this field to either IPv4Only or IPv6Only will exclusively use that address family. Setting this field to IPv4Priority or IPv6Priority will allow dual stack networking with the given address family being prioritised. When this field is not set, Couchbase server will default to using IPv4 for internal communication and also support IPv6 on dual stack systems. This is only supported in Couchbase Server 7.0.2+.

### [](#couchbaseclusters-spec-networking-adminconsoleservicetemplate)couchbaseclusters.spec.networking.adminConsoleServiceTemplate

#### [](#constraints-196)Constraints

**Type**: `object`

#### [](#description-196)Description

AdminConsoleServiceTemplate provides a template used by the Operator to create and manage the admin console service. This allows services to be annotated, the service type defined and any other options that Kubernetes provides. When using a LoadBalancer service type, TLS and dynamic DNS must also be enabled. The Operator reserves the right to modify or replace any field. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#service-v1-core>.

### [](#couchbaseclusters-spec-networking-adminconsoleservicetype)couchbaseclusters.spec.networking.adminConsoleServiceType

#### [](#constraints-197)Constraints

**Type**: `string`

**Default**: `NodePort`

**Enumerations**: `NodePort, LoadBalancer`

#### [](#description-197)Description

**DEPRECATED** \- by adminConsoleServiceTemplate.

AdminConsoleServiceType defines whether to create a node port or load balancer service. When using a LoadBalancer service type, TLS and dynamic DNS must also be enabled. This field must be one of "NodePort" or "LoadBalancer", defaulting to "NodePort".

### [](#couchbaseclusters-spec-networking-adminconsoleservices)couchbaseclusters.spec.networking.adminConsoleServices

#### [](#constraints-198)Constraints

**Type**: `[]string`

**Enumerations**: `admin, data, index, query, search, eventing, analytics`

#### [](#description-198)Description

**DEPRECATED** \- not required by Couchbase Server.

AdminConsoleServices is a selector to choose specific services to expose via the admin console. This field may contain any of "data", "index", "query", "search", "eventing" and "analytics". Each service may only be included once.

### [](#couchbaseclusters-spec-networking-allowexternallyunreachablepods)couchbaseclusters.spec.networking.allowExternallyUnreachablePods

#### [](#constraints-199)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-199)Description

AllowExternallyUnreachablePods is used to allow new pods to be rebalanced into the cluster regardless of whether the external DNS is reachable or not. If this is set to true, pods for which the DNS has not yet propagated will be balanced into the cluster and marked as ready once the WaitForAddressReachableDelay has elapsed. The external DNS will continue to be checked for reachability during each reconciliation loop and the couchbase node will not have it’s alternate addresses updated until it is reachable.

### [](#couchbaseclusters-spec-networking-cloudnativegateway)couchbaseclusters.spec.networking.cloudNativeGateway

#### [](#constraints-200)Constraints

**Type**: `object`

#### [](#description-200)Description

CloudNativeGateway is used to provision a gRPC gateway proxying a Couchbase cluster.

### [](#couchbaseclusters-spec-networking-cloudnativegateway-image)couchbaseclusters.spec.networking.cloudNativeGateway.image

#### [](#constraints-201)Constraints

**Required**

**Type**: `string`

#### [](#description-201)Description

Image is the Cloud Native Gateway image to be used to run the sidecar container. No validation is carried out as this can be any arbitrary repo and tag.

### [](#couchbaseclusters-spec-networking-cloudnativegateway-loglevel)couchbaseclusters.spec.networking.cloudNativeGateway.logLevel

#### [](#constraints-202)Constraints

**Required**

**Type**: `string`

**Default**: `info`

**Enumerations**: `fatal, panic, dpanic, error, warn, info, debug`

#### [](#description-202)Description

**DEVELOPER PREVIEW** \- This feature is in developer preview.

LogLevel controls the verbosity of cloud native logs. This field must be one of "fatal", "panic", "dpanic", "error", "warn", "info", "debug" defaulting to "info".

### [](#couchbaseclusters-spec-networking-cloudnativegateway-servicetemplate)couchbaseclusters.spec.networking.cloudNativeGateway.serviceTemplate

#### [](#constraints-203)Constraints

**Type**: `object`

#### [](#description-203)Description

ServiceTemplate can be used to provice a template used by the Operator when creating the CNG service. This allows services to be annotated, the service type defined and any other options that Kubernetes provides. The Operator reserves the right to modify or replace any field. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#service-v1-core>.

### [](#couchbaseclusters-spec-networking-cloudnativegateway-terminationgraceperiodseconds)couchbaseclusters.spec.networking.cloudNativeGateway.terminationGracePeriodSeconds

#### [](#constraints-204)Constraints

**Type**: `integer`

**Default**: `75`

#### [](#description-204)Description

TerminationGracePeriodSeconds specifies the grace period for the container to terminate. Defaults to 75 seconds.

### [](#couchbaseclusters-spec-networking-cloudnativegateway-tls)couchbaseclusters.spec.networking.cloudNativeGateway.tls

#### [](#constraints-205)Constraints

**Type**: `object`

#### [](#description-205)Description

TLS defines the TLS configuration for the Cloud Native Gateway server including server and client certificate configuration, and TLS security policies. If no TLS config are explicitly provided, the operator generates/manages self-signed certs/keys and creates a k8s secret named `couchbase-cloud-native-gateway-self-signed-secret-<cluster-name>`unique to a Couchbase cluster, which is volume mounted to the cb k8s pod. This action could be overidden at the outset or later, by using the below TLS config or generating the secret of same name as `couchbase-cloud-native-gateway-self-signed-secret-<cluster-name>` with certificates conforming to the keys of well-known type "kubernetes.io/tls" with "tls.crt" and "tls.key". N.B. The secret is on per cluster basis so it’s advised to use the unique cluster name else would be ignored.

### [](#couchbaseclusters-spec-networking-cloudnativegateway-tls-serversecretname)couchbaseclusters.spec.networking.cloudNativeGateway.tls.serverSecretName

#### [](#constraints-206)Constraints

**Type**: `string`

#### [](#description-206)Description

ServerSecretName specifies the secret name, in the same namespace as the cluster, that contains Cloud Native Gateway gRPC server TLS data. The secret is expected to contain "tls.crt" and "tls.key" as per the kubernetes.io/tls secret type.

### [](#couchbaseclusters-spec-networking-disableuioverhttp)couchbaseclusters.spec.networking.disableUIOverHTTP

#### [](#constraints-207)Constraints

**Type**: `boolean`

#### [](#description-207)Description

DisableUIOverHTTP is used to explicitly enable and disable UI access over the HTTP protocol. If not specified, this field defaults to false.

### [](#couchbaseclusters-spec-networking-disableuioverhttps)couchbaseclusters.spec.networking.disableUIOverHTTPS

#### [](#constraints-208)Constraints

**Type**: `boolean`

#### [](#description-208)Description

DisableUIOverHTTPS is used to explicitly enable and disable UI access over the HTTPS protocol. If not specified, this field defaults to false.

### [](#couchbaseclusters-spec-networking-dns)couchbaseclusters.spec.networking.dns

#### [](#constraints-209)Constraints

**Type**: `object`

#### [](#description-209)Description

DNS defines information required for Dynamic DNS support.

### [](#couchbaseclusters-spec-networking-dns-domain)couchbaseclusters.spec.networking.dns.domain

#### [](#constraints-210)Constraints

**Type**: `string`

#### [](#description-210)Description

Domain is the domain to create pods in. When populated the Operator will annotate the admin console and per-pod services with the key "external-dns.alpha.kubernetes.io/hostname". These annotations can be used directly by a Kubernetes External-DNS controller to replicate load balancer service IP addresses into a public DNS server.

### [](#couchbaseclusters-spec-networking-exposeadminconsole)couchbaseclusters.spec.networking.exposeAdminConsole

#### [](#constraints-211)Constraints

**Type**: `boolean`

#### [](#description-211)Description

ExposeAdminConsole creates a service referencing the admin console. The service is configured by the adminConsoleServiceTemplate field.

### [](#couchbaseclusters-spec-networking-exposedfeatureservicetemplate)couchbaseclusters.spec.networking.exposedFeatureServiceTemplate

#### [](#constraints-212)Constraints

**Type**: `object`

#### [](#description-212)Description

ExposedFeatureServiceTemplate provides a template used by the Operator to create and manage per-pod services. This allows services to be annotated, the service type defined and any other options that Kubernetes provides. When using a LoadBalancer service type, TLS and dynamic DNS must also be enabled. The Operator reserves the right to modify or replace any field. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#service-v1-core>.

### [](#couchbaseclusters-spec-networking-exposedfeatureservicetype)couchbaseclusters.spec.networking.exposedFeatureServiceType

#### [](#constraints-213)Constraints

**Type**: `string`

**Default**: `NodePort`

**Enumerations**: `NodePort, LoadBalancer`

#### [](#description-213)Description

**DEPRECATED** \- by exposedFeatureServiceTemplate.

ExposedFeatureServiceType defines whether to create a node port or load balancer service. When using a LoadBalancer service type, TLS and dynamic DNS must also be enabled. This field must be one of "NodePort" or "LoadBalancer", defaulting to "NodePort".

### [](#couchbaseclusters-spec-networking-exposedfeaturetrafficpolicy)couchbaseclusters.spec.networking.exposedFeatureTrafficPolicy

#### [](#constraints-214)Constraints

**Type**: `string`

**Enumerations**: `Cluster, Local`

#### [](#description-214)Description

**DEPRECATED** \- by exposedFeatureServiceTemplate.

ExposedFeatureTrafficPolicy defines how packets should be routed from a load balancer service to a Couchbase pod. When local, traffic is routed directly to the pod. When cluster, traffic is routed to any node, then forwarded on. While cluster routing may be slower, there are some situations where it is required for connectivity. This field must be either "Cluster" or "Local", defaulting to "Local",.

### [](#couchbaseclusters-spec-networking-exposedfeatures)couchbaseclusters.spec.networking.exposedFeatures

#### [](#constraints-215)Constraints

**Type**: `[]string`

**Enumerations**: `admin, xdcr, client, backup, external-cluster-connection`

#### [](#description-215)Description

ExposedFeatures is a list of Couchbase features to expose when using a networking model that exposes the Couchbase cluster externally to Kubernetes. This field also triggers the creation of per-pod services used by clients to connect to the Couchbase cluster. When admin, only the administrator port is exposed, allowing remote administration. When xdcr, only the services required for remote replication are exposed. The xdcr feature is only required when the cluster is the destination of an XDCR replication. When client, all services are exposed as required for client SDK operation. This field may contain any of "admin", "xdcr" and "client". Each feature may only be included once.

### [](#couchbaseclusters-spec-networking-improvedhostnetwork)couchbaseclusters.spec.networking.improvedHostNetwork

#### [](#constraints-216)Constraints

**Type**: `boolean`

#### [](#description-216)Description

ImprovedHostNetwork is used to set the alternate address of the pod to the node name.

### [](#couchbaseclusters-spec-networking-initpodswithnodehostname)couchbaseclusters.spec.networking.initPodsWithNodeHostname

#### [](#constraints-217)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-217)Description

InitPodsWithNodeHostname is used to set the hostname of the pod to the node name.

### [](#couchbaseclusters-spec-networking-loadbalancersourceranges)couchbaseclusters.spec.networking.loadBalancerSourceRanges

#### [](#constraints-218)Constraints

**Type**: `[]string`

**Pattern (Regular Expression)**: `^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}/\d{1,2}$`

#### [](#description-218)Description

**DEPRECATED** \- by adminConsoleServiceTemplate and exposedFeatureServiceTemplate.

LoadBalancerSourceRanges applies only when an exposed service is of type LoadBalancer and limits the source IP ranges that are allowed to use the service. Items must use IPv4 class-less interdomain routing (CIDR) notation e.g. 10.0.0.0/16.

### [](#couchbaseclusters-spec-networking-networkplatform)couchbaseclusters.spec.networking.networkPlatform

#### [](#constraints-219)Constraints

**Type**: `string`

**Enumerations**: `Istio`

#### [](#description-219)Description

NetworkPlatform is used to enable support for various networking technologies. This field must be one of "Istio".

### [](#couchbaseclusters-spec-networking-serviceannotations)couchbaseclusters.spec.networking.serviceAnnotations

#### [](#constraints-220)Constraints

**Type**: `map[string]string`

#### [](#description-220)Description

**DEPRECATED** \- by adminConsoleServiceTemplate and exposedFeatureServiceTemplate.

ServiceAnnotations allows services to be annotated with custom labels. Operator annotations are merged on top of these so have precedence as they are required for correct operation.

### [](#couchbaseclusters-spec-networking-tls)couchbaseclusters.spec.networking.tls

#### [](#constraints-221)Constraints

**Type**: `object`

#### [](#description-221)Description

TLS defines the TLS configuration for the cluster including server and client certificate configuration, and TLS security policies.

### [](#couchbaseclusters-spec-networking-tls-allowplaintextcertreload)couchbaseclusters.spec.networking.tls.allowPlainTextCertReload

#### [](#constraints-222)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-222)Description

AllowPlainTextCertReload allows the reload of TLS certificates in plain text. This option should only be enabled as a means to recover connectivity with server in the event that any of the server certificates expire. When enabled the Operator only attempts plain text cert reloading when expired certificates are detected.

### [](#couchbaseclusters-spec-networking-tls-ciphersuites)couchbaseclusters.spec.networking.tls.cipherSuites

#### [](#constraints-223)Constraints

**Type**: `[]string`

#### [](#description-223)Description

CipherSuites specifies a list of cipher suites for Couchbase server to select from when negotiating TLS handshakes with a client. Suites are not validated by the Operator. Run "openssl ciphers -v" in a Couchbase server pod to interrogate supported values.

### [](#couchbaseclusters-spec-networking-tls-clientcertificatepaths)couchbaseclusters.spec.networking.tls.clientCertificatePaths

#### [](#constraints-224)Constraints

**Type**: `[]object`

#### [](#description-224)Description

ClientCertificatePaths defines where to look in client certificates in order to extract the user name.

### [](#couchbaseclusters-spec-networking-tls-clientcertificatepaths-delimiter)couchbaseclusters.spec.networking.tls.clientCertificatePaths.delimiter

#### [](#constraints-225)Constraints

**Type**: `string`

#### [](#description-225)Description

Delimiter if specified allows a suffix to be stripped from the username, once extracted from the certificate path.

### [](#couchbaseclusters-spec-networking-tls-clientcertificatepaths-path)couchbaseclusters.spec.networking.tls.clientCertificatePaths.path

#### [](#constraints-226)Constraints

**Required**

**Type**: `string`

**Pattern (Regular Expression)**: `^subject\.cn|san\.uri|san\.dnsname|san\.email$`

#### [](#description-226)Description

Path defines where in the X.509 specification to extract the username from. This field must be either "subject.cn", "san.uri", "san.dnsname" or "san.email".

### [](#couchbaseclusters-spec-networking-tls-clientcertificatepaths-prefix)couchbaseclusters.spec.networking.tls.clientCertificatePaths.prefix

#### [](#constraints-227)Constraints

**Type**: `string`

#### [](#description-227)Description

Prefix allows a prefix to be stripped from the username, once extracted from the certificate path.

### [](#couchbaseclusters-spec-networking-tls-clientcertificatepolicy)couchbaseclusters.spec.networking.tls.clientCertificatePolicy

#### [](#constraints-228)Constraints

**Type**: `string`

**Enumerations**: `enable, mandatory`

#### [](#description-228)Description

ClientCertificatePolicy defines the client authentication policy to use. If set, the Operator expects TLS configuration to contain a valid certificate/key pair for the Administrator account.

### [](#couchbaseclusters-spec-networking-tls-nodetonodeencryption)couchbaseclusters.spec.networking.tls.nodeToNodeEncryption

#### [](#constraints-229)Constraints

**Type**: `string`

**Enumerations**: `ControlPlaneOnly, All, Strict`

#### [](#description-229)Description

NodeToNodeEncryption specifies whether to encrypt data between Couchbase nodes within the same cluster. This may come at the expense of performance. When control plane only encryption is used, only cluster management traffic is encrypted between nodes. When all, all traffic is encrypted, including database documents. When strict mode is used, it is the same as all, but also disables all plaintext ports. Strict mode is only available on Couchbase Server versions 7.1 and greater. Node to node encryption can only be used when TLS certificates are managed by the Operator. This field must be either "ControlPlaneOnly", "All", or "Strict".

### [](#couchbaseclusters-spec-networking-tls-passphrase)couchbaseclusters.spec.networking.tls.passphrase

#### [](#constraints-230)Constraints

**Type**: `object`

#### [](#description-230)Description

PassphraseConfig configures the passphrase key to use with encrypted certificates. The passphrase may be registered with Couchbase Server using a local script or a rest endpoint. Private key encryption is only available on Couchbase Server versions 7.1 and greater.

### [](#couchbaseclusters-spec-networking-tls-passphrase-rest)couchbaseclusters.spec.networking.tls.passphrase.rest

#### [](#constraints-231)Constraints

**Type**: `object`

#### [](#description-231)Description

PassphraseRestConfig is the configuration to register a private key passphrase with a rest endpoint. When the private key is accessed, Couchbase Server attempts to extract the password by means of the specified endpoint. The response status must be 200 and the response text must be the exact passphrase excluding newlines and extraneous spaces.

### [](#couchbaseclusters-spec-networking-tls-passphrase-rest-addressfamily)couchbaseclusters.spec.networking.tls.passphrase.rest.addressFamily

#### [](#constraints-232)Constraints

**Type**: `string`

**Default**: `inet`

**Enumerations**: `inet, inet6`

#### [](#description-232)Description

AddressFamily is the address family to use. By default inet (meaning IPV4) is used.

### [](#couchbaseclusters-spec-networking-tls-passphrase-rest-headers)couchbaseclusters.spec.networking.tls.passphrase.rest.headers

#### [](#constraints-233)Constraints

**Type**: `map[string]string`

#### [](#description-233)Description

Headers is a map of one or more key-value pairs to pass alongside the Get request.

### [](#couchbaseclusters-spec-networking-tls-passphrase-rest-timeout)couchbaseclusters.spec.networking.tls.passphrase.rest.timeout

#### [](#constraints-234)Constraints

**Type**: `integer`

**Default**: `5000`

#### [](#description-234)Description

Timeout is the number of milliseconds that must elapse before the call is timed out.

### [](#couchbaseclusters-spec-networking-tls-passphrase-rest-url)couchbaseclusters.spec.networking.tls.passphrase.rest.url

#### [](#constraints-235)Constraints

**Required**

**Type**: `string`

#### [](#description-235)Description

URL is the endpoint to be called to retrieve the passphrase. URL will be called using the GET method and may use http/https protocol.

### [](#couchbaseclusters-spec-networking-tls-passphrase-rest-verifypeer)couchbaseclusters.spec.networking.tls.passphrase.rest.verifyPeer

#### [](#constraints-236)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-236)Description

VerifyPeer ensures peer verification is performed when Https is used.

### [](#couchbaseclusters-spec-networking-tls-passphrase-script)couchbaseclusters.spec.networking.tls.passphrase.script

#### [](#constraints-237)Constraints

**Type**: `object`

#### [](#description-237)Description

PassphraseScriptConfig is the configuration to register a private key passphrase with a script. The Operator auto-provisions the underlying script so this config simply provides a mechanism to perform the decryption of the Couchbase Private Key using a local script.

### [](#couchbaseclusters-spec-networking-tls-passphrase-script-secret)couchbaseclusters.spec.networking.tls.passphrase.script.secret

#### [](#constraints-238)Constraints

**Required**

**Type**: `string`

#### [](#description-238)Description

Secret is the secret containing the passphrase string. The secret is expected to contain "passphrase" key with the passphrase string as a value.

### [](#couchbaseclusters-spec-networking-tls-rootcas)couchbaseclusters.spec.networking.tls.rootCAs

#### [](#constraints-239)Constraints

**Type**: `[]string`

#### [](#description-239)Description

RootCAs defines a set of secrets that reside in this namespace that contain additional CA certificates that should be installed in Couchbase. The CA certificates that are defined here are in addition to those defined for the cluster, optionally by couchbaseclusters.spec.networking.tls.secretSource, and thus should not be duplicated. Each Secret referred to must be of well-known type "kubernetes.io/tls" and must contain one or more CA certificates under the key "tls.crt". Multiple root CA certificates are only supported on Couchbase Server 7.1 and greater, and not with legacy couchbaseclusters.spec.networking.tls.static configuration.

### [](#couchbaseclusters-spec-networking-tls-secretsource)couchbaseclusters.spec.networking.tls.secretSource

#### [](#constraints-240)Constraints

**Type**: `object`

#### [](#description-240)Description

SecretSource enables the user to specify a secret conforming to the Kubernetes TLS secret specification that is used for the Couchbase server certificate, and optionally the Operator’s client certificate, providing cert-manager compatibility without having to specify a separate root CA. A server CA certificate must be supplied by one of the provided methods. Certificates referred to must conform to the keys of well-known type "kubernetes.io/tls" with "tls.crt" and "tls.key". If the "tls.key" is an encrypted private key then the secret type can be the generic Opaque type since "kubernetes.io/tls" type secrets cannot verify encrypted keys.

### [](#couchbaseclusters-spec-networking-tls-secretsource-clientsecretname)couchbaseclusters.spec.networking.tls.secretSource.clientSecretName

#### [](#constraints-241)Constraints

**Type**: `string`

#### [](#description-241)Description

ClientSecretName specifies the secret name, in the same namespace as the cluster, the contains client TLS data. The secret is expected to contain "tls.crt" and "tls.key" as per the Kubernetes.io/tls secret type.

### [](#couchbaseclusters-spec-networking-tls-secretsource-serversecretname)couchbaseclusters.spec.networking.tls.secretSource.serverSecretName

#### [](#constraints-242)Constraints

**Required**

**Type**: `string`

#### [](#description-242)Description

ServerSecretName specifies the secret name, in the same namespace as the cluster, that contains server TLS data. The secret is expected to contain "tls.crt" and "tls.key" as per the kubernetes.io/tls secret type. It may also contain "ca.crt". Only a single PEM formated x509 certificate can be provided to "ca.crt". The single certificate may also bundle together multiple root CA certificates. Multiple root CA certificates are only supported on Couchbase Server 7.1 and greater.

### [](#couchbaseclusters-spec-networking-tls-static)couchbaseclusters.spec.networking.tls.static

#### [](#constraints-243)Constraints

**Type**: `object`

#### [](#description-243)Description

**DEPRECATED** \- by couchbaseclusters.spec.networking.tls.secretSource.

Static enables user to generate static x509 certificates and keys, put them into Kubernetes secrets, and specify them here. Static secrets are Couchbase specific, and follow no well-known standards.

### [](#couchbaseclusters-spec-networking-tls-static-operatorsecret)couchbaseclusters.spec.networking.tls.static.operatorSecret

#### [](#constraints-244)Constraints

**Type**: `string`

#### [](#description-244)Description

OperatorSecret is a secret name containing TLS certs used by operator to talk securely to this cluster. The secret must contain a CA certificate (data key ca.crt). If client authentication is enabled, then the secret must also contain a client certificate chain (data key "couchbase-operator.crt") and private key (data key "couchbase-operator.key").

### [](#couchbaseclusters-spec-networking-tls-static-serversecret)couchbaseclusters.spec.networking.tls.static.serverSecret

#### [](#constraints-245)Constraints

**Type**: `string`

#### [](#description-245)Description

ServerSecret is a secret name containing TLS certs used by each Couchbase member pod for the communication between Couchbase server and its clients. The secret must contain a certificate chain (data key "chain.pem") and a private key (data key "pkey.key"). The private key must be in the PKCS#1 RSA format. The certificate chain must have a required set of X.509v3 subject alternative names for all cluster addressing modes. See the Operator TLS documentation for more information.

### [](#couchbaseclusters-spec-networking-tls-tlsminimumversion)couchbaseclusters.spec.networking.tls.tlsMinimumVersion

#### [](#constraints-246)Constraints

**Type**: `string`

**Default**: `TLS1.2`

**Enumerations**: `TLS1.0, TLS1.1, TLS1.2, TLS1.3`

#### [](#description-246)Description

TLSMinimumVersion specifies the minimum TLS version the Couchbase server can negotiate with a client. Must be one of TLS1.0, TLS1.1 TLS1.2 or TLS1.3, defaulting to TLS1.2\. TLS1.3 is only valid for Couchbase Server 7.1.0 onward. TLS1.0 and TLS1.1 are not valid for Couchbase Server 7.6.0 onward.

### [](#couchbaseclusters-spec-networking-tls-validatebarehostnames)couchbaseclusters.spec.networking.tls.validateBareHostnames

#### [](#constraints-247)Constraints

**Required**

**Type**: `boolean`

**Default**: `True`

#### [](#description-247)Description

ValidateBareHostnames controls whether the operator expects bare hostname entries (like "<cluster-name>-srv") in server certificates. When false, the operator will not require bare hostname SAN entries for its internal TLS verification. Defaults to true for backward compatibility.

### [](#couchbaseclusters-spec-networking-waitforaddressreachable)couchbaseclusters.spec.networking.waitForAddressReachable

#### [](#constraints-248)Constraints

**Type**: `string`

**Default**: `10m`

#### [](#description-248)Description

WaitForAddressReachable is used to set the timeout between when polling of external addresses is started, and when it is deemed a failure. Polling of DNS name availability inherently dangerous due to negative caching, so prefer the use of an initial `waitForAddressReachableDelay` to allow propagation. Once the timeout has elapsed, pods without a reachable alternate address that have not been balanced into the cluster will be removed. This field will not effect pods that have already been balanced into the cluster and those will continue to have their alternate address validated during each reconciliation loop until it can be reached.

### [](#couchbaseclusters-spec-networking-waitforaddressreachabledelay)couchbaseclusters.spec.networking.waitForAddressReachableDelay

#### [](#constraints-249)Constraints

**Type**: `string`

**Default**: `2m`

#### [](#description-249)Description

WaitForAddressReachableDelay is used to defer operator checks that ensure external addresses are reachable before new nodes are balanced in to the cluster. This prevents negative DNS caching while waiting for external-DDNS controllers to propagate addresses. Pods will not be marked as ready until external addresses are reachable which at the earliest will be after this delay has elapsed.

### [](#couchbaseclusters-spec-onlinevolumeexpansiontimeoutinmins)couchbaseclusters.spec.onlineVolumeExpansionTimeoutInMins

#### [](#constraints-250)Constraints

**Type**: `integer`

**Minimum**: `0`

**Maximum**: `30`

#### [](#description-250)Description

OnlineVolumeExpansionTimeoutInMins must be provided as a retry mechanism with a timeout in minutes for expanding volumes. This must only be provided, if EnableOnlineVolumeExpansion is set to true. Value must be between 0 and 30\. If no value is provided, then it defaults to 10 minutes.

### [](#couchbaseclusters-spec-paused)couchbaseclusters.spec.paused

#### [](#constraints-251)Constraints

**Type**: `boolean`

#### [](#description-251)Description

Paused is to pause the control of the operator for the Couchbase cluster. This does not pause the cluster itself, instead stopping the operator from taking any action.

### [](#couchbaseclusters-spec-perserviceclasspdb)couchbaseclusters.spec.perServiceClassPDB

#### [](#constraints-252)Constraints

**Type**: `boolean`

**Default**: `False`

#### [](#description-252)Description

PerServiceClassPDB determines whether a pod disruption budget (PDB) should be created for each service class. By default, a single PDB will be created for the cluster with a minAvailable value of one less than the total number of requested Couchbase nodes in the cluster, meaning only a single Couchbase node can be voluntarily disrupted at a time. When this field is set to true, a PDB will be created for each service class, with a minAvailable value of one less than the service class size. This allows for a more granular control over the number of Couchbase nodes that can be voluntarily disrupted at a time, such as during a Kubernetes upgrade. In order to enable this feature, the size of each service class must be at least 2 and the maximum number of Couchbase nodes that the PDB’s would allow to be disrupted at once cannot exceed 50% of the total number of Couchbase nodes requested in the cluster specification. Furthermore, the requested number of replicas for both the index and data services must remain less than the minimum number of Couchbase nodes that the server class PDB’s will cumulatively allow for.

### [](#couchbaseclusters-spec-platform)couchbaseclusters.spec.platform

#### [](#constraints-253)Constraints

**Type**: `string`

**Enumerations**: `aws, gce, azure`

#### [](#description-253)Description

Platform gives a hint as to what platform we are running on and how to configure services. This field must be one of "aws", "gke" or "azure".

### [](#couchbaseclusters-spec-recoverypolicy)couchbaseclusters.spec.recoveryPolicy

#### [](#constraints-254)Constraints

**Type**: `string`

**Enumerations**: `PrioritizeDataIntegrity, PrioritizeUptime`

#### [](#description-254)Description

RecoveryPolicy controls how aggressive the Operator is when recovering cluster topology. When PrioritizeDataIntegrity, the Operator will delegate failover exclusively to Couchbase server, relying on it to only allow recovery when safe to do so. When PrioritizeUptime, the Operator will wait for a period after the expected auto-failover of the cluster, before forcefully failing-over the pods. This may cause data loss, and is only expected to be used on clusters with ephemeral data, where the loss of the pod means that the data is known to be unrecoverable. This field must be either "PrioritizeDataIntegrity" or "PrioritizeUptime", defaulting to "PrioritizeDataIntegrity".

### [](#couchbaseclusters-spec-rollingupgrade)couchbaseclusters.spec.rollingUpgrade

#### [](#constraints-255)Constraints

**Type**: `object`

#### [](#description-255)Description

**DEPRECATED** \- By spec.upgrade.rollingUpgrade.

When `spec.upgradeStrategy` is set to `RollingUpgrade` it will, by default, upgrade one pod at a time. If this field is specified then that number can be increased.

### [](#couchbaseclusters-spec-rollingupgrade-maxupgradable)couchbaseclusters.spec.rollingUpgrade.maxUpgradable

#### [](#constraints-256)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-256)Description

MaxUpgradable allows the number of pods affected by an upgrade at any one time to be increased. By default a rolling upgrade will upgrade one pod at a time. This field allows that limit to be removed. This field must be greater than zero. The smallest of `maxUpgradable` and `maxUpgradablePercent` takes precedence if both are defined.

### [](#couchbaseclusters-spec-rollingupgrade-maxupgradablepercent)couchbaseclusters.spec.rollingUpgrade.maxUpgradablePercent

#### [](#constraints-257)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(100|[1-9][0-9]|[1-9])%$`

#### [](#description-257)Description

MaxUpgradablePercent allows the number of pods affected by an upgrade at any one time to be increased. By default a rolling upgrade will upgrade one pod at a time. This field allows that limit to be removed. This field must be an integer percentage, e.g. "10%", in the range 1% to 100%. Percentages are relative to the total cluster size, and rounded down to the nearest whole number, with a minimum of 1\. For example, a 10 pod cluster, and 25% allowed to upgrade, would yield 2.5 pods per iteration, rounded down to 2\. The smallest of `maxUpgradable` and `maxUpgradablePercent` takes precedence if both are defined.

### [](#couchbaseclusters-spec-security)couchbaseclusters.spec.security

#### [](#constraints-258)Constraints

**Required**

**Type**: `object`

#### [](#description-258)Description

Security defines Couchbase cluster security options such as the administrator account username and password, and user RBAC settings.

### [](#couchbaseclusters-spec-security-adminsecret)couchbaseclusters.spec.security.adminSecret

#### [](#constraints-259)Constraints

**Required**

**Type**: `string`

#### [](#description-259)Description

AdminSecret is the name of a Kubernetes secret to use for administrator authentication. The admin secret must contain the keys "username" and "password". The password data must be at least 6 characters in length, and not contain the any of the characters `()<>,;:\"/[]?={}`.

### [](#couchbaseclusters-spec-security-encryptionatrest)couchbaseclusters.spec.security.encryptionAtRest

#### [](#constraints-260)Constraints

**Type**: `object`

#### [](#description-260)Description

EncryptionAtRest configures encryption at rest for the cluster. This field is only supported on Couchbase Server 8.0.0+.

### [](#couchbaseclusters-spec-security-encryptionatrest-audit)couchbaseclusters.spec.security.encryptionAtRest.audit

#### [](#constraints-261)Constraints

**Type**: `object`

#### [](#description-261)Description

Audit is the configuration for encryption at rest for the cluster.

### [](#couchbaseclusters-spec-security-encryptionatrest-audit-enabled)couchbaseclusters.spec.security.encryptionAtRest.audit.enabled

#### [](#constraints-262)Constraints

**Required**

**Type**: `boolean`

#### [](#description-262)Description

Enabled enables encryption at rest for the cluster.

### [](#couchbaseclusters-spec-security-encryptionatrest-audit-keylifetime)couchbaseclusters.spec.security.encryptionAtRest.audit.keyLifetime

#### [](#constraints-263)Constraints

**Type**: `string`

**Default**: `8760h`

#### [](#description-263)Description

KeyLifetime is the lifetime of the encryption key. Must be greater or equal to 30 days. Default is 365 days.

### [](#couchbaseclusters-spec-security-encryptionatrest-audit-keyname)couchbaseclusters.spec.security.encryptionAtRest.audit.keyName

#### [](#constraints-264)Constraints

**Type**: `string`

#### [](#description-264)Description

Key is the name of the encryption key to use for encryption at rest. If not provided, the operator will use the master password.

### [](#couchbaseclusters-spec-security-encryptionatrest-audit-rotationinterval)couchbaseclusters.spec.security.encryptionAtRest.audit.rotationInterval

#### [](#constraints-265)Constraints

**Type**: `string`

**Default**: `720h`

#### [](#description-265)Description

RotationInterval is the interval at which the encryption key will be rotated. Must be greater or equal to 7 days. Default is 30 days.

### [](#couchbaseclusters-spec-security-encryptionatrest-configuration)couchbaseclusters.spec.security.encryptionAtRest.configuration

#### [](#constraints-266)Constraints

**Required**

**Type**: `object`

**Default**: `{'enabled': True}`

#### [](#description-266)Description

Configuration defines how the configurations on the cluster should be encrypted at rest.

### [](#couchbaseclusters-spec-security-encryptionatrest-configuration-enabled)couchbaseclusters.spec.security.encryptionAtRest.configuration.enabled

#### [](#constraints-267)Constraints

**Required**

**Type**: `boolean`

#### [](#description-267)Description

Enabled enables encryption at rest for the cluster.

### [](#couchbaseclusters-spec-security-encryptionatrest-configuration-keylifetime)couchbaseclusters.spec.security.encryptionAtRest.configuration.keyLifetime

#### [](#constraints-268)Constraints

**Type**: `string`

**Default**: `8760h`

#### [](#description-268)Description

KeyLifetime is the lifetime of the encryption key. Must be greater or equal to 30 days. Default is 365 days.

### [](#couchbaseclusters-spec-security-encryptionatrest-configuration-keyname)couchbaseclusters.spec.security.encryptionAtRest.configuration.keyName

#### [](#constraints-269)Constraints

**Type**: `string`

#### [](#description-269)Description

Key is the name of the encryption key to use for encryption at rest. If not provided, the operator will use the master password.

### [](#couchbaseclusters-spec-security-encryptionatrest-configuration-rotationinterval)couchbaseclusters.spec.security.encryptionAtRest.configuration.rotationInterval

#### [](#constraints-270)Constraints

**Type**: `string`

**Default**: `720h`

#### [](#description-270)Description

RotationInterval is the interval at which the encryption key will be rotated. Must be greater or equal to 7 days. Default is 30 days.

### [](#couchbaseclusters-spec-security-encryptionatrest-log)couchbaseclusters.spec.security.encryptionAtRest.log

#### [](#constraints-271)Constraints

**Type**: `object`

#### [](#description-271)Description

Log is the configuration for encryption at rest for log files. NOTE: Enabled encryption at rest of logs will break fluent-bit log streaming.

### [](#couchbaseclusters-spec-security-encryptionatrest-log-enabled)couchbaseclusters.spec.security.encryptionAtRest.log.enabled

#### [](#constraints-272)Constraints

**Required**

**Type**: `boolean`

#### [](#description-272)Description

Enabled enables encryption at rest for the cluster.

### [](#couchbaseclusters-spec-security-encryptionatrest-log-keylifetime)couchbaseclusters.spec.security.encryptionAtRest.log.keyLifetime

#### [](#constraints-273)Constraints

**Type**: `string`

**Default**: `8760h`

#### [](#description-273)Description

KeyLifetime is the lifetime of the encryption key. Must be greater or equal to 30 days. Default is 365 days.

### [](#couchbaseclusters-spec-security-encryptionatrest-log-keyname)couchbaseclusters.spec.security.encryptionAtRest.log.keyName

#### [](#constraints-274)Constraints

**Type**: `string`

#### [](#description-274)Description

Key is the name of the encryption key to use for encryption at rest. If not provided, the operator will use the master password.

### [](#couchbaseclusters-spec-security-encryptionatrest-log-rotationinterval)couchbaseclusters.spec.security.encryptionAtRest.log.rotationInterval

#### [](#constraints-275)Constraints

**Type**: `string`

**Default**: `720h`

#### [](#description-275)Description

RotationInterval is the interval at which the encryption key will be rotated. Must be greater or equal to 7 days. Default is 30 days.

### [](#couchbaseclusters-spec-security-encryptionatrest-managed)couchbaseclusters.spec.security.encryptionAtRest.managed

#### [](#constraints-276)Constraints

**Type**: `boolean`

#### [](#description-276)Description

Managed defines whether the operator should manage encryption at rest for the cluster. This includes encryption keys and encryption at rest settings.

### [](#couchbaseclusters-spec-security-encryptionatrest-selector)couchbaseclusters.spec.security.encryptionAtRest.selector

#### [](#constraints-277)Constraints

**Type**: `object`

#### [](#description-277)Description

Selector is a label selector used to select the encryption keys to use.

### [](#couchbaseclusters-spec-security-encryptionatrest-selector-matchexpressions)couchbaseclusters.spec.security.encryptionAtRest.selector.matchExpressions

#### [](#constraints-278)Constraints

**Type**: `[]object`

#### [](#description-278)Description

matchExpressions is a list of label selector requirements. The requirements are ANDed.

### [](#couchbaseclusters-spec-security-encryptionatrest-selector-matchexpressions-key)couchbaseclusters.spec.security.encryptionAtRest.selector.matchExpressions.key

#### [](#constraints-279)Constraints

**Required**

**Type**: `string`

#### [](#description-279)Description

key is the label key that the selector applies to.

### [](#couchbaseclusters-spec-security-encryptionatrest-selector-matchexpressions-operator)couchbaseclusters.spec.security.encryptionAtRest.selector.matchExpressions.operator

#### [](#constraints-280)Constraints

**Required**

**Type**: `string`

#### [](#description-280)Description

operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist.

### [](#couchbaseclusters-spec-security-encryptionatrest-selector-matchexpressions-values)couchbaseclusters.spec.security.encryptionAtRest.selector.matchExpressions.values

#### [](#constraints-281)Constraints

**Type**: `[]string`

#### [](#description-281)Description

values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch.

### [](#couchbaseclusters-spec-security-encryptionatrest-selector-matchlabels)couchbaseclusters.spec.security.encryptionAtRest.selector.matchLabels

#### [](#constraints-282)Constraints

**Type**: `map[string]string`

#### [](#description-282)Description

matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed.

### [](#couchbaseclusters-spec-security-ldap)couchbaseclusters.spec.security.ldap

#### [](#constraints-283)Constraints

**Type**: `object`

#### [](#description-283)Description

LDAP provides settings to authenticate and authorize LDAP users with Couchbase Server. When specified, the Operator keeps these settings in sync with Cocuhbase Server’s LDAP configuration. Leave empty to manually manage LDAP configuration.

### [](#couchbaseclusters-spec-security-ldap-authenticationenabled)couchbaseclusters.spec.security.ldap.authenticationEnabled

#### [](#constraints-284)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-284)Description

AuthenticationEnabled allows users who attempt to access Couchbase Server without having been added as local users to be authenticated against the specified LDAP Host(s).

### [](#couchbaseclusters-spec-security-ldap-authorizationenabled)couchbaseclusters.spec.security.ldap.authorizationEnabled

#### [](#constraints-285)Constraints

**Type**: `boolean`

#### [](#description-285)Description

AuthorizationEnabled allows authenticated LDAP users to be authorized with RBAC roles granted to any Couchbase Server group associated with the user.

### [](#couchbaseclusters-spec-security-ldap-binddn)couchbaseclusters.spec.security.ldap.bindDN

#### [](#constraints-286)Constraints

**Type**: `string`

#### [](#description-286)Description

DN to use for searching users and groups synchronization. More info: <https://docs.couchbase.com/server/current/manage/manage-security/configure-ldap.html>.

### [](#couchbaseclusters-spec-security-ldap-bindsecret)couchbaseclusters.spec.security.ldap.bindSecret

#### [](#constraints-287)Constraints

**Required**

**Type**: `string`

#### [](#description-287)Description

BindSecret is the name of a Kubernetes secret to use containing password for LDAP user binding. The bindSecret must have a key with the name "password" and a value which corresponds to the password of the binding LDAP user.

### [](#couchbaseclusters-spec-security-ldap-cacert)couchbaseclusters.spec.security.ldap.cacert

#### [](#constraints-288)Constraints

**Type**: `string`

#### [](#description-288)Description

**DEPRECATED** \- Field is ignored, use tlsSecret.

CA Certificate in PEM format to be used in LDAP server certificate validation. This cert is the string form of the secret provided to `spec.tls.tlsSecret`.

### [](#couchbaseclusters-spec-security-ldap-cachevaluelifetime)couchbaseclusters.spec.security.ldap.cacheValueLifetime

#### [](#constraints-289)Constraints

**Type**: `integer`

**Default**: `30000`

#### [](#description-289)Description

Lifetime of values in cache in milliseconds. Default 300000 ms. More info: <https://docs.couchbase.com/server/current/manage/manage-security/configure-ldap.html>.

### [](#couchbaseclusters-spec-security-ldap-encryption)couchbaseclusters.spec.security.ldap.encryption

#### [](#constraints-290)Constraints

**Type**: `string`

**Enumerations**: `None, StartTLSExtension, TLS`

#### [](#description-290)Description

Encryption determines how the connection with the LDAP server should be encrypted. Encryption may set as either StartTLSExtension, TLS, or false. When set to "false" then no verification of the LDAP hostname is performed. When Encryption is StartTLSExtension, or TLS is set then the default behavior is to use the certificate already loaded into the Couchbase Cluster for certificate validation, otherwise `ldap.tlsSecret` may be set to override The Couchbase certificate.

### [](#couchbaseclusters-spec-security-ldap-groupsquery)couchbaseclusters.spec.security.ldap.groupsQuery

#### [](#constraints-291)Constraints

**Type**: `string`

#### [](#description-291)Description

LDAP query, to get the users' groups by username in RFC4516 format. More info: <https://docs.couchbase.com/server/current/manage/manage-security/configure-ldap.html>.

### [](#couchbaseclusters-spec-security-ldap-hosts)couchbaseclusters.spec.security.ldap.hosts

#### [](#constraints-292)Constraints

**Required**

**Type**: `[]string`

**Minimum Items**: `1`

#### [](#description-292)Description

List of LDAP hosts to provide authentication-support for Couchbase Server. Host name must be a valid IP address or DNS Name e.g openldap.default.svc, 10.0.92.147.

### [](#couchbaseclusters-spec-security-ldap-middleboxcompmode)couchbaseclusters.spec.security.ldap.middleboxCompMode

#### [](#constraints-293)Constraints

**Type**: `boolean`

**Default**: `True`

#### [](#description-293)Description

Sets middlebox compatibility mode for LDAP. This option is only available on Couchbase Server 7.6.0+.

### [](#couchbaseclusters-spec-security-ldap-nestedgroupsenabled)couchbaseclusters.spec.security.ldap.nestedGroupsEnabled

#### [](#constraints-294)Constraints

**Type**: `boolean`

#### [](#description-294)Description

If enabled Couchbase server will try to recursively search for groups for every discovered ldap group. groups\_query will be user for the search. More info: <https://docs.couchbase.com/server/current/manage/manage-security/configure-ldap.html>.

### [](#couchbaseclusters-spec-security-ldap-nestedgroupsmaxdepth)couchbaseclusters.spec.security.ldap.nestedGroupsMaxDepth

#### [](#constraints-295)Constraints

**Type**: `integer`

**Default**: `10`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-295)Description

Maximum number of recursive groups requests the server is allowed to perform. Requires NestedGroupsEnabled. Values between 1 and 100: the default is 10\. More info: <https://docs.couchbase.com/server/current/manage/manage-security/configure-ldap.html>.

### [](#couchbaseclusters-spec-security-ldap-port)couchbaseclusters.spec.security.ldap.port

#### [](#constraints-296)Constraints

**Required**

**Type**: `integer`

**Default**: `389`

#### [](#description-296)Description

LDAP port. This is typically 389 for LDAP, and 636 for LDAPS.

### [](#couchbaseclusters-spec-security-ldap-servercertvalidation)couchbaseclusters.spec.security.ldap.serverCertValidation

#### [](#constraints-297)Constraints

**Type**: `boolean`

#### [](#description-297)Description

Whether server certificate validation be enabled.

### [](#couchbaseclusters-spec-security-ldap-tlssecret)couchbaseclusters.spec.security.ldap.tlsSecret

#### [](#constraints-298)Constraints

**Type**: `string`

#### [](#description-298)Description

TLSSecret is the name of a Kubernetes secret to use explcitly for LDAP ca cert. If TLSSecret is not provided, certificates found in `couchbaseclusters.spec.networking.tls.rootCAs`will be used instead. If provided, the secret must contain the ca to be used under the name "ca.crt".

### [](#couchbaseclusters-spec-security-ldap-userdnmapping)couchbaseclusters.spec.security.ldap.userDNMapping

#### [](#constraints-299)Constraints

**Type**: `object`

#### [](#description-299)Description

User to distinguished name (DN) mapping. If none is specified, the username is used as the user’s distinguished name. More info: <https://docs.couchbase.com/server/current/manage/manage-security/configure-ldap.html>.

### [](#couchbaseclusters-spec-security-ldap-userdnmapping-query)couchbaseclusters.spec.security.ldap.userDNMapping.query

#### [](#constraints-300)Constraints

**Type**: `string`

#### [](#description-300)Description

Query is the LDAP query to run to map from Couchbase user to LDAP distinguished name.

### [](#couchbaseclusters-spec-security-ldap-userdnmapping-template)couchbaseclusters.spec.security.ldap.userDNMapping.template

#### [](#constraints-301)Constraints

**Type**: `string`

#### [](#description-301)Description

This field specifies list of templates to use for providing username to DN mapping. The template may contain a placeholder specified as `%u` to represent the Couchbase user who is attempting to gain access.

### [](#couchbaseclusters-spec-security-passwordpolicy)couchbaseclusters.spec.security.passwordPolicy

#### [](#constraints-302)Constraints

**Type**: `object`

#### [](#description-302)Description

PasswordPolicy specifies a series of character-related requirements that must be met by all passwords whose definition occurs subsequent to the establishing of the policy. If this is updated, previously defined passwords continue to be valid, even if they do not meet the requirements specified in the new policy. If RBAC is managed, any CouchbaseUser resources which match the RBAC resource selector will be checked against this policy.

### [](#couchbaseclusters-spec-security-passwordpolicy-enforcedigits)couchbaseclusters.spec.security.passwordPolicy.enforceDigits

#### [](#constraints-303)Constraints

**Type**: `boolean`

#### [](#description-303)Description

EnforceDigits sets whether passwords must contain at least one digit.

### [](#couchbaseclusters-spec-security-passwordpolicy-enforcelowercase)couchbaseclusters.spec.security.passwordPolicy.enforceLowercase

#### [](#constraints-304)Constraints

**Type**: `boolean`

#### [](#description-304)Description

EnforceLowercase sets whether passwords must contain at least one lowercase letter.

### [](#couchbaseclusters-spec-security-passwordpolicy-enforcespecialchars)couchbaseclusters.spec.security.passwordPolicy.enforceSpecialChars

#### [](#constraints-305)Constraints

**Type**: `boolean`

#### [](#description-305)Description

EnforceSpecialChars sets whether passwords must contain at least one special character. If this is set to true, the allowed special chars are limited to: @, %, +, /, ', \\, ", !, #, $, ^, ?, :, ,, (, ), {, }, \[, \], \~, \`, -, and \_.

### [](#couchbaseclusters-spec-security-passwordpolicy-enforceuppercase)couchbaseclusters.spec.security.passwordPolicy.enforceUppercase

#### [](#constraints-306)Constraints

**Type**: `boolean`

#### [](#description-306)Description

EnforceUppercase sets whether passwords must contain at least one uppercase letter.

### [](#couchbaseclusters-spec-security-passwordpolicy-minlength)couchbaseclusters.spec.security.passwordPolicy.minLength

#### [](#constraints-307)Constraints

**Type**: `integer`

**Minimum**: `0`

**Maximum**: `100`

#### [](#description-307)Description

MinLength sets the minimum length a password must be, This field must be between 0 and 100\. If this field is set to 0, Couchbase Server will permit the definition of highly insecure zero-length passwords which is not recommended.

### [](#couchbaseclusters-spec-security-passwordpolicy-passwordresetonpolicychangeexemptusers)couchbaseclusters.spec.security.passwordPolicy.passwordResetOnPolicyChangeExemptUsers

#### [](#constraints-308)Constraints

**Type**: `[]string`

#### [](#description-308)Description

PolicyChangePasswordResetExemptUsers defines names of CouchbaseUser resources that will not be required to change their password if requirePasswordResetOnPolicyChange is set to true and the password policy is updated. This field is only available for Couchbase Server 8.0.0+.

### [](#couchbaseclusters-spec-security-passwordpolicy-requirepasswordresetonpolicychange)couchbaseclusters.spec.security.passwordPolicy.requirePasswordResetOnPolicyChange

#### [](#constraints-309)Constraints

**Type**: `boolean`

#### [](#description-309)Description

RequirePasswordResetOnPolicyChange defines whether users will be required to change their password when the password policy is updated. This field is only available for Couchbase Server 8.0.0+.

### [](#couchbaseclusters-spec-security-podsecuritycontext)couchbaseclusters.spec.security.podSecurityContext

#### [](#constraints-310)Constraints

**Type**: `object`

#### [](#description-310)Description

PodSecurityContext allows the configuration of the security context for all Couchbase server pods. When using persistent volumes you may need to set the fsGroup field in order to write to the volume. For non-root clusters you must also set runAsUser to 1000, corresponding to the Couchbase user in official container images. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>.

### [](#couchbaseclusters-spec-security-podsecuritycontext-fsgroup)couchbaseclusters.spec.security.podSecurityContext.fsGroup

#### [](#constraints-311)Constraints

**Type**: `integer`

#### [](#description-311)Description

A special supplemental group that applies to all containers in a pod. Some volume types allow the Kubelet to change the ownership of that volume to be owned by the pod:

1\. The owning GID will be the FSGroup 2\. The setgid bit is set (new files created in the volume will be owned by FSGroup) 3\. The permission bits are OR’d with rw-rw----

If unset, the Kubelet will not modify the ownership and permissions of any volume. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-podsecuritycontext-fsgroupchangepolicy)couchbaseclusters.spec.security.podSecurityContext.fsGroupChangePolicy

#### [](#constraints-312)Constraints

**Type**: `string`

#### [](#description-312)Description

fsGroupChangePolicy defines behavior of changing ownership and permission of the volume before being exposed inside Pod. This field will only apply to volume types which support fsGroup based ownership(and permissions). It will have no effect on ephemeral volume types such as: secret, configmaps and emptydir. Valid values are "OnRootMismatch" and "Always". If not specified, "Always" is used. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-podsecuritycontext-runasgroup)couchbaseclusters.spec.security.podSecurityContext.runAsGroup

#### [](#constraints-313)Constraints

**Type**: `integer`

#### [](#description-313)Description

The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-podsecuritycontext-runasnonroot)couchbaseclusters.spec.security.podSecurityContext.runAsNonRoot

#### [](#constraints-314)Constraints

**Type**: `boolean`

#### [](#description-314)Description

Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

### [](#couchbaseclusters-spec-security-podsecuritycontext-runasuser)couchbaseclusters.spec.security.podSecurityContext.runAsUser

#### [](#constraints-315)Constraints

**Type**: `integer`

#### [](#description-315)Description

The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-podsecuritycontext-selinuxoptions)couchbaseclusters.spec.security.podSecurityContext.seLinuxOptions

#### [](#constraints-316)Constraints

**Type**: `object`

#### [](#description-316)Description

The SELinux context to be applied to all containers. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in SecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence for that container. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-podsecuritycontext-selinuxoptions-level)couchbaseclusters.spec.security.podSecurityContext.seLinuxOptions.level

#### [](#constraints-317)Constraints

**Type**: `string`

#### [](#description-317)Description

Level is SELinux level label that applies to the container.

### [](#couchbaseclusters-spec-security-podsecuritycontext-selinuxoptions-role)couchbaseclusters.spec.security.podSecurityContext.seLinuxOptions.role

#### [](#constraints-318)Constraints

**Type**: `string`

#### [](#description-318)Description

Role is a SELinux role label that applies to the container.

### [](#couchbaseclusters-spec-security-podsecuritycontext-selinuxoptions-type)couchbaseclusters.spec.security.podSecurityContext.seLinuxOptions.type

#### [](#constraints-319)Constraints

**Type**: `string`

#### [](#description-319)Description

Type is a SELinux type label that applies to the container.

### [](#couchbaseclusters-spec-security-podsecuritycontext-selinuxoptions-user)couchbaseclusters.spec.security.podSecurityContext.seLinuxOptions.user

#### [](#constraints-320)Constraints

**Type**: `string`

#### [](#description-320)Description

User is a SELinux user label that applies to the container.

### [](#couchbaseclusters-spec-security-podsecuritycontext-seccompprofile)couchbaseclusters.spec.security.podSecurityContext.seccompProfile

#### [](#constraints-321)Constraints

**Type**: `object`

#### [](#description-321)Description

The seccomp options to use by the containers in this pod. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-podsecuritycontext-seccompprofile-localhostprofile)couchbaseclusters.spec.security.podSecurityContext.seccompProfile.localhostProfile

#### [](#constraints-322)Constraints

**Type**: `string`

#### [](#description-322)Description

localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.

### [](#couchbaseclusters-spec-security-podsecuritycontext-seccompprofile-type)couchbaseclusters.spec.security.podSecurityContext.seccompProfile.type

#### [](#constraints-323)Constraints

**Required**

**Type**: `string`

#### [](#description-323)Description

type indicates which kind of seccomp profile will be applied. Valid options are:

Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.

### [](#couchbaseclusters-spec-security-podsecuritycontext-supplementalgroups)couchbaseclusters.spec.security.podSecurityContext.supplementalGroups

#### [](#constraints-324)Constraints

**Type**: `[]integer`

#### [](#description-324)Description

A list of groups applied to the first process run in each container, in addition to the container’s primary GID, the fsGroup (if specified), and group memberships defined in the container image for the uid of the container process. If unspecified, no additional groups are added to any container. Note that group memberships defined in the container image for the uid of the container process are still effective, even if they are not included in this list. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-podsecuritycontext-sysctls)couchbaseclusters.spec.security.podSecurityContext.sysctls

#### [](#constraints-325)Constraints

**Type**: `[]object`

#### [](#description-325)Description

Sysctls hold a list of namespaced sysctls used for the pod. Pods with unsupported sysctls (by the container runtime) might fail to launch. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-podsecuritycontext-sysctls-name)couchbaseclusters.spec.security.podSecurityContext.sysctls.name

#### [](#constraints-326)Constraints

**Required**

**Type**: `string`

#### [](#description-326)Description

Name of a property to set.

### [](#couchbaseclusters-spec-security-podsecuritycontext-sysctls-value)couchbaseclusters.spec.security.podSecurityContext.sysctls.value

#### [](#constraints-327)Constraints

**Required**

**Type**: `string`

#### [](#description-327)Description

Value of a property to set.

### [](#couchbaseclusters-spec-security-podsecuritycontext-windowsoptions)couchbaseclusters.spec.security.podSecurityContext.windowsOptions

#### [](#constraints-328)Constraints

**Type**: `object`

#### [](#description-328)Description

The Windows specific settings applied to all containers. If unspecified, the options within a container’s SecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.

### [](#couchbaseclusters-spec-security-podsecuritycontext-windowsoptions-gmsacredentialspec)couchbaseclusters.spec.security.podSecurityContext.windowsOptions.gmsaCredentialSpec

#### [](#constraints-329)Constraints

**Type**: `string`

#### [](#description-329)Description

GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.

### [](#couchbaseclusters-spec-security-podsecuritycontext-windowsoptions-gmsacredentialspecname)couchbaseclusters.spec.security.podSecurityContext.windowsOptions.gmsaCredentialSpecName

#### [](#constraints-330)Constraints

**Type**: `string`

#### [](#description-330)Description

GMSACredentialSpecName is the name of the GMSA credential spec to use.

### [](#couchbaseclusters-spec-security-podsecuritycontext-windowsoptions-hostprocess)couchbaseclusters.spec.security.podSecurityContext.windowsOptions.hostProcess

#### [](#constraints-331)Constraints

**Type**: `boolean`

#### [](#description-331)Description

HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.

### [](#couchbaseclusters-spec-security-podsecuritycontext-windowsoptions-runasusername)couchbaseclusters.spec.security.podSecurityContext.windowsOptions.runAsUserName

#### [](#constraints-332)Constraints

**Type**: `string`

#### [](#description-332)Description

The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

### [](#couchbaseclusters-spec-security-rbac)couchbaseclusters.spec.security.rbac

#### [](#constraints-333)Constraints

**Type**: `object`

#### [](#description-333)Description

RBAC is the options provided for enabling and selecting RBAC User resources to manage.

### [](#couchbaseclusters-spec-security-rbac-managed)couchbaseclusters.spec.security.rbac.managed

#### [](#constraints-334)Constraints

**Type**: `boolean`

#### [](#description-334)Description

Managed defines whether RBAC is managed by us or the clients.

### [](#couchbaseclusters-spec-security-rbac-selector)couchbaseclusters.spec.security.rbac.selector

#### [](#constraints-335)Constraints

**Type**: `object`

#### [](#description-335)Description

Selector is a label selector used to list RBAC resources in the namespace that are managed by the Operator.

### [](#couchbaseclusters-spec-security-securitycontext)couchbaseclusters.spec.security.securityContext

#### [](#constraints-336)Constraints

**Type**: `object`

#### [](#description-336)Description

SecurityContext defines the security options the container should be run with. If set, the fields of SecurityContext override the equivalent fields of PodSecurityContext. Use securityContext.allowPrivilegeEscalation field to grant more privileges than its parent process. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>.

### [](#couchbaseclusters-spec-security-securitycontext-allowprivilegeescalation)couchbaseclusters.spec.security.securityContext.allowPrivilegeEscalation

#### [](#constraints-337)Constraints

**Type**: `boolean`

#### [](#description-337)Description

AllowPrivilegeEscalation controls whether a process can gain more privileges than its parent process. This bool directly controls if the no\_new\_privs flag will be set on the container process. AllowPrivilegeEscalation is true always when the container is: 1) run as Privileged 2) has CAP\_SYS\_ADMIN Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-capabilities)couchbaseclusters.spec.security.securityContext.capabilities

#### [](#constraints-338)Constraints

**Type**: `object`

#### [](#description-338)Description

The capabilities to add/drop when running containers. Defaults to the default set of capabilities granted by the container runtime. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-capabilities-add)couchbaseclusters.spec.security.securityContext.capabilities.add

#### [](#constraints-339)Constraints

**Type**: `[]string`

#### [](#description-339)Description

Added capabilities.

### [](#couchbaseclusters-spec-security-securitycontext-capabilities-drop)couchbaseclusters.spec.security.securityContext.capabilities.drop

#### [](#constraints-340)Constraints

**Type**: `[]string`

#### [](#description-340)Description

Removed capabilities.

### [](#couchbaseclusters-spec-security-securitycontext-privileged)couchbaseclusters.spec.security.securityContext.privileged

#### [](#constraints-341)Constraints

**Type**: `boolean`

#### [](#description-341)Description

Run container in privileged mode. Processes in privileged containers are essentially equivalent to root on the host. Defaults to false. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-procmount)couchbaseclusters.spec.security.securityContext.procMount

#### [](#constraints-342)Constraints

**Type**: `string`

#### [](#description-342)Description

procMount denotes the type of proc mount to use for the containers. The default is DefaultProcMount which uses the container runtime defaults for readonly paths and masked paths. This requires the ProcMountType feature flag to be enabled. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-readonlyrootfilesystem)couchbaseclusters.spec.security.securityContext.readOnlyRootFilesystem

#### [](#constraints-343)Constraints

**Type**: `boolean`

#### [](#description-343)Description

Whether this container has a read-only root filesystem. Default is false. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-runasgroup)couchbaseclusters.spec.security.securityContext.runAsGroup

#### [](#constraints-344)Constraints

**Type**: `integer`

#### [](#description-344)Description

The GID to run the entrypoint of the container process. Uses runtime default if unset. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-runasnonroot)couchbaseclusters.spec.security.securityContext.runAsNonRoot

#### [](#constraints-345)Constraints

**Type**: `boolean`

#### [](#description-345)Description

Indicates that the container must run as a non-root user. If true, the Kubelet will validate the image at runtime to ensure that it does not run as UID 0 (root) and fail to start the container if it does. If unset or false, no such validation will be performed. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

### [](#couchbaseclusters-spec-security-securitycontext-runasuser)couchbaseclusters.spec.security.securityContext.runAsUser

#### [](#constraints-346)Constraints

**Type**: `integer`

#### [](#description-346)Description

The UID to run the entrypoint of the container process. Defaults to user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-selinuxoptions)couchbaseclusters.spec.security.securityContext.seLinuxOptions

#### [](#constraints-347)Constraints

**Type**: `object`

#### [](#description-347)Description

The SELinux context to be applied to the container. If unspecified, the container runtime will allocate a random SELinux context for each container. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-selinuxoptions-level)couchbaseclusters.spec.security.securityContext.seLinuxOptions.level

#### [](#constraints-348)Constraints

**Type**: `string`

#### [](#description-348)Description

Level is SELinux level label that applies to the container.

### [](#couchbaseclusters-spec-security-securitycontext-selinuxoptions-role)couchbaseclusters.spec.security.securityContext.seLinuxOptions.role

#### [](#constraints-349)Constraints

**Type**: `string`

#### [](#description-349)Description

Role is a SELinux role label that applies to the container.

### [](#couchbaseclusters-spec-security-securitycontext-selinuxoptions-type)couchbaseclusters.spec.security.securityContext.seLinuxOptions.type

#### [](#constraints-350)Constraints

**Type**: `string`

#### [](#description-350)Description

Type is a SELinux type label that applies to the container.

### [](#couchbaseclusters-spec-security-securitycontext-selinuxoptions-user)couchbaseclusters.spec.security.securityContext.seLinuxOptions.user

#### [](#constraints-351)Constraints

**Type**: `string`

#### [](#description-351)Description

User is a SELinux user label that applies to the container.

### [](#couchbaseclusters-spec-security-securitycontext-seccompprofile)couchbaseclusters.spec.security.securityContext.seccompProfile

#### [](#constraints-352)Constraints

**Type**: `object`

#### [](#description-352)Description

The seccomp options to use by this container. If seccomp options are provided at both the pod & container level, the container options override the pod options. Note that this field cannot be set when spec.os.name is windows.

### [](#couchbaseclusters-spec-security-securitycontext-seccompprofile-localhostprofile)couchbaseclusters.spec.security.securityContext.seccompProfile.localhostProfile

#### [](#constraints-353)Constraints

**Type**: `string`

#### [](#description-353)Description

localhostProfile indicates a profile defined in a file on the node should be used. The profile must be preconfigured on the node to work. Must be a descending path, relative to the kubelet’s configured seccomp profile location. Must be set if type is "Localhost". Must NOT be set for any other type.

### [](#couchbaseclusters-spec-security-securitycontext-seccompprofile-type)couchbaseclusters.spec.security.securityContext.seccompProfile.type

#### [](#constraints-354)Constraints

**Required**

**Type**: `string`

#### [](#description-354)Description

type indicates which kind of seccomp profile will be applied. Valid options are:

Localhost - a profile defined in a file on the node should be used. RuntimeDefault - the container runtime default profile should be used. Unconfined - no profile should be applied.

### [](#couchbaseclusters-spec-security-securitycontext-windowsoptions)couchbaseclusters.spec.security.securityContext.windowsOptions

#### [](#constraints-355)Constraints

**Type**: `object`

#### [](#description-355)Description

The Windows specific settings applied to all containers. If unspecified, the options from the PodSecurityContext will be used. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence. Note that this field cannot be set when spec.os.name is linux.

### [](#couchbaseclusters-spec-security-securitycontext-windowsoptions-gmsacredentialspec)couchbaseclusters.spec.security.securityContext.windowsOptions.gmsaCredentialSpec

#### [](#constraints-356)Constraints

**Type**: `string`

#### [](#description-356)Description

GMSACredentialSpec is where the GMSA admission webhook (<https://github.com/kubernetes-sigs/windows-gmsa>) inlines the contents of the GMSA credential spec named by the GMSACredentialSpecName field.

### [](#couchbaseclusters-spec-security-securitycontext-windowsoptions-gmsacredentialspecname)couchbaseclusters.spec.security.securityContext.windowsOptions.gmsaCredentialSpecName

#### [](#constraints-357)Constraints

**Type**: `string`

#### [](#description-357)Description

GMSACredentialSpecName is the name of the GMSA credential spec to use.

### [](#couchbaseclusters-spec-security-securitycontext-windowsoptions-hostprocess)couchbaseclusters.spec.security.securityContext.windowsOptions.hostProcess

#### [](#constraints-358)Constraints

**Type**: `boolean`

#### [](#description-358)Description

HostProcess determines if a container should be run as a 'Host Process' container. All of a Pod’s containers must have the same effective HostProcess value (it is not allowed to have a mix of HostProcess containers and non-HostProcess containers). In addition, if HostProcess is true then HostNetwork must also be set to true.

### [](#couchbaseclusters-spec-security-securitycontext-windowsoptions-runasusername)couchbaseclusters.spec.security.securityContext.windowsOptions.runAsUserName

#### [](#constraints-359)Constraints

**Type**: `string`

#### [](#description-359)Description

The UserName in Windows to run the entrypoint of the container process. Defaults to the user specified in image metadata if unspecified. May also be set in PodSecurityContext. If set in both SecurityContext and PodSecurityContext, the value specified in SecurityContext takes precedence.

### [](#couchbaseclusters-spec-security-uisessiontimeout)couchbaseclusters.spec.security.uiSessionTimeout

#### [](#constraints-360)Constraints

**Type**: `integer`

**Default**: `0`

**Minimum**: `0`

**Maximum**: `16666`

#### [](#description-360)Description

UISessionTimeout sets how long, in minutes, before a user is declared inactive and signed out from the Couchbase Server UI. 0 represents no time out.

### [](#couchbaseclusters-spec-securitycontext)couchbaseclusters.spec.securityContext

#### [](#constraints-361)Constraints

**Type**: `object`

#### [](#description-361)Description

**DEPRECATED** \- by spec.security.securityContext SecurityContext allows the configuration of the security context for all Couchbase server pods.

When using persistent volumes you may need to set the fsGroup field in order to write to the volume. For non-root clusters you must also set runAsUser to 1000, corresponding to the Couchbase user in official container images. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/security-context/>.

### [](#couchbaseclusters-spec-servergroups)couchbaseclusters.spec.serverGroups

#### [](#constraints-362)Constraints

**Type**: `[]string`

**Pattern (Regular Expression)**: `^[A-Za-z0-9]([A-Za-z0-9._-]\*[A-Za-z0-9])?$`

#### [](#description-362)Description

ServerGroups define the set of availability zones you want to distribute pods over, and construct Couchbase server groups for. By default, most cloud providers will label nodes with the key "topology.kubernetes.io/zone", the values associated with that key are used here to provide explicit scheduling by the Operator. You may manually label nodes using the "topology.kubernetes.io/zone" key, to provide failure-domain aware scheduling when none is provided for you. Global server groups are applied to all server classes, and may be overridden on a per-server class basis to give more control over scheduling and server groups.

### [](#couchbaseclusters-spec-servers)couchbaseclusters.spec.servers

#### [](#constraints-363)Constraints

**Required**

**Type**: `[]object`

**Minimum Items**: `1`

#### [](#description-363)Description

Servers defines server classes for the Operator to provision and manage. A server class defines what services are running and how many members make up that class. Specifying multiple server classes allows the Operator to provision clusters with Multi-Dimensional Scaling (MDS). At least one server class must be defined, and at least one server class must be running the data service.

### [](#couchbaseclusters-spec-servers-autoscaleenabled)couchbaseclusters.spec.servers.autoscaleEnabled

#### [](#constraints-364)Constraints

**Type**: `boolean`

#### [](#description-364)Description

AutoscaledEnabled defines whether the autoscaling feature is enabled for this class. When true, the Operator will create a CouchbaseAutoscaler resource for this server class. The CouchbaseAutoscaler implements the Kubernetes scale API and can be controlled by the Kubernetes horizontal pod autoscaler (HPA).

### [](#couchbaseclusters-spec-servers-env)couchbaseclusters.spec.servers.env

#### [](#constraints-365)Constraints

**Type**: `[]object`

#### [](#description-365)Description

Env allows the setting of environment variables in the Couchbase server container.

### [](#couchbaseclusters-spec-servers-envfrom)couchbaseclusters.spec.servers.envFrom

#### [](#constraints-366)Constraints

**Type**: `[]object`

#### [](#description-366)Description

EnvFrom allows the setting of environment variables in the Couchbase server container.

### [](#couchbaseclusters-spec-servers-image)couchbaseclusters.spec.servers.image

#### [](#constraints-367)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(.*?(:\d+)?/)?.\*?/.*?(:.\*?\d+\.\d+\.\d+.\*|@sha256:[0-9a-f]{64})$`

#### [](#description-367)Description

**DEPRECATED** \- use spec.image and spec.upgrade instead Image is the container image name that will be used to launch Couchbase server instances in this server class.

You cannot downgrade the Couchbase version. Across spec.image and all server classes there can only be two different Couchbase images. Updating this field to a value different than spec.image will cause an automatic upgrade of the server class. If it isn’t specified then the cluster image will be used.

### [](#couchbaseclusters-spec-servers-name)couchbaseclusters.spec.servers.name

#### [](#constraints-368)Constraints

**Required**

**Type**: `string`

#### [](#description-368)Description

Name is a textual name for the server configuration and must be unique. The name is used by the operator to uniquely identify a server class, and map pods back to an intended configuration.

### [](#couchbaseclusters-spec-servers-pod)couchbaseclusters.spec.servers.pod

#### [](#constraints-369)Constraints

**Type**: `object`

#### [](#description-369)Description

Pod defines a template used to create pod for each Couchbase server instance. Modifying pod metadata such as labels and annotations will update the pod in-place. Any other modification will result in a cluster upgrade in order to fulfill the request. The Operator reserves the right to modify or replace any field. More info: <https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#pod-v1-core>.

### [](#couchbaseclusters-spec-servers-resources)couchbaseclusters.spec.servers.resources

#### [](#constraints-370)Constraints

**Type**: `object`

#### [](#description-370)Description

Resources are the resource requirements for the Couchbase server container. This field overrides any automatic allocation as defined by `spec.autoResourceAllocation`.

### [](#couchbaseclusters-spec-servers-servergroups)couchbaseclusters.spec.servers.serverGroups

#### [](#constraints-371)Constraints

**Type**: `[]string`

**Pattern (Regular Expression)**: `^[A-Za-z0-9]([A-Za-z0-9._-]\*[A-Za-z0-9])?$`

#### [](#description-371)Description

ServerGroups define the set of availability zones you want to distribute pods over, and construct Couchbase server groups for. By default, most cloud providers will label nodes with the key "topology.kubernetes.io/zone", the values associated with that key are used here to provide explicit scheduling by the Operator. You may manually label nodes using the "topology.kubernetes.io/zone" key, to provide failure-domain aware scheduling when none is provided for you. Global server groups are applied to all server classes, and may be overridden on a per-server class basis to give more control over scheduling and server groups.

### [](#couchbaseclusters-spec-servers-services)couchbaseclusters.spec.servers.services

#### [](#constraints-372)Constraints

**Required**

**Type**: `[]string`

**Enumerations**: `admin, data, index, query, search, eventing, analytics`

#### [](#description-372)Description

Services is the set of Couchbase services to run on this server class. At least one class must contain the data service. The field may contain any of "data", "index", "query", "search", "eventing" or "analytics". Each service may only be specified once. An empty list can also be specified for an Arbiter class ("\[\]") if Couchbase version is 7.6.0 or greater.

### [](#couchbaseclusters-spec-servers-size)couchbaseclusters.spec.servers.size

#### [](#constraints-373)Constraints

**Required**

**Type**: `integer`

**Minimum**: `1`

#### [](#description-373)Description

Size is the expected requested of the server class. This field must be greater than or equal to 1.

### [](#couchbaseclusters-spec-servers-volumemounts)couchbaseclusters.spec.servers.volumeMounts

#### [](#constraints-374)Constraints

**Type**: `object`

#### [](#description-374)Description

VolumeMounts define persistent volume claims to attach to pod.

### [](#couchbaseclusters-spec-servers-volumemounts-analytics)couchbaseclusters.spec.servers.volumeMounts.analytics

#### [](#constraints-375)Constraints

**Type**: `[]string`

#### [](#description-375)Description

AnalyticsClaims are persistent volumes that encompass analytics storage associated with the analytics service. Analytics claims can only be used on server classes running the analytics service, and must be used in conjunction with the default claim. This field allows the analytics service to use different storage media (e.g. SSD), and scale horizontally, to improve performance of this service. This field references a volume claim template name as defined in "spec.volumeClaimTemplates".

### [](#couchbaseclusters-spec-servers-volumemounts-data)couchbaseclusters.spec.servers.volumeMounts.data

#### [](#constraints-376)Constraints

**Type**: `string`

#### [](#description-376)Description

DataClaim is a persistent volume that encompasses key/value storage associated with the data service. The data claim can only be used on server classes running the data service, and must be used in conjunction with the default claim. This field allows the data service to use different storage media (e.g. SSD) to improve performance of this service. This field references a volume claim template name as defined in "spec.volumeClaimTemplates".

### [](#couchbaseclusters-spec-servers-volumemounts-default)couchbaseclusters.spec.servers.volumeMounts.default

#### [](#constraints-377)Constraints

**Type**: `string`

#### [](#description-377)Description

DefaultClaim is a persistent volume that encompasses all Couchbase persistent data, including document storage, indexes and logs. The default volume can be used with any server class. Use of the default claim allows the Operator to recover failed pods from the persistent volume far quicker than if the pod were using ephemeral storage. The default claim cannot be used at the same time as the logs claim within the same server class. This field references a volume claim template name as defined in "spec.volumeClaimTemplates".

### [](#couchbaseclusters-spec-servers-volumemounts-index)couchbaseclusters.spec.servers.volumeMounts.index

#### [](#constraints-378)Constraints

**Type**: `string`

#### [](#description-378)Description

IndexClaim s a persistent volume that encompasses index storage associated with the index and search services. The index claim can only be used on server classes running the index or search services, and must be used in conjunction with the default claim. This field allows the index and/or search service to use different storage media (e.g. SSD) to improve performance of this service. This field references a volume claim template name as defined in "spec.volumeClaimTemplates". Whilst this references index primarily, note that the full text search (FTS) service also uses this same mount.

### [](#couchbaseclusters-spec-servers-volumemounts-logs)couchbaseclusters.spec.servers.volumeMounts.logs

#### [](#constraints-379)Constraints

**Type**: `string`

#### [](#description-379)Description

LogsClaim is a persistent volume that encompasses only Couchbase server logs to aid with supporting the product. The logs claim can only be used on server classes running the following services: query, search & eventing. The logs claim cannot be used at the same time as the default claim within the same server class. This field references a volume claim template name as defined in "spec.volumeClaimTemplates". Whilst the logs claim can be used with the search service, the recommendation is to use the default claim for these. The reason for this is that a failure of these nodes will require indexes to be rebuilt and subsequent performance impact.

### [](#couchbaseclusters-spec-softwareupdatenotifications)couchbaseclusters.spec.softwareUpdateNotifications

#### [](#constraints-380)Constraints

**Type**: `boolean`

#### [](#description-380)Description

SoftwareUpdateNotifications enables software update notifications in the UI. When enabled, the UI will alert when a Couchbase server upgrade is available.

### [](#couchbaseclusters-spec-upgrade)couchbaseclusters.spec.upgrade

#### [](#constraints-381)Constraints

**Type**: `object`

#### [](#description-381)Description

Upgrade defines the upgrade configuration for a Couchbase cluster.

### [](#couchbaseclusters-spec-upgrade-previousversionpodcount)couchbaseclusters.spec.upgrade.previousVersionPodCount

#### [](#constraints-382)Constraints

**Type**: `integer`

**Default**: `0`

**Minimum**: `0`

#### [](#description-382)Description

PreviousVersionPodCount is the number of pods that will be left running at the existing version. NOTE: The cluster will not be fully upgraded until all pods are at the new version. The default is 0.

### [](#couchbaseclusters-spec-upgrade-rollingupgrade)couchbaseclusters.spec.upgrade.rollingUpgrade

#### [](#constraints-383)Constraints

**Type**: `object`

#### [](#description-383)Description

When `spec.upgradeStrategy` is set to `RollingUpgrade` it will, by default, upgrade one pod at a time. If this field is specified then that number can be increased.

### [](#couchbaseclusters-spec-upgrade-rollingupgrade-maxupgradable)couchbaseclusters.spec.upgrade.rollingUpgrade.maxUpgradable

#### [](#constraints-384)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-384)Description

MaxUpgradable allows the number of pods affected by an upgrade at any one time to be increased. By default a rolling upgrade will upgrade one pod at a time. This field allows that limit to be removed. This field must be greater than zero. The smallest of `maxUpgradable` and `maxUpgradablePercent` takes precedence if both are defined.

### [](#couchbaseclusters-spec-upgrade-rollingupgrade-maxupgradablepercent)couchbaseclusters.spec.upgrade.rollingUpgrade.maxUpgradablePercent

#### [](#constraints-385)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(100|[1-9][0-9]|[1-9])%$`

#### [](#description-385)Description

MaxUpgradablePercent allows the number of pods affected by an upgrade at any one time to be increased. By default a rolling upgrade will upgrade one pod at a time. This field allows that limit to be removed. This field must be an integer percentage, e.g. "10%", in the range 1% to 100%. Percentages are relative to the total cluster size, and rounded down to the nearest whole number, with a minimum of 1\. For example, a 10 pod cluster, and 25% allowed to upgrade, would yield 2.5 pods per iteration, rounded down to 2\. The smallest of `maxUpgradable` and `maxUpgradablePercent` takes precedence if both are defined.

### [](#couchbaseclusters-spec-upgrade-stabilizationperiod)couchbaseclusters.spec.upgrade.stabilizationPeriod

#### [](#constraints-386)Constraints

**Type**: `string`

#### [](#description-386)Description

StabilizationPeriod is the time the operator will wait after an upgrade cycle before starting the next upgrade cycle. If not specified the operator will start the next upgrade immediately.

### [](#couchbaseclusters-spec-upgrade-upgradeorder)couchbaseclusters.spec.upgrade.upgradeOrder

#### [](#constraints-387)Constraints

**Type**: `[]string`

#### [](#description-387)Description

UpgradeOrder defines the sequence in which nodes will be upgraded. The sequence will be interpreted based on what `spec.upgrade.upgradeOrderBy` is set to. If `spec.upgrade.upgradeOrderType` is set to "Nodes" then the sequence will be a list of node names. If `spec.upgrade.upgradeOrderType` is set to "ServerGroups" then the sequence will be a list of server group names. If `spec.upgrade.upgradeOrderType` is set to "ServerClasses" then the sequence will be a list of server class names. If `spec.upgrade.upgradeOrderType` is set to "Services" then the sequence will be a list of service names.

### [](#couchbaseclusters-spec-upgrade-upgradeordertype)couchbaseclusters.spec.upgrade.upgradeOrderType

#### [](#constraints-388)Constraints

**Type**: `string`

**Default**: `Nodes`

**Enumerations**: `Nodes, ServerGroups, ServerClasses, Services`

#### [](#description-388)Description

UpgradeOrderType defines the order in which spec.upgrade.upgradeOrderSequence will be interpreted.

### [](#couchbaseclusters-spec-upgrade-upgradeprocess)couchbaseclusters.spec.upgrade.upgradeProcess

#### [](#constraints-389)Constraints

**Type**: `string`

**Default**: `SwapRebalance`

**Enumerations**: `SwapRebalance, DeltaRecovery, InPlaceUpgrade`

#### [](#description-389)Description

UpgradeProcess defines the process that will be used when performing a couchbase cluster upgrade. When SwapRebalance is requested (default), pods will be upgraded using either a RollingUpgrade or ImmediateUpgrade (determined by UpgradeStrategy). When InPlaceUpgrade is requested, the operator will perform an in-place upgrade on a best effort basis. InPlaceUpgrade cannot be used if the UpgradeStrategy is set to ImmediateUpgrade.

### [](#couchbaseclusters-spec-upgrade-upgradestrategy)couchbaseclusters.spec.upgrade.upgradeStrategy

#### [](#constraints-390)Constraints

**Type**: `string`

**Default**: `RollingUpgrade`

**Enumerations**: `RollingUpgrade, ImmediateUpgrade`

#### [](#description-390)Description

UpgradeStrategy controls how aggressive the Operator is when performing a cluster upgrade. When a rolling upgrade is requested, pods are upgraded one at a time. This strategy is slower, however less disruptive. When an immediate upgrade strategy is requested, all pods are upgraded at the same time. This strategy is faster, but more disruptive. This field must be either "RollingUpgrade" or "ImmediateUpgrade", defaulting to "RollingUpgrade".

### [](#couchbaseclusters-spec-upgradeprocess)couchbaseclusters.spec.upgradeProcess

#### [](#constraints-391)Constraints

**Type**: `string`

**Enumerations**: `SwapRebalance, DeltaRecovery, InPlaceUpgrade`

#### [](#description-391)Description

**DEPRECATED** \- By spec.upgrade.upgradeProcess.

UpgradeProcess defines the process that will be used when performing a couchbase cluster upgrade. When SwapRebalance is requested (default), pods will be upgraded using either a RollingUpgrade or ImmediateUpgrade (determined by UpgradeStrategy). When InPlaceUpgrade is requested, the operator will perform an in-place upgrade on a best effort basis. InPlaceUpgrade cannot be used if the UpgradeStrategy is set to ImmediateUpgrade.

### [](#couchbaseclusters-spec-upgradestrategy)couchbaseclusters.spec.upgradeStrategy

#### [](#constraints-392)Constraints

**Type**: `string`

**Enumerations**: `RollingUpgrade, ImmediateUpgrade`

#### [](#description-392)Description

**DEPRECATED** \- By spec.upgrade.upgradeStrategy.

UpgradeStrategy controls how aggressive the Operator is when performing a cluster upgrade. When a rolling upgrade is requested, pods are upgraded one at a time. This strategy is slower, however less disruptive. When an immediate upgrade strategy is requested, all pods are upgraded at the same time. This strategy is faster, but more disruptive. This field must be either "RollingUpgrade" or "ImmediateUpgrade", defaulting to "RollingUpgrade".

### [](#couchbaseclusters-spec-volumeclaimtemplates)couchbaseclusters.spec.volumeClaimTemplates

#### [](#constraints-393)Constraints

**Type**: `[]object`

#### [](#description-393)Description

VolumeClaimTemplates define the desired characteristics of a volume that can be requested/claimed by a pod, for example the storage class to use and the volume size. Volume claim templates are referred to by name by server class volume mount configuration.

### [](#couchbaseclusters-spec-xdcr)couchbaseclusters.spec.xdcr

#### [](#constraints-394)Constraints

**Type**: `object`

#### [](#description-394)Description

XDCR defines whether the Operator should manage XDCR, remote clusters and how to lookup replication resources.

### [](#couchbaseclusters-spec-xdcr-globalsettings)couchbaseclusters.spec.xdcr.globalSettings

#### [](#constraints-395)Constraints

**Type**: `object`

#### [](#description-395)Description

GlobalSettings configures cluster-wide XDCR advanced settings. These settings provide defaults for new replications and do not affect existing replications retroactively. Only specified fields are applied; unspecified fields are left unchanged on the server.

### [](#couchbaseclusters-spec-xdcr-globalsettings-checkpointinterval)couchbaseclusters.spec.xdcr.globalSettings.checkpointInterval

#### [](#constraints-396)Constraints

**Type**: `integer`

**Minimum**: `60`

**Maximum**: `14400`

#### [](#description-396)Description

CheckpointInterval is the interval in seconds between checkpoints. This field defaults to 600 and must be between 60 and 14400.

### [](#couchbaseclusters-spec-xdcr-globalsettings-collectionsosomode)couchbaseclusters.spec.xdcr.globalSettings.collectionsOSOMode

#### [](#constraints-397)Constraints

**Type**: `boolean`

#### [](#description-397)Description

CollectionsOSOMode optimizes for out-of-order mutations streaming (performance toggle). This field defaults to true.

### [](#couchbaseclusters-spec-xdcr-globalsettings-compressiontype)couchbaseclusters.spec.xdcr.globalSettings.compressionType

#### [](#constraints-398)Constraints

**Type**: `string`

**Enumerations**: `Auto, None`

#### [](#description-398)Description

CompressionType is the compression used for XDCR traffic. This field must be one of "Auto" or "None", defaulting to "Auto".

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging

#### [](#constraints-399)Constraints

**Type**: `object`

#### [](#description-399)Description

ConflictLogging is the configuration for conflict logging. This feature is available in Couchbase Server 8.0.0 and later.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-enabled)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.enabled

#### [](#constraints-400)Constraints

**Type**: `boolean`

#### [](#description-400)Description

Enabled defines whether conflict logging is enabled.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-logcollection)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.logCollection

#### [](#constraints-401)Constraints

**Type**: `object`

#### [](#description-401)Description

LogCollection defines the collection to log conflicts to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-logcollection-bucket)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.logCollection.bucket

#### [](#constraints-402)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-402)Description

Bucket defines the bucket to log conflicts to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-logcollection-collection)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.logCollection.collection

#### [](#constraints-403)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-403)Description

Collection defines the collection to log conflicts to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-logcollection-scope)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.logCollection.scope

#### [](#constraints-404)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-404)Description

Scope defines the scope to log conflicts to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules

#### [](#constraints-405)Constraints

**Type**: `object`

#### [](#description-405)Description

LoggingRules defines the list of logging rules for conflict logging. The rules can be scoped to a specific scope or a specific collection in a scope. The rules can disable logging, log to the default collection defined at `spec.conflictLogging.logCollection`, or log to a different collection.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-customcollectionrules)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.customCollectionRules

#### [](#constraints-406)Constraints

**Type**: `[]object`

#### [](#description-406)Description

CustomCollectionRules defines the rules for logging to a different collection.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-customcollectionrules-collection)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.customCollectionRules.collection

#### [](#constraints-407)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-407)Description

Collection defines the collection to apply the rule to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-customcollectionrules-logcollection)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.customCollectionRules.logCollection

#### [](#constraints-408)Constraints

**Required**

**Type**: `object`

#### [](#description-408)Description

LogCollection defines the collection to log conflicts to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-customcollectionrules-logcollection-bucket)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.customCollectionRules.logCollection.bucket

#### [](#constraints-409)Constraints

**Type**: `string`

**Maximum Length**: `100`

**Pattern (Regular Expression)**: `^[a-zA-Z0-9-_%\.]{1,100}$`

#### [](#description-409)Description

Bucket defines the bucket to log conflicts to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-customcollectionrules-logcollection-collection)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.customCollectionRules.logCollection.collection

#### [](#constraints-410)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-410)Description

Collection defines the collection to log conflicts to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-customcollectionrules-logcollection-scope)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.customCollectionRules.logCollection.scope

#### [](#constraints-411)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-411)Description

Scope defines the scope to log conflicts to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-customcollectionrules-scope)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.customCollectionRules.scope

#### [](#constraints-412)Constraints

**Required**

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-412)Description

Scope defines the scope to apply the rule to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-defaultcollectionrules)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.defaultCollectionRules

#### [](#constraints-413)Constraints

**Type**: `[]object`

#### [](#description-413)Description

DefaultCollectionRules defines the rules for logging to the default collection.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-defaultcollectionrules-collection)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.defaultCollectionRules.collection

#### [](#constraints-414)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-414)Description

Collection defines the collection to apply the rule to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-defaultcollectionrules-scope)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.defaultCollectionRules.scope

#### [](#constraints-415)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-415)Description

Scope defines the scope to apply the rule to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-nologgingrules)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.noLoggingRules

#### [](#constraints-416)Constraints

**Type**: `[]object`

#### [](#description-416)Description

NoLoggingRules defines the rules for disabling logging to for conflicts in a specific scope or collection.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-nologgingrules-collection)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.noLoggingRules.collection

#### [](#constraints-417)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-417)Description

Collection defines the collection to apply the rule to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-conflictlogging-loggingrules-nologgingrules-scope)couchbaseclusters.spec.xdcr.globalSettings.conflictLogging.loggingRules.noLoggingRules.scope

#### [](#constraints-418)Constraints

**Type**: `string`

**Minimum Length**: `1`

**Maximum Length**: `251`

**Pattern (Regular Expression)**: `^(_default|[a-zA-Z0-9\-][a-zA-Z0-9\-%_]{0,250})$`

#### [](#description-418)Description

Scope defines the scope to apply the rule to.

### [](#couchbaseclusters-spec-xdcr-globalsettings-desiredlatency)couchbaseclusters.spec.xdcr.globalSettings.desiredLatency

#### [](#constraints-419)Constraints

**Type**: `integer`

#### [](#description-419)Description

DesiredLatency is the target latency (ms) for high-priority replications; lower values result in faster replication but greater load. This field defaults to 50.

### [](#couchbaseclusters-spec-xdcr-globalsettings-docbatchsizekb)couchbaseclusters.spec.xdcr.globalSettings.docBatchSizeKb

#### [](#constraints-420)Constraints

**Type**: `integer`

**Minimum**: `10`

**Maximum**: `10000`

#### [](#description-420)Description

DocBatchSizeKb is the size (KB) of document batches sent. This field defaults to 2048 and must be between 10 and 10000.

### [](#couchbaseclusters-spec-xdcr-globalsettings-failurerestartinterval)couchbaseclusters.spec.xdcr.globalSettings.failureRestartInterval

#### [](#constraints-421)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `300`

#### [](#description-421)Description

FailureRestartInterval is the seconds to wait before restarting after a failure. This field defaults to 10 and must be between 1 and 300.

### [](#couchbaseclusters-spec-xdcr-globalsettings-filterbinary)couchbaseclusters.spec.xdcr.globalSettings.filterBinary

#### [](#constraints-422)Constraints

**Type**: `boolean`

#### [](#description-422)Description

FilterBinary specifies whether binary documents should be replicated. The value can be true or false (the default). If the value is true, binary documents are not replicated, regardless of whether a filterExpression is applied. If the value is false:.

### [](#couchbaseclusters-spec-xdcr-globalsettings-filterbypassexpiry)couchbaseclusters.spec.xdcr.globalSettings.filterBypassExpiry

#### [](#constraints-423)Constraints

**Type**: `boolean`

#### [](#description-423)Description

FilterBypassExpiry when true, TTL is removed before replication. This field defaults to false.

### [](#couchbaseclusters-spec-xdcr-globalsettings-filterbypassuncommittedtxn)couchbaseclusters.spec.xdcr.globalSettings.filterBypassUncommittedTxn

#### [](#constraints-424)Constraints

**Type**: `boolean`

#### [](#description-424)Description

FilterBypassUncommittedTxn when true, documents with uncommitted txn xattrs are not replicated. This field defaults to false.

### [](#couchbaseclusters-spec-xdcr-globalsettings-filterdeletion)couchbaseclusters.spec.xdcr.globalSettings.filterDeletion

#### [](#constraints-425)Constraints

**Type**: `boolean`

#### [](#description-425)Description

FilterDeletion when true, delete mutations are filtered out (not replicated). This field defaults to false.

### [](#couchbaseclusters-spec-xdcr-globalsettings-filterexpiration)couchbaseclusters.spec.xdcr.globalSettings.filterExpiration

#### [](#constraints-426)Constraints

**Type**: `boolean`

#### [](#description-426)Description

FilterExpiration when true, expiry mutations are filtered out. This field defaults to false.

### [](#couchbaseclusters-spec-xdcr-globalsettings-gogc)couchbaseclusters.spec.xdcr.globalSettings.goGC

#### [](#constraints-427)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-427)Description

GoGC is the Go GC target percentage for XDCR processes. Valid values are integers from 1-100, defaulting to 100.

### [](#couchbaseclusters-spec-xdcr-globalsettings-gomaxprocs)couchbaseclusters.spec.xdcr.globalSettings.goMaxProcs

#### [](#constraints-428)Constraints

**Type**: `integer`

#### [](#description-428)Description

GoMaxProcs is the max threads per node for XDCR. This field defaults to 4.

### [](#couchbaseclusters-spec-xdcr-globalsettings-hlvpruningwindowsec)couchbaseclusters.spec.xdcr.globalSettings.hlvPruningWindowSec

#### [](#constraints-429)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-429)Description

HlvPruningWindowSec is the HLV pruning window (sec) for hybrid logical vector conflict resolution.

### [](#couchbaseclusters-spec-xdcr-globalsettings-jsfunctiontimeoutms)couchbaseclusters.spec.xdcr.globalSettings.jsFunctionTimeoutMs

#### [](#constraints-430)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-430)Description

JSFunctionTimeoutMs is the timeout for JS custom conflict-resolution functions (ms).

### [](#couchbaseclusters-spec-xdcr-globalsettings-loglevel)couchbaseclusters.spec.xdcr.globalSettings.logLevel

#### [](#constraints-431)Constraints

**Type**: `string`

**Enumerations**: `Error, Info, Debug, Trace`

#### [](#description-431)Description

LogLevel is the logging verbosity for XDCR. This field must be one of "Error", "Info", "Debug", or "Trace", defaulting to "Info".

### [](#couchbaseclusters-spec-xdcr-globalsettings-mergefunctionmapping)couchbaseclusters.spec.xdcr.globalSettings.mergeFunctionMapping

#### [](#constraints-432)Constraints

**Type**: `map[string]string`

#### [](#description-432)Description

MergeFunctionMapping maps collection specifiers (scope.collection) to merge function names for custom conflict resolution. Note: Global settings only support bucket-level mappings. Collection-level mappings will cause server errors. Nil values can be used to explicitly unset merge functions for specific collections.

### [](#couchbaseclusters-spec-xdcr-globalsettings-mobile)couchbaseclusters.spec.xdcr.globalSettings.mobile

#### [](#constraints-433)Constraints

**Type**: `string`

**Enumerations**: `Off, Active`

#### [](#description-433)Description

Mobile enables mobile (Sync Gateway) active-active mode. This field must be one of "Active" or "Off", defaulting to "Off".

### [](#couchbaseclusters-spec-xdcr-globalsettings-networkusagelimit)couchbaseclusters.spec.xdcr.globalSettings.networkUsageLimit

#### [](#constraints-434)Constraints

**Type**: `integer`

**Minimum**: `0`

#### [](#description-434)Description

NetworkUsageLimit is the upper limit for replication network usage (MB/s). This field defaults to 0 (no limit).

### [](#couchbaseclusters-spec-xdcr-globalsettings-optimisticreplicationthreshold)couchbaseclusters.spec.xdcr.globalSettings.optimisticReplicationThreshold

#### [](#constraints-435)Constraints

**Type**: `integer`

**Minimum**: `0`

**Maximum**: `20971520`

#### [](#description-435)Description

OptimisticReplicationThreshold is the size threshold below which documents replicate optimistically. This field defaults to 256 and must be between 0 and 20971520.

### [](#couchbaseclusters-spec-xdcr-globalsettings-priority)couchbaseclusters.spec.xdcr.globalSettings.priority

#### [](#constraints-436)Constraints

**Type**: `string`

**Enumerations**: `High, Medium, Low`

#### [](#description-436)Description

Priority is the resource priority for replication streams. This field must be one of "High", "Medium", or "Low", defaulting to "High".

### [](#couchbaseclusters-spec-xdcr-globalsettings-retryonremoteautherr)couchbaseclusters.spec.xdcr.globalSettings.retryOnRemoteAuthErr

#### [](#constraints-437)Constraints

**Type**: `boolean`

#### [](#description-437)Description

RetryOnRemoteAuthErr defines whether to retry connections when remote auth fails. This field defaults to true.

### [](#couchbaseclusters-spec-xdcr-globalsettings-retryonremoteautherrmaxwaitsec)couchbaseclusters.spec.xdcr.globalSettings.retryOnRemoteAuthErrMaxWaitSec

#### [](#constraints-438)Constraints

**Type**: `integer`

**Minimum**: `1`

#### [](#description-438)Description

RetryOnRemoteAuthErrMaxWaitSec is the max wait seconds for retrying remote auth failures. Only effective if retryOnRemoteAuthErr is true. This field defaults to 360.

### [](#couchbaseclusters-spec-xdcr-globalsettings-sourcenozzlepernode)couchbaseclusters.spec.xdcr.globalSettings.sourceNozzlePerNode

#### [](#constraints-439)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-439)Description

SourceNozzlePerNode is the number of source nozzles (parallelism) per source node. This field defaults to 2 and must be between 1 and 100.

### [](#couchbaseclusters-spec-xdcr-globalsettings-statsinterval)couchbaseclusters.spec.xdcr.globalSettings.statsInterval

#### [](#constraints-440)Constraints

**Type**: `integer`

**Minimum**: `200`

**Maximum**: `600000`

#### [](#description-440)Description

StatsInterval is the interval for statistics updates (ms). This field defaults to 1000 and must be between 200 and 600000.

### [](#couchbaseclusters-spec-xdcr-globalsettings-targetnozzlepernode)couchbaseclusters.spec.xdcr.globalSettings.targetNozzlePerNode

#### [](#constraints-441)Constraints

**Type**: `integer`

**Minimum**: `1`

**Maximum**: `100`

#### [](#description-441)Description

TargetNozzlePerNode is the number of target nozzles per target node (parallelism). This field defaults to 2 and must be between 1 and 100.

### [](#couchbaseclusters-spec-xdcr-globalsettings-workerbatchsize)couchbaseclusters.spec.xdcr.globalSettings.workerBatchSize

#### [](#constraints-442)Constraints

**Type**: `integer`

**Minimum**: `500`

**Maximum**: `10000`

#### [](#description-442)Description

WorkerBatchSize is the number of mutations per worker batch. This field defaults to 500 and must be between 500 and 10000.

### [](#couchbaseclusters-spec-xdcr-managed)couchbaseclusters.spec.xdcr.managed

#### [](#constraints-443)Constraints

**Type**: `boolean`

#### [](#description-443)Description

Managed defines whether XDCR is managed by the operator or not.

### [](#couchbaseclusters-spec-xdcr-remoteclusters)couchbaseclusters.spec.xdcr.remoteClusters

#### [](#constraints-444)Constraints

**Type**: `[]object`

#### [](#description-444)Description

RemoteClusters is a set of named remote clusters to establish replications to.

### [](#couchbaseclusters-spec-xdcr-remoteclusters-authenticationsecret)couchbaseclusters.spec.xdcr.remoteClusters.authenticationSecret

#### [](#constraints-445)Constraints

**Type**: `string`

#### [](#description-445)Description

AuthenticationSecret is a secret used to authenticate when establishing a remote connection. It is only required when not using mTLS. The secret must contain a username (secret key "username") and password (secret key "password").

### [](#couchbaseclusters-spec-xdcr-remoteclusters-hostname)couchbaseclusters.spec.xdcr.remoteClusters.hostname

#### [](#constraints-446)Constraints

**Required**

**Type**: `string`

**Pattern (Regular Expression)**: `couchbase|http)(s)?(://?\b((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)(\.|${4}\b)|([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)\*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9]|\[(\s\*([0-9A-Fa-f]{1,4}:){7}([0-9A-Fa-f]{1,4}|:|[0-9A-Fa-f]{1,4}:){6}(:[0-9A-Fa-f]{1,4}|((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d{3})|:))|[0-9A-Fa-f]{1,4}:){5}(((:[0-9A-Fa-f]{1,4}){1,2})|:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d{3})|:))|[0-9A-Fa-f]{1,4}:){4}(((:[0-9A-Fa-f]{1,4}){1,3})|((:[0-9A-Fa-f]{1,4})?:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d{3}))|:))|[0-9A-Fa-f]{1,4}:){3}(((:[0-9A-Fa-f]{1,4}){1,4})|((:[0-9A-Fa-f]{1,4}){0,2}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d{3}))|:))|[0-9A-Fa-f]{1,4}:){2}(((:[0-9A-Fa-f]{1,4}){1,5})|((:[0-9A-Fa-f]{1,4}){0,3}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d{3}))|:))|[0-9A-Fa-f]{1,4}:){1}(((:[0-9A-Fa-f]{1,4}){1,6})|((:[0-9A-Fa-f]{1,4}){0,4}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d{3}))|:))|(:(:[0-9A-Fa-f]{1,4}){1,7})|((:[0-9A-Fa-f]{1,4}){0,5}:((25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d)(\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]?\d{3}))|:)))(%.+)?\s\*\]))(:[0-9]{0,5})?(\\{0,1}\?network=[&]+)?$`

#### [](#description-446)Description

Hostname is the connection string to use to connect the remote cluster. To use IPv6, place brackets (`[`, `]`) around the IPv6 value.

### [](#couchbaseclusters-spec-xdcr-remoteclusters-name)couchbaseclusters.spec.xdcr.remoteClusters.name

#### [](#constraints-447)Constraints

**Required**

**Type**: `string`

#### [](#description-447)Description

Name of the remote cluster. Note that, -operator-managed is added as suffix by operator automatically to the name in order to diffrentiate from non operator managed remote clusters.

### [](#couchbaseclusters-spec-xdcr-remoteclusters-replications)couchbaseclusters.spec.xdcr.remoteClusters.replications

#### [](#constraints-448)Constraints

**Type**: `object`

#### [](#description-448)Description

Replications are replication streams from this cluster to the remote one. This field defines how to look up CouchbaseReplication resources. By default any CouchbaseReplication resources in the namespace will be considered.

### [](#couchbaseclusters-spec-xdcr-remoteclusters-replications-selector)couchbaseclusters.spec.xdcr.remoteClusters.replications.selector

#### [](#constraints-449)Constraints

**Type**: `object`

#### [](#description-449)Description

Selector allows CouchbaseReplication resources to be filtered based on labels.

### [](#couchbaseclusters-spec-xdcr-remoteclusters-tls)couchbaseclusters.spec.xdcr.remoteClusters.tls

#### [](#constraints-450)Constraints

**Type**: `object`

#### [](#description-450)Description

TLS if specified references a resource containing the necessary certificate data for an encrypted connection.

### [](#couchbaseclusters-spec-xdcr-remoteclusters-tls-secret)couchbaseclusters.spec.xdcr.remoteClusters.tls.secret

#### [](#constraints-451)Constraints

**Required**

**Type**: `string`

#### [](#description-451)Description

Secret references a secret containing the CA certificate (data key "ca"), and optionally a client certificate (data key "certificate") and key (data key "key").

### [](#couchbaseclusters-spec-xdcr-remoteclusters-uuid)couchbaseclusters.spec.xdcr.remoteClusters.uuid

#### [](#constraints-452)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^[0-9a-f]{32}$`

#### [](#description-452)Description

UUID of the remote cluster. The UUID of a CouchbaseCluster resource is advertised in the status.clusterId field of the resource.

## [](#couchbaseclusters-status)couchbaseclusters.status

### [](#constraints-453)Constraints

**Type**: `object`

### [](#description-453)Description

ClusterStatus defines any read-only status fields for the Couchbase server cluster.

### [](#couchbaseclusters-status-allocations)couchbaseclusters.status.allocations

#### [](#constraints-454)Constraints

**Type**: `[]object`

#### [](#description-454)Description

Allocations shows memory allocations within server classes.

### [](#couchbaseclusters-status-allocations-allocatedmemory)couchbaseclusters.status.allocations.allocatedMemory

#### [](#constraints-455)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-455)Description

AllocatedMemory defines the total memory allocated for constrained Couchbase services. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-status-allocations-allocatedmemorypercent)couchbaseclusters.status.allocations.allocatedMemoryPercent

#### [](#constraints-456)Constraints

**Type**: `integer`

#### [](#description-456)Description

AllocatedMemoryPercent is set when memory resources are requested and define how much of the requested memory is allocated to constrained Couchbase services.

### [](#couchbaseclusters-status-allocations-analyticsserviceallocation)couchbaseclusters.status.allocations.analyticsServiceAllocation

#### [](#constraints-457)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-457)Description

AnalyticsServiceAllocation is set when the analytics service is enabled for this class and defines how much memory this service consumes per pod. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-status-allocations-dataserviceallocation)couchbaseclusters.status.allocations.dataServiceAllocation

#### [](#constraints-458)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-458)Description

DataServiceAllocation is set when the data service is enabled for this class and defines how much memory this service consumes per pod. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-status-allocations-eventingserviceallocation)couchbaseclusters.status.allocations.eventingServiceAllocation

#### [](#constraints-459)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-459)Description

EventingServiceAllocation is set when the eventing service is enabled for this class and defines how much memory this service consumes per pod. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-status-allocations-indexserviceallocation)couchbaseclusters.status.allocations.indexServiceAllocation

#### [](#constraints-460)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-460)Description

IndexServiceAllocation is set when the index service is enabled for this class and defines how much memory this service consumes per pod. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-status-allocations-name)couchbaseclusters.status.allocations.name

#### [](#constraints-461)Constraints

**Required**

**Type**: `string`

#### [](#description-461)Description

Name is the name of the server class defined in spec.servers.

### [](#couchbaseclusters-status-allocations-requestedmemory)couchbaseclusters.status.allocations.requestedMemory

#### [](#constraints-462)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-462)Description

RequestedMemory, if set, defines the Kubernetes resource request for the server class. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-status-allocations-searchserviceallocation)couchbaseclusters.status.allocations.searchServiceAllocation

#### [](#constraints-463)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-463)Description

SearchServiceAllocation is set when the search service is enabled for this class and defines how much memory this service consumes per pod. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-status-allocations-unusedmemory)couchbaseclusters.status.allocations.unusedMemory

#### [](#constraints-464)Constraints

**Type**: `string`

**Pattern (Regular Expression)**: `^(\+|-)?[0-9]+(\.[0-9]*)?)|(\.[0-9]+[KMGTPE]i)|[numkMGTPE]|([eE](\+|-)?(([0-9]+(\.[0-9]\*)?)|(\.[0-9]+))?$`

#### [](#description-464)Description

UnusedMemory is set when memory resources are requested and is the difference between the requestedMemory and allocatedMemory. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/#resource-units-in-kubernetes>.

### [](#couchbaseclusters-status-allocations-unusedmemorypercent)couchbaseclusters.status.allocations.unusedMemoryPercent

#### [](#constraints-465)Constraints

**Type**: `integer`

#### [](#description-465)Description

UnusedMemoryPercent is set when memory resources are requested and defines how much requested memory is not allocated. Couchbase server expects at least a 20% overhead.

### [](#couchbaseclusters-status-autoscalers)couchbaseclusters.status.autoscalers

#### [](#constraints-466)Constraints

**Type**: `[]string`

#### [](#description-466)Description

Autscalers describes all the autoscalers managed by the cluster.

### [](#couchbaseclusters-status-buckets)couchbaseclusters.status.buckets

#### [](#constraints-467)Constraints

**Type**: `[]object`

#### [](#description-467)Description

Buckets describes all the buckets managed by the cluster.

### [](#couchbaseclusters-status-buckets-compressionmode)couchbaseclusters.status.buckets.compressionMode

#### [](#constraints-468)Constraints

**Required**

**Type**: `string`

#### [](#description-468)Description

CompressionMode defines how documents are compressed.

### [](#couchbaseclusters-status-buckets-conflictresolution)couchbaseclusters.status.buckets.conflictResolution

#### [](#constraints-469)Constraints

**Required**

**Type**: `string`

#### [](#description-469)Description

ConflictResolution is relevant for `couchbase` and `ephemeral` bucket types and indicates how to resolve conflicts when using multi-master XDCR.

### [](#couchbaseclusters-status-buckets-enableflush)couchbaseclusters.status.buckets.enableFlush

#### [](#constraints-470)Constraints

**Required**

**Type**: `boolean`

#### [](#description-470)Description

EnableFlush is whether a client can delete all documents in a bucket.

### [](#couchbaseclusters-status-buckets-enableindexreplica)couchbaseclusters.status.buckets.enableIndexReplica

#### [](#constraints-471)Constraints

**Required**

**Type**: `boolean`

#### [](#description-471)Description

EnableIndexReplica is whether indexes against bucket documents are replicated.

### [](#couchbaseclusters-status-buckets-evictionpolicy)couchbaseclusters.status.buckets.evictionPolicy

#### [](#constraints-472)Constraints

**Required**

**Type**: `string`

#### [](#description-472)Description

EvictionPolicy is relevant for `couchbase` and `ephemeral` bucket types and indicates how documents are evicted from memory when it is exhausted.

### [](#couchbaseclusters-status-buckets-iopriority)couchbaseclusters.status.buckets.ioPriority

#### [](#constraints-473)Constraints

**Required**

**Type**: `string`

#### [](#description-473)Description

IoPriority is `low` or `high` depending on the number of threads spawned for data processing.

### [](#couchbaseclusters-status-buckets-memoryquota)couchbaseclusters.status.buckets.memoryQuota

#### [](#constraints-474)Constraints

**Required**

**Type**: `integer`

#### [](#description-474)Description

BucketMemoryQuota is the bucket memory quota in megabytes.

### [](#couchbaseclusters-status-buckets-name)couchbaseclusters.status.buckets.name

#### [](#constraints-475)Constraints

**Required**

**Type**: `string`

#### [](#description-475)Description

BucketName is the full name of the bucket.

### [](#couchbaseclusters-status-buckets-numvbuckets)couchbaseclusters.status.buckets.numVBuckets

#### [](#constraints-476)Constraints

**Type**: `integer`

#### [](#description-476)Description

NumVBuckets is the number of vbuckets in the bucket.

### [](#couchbaseclusters-status-buckets-password)couchbaseclusters.status.buckets.password

#### [](#constraints-477)Constraints

**Required**

**Type**: `string`

#### [](#description-477)Description

BucketPassword will never be populated.

### [](#couchbaseclusters-status-buckets-replicas)couchbaseclusters.status.buckets.replicas

#### [](#constraints-478)Constraints

**Required**

**Type**: `integer`

#### [](#description-478)Description

BucketReplicas is the number of data replicas.

### [](#couchbaseclusters-status-buckets-storagebackend)couchbaseclusters.status.buckets.storageBackend

#### [](#constraints-479)Constraints

**Type**: `string`

#### [](#description-479)Description

BucketStorageBackend is the storage backend of the bucket.

### [](#couchbaseclusters-status-buckets-type)couchbaseclusters.status.buckets.type

#### [](#constraints-480)Constraints

**Required**

**Type**: `string`

#### [](#description-480)Description

BucketType is the type of the bucket.

### [](#couchbaseclusters-status-clusterid)couchbaseclusters.status.clusterId

#### [](#constraints-481)Constraints

**Type**: `string`

#### [](#description-481)Description

ClusterID is the unique cluster UUID. This is generated every time a new cluster is created, so may vary over the lifetime of a cluster if it is recreated by disaster recovery mechanisms.

### [](#couchbaseclusters-status-conditions)couchbaseclusters.status.conditions

#### [](#constraints-482)Constraints

**Type**: `[]object`

#### [](#description-482)Description

Current service state of the Couchbase cluster.

### [](#couchbaseclusters-status-conditions-lasttransitiontime)couchbaseclusters.status.conditions.lastTransitionTime

#### [](#constraints-483)Constraints

**Type**: `string`

#### [](#description-483)Description

Last time the condition transitioned from one status to another.

### [](#couchbaseclusters-status-conditions-lastupdatetime)couchbaseclusters.status.conditions.lastUpdateTime

#### [](#constraints-484)Constraints

**Type**: `string`

#### [](#description-484)Description

Last time the condition status message updated.

### [](#couchbaseclusters-status-conditions-message)couchbaseclusters.status.conditions.message

#### [](#constraints-485)Constraints

**Type**: `string`

#### [](#description-485)Description

A human readable message indicating details about the transition.

### [](#couchbaseclusters-status-conditions-reason)couchbaseclusters.status.conditions.reason

#### [](#constraints-486)Constraints

**Type**: `string`

#### [](#description-486)Description

Unique, one-word, CamelCase reason for the condition’s last transition.

### [](#couchbaseclusters-status-conditions-status)couchbaseclusters.status.conditions.status

#### [](#constraints-487)Constraints

**Required**

**Type**: `string`

#### [](#description-487)Description

Status is the status of the condition. Can be one of True, False, Unknown.

### [](#couchbaseclusters-status-conditions-type)couchbaseclusters.status.conditions.type

#### [](#constraints-488)Constraints

**Required**

**Type**: `string`

**Enumerations**: `Available, Balanced, ManageConfig, Scaling, ScalingUp, ScalingDown, Upgrading, Hibernating, Error, AutoscaleReady, Synchronized, WaitingBetweenMigrations, Migrating, Rebalancing, ExpandingVolume, BucketMigrating, Unreconcilable, WaitingBetweenUpgrades, MixedMode, ManualInterventionRequired, ServicesMismatch`

#### [](#description-488)Description

Type is the type of condition.

### [](#couchbaseclusters-status-controlpaused)couchbaseclusters.status.controlPaused

#### [](#constraints-489)Constraints

**Type**: `boolean`

#### [](#description-489)Description

ControlPaused indicates if the Operator has acknowledged and paused the control of the cluster.

### [](#couchbaseclusters-status-currentversion)couchbaseclusters.status.currentVersion

#### [](#constraints-490)Constraints

**Type**: `string`

#### [](#description-490)Description

CurrentVersion is the current Couchbase version. This reflects the version of the whole cluster, therefore during upgrade, it is only updated when the upgrade has completed.

### [](#couchbaseclusters-status-groups)couchbaseclusters.status.groups

#### [](#constraints-491)Constraints

**Type**: `[]string`

#### [](#description-491)Description

Groups describes all the groups managed by the cluster.

### [](#couchbaseclusters-status-lastupdatetime)couchbaseclusters.status.lastUpdateTime

#### [](#constraints-492)Constraints

**Type**: `string`

#### [](#description-492)Description

LastUpdateTime is the time that the cluster object was last updated.

### [](#couchbaseclusters-status-members)couchbaseclusters.status.members

#### [](#constraints-493)Constraints

**Type**: `object`

#### [](#description-493)Description

Members are the Couchbase members in the cluster.

### [](#couchbaseclusters-status-members-ready)couchbaseclusters.status.members.ready

#### [](#constraints-494)Constraints

**Type**: `[]string`

#### [](#description-494)Description

Ready are the Couchbase members that are clustered and ready to serve client requests. The member names are the same as the Couchbase pod names.

### [](#couchbaseclusters-status-members-unready)couchbaseclusters.status.members.unready

#### [](#constraints-495)Constraints

**Type**: `[]string`

#### [](#description-495)Description

Unready are the Couchbase members not clustered or unready to serve client requests. The member names are the same as the Couchbase pod names.

### [](#couchbaseclusters-status-rebalanceattempts)couchbaseclusters.status.rebalanceAttempts

#### [](#constraints-496)Constraints

**Type**: `integer`

#### [](#description-496)Description

RebalanceAttempts is the number of consecutive reconciliation loops that the operator has failed to rebalance after exhausting all retries.

### [](#couchbaseclusters-status-size)couchbaseclusters.status.size

#### [](#constraints-497)Constraints

**Required**

**Type**: `integer`

#### [](#description-497)Description

Size is the current size of the cluster in terms of pods. Individual pod status conditions are listed in the members status.

### [](#couchbaseclusters-status-users)couchbaseclusters.status.users

#### [](#constraints-498)Constraints

**Type**: `[]string`

#### [](#description-498)Description

Users describes all the users managed by the cluster.