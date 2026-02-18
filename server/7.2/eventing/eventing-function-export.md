---
title: Exporting Functions
description: Couchbase provides an option to export Functions as a JSON document.
editUrl: https://github.com/couchbase/docs-server/edit/release/7.2/modules/eventing/pages/eventing-function-export.adoc
pubDate: 2026-02-18T18:09:36.163Z
---

[View original HTML](/server/7.2/eventing/eventing-function-export.html)

# Exporting Functions

> Couchbase provides an option to export Functions as a JSON document. Using the export and import options, you can port defined Functions from your Test-to-Test, Test-to-Production, or Production-to-Production environments. 

To export a Function:

1. Access the **Couchbase Web Console** \> **Eventing** page.
2. Click on any **function name** to expand the UI to show additional controls.  
![addfunc 04 newundeployed](_images/addfunc_04_newundeployed.png)
3. Click on the **Export** button in the Function’s controls. The Function definition gets exported to your local file system.

A sample exported file for the **case\_2\_enrich\_ips** function demonstrated in the [Data Enrichment](eventing-example-data-enrichment.md) Example is shown below. Ensure that you refrain from editing an exported file before importing the file back to the Couchbase cluster.

[{"appcode":"function OnUpdate(doc, meta) {\n  log('document', doc);\n  doc[\"ip_num_start\"] = get_numip_first_3_octets(doc[\"ip_start\"]);\n  doc[\"ip_num_end\"]   = get_numip_first_3_octets(doc[\"ip_end\"]);\n  // !!! write back to the source bucket !!!\n  src[meta.id]=doc;\n}\nfunction get_numip_first_3_octets(ip) {\n  var return_val = 0;\n  if (ip) {\n    var parts = ip.split('.');\n    //IP Number = A x (256*256*256) + B x (256*256) + C x 256 + D\n    return_val = (parts[0]*(256*256*256)) + (parts[1]*(256*256)) + (parts[2]*256) + parseInt(parts[3]);\n    return return_val;\n  }\n}","depcfg":{"buckets":[{"alias":"src","bucket_name":"source","access":"rw"}],"curl":[],"metadata_bucket":"metadata","source_bucket":"source"},"version":"evt-6.5.0-4960-ee","handleruuid":1408181362,"id":0,"function_instance_id":"S8vQl1","appname":"case_2_enrich_ips","settings":{"dcp_stream_boundary":"everything","deadline_timeout":62,"deployment_status":false,"description":"On mutation enrich the mutated document in the same bucket with additional fields","execution_timeout":60,"language_compatibility":"6.5.0","log_level":"INFO","n1ql_consistency":"none","processing_status":false,"user_prefix":"eventing","using_timer":false,"worker_count":3},"using_timer":false,"src_mutation":true}]