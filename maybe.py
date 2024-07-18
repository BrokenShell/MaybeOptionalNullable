from typing import Union, Any, Callable

# MaybeNumber = int | float
#
#
# def process_number(value: MaybeNumber) -> str:
#     return f"Processed value is {value * 2}"
#
#
# print(process_number(42))
# print(process_number(3.14))


# MaybeCallableString = Union[str, Callable[[], str]]
#
#
# def handle_maybe_callable(value: MaybeCallableString) -> str:
#     if callable(value):
#         return value()
#     return value
#
#
# def greeting() -> str:
#     return "Hello from a function!"
#
#
# print(handle_maybe_callable("Hello from a string!"))
# print(handle_maybe_callable(greeting))


MaybeCallable = Callable[[], Any] | Any


def flatten(maybe_callable: MaybeCallable, *args, **kwargs) -> Any:
    if callable(maybe_callable):
        return flatten(maybe_callable(*args, **kwargs))
    else:
        return maybe_callable
