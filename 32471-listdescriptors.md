- `MiniscriptDescriptor` has a `miniscript::NodeRef` object.
- The `ToPrivateString` of `DescriptorImpl` class calls the `ToStringHelper` function.
- It further calls the `m_node->ToString` function that takes a `ctx` as the first parameter.

```cpp
std::string ToString(const CTx& ctx, bool* has_priv_key = nullptr) const {
```

- In case of `ToPrivateString` callee, a `StringMaker` is passed as the context in the miniscript node function.

```cpp
out = m_node->ToString(StringMaker(arg, m_pubkey_args, type == StringType::PRIVATE), &has_priv_key);
```

- In case of the `ParseScript` callee, a `KeyParser` is passed as the context while creating `node` via
`miniscript::FromString` function. This context would be later used in the `ToString` function of the 
`node`.

```cpp
error = insane_node->ToString(parser);
```