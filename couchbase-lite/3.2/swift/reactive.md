---
title: Reactive APIs
description: The Reactive APIs are enhanced APIs for Swift that streamline data
  modeling and enable reactive programming patterns.
editUrl: https://github.com/couchbase/docs-couchbase-lite/edit/release/3.2/modules/swift/pages/reactive.adoc
pubDate: 2026-02-20T16:52:32.702Z
link: xref:3.2@couchbase-lite:swift:reactive.adoc[]
---

[View original HTML](/couchbase-lite/3.2/swift/reactive.html)

# Reactive APIs

> The Reactive APIs are enhanced APIs for Swift that streamline data modeling and enable reactive programming patterns. 

The Reactive APIs are designed for developers building apps with SwiftUI, Combine, or Swift’s new Observation framework. They provide two tightly integrated capabilities:

* **Codable protocol compatibility** — enables automatic mapping between Couchbase Lite documents and Swift model objects using the [Codable](https://developer.apple.com/documentation/swift/codable) protocol, reducing boilerplate and improving type safety.
* **Change publishers** — provides [Combine](https://developer.apple.com/documentation/combine) and [Observation](https://developer.apple.com/documentation/observation) publishers for observing changes to queries, documents, and collections, enabling SwiftUI views and view models to react automatically to underlying data updates.

Together, these APIs allow developers to define Swift classes that can be directly persisted as Couchbase Lite documents and observed for changes in a reactive UI context. They eliminate the need for manual dictionary manipulation, JSON conversion, or explicit change listeners.

The Reactive APIs are available for Swift in Couchbase Lite 3.2.3 and later.

## [](#represent-documents-as-codable-model-objects)Represent Documents as Codable Model Objects

Prior to the Reactive APIs, Couchbase Lite developers working with Swift could interact with documents through APIs that require manual handling of data conversion. For example, reading and writing data would often involve using the Mutable Documents abstraction and working directly with dictionary representations. While this approach provides flexibility, it can involve additional steps for developers when integrating Swift models into their applications. For more information, see [Documents](document.md).

The Reactive APIs simplify this process by introducing native adherence to the [Codable](https://developer.apple.com/documentation/swift/codable) protocol. This eliminates intermediate conversion layers, reducing the need to convert from Fleece format to JSON, and then to app-specific object representation.

### [](#map-couchbase-lite-data-to-swift-codable-document-models)Map Couchbase Lite Data to Swift Codable Document Models

A **document model** is a Swift class that conforms to Codable and includes an optional property annotated with `@DocumentID`. This special property wrapper associates the model with a Couchbase Lite document via its unique document ID.

If no document ID is provided, Couchbase Lite generates a new one automatically and assigns to the model when it is encoded and saved.

> [!NOTE]
> Document models must be declared as classes, not structs. This ensures reference semantics and avoids issues where multiple in-memory objects point to the same document.

Example 1\. Data model

```swift
class Task: Codable {
    @DocumentID var id: String?
    var title: String
    var completed: Bool?
}
```

## [](#manipulate-documents-as-codable-model-objects)Manipulate Documents as Codable Model Objects

Once defined, document models can be persisted, retrieved, and removed using type-safe APIs on the Collection object.

### [](#get-a-document-as-a-decodable-object)Get a Document as a Decodable Object

To get a document from a collection and decode it into a Swift model:

* Use the `document` function with the collection.
* Specify the document ID and type.

```swift
let document = try collection.document(id: task.id!, as: Task.self)
```

For API details, see [Document Management](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Collection.html#/Document%20Management).

### [](#save-an-encodable-object-as-a-document)Save an Encodable Object as a Document

To save a document represented by a Swift model object into a collection:

* Use the `save` function with the collection.
* Specify the object.
* Optionally, specify a conflict handler or a concurrency control. By default, last-write-wins concurrency control will be used if a conflict occurs.

```swift
try collection.save(from: task)
```

Specify a conflict handler

```swift
let resolved = try collection.save(from: task) { newTask, existingTask in
    newTask.title = "New Task"
    newTask.completed = false
    return true
}
```

Specify concurrency control

```swift
let resolved = try collection.save(from: task, concurrencyControl: .failOnConflict)
```

For API details, see [Document Management](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Collection.html#/Document%20Management).

### [](#delete-a-document)Delete a Document

To remove a document represented by a Swift model object from a collection:

* Use the `delete` function with the collection.
* Specify the object.
* Optionally, specify a concurrency control. By default, last-write-wins concurrency control will be used if a conflict occurs.

```swift
try collection.delete(for: task)
```

Specify concurrency control

```swift
let resolved = try collection.delete(for: task, concurrencyControl: .failOnConflict)
```

For API details, see [Document Management](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Collection.html#/Document%20Management).

### [](#purge-a-document)Purge a Document

Purging a document is permanent deletion, not replicated.

To purge a document represented by a Swift model object from a collection:

* Use the `purge` function with the collection.
* Specify the object.

```swift
try collection.purge(for: task)
```

For API details, see [Document Management](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Collection.html#/Document%20Management).

## [](#decode-query-results)Decode Query Results

The Reactive APIs enable you to decode Couchbase SQL++ query results directly into model objects. This makes queries observable, so that you can refresh the application automatically as the results change.

With prior solutions such as [Live Queries](query-live.md), you need to trigger user interface updates manually inside the listener. This can lead to complex and difficult-to-maintain state management. With the Reactive APIs, you can use SwiftUI’s minimalistic and declarative approach to manage querying and updating the user interface.

To make query results observable, the model object only needs to conform to the decodable protocol, and does not require a document ID property annotated with the `@DocumentID` property wrapper.

However, if you wish to save any result later, the decoding model must include a document ID property with the `@DocumentID` property wrapper. Additionally, the query result must include a document ID, which can be retrieved using the `meta().id` expression, as shown in [Example 2](#ex-query-doc-id).

Example 2\. Query results with document ID

```sqlpp
SELECT meta().id AS id, title FROM _default.tasks
```

### [](#get-a-query-result-as-decodable)Get a Query Result as Decodable

To get a query’s result as a decodable model object:

* Use the `data` function with the query result.
* Specify the decodable model type.
* Optionally, specify a [data key](#datakey).

```swift
let results = try query.execute().allResults()
for result in results {
    task = try result.data(as: Task.self)
}
```

For API details, see [ReadOnlyArrayProtocol](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Result.html#/ReadOnlyArrayProtocol).

> [!NOTE]
> When saving a document model decoded from the query’s result, the document associated with the model will be retrieved during the save time. As a result, the document may not be the same document during the query time if the document has been changed.

### [](#get-all-query-results-as-decodable)Get All Query Results as Decodable

To get all a query’s results as an array of a decodable model objects:

* Use the `data` function with the query result set.
* Specify the decodable model type.
* Optionally, specify a [data key](#datakey).

```swift
tasks = try query.execute().data(as: Task.self)
```

For API details, see [ResultSet](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/ResultSet.html).

> [!WARNING]
> Getting all the query’s results as an array of decodable model objects may take a long time and consume a large amount of memory, depending on the data size and the number of results.

### [](#datakey)Specify a Data Key

If the query includes a wildcard (`*`), you can provide an optional data key to the `data` function to specify the alias of the `*` dictionary. For instance, in [Example 3](#ex-query-wildcard), the wildcard produces a dictionary with the alias `data`.

Example 3\. Query with a wildcard

```sqlpp
SELECT meta().id AS id, * AS data FROM _default.tasks
```

When using `data(as:, dataKey:)` to decode the query result, setting the data key to `data` ensures the correct source is used.

## [](#publish-change-notifications)Publish Change Notifications

To align with declarative programming paradigms, the Reactive APIs provide an efficient way to publish change notifications. This allows for automatic updates to UI components, streamlined data pipelines, and improved code readability.

To publish change notifications, the Reactive APIs provide interoperability with two underlying Swift frameworks. The way that you use the Reactive APIs differs slightly, depending on the underlying framework. The framework that you use depends on your operating system version.

* The [Combine](https://developer.apple.com/documentation/combine) framework is available in iOS 13 and later, and macOS 10.15 to 14.
* The [Observation](https://developer.apple.com/documentation/observation) framework is available in iOS 17 and later, and macOS 14 and later.

### [](#publish-query-result-changes)Publish Query Result Changes

To get a publisher that emits `QueryChange` events whenever a query result changes:

* Use the `changePublisher` function with the query.
* Optionally, specify the dispatch queue on which the changes are to be delivered. By default, the main queue is used.

```swift
query.changePublisher()
    .map { try! $0.results?.data(as: Task.self) ?? [] }
    .sink { [weak self] tasks in
        self?.tasks = tasks
    }
    .store(in: &cancellables)
```

For API details, see [Query](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Query.html).

> [!NOTE]
> The emitted `QueryChange` contains the entire new result set of the query, not just the delta.

### [](#publish-document-changes)Publish Document Changes

To get a publisher that emits `CollectionChange` events whenever any documents are added, removed or changed in that collection:

* Use the `changePublisher` function with the collection.
* Optionally, specify the dispatch queue on which the changes are to be delivered. By default, the main queue is used.

```swift
collection.changePublisher()
    .sink { change in print("Collection \(change.collection.name) changed.") }
    .store(in: &cancellables)
```

For API details, see [Combine Publisher](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Collection.html#/Combine%20Publisher).

To get a publisher that emits `DocumentChange` events whenever a specific document in a collection changes:

* Use the `documentChangePublisher` function with the collection.
* Specify the document ID.
* Optionally, specify the dispatch queue on which the changes are to be delivered. By default, the main queue is used.

```swift
collection.documentChangePublisher(for: task.id!)
    .sink { change in
        print("Task \(change.documentID) in collection \(change.collection.name) changed.")
    }
    .store(in: &cancellables)
```

For API details, see [Combine Publisher](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Collection.html#/Combine%20Publisher).

### [](#publish-replicator-changes)Publish Replicator Changes

To get a publisher that emits `ReplicatorChange` events when a replicator’s status changes:

* Use the `changePublisher` function with the replicator.
* Optionally, specify the dispatch queue on which the changes are to be delivered. By default, the main queue is used.

```swift
replicator.changePublisher()
    .sink { change in print("Replicator status changed: \(change)") }
    .store(in: &cancellables)
```

For API details, see [Combine Publisher](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Replicator.html#/Combine%20Publisher).

To get a publisher that emits `DocumentReplication` events whenever documents are pushed or pulled during replication:

* Use the `documentReplicationPublisher` function with the replicator.
* Optionally, specify the dispatch queue on which the changes are to be delivered. By default, the main queue is used.

```swift
replicator.documentReplicationPublisher()
    .sink { change in
        change.documents.forEach { task in
            print("Task \(task.id) replicated.")
        }
    }
    .store(in: &cancellables)
```

For API details, see [Combine Publisher](https://docs.couchbase.com/mobile/3.2.4/couchbase-lite-swift/Classes/Replicator.html#/Combine%20Publisher).

## [](#examples)Examples

### [](#viewmodel)ViewModel

* Combine Framework
* Observation Framework

For iOS 13 and later, or macOS 10.15 to 14:

```swift
@MainActor
class TodoViewModel: ObservableObject {
   @Published var todos: [Task] = []

   private let db: Database
   private let tasks: Collection
   private var cancellables = Set<AnyCancellable>()

   init() {
       self.db = AppDataStore.shared.database
       self.tasks = db.collection(name: "tasks")


       let query = "SELECT meta().id, title, completed from tasks"
       try? db.createQuery(query).publish()
           .map { $0.results?.data(as: Task.self) ?? [] }
           .sink { [weak self] tasks in self?.todos = tasks }
           .store(in: &cancellables)
   }

   func addTask(title: String) throws {
       try tasks.save(from: Task(title: title))
   }

   func toggleCompletion(for task: Task) throws {
       if let index = todos.firstIndex(where: { $0.id == task.id }) {
           todos[index].completed.toggle() // Reflect UI right away
           try tasks.save(from: todos[index])
       }
   }

   func deleteTask(_ task: Task) throws {
       try tasks.delete(for: task)
   }
}
```

For iOS 17 and later, or macOS 14 and later:

```swift
@Observable class TodoViewModel {
    var todos: [Task] = []    // Observable property automatically tracked by SwiftUI

    private let db: Database
    private let tasks: Collection

    init() {
        self.db = AppDataStore.shared.database
        self.tasks = db.collection(name: "tasks")

        let query = "SELECT meta().id, title, completed FROM tasks"

        // Subscribe to changes and update todos directly
        try? db.createQuery(query).publish()
            .map { $0.results?.data(as: Task.self) ?? [] }
            .sink { [weak self] tasks in
                self?.todos = tasks
            }
    }

    func addTask(title: String) throws {
        try tasks.save(from: Task(title: title, completed: false))
    }

    func toggleCompletion(for task: Task) throws {
        if let index = todos.firstIndex(where: { $0.id == task.id }) {
            todos[index].completed.toggle()
            try tasks.save(from: todos[index])
        }
    }

    func deleteTask(_ task: Task) throws {
        try tasks.delete(for: task)
    }
}
```

### [](#view)View

* Combine Framework
* Observation Framework

For iOS 13 and later, or macOS 10.15 to 14:

```swift
​​struct TodoListView: View {
    @StateObject private var viewModel = TodoViewModel()

    var body: some View {
        List {
            ForEach(viewModel.todos) { task in
                HStack {
                    Text(task.title)
                    Spacer()
                    Button(action: {
                        try? viewModel.toggleCompletion(for: task)
                    }) {
                        Image(systemName: task.completed ? "checkmark" : "circle")
                            .foregroundColor(task.completed ? .green : .gray)
                    }
                }
            }
            .onDelete { indexSet in
                indexSet.forEach { index in
                    let task = viewModel.todos[index]
                    try? viewModel.deleteTask(task)
                }
            }
        }
        .toolbar {
            ToolbarItem(placement: .navigationBarTrailing) {
                Button(action: { try? viewModel.addTask(title: "New Task") }) {
                    Image(systemName: "plus")
                }
            }
        }
    }
}
```

For iOS 17 and later, or macOS 14 and later:

```swift
​struct TodoView: View {
    @State var viewModel = TodoViewModel()
    @State private var newTaskTitle = ""

    var body: some View {
        VStack {
            TextField("New Task", text: $newTaskTitle)
                .textFieldStyle(.roundedBorder)
                .padding()

            Button("Add") {
                guard !newTaskTitle.isEmpty else { return }
                try? viewModel.addTask(title: newTaskTitle)
                newTaskTitle = ""
            }

            List(viewModel.todos, id: \.id) { task in
                HStack {
                    Button(action: { try? viewModel.toggleCompletion(for: task) }) {
                        Image(systemName: task.completed ? "checkmark.circle.fill" : "circle")
                    }

                    Text(task.title)
                        .strikethrough(task.completed)

                    Spacer()

                    Button(action: { try? viewModel.deleteTask(task) }) {
                        Image(systemName: "trash")
                    }
                }
            }
        }
        .padding()
    }
}
```

## [](#see-also)See Also

* [Manage Scopes and Collections](scopes-collections-manage.md)
* [Documents](document.md)
* [Result Sets](query-resultsets.md)
* [Handling Data Conflicts](conflict.md)