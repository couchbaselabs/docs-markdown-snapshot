---
title: What&#8217;s New?
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.5/modules/ROOT/pages/whats-new.adoc
  xref: xref:2.5@operator::whats-new.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.5/whats-new.html)

# What&#8217;s New?

Autonomous Operator 2.5 release is primarily focused on platform updates, feature parity with Couchbase Server, improvements to Pod Management and Security, as well as a number of minor fixes.

## [](#platform-updates)Platform Updates

Autonomous Operator 2.5 is supported on versions 1.24 through 1.28 of Kubernetes, Rancher K3s, the equivalent managed cloud versions from Amazon Elastic Kubernetes Service (EKS), Google Kubernetes Engine (GKE), Microsoft Azure Kubernetes Service (AKS), and Red Hat OpenShift.

## [](#feature-parity-with-couchbase-server)Feature Parity with Couchbase Server

The Operator now allows Data Service (`memcached`) AuxIO and NonIO Threads to be configured. See [couchbaseclusters.spec.cluster.data.auxIOThreads](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-data-auxiothreads) and [couchbaseclusters.spec.cluster.data.nonIOThreads](resource/couchbasecluster.md#couchbaseclusters-spec-cluster-data-noniothreads).

The CouchbaseBackup resource now has a Default Recovery Method which specifies how `cbbackupmgr` should recover from broken Backup/Restore attempts. See [couchbasebackups.spec.defaultRecoveryMethod](resource/couchbasebackup.md#couchbasebackups-spec-defaultrecoverymethod).

## [](#pod-management)Pod Management

The Operator now parallelizes pod creation, for example during cluster creation and when performing upgrades, saving overall wall-clock time.

The Operator now adds specific labels to the PodDisruptionBudget for Cluster Member Pods, to make sure that only Cluster Members are included in the count used during a disruption. Similarly, the internal pod cache behaviour has been improved to only cache Cluster Member pods.

## [](#pod-and-container-security-contexts)Pod and Container Security Contexts

From Operator 2.5, [couchbaseclusters.spec.securityContext](resource/couchbasecluster.md#couchbaseclusters-spec-securitycontext) has been deprecated in favour of [couchbaseclusters.spec.security.podSecurityContext](resource/couchbasecluster.md#couchbaseclusters-spec-security-podsecuritycontext) and [couchbaseclusters.spec.security.securityContext](resource/couchbasecluster.md#couchbaseclusters-spec-security-securitycontext), to define privilege and access control settings for Pods or Containers. See [Configure a Security Context for a Pod or Container](https://kubernetes.io/docs/tasks/configure-pod-container/security-context/) for details.