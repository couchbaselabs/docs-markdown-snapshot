[View original HTML](/server/7.6/cli/cbepctl/set-checkpoint_param.html)

> The command `set checkpoint_param` sets the checkpoint. 

## [](#syntax)Syntax

The basic syntax is:

cbepctl [host]:11210 -b [bucket-name] set checkpoint_param [parameter] [value]

## [](#description)Description

This command changes checkpoint configuration parameters.

## [](#options)Options

The following are the command options:

__Table 1\. set checkpoint\_param options__
| Options                                   | Description                                                                                                                                                                                                                                                                        |
| ----------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| max\_checkpoints                          | The expected maximum number of checkpoints in each vBucket on a balanced system. NOTE: This value does not act as a hard limit for a single vBucket. The system uses it along with checkpoint\_memory\_ratio to compute checkpoint\_max\_size, which triggers checkpoint creation. |
| checkpoint\_memory\_ratio                 | Maximum portion of the bucket quota that the system can allocate to checkpoints.                                                                                                                                                                                                   |
| checkpoint\_memory\_recovery\_upper\_mark | Fraction of the checkpoint quota computed by checkpoint\_memory\_ratio that triggers an attempt to release memory from checkpoints.                                                                                                                                                |
| checkpoint\_memory\_recovery\_lower\_mark | Fraction of the checkpoint quota computed by checkpoint\_memory\_ratio that represents the target for checkpoint memory recovery. Memory recovery stops when this target is reached.                                                                                               |
| checkpoint\_max\_size                     | Maximum size in bytes of a single checkpoint. Use 0 to allow ep-engine to configure this value automatically.                                                                                                                                                                      |
| checkpoint\_destruction\_tasks            | Number of background tasks that destroy closed and unreferenced checkpoints to free memory.                                                                                                                                                                                        |