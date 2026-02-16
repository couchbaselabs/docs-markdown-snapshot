[View original HTML](/ai/build/model-service/configure-llm-performance.html)

> The Capella Model Service offers options to tweak the performance of your LLM. 

The following performance settings are available when deploying a Large Language Model (LLM):

* [Quantization](#quantization)
* [Optimization Profiles](#optimization-profiles)

## [](#quantization)Quantization

Quantization is a technique used to reduce the model size and improve inference speed by representing the model weights with lower precision. You can decrease the memory footprint of the model and speed up response times, making it more efficient for real-time applications. This is useful for deploying LLMs in resource-constrained environments. However, quantization can cause decreased model accuracy, so it’s important to test if it works well for your specific application and use case.

### [](#considerations)Considerations

When choosing to apply quantization to your LLM, consider the following factors:

Performance Needs

If your application requires low latency and fast response times, quantization can help achieve these goals by speeding up inference.

Accuracy Requirements

If your application demands high accuracy and precision, be cautious with quantization as it may introduce some loss in model performance.

Resource Constraints

If you’re deploying the model using limited computational resources or memory, quantization can help reduce the resource requirements.

You cannot customize the quantization settings on all LLMs available through the Model Service.

## [](#optimization-profiles)Optimization Profiles

Tune the performance of your LLM by adjusting various parameters such as batch size, sequence length, and hardware acceleration options all at once by choosing an optimization profile. By selecting the appropriate optimization profile, you can balance between latency and throughput for your specific use case.

The following optimization profiles are available:

Latency

Minimizes time to first token (TTFT) and inter-token latency (ITL) — the time between generating successive tokens. This profile is ideal for real-time applications where immediate responses are critical, such as chatbots, interactive assistants, or live customer support systems.

Throughput

Maximizes the aggregate number of output tokens generated per second across all concurrent requests. This profile focuses on overall throughput rather than per-request speed. It’s ideal for batch processing tasks, bulk content generation, or scenarios where processing multiple requests efficiently is more important than immediate responses to individual requests.

### [](#considerations-2)Considerations

When choosing an optimization profile for your LLM, consider the following factors:

Use Case

The specific requirements of your application influence the ideal optimization profile. For example, real-time applications may prioritize low latency, while batch processing tasks may need high throughput.

Expected Load

Consider your expected request patterns. High-frequency, single-user interactions benefit from latency optimization, while high-volume, multi-user scenarios may benefit from throughput optimization.

You cannot customize the optimization profiles on all LLMs available through the Model Service.

## [](#see-also)See Also

* [Deploy a Large Language Model (LLM)](deploy-llm-model.md)
* [Configure LLM Value Adds](configure-value-adds.md)
* [Configure Guardrails and Security](configure-guardrails-security.md)