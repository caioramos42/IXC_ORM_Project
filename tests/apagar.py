class Anyclass():
    def __init__(self, value: int, otherValue: int):
        self.value: int = value
        self.otherValue: int = otherValue

value1 = 1
value2 = 2
if init:
    # Does this class have a post-init function?
    has_post_init = hasattr(cls, _POST_INIT_NAME)

    _init_fn(all_init_fields,
                std_init_fields,
                kw_only_init_fields,
                frozen,
                has_post_init,
                # The name to use for the "self"
                # param in __init__.  Use "self"
                # if possible.
                '__dataclass_self__' if 'self' in fields
                else 'self',
                func_builder,
                slots,
                )
print(Anyclass(value1, value2).value)
