---
title: Use Couchbase AI Data Plane AI Functions
description: Use AI Functions to summarize text, classify content, detect
  sentiment, explain patterns, and more — all within your SQL++ queries.
pubDate: 2026-08-17T09:53:44.266Z
antora:
  editUrl: https://github.com/couchbaselabs/docs-ai/edit/main/modules/build/pages/ai-functions.adoc
  xref: xref:ai:build:ai-functions.adoc[]
---

[Consult the llms.txt file for a full list of contents](/llms.txt)
[View original HTML](/ai/build/ai-functions.html)

# Use Couchbase AI Data Plane AI Functions

> Use AI Functions to summarize text, classify content, detect sentiment, explain patterns, and more — all within your SQL++ queries. 

Couchbase AI Data Plane AI Functions combine SQL++ with language models to analyze your data. Use large language models (LLMs) such as OpenAI, Bedrock, or models hosted in the [AI Data Plane Model Service](model-service/deploy-llm-model.md) to run task-based functions using familiar SQL++ queries directly within Capella's query editor.

The following AI Data Plane AI Functions are available:

* **Sentiment Analysis**: Determines text sentiment, such as positive, negative, neutral, or mixed.
* **Summarization**: Condenses lengthy text into key insights.
* **Classification**: Classifies data based on specified labels to improve organization and decision-making.
* **Entity Extraction**: Identifies user specified labels or entities. For example, you can extract entities such as persons, locations, organizations, and more from text or images.
* **Grammar Correction**: Fixes grammatical errors in the input text.
* **Text Generation**: Produces text from a prompt.
* **Masking**: Hides personally identifiable information (PII) like names and emails.
* **Similarity**: Compares texts and generates scores indicating how similar they are to each other.
* **Translation**: Converts text between languages.
* **Completion**: Allows you to define your own tasks using prompts and generates tailored responses. Combine with AI Guardrails for safe content generation.

> [!NOTE]
> When you use AI Functions, Capella charges based on your Model Service usage and Query Service usage. If you're using external LLMs such as OpenAI and Amazon Bedrock, you incur charges from those model service providers.

## [](#prerequisites)Prerequisites

