# Flexible Types

## Nullable
Nullables are variables that can either hold a value or be None. This approach is common in many programming languages, including Python. While nullables offer a straightforward way to represent the absence of a value, they also introduce the risk of NoneType errors if not handled properly. Developers must constantly check for the presence of None before accessing or manipulating nullable values, adding extra boilerplate code and potential points of failure. Despite their simplicity, nullables require careful management to avoid runtime errors and maintain code stability.

## Optional
Optionals in programming can hold a value or not be passed in at all. In Python, this is often achieved by providing a viable default value for a function argument. This allows developers to write functions that can gracefully handle the absence of certain parameters without requiring explicit checks for null or missing values. The use of optionals ensures that code remains clean and readable, while still providing flexibility in function calls. It eliminates the need for additional conditional logic to handle missing parameters, making the code more concise and less error-prone.

## Maybe
Maybes represent a value that can be one of two or more non-null types. Unlike nullables, which can be None, maybes ensure that the value is always a valid type, thereby eliminating null reference errors. This concept is prevalent in functional programming, where a Maybe type can be used to represent different states or results. For example, a Maybe type might encapsulate either a successful result or an error message, without ever resorting to None. By ensuring that values are always non-null, maybes promote safer and more predictable code, reducing the likelihood of runtime exceptions.

### MaybeCallable
My favorite type of maybe is MaybeCallable. This is a type that must be either a function type or the type that one of those functions can return. For example, a MaybeCallableString would either be a string or a function that returns a string. By avoiding nullables, MaybeCallable ensures that the code always deals with valid, executable functions or a well-defined alternative. This type is particularly useful in scenarios where optional callbacks or handlers are needed, providing a clear and safe way to handle different behaviors without the risk of None or null reference errors. MaybeCallable exemplifies the power and flexibility of maybes, ensuring robust and maintainable code.
