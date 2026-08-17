---
title: Resource Validation
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbase/docs-operator/edit/release/2.8/modules/ROOT/pages/concept-validation.adoc
  xref: xref:2.8@operator::concept-validation.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/operator/2.8/concept-validation.html)

# Resource Validation

> Validating your resources to ensure there are no errors in your deployment. 

## [](#overview)Overview

Validation for couchbase resources is carried out by the admission controller and the operator itself. This will check for any potential errors in the resources and incompatibilities in changes made to cluster resources.

> [!IMPORTANT]
> The admission controller should **always** be run alongside the operator to validate resources. The validation built in to the operator should only be used as a last resort.

### [](#operator-validation)Operator Validation

The operator will carry out the same validations as the admission controller on each reconcile. This will detect any issues in couchbase resources and validate any changes that are made.

> [!WARNING]
> The operator validation may not work correctly if changes are made while the operator pod is down. To ensure this does not happen, either make sure the admission controller is running or that no changes are made while the operator pod is down. If errors do occur, revert your changes.

If the operator detects any errors in a resource during validation, it will not reconcile the resource until the error is resolved. An error condition will be applied to the cluster and the object will have a validation failed status applied to it such as the one below.

```console
Message:
 validation failure list:
  version error: cannot upgrade from 7.6.0 to 7.2.6. Downgrades are not
Reason: ErrorEncountered
Status: True
Type: Error
```

### [](#admission-controller-validation)Admission Controller Validation

The best way to validate resources is via the Admission Controller. This will validate all of the resources regardless of the operator pod running or not. This will allow for the best detection of errors in resources or compatibility errors during upgrades or changes made to any resource.

> [!IMPORTANT]
> The admission controller should always be run alongside the operator. The operator can be run independently of the admission controller however, errors may occur and validation may not be as reliable.