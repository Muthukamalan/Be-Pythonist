## Modules can be imported using
- the `import` statement
- the `importlib.import_module` 

## When a module is imported
- system cache is checked first in `sys.modules`
- if not located
    - finders sys.meta_path
    - loaders ModuleSpec
- "empty" modules created before cache and ref
- ref to the module is added o the system
- module is compiled
- module is executed `module.__dict__`


```python
import math
type(math)
math.__spec__
math.__name__
math.__pakcage__
math.__file__



import fractions
type(fractions)
fractions.__spec__
fractions.__name__
fractions.__package__
fractions.__file__
```

[doc1](https://docs.python.org/3/tutorial/modules.html)
[doc2](https://docs.python.org/3/reference/import.html)
PEP302