* You have deployed a [paid](../../cloud/clusters/create-database.md) Capella operational cluster with:

  * Couchbase Server version 8.0 or later. To upgrade your operational cluster, see [Upgrading a Cluster](../../cloud/clusters/upgrade-database.md).
  * The [Query Service](../../cloud/clusters/databases.md#couchbase-services) enabled on 1 of your nodes.
  * The [Developer Pro](../../cloud/billing/billing.md#dev-pro) or [Enterprise](../../cloud/billing/billing.md#enterprise) Support Plan.
  * [Multiple Availability Zones](../../cloud/clusters/databases.md#availability) (AZ).
  * A bucket with scopes, collections, and JSON documents. For more information about how to upload data to Capella, see [Import and Export Data](../../cloud/guides/load.md).  
  If you do not have a dataset, use the `travel-sample` dataset.
* To enable and update AI Functions in the Capella UI, you need 1 of the following organization or project roles:

  * [Organization Owner](../../cloud/organizations/organization-user-roles.md#organization-role-organization-owner)
  * [Project Owner](../../cloud/projects/project-roles.md#project-owner-role)
  * [Cluster Manager](../../cloud/projects/project-roles.md#project-cluster-manager-role)
  * [Data Writer](../../cloud/projects/project-roles.md#project-cluster-data-reader-writer)
* To view and run AI Functions:

  * In the Capella UI Query tab, you must have 1 of the following project roles:

    * [Cluster Viewer](../../cloud/projects/project-roles.md#project-cluster-viewer-role)
    * [Data Reader](../../cloud/projects/project-roles.md#project-cluster-data-reader)
  * Your application must connect using 1 of the following types of cluster access credentials:

    * [Basic access credentials](../../cloud/clusters/cluster-rbac.md#basic-access-credentials)
    * [Advanced access credentials](../../cloud/clusters/cluster-rbac.md#advanced-access-credentials) assigned with a role that includes the `Query Curl Access` [privilege](../../cloud/clusters/cluster-rbac.md#privileges-for-advanced-access-credentials).
* A deployed LLM with:

  * The [AI Data Plane Model Service](model-service/deploy-llm-model.md)
  * [OpenAI](https://openai.com/)
  * [Amazon Bedrock](https://aws.amazon.com/bedrock/)
* (Recommended) If you have a production workload, [enable private networking](../security/add-aws-privatelink.md) to use AI Functions.  
> [!NOTE]  
> If you want to enable private networking for your AI Functions, your AI Data Plane model and Capella operational cluster need to be deployed within the same AWS region.
* (Recommended) You have guardrails selected for your chosen model. This includes keyword filtering and jailbreak detection. Guardrails are important to have when you use the completion function. For more information, see [Deploy a Large Language Model (LLM)](model-service/deploy-llm-model.md).

## [](#enable-ai-functions)Enable AI Functions

You can enable AI Functions on any of your Capella operational clusters. Enabling AI Functions on 1 cluster does not automatically enable it on your other clusters. You need to enable AI Functions individually for each cluster.

To enable AI Data Plane AI Functions:

1. Do 1 of the following:

  1. Go to **AI Data Plane** **AI Functions**.
  2. On the **Operational** tab, click the name of the cluster where you want to enable AI Functions.

    1. Go to **AI Functions**.
2. Click **Enable AI Functions**.
3. Select the functions you want to use, and click **Next**.
4. Select 1 of the model options:  
> [!NOTE]  
> Private networking is only available for AI Data Plane models.

  * AI Data Plane Model
  * OpenAI Model
  * AWS Bedrock Model

  1. Select **Capella Model**.
  2. Choose your AI Data Plane model.
  3. Enter your **API Key ID** and **API Key Token**, or upload your `.txt` credentials file. For more information about API keys for AI Data Plane models, see [Get Started with the Couchbase AI Data Plane APIs](../api-guide/api-start.md).
  4. Click **Next**.

  1. Select **OpenAI Model**.
  2. Choose your OpenAI model.
  3. (Optional) To use a new OpenAI API key, click **Add New OpenAI API Key**.

    1. Click **Add API Key**
    2. Enter a name to identify your API Key in Capella.
    3. Enter your **OpenAI API Key** from OpenAI.
    4. Click **Add Key**.
  4. Choose your OpenAI API Key.
  5. Click **Next**.

  1. Select **AWS Bedrock Model**.
  2. Enter your **Model ID** and choose your AWS **Region**.
  3. (Optional) To use a new Amazon Bedrock key, click **New Bedrock Credentials**.

    1. Click **Add Credentials**
    2. Enter a name to identify your credential in Capella.
    3. Enter your **Access Key ID** and **Secret Access Key** from Amazon Bedrock.
    4. Click **Add Credentials**.
  4. Choose your Bedrock credentials.
  5. Click **Next**.
5. Choose a Capella operational cluster for your functions.
6. (Optional) If your AI Data Plane model and your Capella operational cluster have the same AWS region, choose whether you want to enable private networking for your functions. This enables private networking between your LLM's AWS region and your Capella operational cluster.  
> [!NOTE]  
> You cannot disable private networking later.
7. Click **Complete Setup**.

## [](#run-an-ai-function)Run an AI Function

Run AI Functions like any other SQL++ query using the [Query tab](../../cloud/clusters/query-service/query-workbench.md) on the operational cluster where you have configured AI Functions.

> [!IMPORTANT]
> When using input prompts with AI Data Plane, Bedrock, or OpenAI LLMs, turn on model guardrails for security.

Experiment with AI Functions with your own data or by loading a sample query into the Query tab of your operational cluster. The following sample queries require the `travel-sample` dataset on the same cluster where you configured your AI Functions LLM.

For more information about how to load the `travel-sample` into your operational cluster, see [Import Sample Data](../../cloud/clusters/data-service/import-data-documents.md#import-sample-data).

To load a sample query:

1. Copy a [sample query](#sample-queries) from the list of AI Data Plane AI Functions available. For example, copy the sample query for [Sentiment Analysis](#sentiment-analysis).
2. In your Capella operational cluster, go to **Data Tools** **Query**.
3. In the query editor, replace the existing text with the sample query you copied.
4. Press Enter or click **Run**. The query results are automatically displayed in JSON format.

Test these functions using your own data, queries, and prompts. You can specify a prompt in the SQL++ statement for prompt engineering to guide the LLM. Use prompts to capture language, output format, examples, and other nuances that the LLM requires to perform these functions.

AI Function performance depends on the number and size of query nodes, data volume, and query complexity. Larger or more complex queries may require [scaling your cluster](../../cloud/clusters/scale-database.md) to maintain performance.

> [!NOTE]
> If you receive an error code `3000` after running your query, it indicates the function you're using is not enabled or associated with an LLM. You need to [enable the function](#enable-ai-functions) and try again. For more information about SQL++ error codes, see [SQL++ Error Codes](../../cloud/n1ql/n1ql-language-reference/n1ql-error-codes.md).

## [](#view-ai-functions)View AI Functions

To view a list of AI Functions in your organization and their associated operational clusters:

1. Go to **AI Data Plane** **AI Functions**.
2. (Optional) Filter the list of AI Functions by their associated operational cluster, function name, and model service provider.

To view more details about the AI Functions associated with an operational cluster, do 1 of the following:

1. Go to **Operational** and click the name of the cluster.

  1. Go to **AI Functions**.
2. From **AI Data Plane** **AI Functions**, click the name of an operational cluster.

You can view the status of each of your AI Functions and [change their associated model](#change-model-association). Click the name of the associated model to get more information.

The status of your AI Function can be dependent on the status of its associated model. An AI function can have 1 of the following statuses:

| Status            | Description                                                                                                                                                           |
| ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Healthy           | The model associated to your AI Functions is in a healthy state.                                                                                                      |
| Unhealthy         | The model associated to your AI Functions is in an unhealthy state.                                                                                                   |
| Deploying         | After you enable your AI Functions, they enter a deploying state. This may take some time. You can use your AI Functions when the status changes to **Healthy**.      |
| Deployment Failed | Your AI Functions failed to deploy.                                                                                                                                   |
| Updating          | Your AI Functions are updating after you changed the associated model. This may take some time. You can use your AI Functions when the status changes to **Healthy**. |

## [](#change-model-association)Change Model Association for an AI Function

You can change the model associated with your AI Function. The model options for AI Functions include:

* An AI Data Plane model
* An OpenAI model
* An AWS Bedrock model

To change the model associated with your AI Function:

1. On the **Operational** tab, click the name of the cluster where you want to change the model association for your AI Functions.
2. Go to **AI Functions**.
3. Find the AI Function you want to associate with a different model and go to **More Options (⋮)** **Edit associated model**.
4. Select 1 of the model options:

  * AI Data Plane Model
  * OpenAI Model
  * AWS Bedrock Model

  1. Select **Capella Model**.
  2. Choose your AI Data Plane model.
  3. Enter your **API Key ID** and **API Key Token**, or upload your `.txt` credentials file. For more information about API keys for AI Data Plane models, see [Get Started with the Couchbase AI Data Plane APIs](../api-guide/api-start.md).
  4. Click **Next**.

  1. Select **OpenAI Model**.
  2. Choose your OpenAI model.
  3. (Optional) To use a new OpenAI API key, click **Add New OpenAI API Key**.

    1. Click **Add API Key**
    2. Enter a name to identify your API Key in Capella.
    3. Enter your **OpenAI API Key** from OpenAI.
    4. Click **Add Key**.
  4. Choose your OpenAI API Key.
  5. Click **Next**.

  1. Select **AWS Bedrock Model**.
  2. Enter your **Model ID** and choose your AWS **Region**.
  3. (Optional) To use a new Amazon Bedrock key, click **New Bedrock Credentials**.

    1. Click **Add Credentials**
    2. Enter a name to identify your credential in Capella.
    3. Enter your **Access Key ID** and **Secret Access Key** from Amazon Bedrock.
    4. Click **Add Credentials**.
  4. Choose your Bedrock credentials.
  5. Click **Next**.
5. Click **Associate Functions**.

## [](#delete-ai-functions)Delete AI Functions

You cannot delete an AI Function. Once you have deployed an AI Function, you cannot remove it from the operational cluster.

You can only [change the model](#change-model-association) associated with that AI Function.

## [](#sample-queries)View Sample Queries

View sample queries for all the available AI Functions and their general responses:

* [Sentiment Analysis](#sentiment-analysis)
* [Summarization](#summarization)
* [Classification](#classification)
* [Entity Extraction](#entity-extraction)
* [Grammar Correction](#grammar-correction)
* [Text Generation](#text-generation)
* [Masking](#masking)
* [Similarity](#similarity)
* [Translation](#translation)
* [Completion](#completion)

> [!NOTE]
> Model Type
> 
> When working with different LLMs, keep the following in mind:
> 
> * Responses may vary slightly depending on the model selected.
> * When using reasoning models, it's recommended to set a higher `max_tokens` value. For these models, reasoning tokens count towards the total token limit. If your token limit is too low, it may cause truncated responses.

### [](#sentiment-analysis)Sentiment Analysis

To analyze the sentiment of a text, use the `ai_sentiment` function. The LLM identifies the sentiment as either positive, negative, neutral, or mixed.

In the following example using the `travel-sample` dataset, the LLM has identified the hostel review as positive:

Query

```sql++
SELECT h.name AS hotel_name,
       r.author,
       r.content,
       default:ai_sentiment({
           "text": r.content,
           "temperature": 0.3,
           "max_tokens": 500
       }) AS review_sentiment
FROM `travel-sample`.`inventory`.`hotel` AS h
UNNEST h.reviews AS r
LIMIT 1;
```

Result

```json
[
  {
    "hotel_name": "Medway Youth Hostel",
    "author": "Ozella Sipes",
    "content": "This was our 2nd trip here and we enjoyed it as much or more than last year. Excellent location across from the French Market and just across the street from the streetcar stop. Very convenient to several small but good restaurants. Very clean and well maintained. Housekeeping and other staff are all friendly and helpful. We really enjoyed sitting on the 2nd floor terrace over the entrance and \"people-watching\" on Esplanade Ave., also talking with our fellow guests. Some furniture could use a little updating or replacement, but nothing major.",
    "review_sentiment": [
      {
        "response": "The sentiment of the text is overwhelmingly positive. The reviewer expresses enjoyment of their stay, highlighting the excellent location, convenience, cleanliness, and the friendliness of the staff. They mention specific positive experiences, such as sitting on the terrace and interacting with other guests"
      }
    ]
  }
]
```

### [](#summarization)Summarization

To summarize a long text, use the `ai_summary` function. With the provided text, the LLM returns a concise summary within your specified word limit.

In the following example using the `travel-sample` dataset, the LLM has summarized long hotel descriptions with a 20 word limit:

Query

```sql++
SELECT name,
       default:ai_summary({
           "text": description,
           "max_words": 200,
           "temperature": 0.4
       }) AS summarized_description
FROM `travel-sample`.`inventory`.`hotel`
WHERE description IS NOT NULL
LIMIT 2;
```

Result

```json
[
  {
    "name": "Medway Youth Hostel",
    "summarized_description": [
      {
        "response": "40-bed summer hostel in a converted Oast House, 3 miles from Gillingham, in a semi-rural area."
      }
    ]
  },
  {
    "name": "The Balmoral Guesthouse",
    "summarized_description": [
      {
        "response": "Modernized, affordable guesthouse near Gillingham station with cooking facilities, no meals provided."
      }
    ]
  }
]
```

### [](#classification)Classification

To classify your data into specific categories, use the `ai_classification` function. Provide the specific classes you want the LLM to use.

In the following example using the `travel-sample` dataset, the LLM has classified different airlines into flight categories:

```sql++
SELECT name,
       callsign,
       default:ai_classification({
           "text": name,
           "labels": ["commercial", "charter", "cargo"],
           "temperature": 0.2,
           "max_tokens": 600
       }) AS airline_category
FROM `travel-sample`.`inventory`.`airline`
LIMIT 10;
```

Result

```json
[
  {
    "name": "40-Mile Air",
    "callsign": "MILE-AIR",
    "airline_category": [
      {
        "response": "charter"
      }
    ]
  },
  {
    "name": "Texas Wings",
    "callsign": "TXW",
    "airline_category": [
      {
        "response": "cargo"
      }
    ]
  },
  {
    "name": "Atifly",
    "callsign": "atifly",
    "airline_category": [
      {
        "response": "cargo"
      }
    ]
  },
  {
    "name": "Jc royal.britannica",
    "callsign": null,
    "airline_category": [
      {
        "response": "cargo"
      }
    ]
  },
  {
    "name": "Locair",
    "callsign": "LOCAIR",
    "airline_category": [
      {
        "response": "cargo"
      }
    ]
  },
  {
    "name": "SeaPort Airlines",
    "callsign": "SASQUATCH",
    "airline_category": [
      {
        "response": "charter"
      }
    ]
  },
  {
    "name": "Alaska Central Express",
    "callsign": "ACE AIR",
    "airline_category": [
      {
        "response": "cargo"
      }
    ]
  },
  {
    "name": "Astraeus",
    "callsign": "FLYSTAR",
    "airline_category": [
      {
        "response": "cargo"
      }
    ]
  },
  {
    "name": "Air Austral",
    "callsign": "REUNION",
    "airline_category": [
      {
        "response": "cargo"
      }
    ]
  },
  {
    "name": "Airlinair",
    "callsign": "AIRLINAIR",
    "airline_category": [
      {
        "response": "commercial"
      }
    ]
  }
]
```

### [](#entity-extraction)Entity Extraction

To extract specific information from a text, use the `ai_extraction` function. Given a text, provide specific labels you want to define. The LLM identifies and returns relevant data corresponding to your labels.

In the following example using the `travel-sample` dataset, the LLM has extracted the name of the organization and the location of the provided text:

```sql++
SELECT name,
       content,
       default:ai_extraction({
           "text": content,
           "labels": ["organization", "location"],
           "temperature": 0.3,
           "max_tokens": 2000
       }) AS extracted_entities
FROM `travel-sample`.`inventory`.`landmark`
WHERE content IS NOT NULL
LIMIT 1;
```

Result

```json
[
  {
    "name": "Royal Engineers Museum",
    "content": "Adult - £6.99 for an Adult ticket that allows you to come back for further visits within a year (children's and concessionary tickets also available). Museum on military engineering and the history of the British Empire. A quite extensive collection that takes about half a day to see. Of most interest to fans of British and military history or civil engineering. The outside collection of tank mounted bridges etc can be seen for free. There is also an extensive series of themed special event weekends, admission to which is included in the cost of the annual ticket.",
    "extracted_entities": [
      {
        "response": "{organization: Museum on military engineering, location: British Empire}"
      }
    ]
  }
]
```

### [](#grammar-correction)Grammar Correction

To correct the grammatical errors of a text, use the `ai_corrected_grammar` function. The LLM analyzes your input text and returns a corrected version with proper English grammar.

In the following example using the `travel-sample` dataset, the LLM has corrected the grammatical errors of a hotel review:

```sql++
SELECT r.content AS original_review,
       default:ai_corrected_grammar({
           "text": r.content,
           "temperature": 0.2,
           "max_tokens": 3000
       }) AS corrected_review
FROM `travel-sample`.`inventory`.`hotel` AS h
UNNEST h.reviews AS r
WHERE r.content IS NOT NULL
LIMIT 1;
```

Result

```json
[
  {
    "original_review": "This was our 2nd trip here and we enjoyed it as much or more than last year. Excellent location across from the French Market and just across the street from the streetcar stop. Very convenient to several small but good restaurants. Very clean and well maintained. Housekeeping and other staff are all friendly and helpful. We really enjoyed sitting on the 2nd floor terrace over the entrance and \"people-watching\" on Esplanade Ave., also talking with our fellow guests. Some furniture could use a little updating or replacement, but nothing major.",
    "corrected_review": [
      {
        "response": "This was our second trip here, and we enjoyed it as much, if not more, than last year. The location is excellent, across from the French Market, and just across the street from the streetcar stop, making it very convenient to several small but good restaurants. The property is very clean"
      }
    ]
  }
]
```

### [](#text-generation)Text Generation

To generate text from a prompt, use the `ai_generated_text` function. Supply a prompt and a set of labels. The LLM generates and returns relevant data corresponding to each label.

In the following example using the `travel-sample` dataset, the LLM has generated promo titles for different hotels:

```sql++
SELECT name,
       default:ai_generated_text({
           "prompt": "Create a hotel stay promo title for " || name,
           "temperature": 0.8,
           "max_tokens": 1000
       }) AS promo_title
FROM `travel-sample`.`inventory`.`hotel`
WHERE vacancy = TRUE
LIMIT 2;
```

Result

```json
[
  {
    "name": "Medway Youth Hostel",
    "promo_title": [
      {
        "response": "Experience Unforgettable Nights at Medway Youth Hostel: 20% Off & Breakfast Included!"
      }
    ]
  },
  {
    "name": "The Robins",
    "promo_title": [
      {
        "response": "Luxury Escape: 30% Off Stay at The Robins – Indulge in Complimentary Amenities"
      }
    ]
  }
]
```

### [](#masking)Masking

To protect sensitive information, use the `ai_masked` function. Provide a text and a set of labels identifying entities you want masked. The LLM replaces these entities with placeholders.

In the following example using the `travel-sample` dataset, the LLM has masked the requested labels such as locations, phone numbers, and website URLs:

```sql++
SELECT name,
       content AS original_text,
       default:ai_masked({
           "text": content,
           "labels": ["person", "location", "email", "phone", "website"],
           "temperature": 0.2,
           "max_tokens": 3000
       }) AS masked_text
FROM `travel-sample`.`inventory`.`landmark`
WHERE content LIKE '%@%' OR content LIKE '%contact%'
LIMIT 1;
```

Result

```json
[
  {
    "name": "Isle of Kerrera",
    "original_text": "There are two great hiking trails on the island ([http://www.walkhighlands.co.uk/argyll/kerrera-gylen.shtml South] with '''Gylen Castle''' and [http://www.walkhighlands.co.uk/argyll/kerrera-hutcheson.shtml North] with '''Hutcheson's Monument'''). There is a tiny ferry terminal about 3 km South West of Oban on Gallanach Road and the ferry will bring you to the starting point of the two trails. The [http://www.kerrera-ferry.co.uk ferry] runs throughout the year with more frequent rides in summer (Easter - October) and less frequent ones in winter (October - Easter). £4.50 return for adults, £2.00 return for children, bicycles are free. The ferryman can be contacted by phone: +44 (0)1631 563665 or kerreraferry@hotmail.com. To attract the ferry on the mainland, you need to slide a wooden board to reveal a black surface before the scheduled timing.",
    "masked_text": [
      {
        "response": "There are two great hiking trails on the island ([******* South] with '''Gylen Castle''' and [******* North] with '''Hutcheson's Monument'''). There is a tiny ferry terminal about 3 km South West of ******* on Gallanach Road and the ferry will bring you to the starting point of the two trails. The [******* ferry] runs throughout the year with more frequent rides in summer (Easter - October) and less frequent ones in winter (October - Easter). £4.50 return for adults, £2.00 return for children, bicycles are free. The ferryman can be contacted by phone: ******* or *******. To attract the ferry on the mainland, you need to slide a wooden board to reveal a black surface before the scheduled timing."
      }
    ]
  }
]
```

### [](#similarity)Similarity

To evaluate the relationship between 2 texts, use the `ai_similarity` scoring function that returns a value between 0 and 1\. This score quantifies how close the texts are related in meaning, with 0 indicating no similarity and 1 indicating identical or highly similar content.

In the following example using the `travel-sample` dataset, the LLM identified the similarity scoring of different hotel reviews:

```sql++
SELECT h.name AS hotel_name,
       default:ai_similarity({
           "text1": r1.content,
           "text2": r2.content,
           "temperature": 0.0,
           "max_tokens": 500
       }) AS review_similarity
FROM `travel-sample`.`inventory`.`hotel` AS h
UNNEST h.reviews AS r1
UNNEST h.reviews AS r2
LIMIT 3;
```

Result

```json
[
  {
    "hotel_name": "Medway Youth Hostel",
    "review_similarity": [
      {
        "response": "1.0"
      }
    ]
  },
  {
    "hotel_name": "Medway Youth Hostel",
    "review_similarity": [
      {
        "response": "0.65"
      }
    ]
  },
  {
    "hotel_name": "Medway Youth Hostel",
    "review_similarity": [
      {
        "response": "0.45"
      }
    ]
  }
]
```

### [](#translation)Translation

To translate a text to a specified target language, use the `ai_translation` function. Indicate the language you want your text translated to.

In the following example using the `travel-sample` dataset, the LLM is translating the text from English to Spanish:

```sql++
SELECT name,
       description,
       default:ai_translation({
           "text": description,
           "to_language": "es",
           "temperature": 0.3,
           "max_tokens": 1500
       }) AS description_in_spanish
FROM `travel-sample`.`inventory`.`hotel`
WHERE description IS NOT NULL
LIMIT 2;
```

Result

```json
[
  {
    "name": "Medway Youth Hostel",
    "description": "40 bed summer hostel about 3 miles from Gillingham, housed in a districtive converted Oast House in a semi-rural setting.",
    "description_in_spanish": [
      {
        "response": "Albergue de verano con 40 camas situado a aproximadamente 3 millas de Gillingham, alojado en una distintiva casa convertida de Oast en un entorno semi rural."
      }
    ]
  },
  {
    "name": "The Balmoral Guesthouse",
    "description": "A recently modernised basic but cheap guesthouse across the road from Gillingham station. No meals, but many rooms have a fridge and hob for cooking.",
    "description_in_spanish": [
      {
        "response": "Un hospedaje básico recientemente modernizado, pero económico, ubicado a pocas calles de la estación de Gillingham. No se ofrecen comidas, pero muchas habitaciones tienen un refrigerador y una estufa para cocinar."
      }
    ]
  }
]
```

### [](#completion)Completion

To generate tailored text completions, use the `ai_completion` function. Define a unique system and user prompt, and optionally configure parameters such as temperature and maximum tokens. Unlike other pre-defined functions, your inputs directly shape the LLM's behavior, producing responses aligned with your specific querying needs. As a result, the function provides the flexibility to create your own tasks and design entirely custom interactions with the model.

In the following example using the `travel-sample` dataset, based on the specific request from the system and user prompt, the LLM was able to write unique advertisements for all the hotels in the dataset:

Query

```sql++
SELECT name,
       default:ai_completion({
           "system_prompt": "You are a creative hotel marketing assistant.",
           "user_prompt": "Write a one-line catchy advertisement for the hotel: " || name,
           "temperature": 0.7,
           "max_tokens": 1000
       }) AS ad_slogan
FROM `travel-sample`.`inventory`.`hotel`
LIMIT 5;
```

Result

```json
[
  {
    "name": "Medway Youth Hostel",
    "ad_slogan": [
      {
        "response": "Discover Adventure and Connection at Medway Youth Hostel – Where Every Stay is a New Story!"
      }
    ]
  },
  {
    "name": "The Balmoral Guesthouse",
    "ad_slogan": [
      {
        "response": "Experience timeless elegance and cozy charm at The Balmoral Guesthouse – where every stay feels like coming home!"
      }
    ]
  },
  {
    "name": "The Robins",
    "ad_slogan": [
      {
        "response": "Experience timeless elegance and modern comfort at The Robins—where every stay feels like coming home!"
      }
    ]
  },
  {
    "name": "Le Clos Fleuri",
    "ad_slogan": [
      {
        "response": "Escape to Le Clos Fleuri: Where Every Stay Blooms into a Memorable Experience!"
      }
    ]
  },
  {
    "name": "Glasgow Grand Central",
    "ad_slogan": [
      {
        "response": "Experience timeless elegance and modern luxury at Glasgow Grand Central – where your stay becomes a story worth sharing."
      }
    ]
  }
]
```

## [](#ai-functions-billing)AI Functions Billing

For information about how Couchbase bills you according to your AI Functions usage, see [AI Functions Billing](../../cloud/billing/billing.md#ai-functions).

## [](#next-steps)Next Steps

* [Deploy an Embedding Model](model-service/deploy-embed-model.md)
* [Deploy a Large Language Model (LLM)](model-service/deploy-llm-model.md)