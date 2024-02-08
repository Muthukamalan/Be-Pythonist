# Setup


# Pre-Requisites
- variables and simple types such as `str` , `bool` , `int`  and `float`  types
- `for` and `while`  loops
- `if`...`else`...  statements
- defining functions (using the `def`  statement)
- writing simple classes using the `class`  keyword and the `__init__`  function
- using simple `lists` , `tuples` , `dictionaries`  and `sets`


#  Content [Deep Dive Functional](https://www.udemy.com/course/python-3-deep-dive-part-1/)

## Basics Review
- [X] Type Hierarchy
- [X] Multi-Line Statement and String
- [X] Variable name
- [X] Conditionals
- [X] Functions
- [X] While
- [X] Break,Continue and Try
- [X] For loop
- [X] Classes

## Variables and Memory
- [X] Variable and Memory Reference
- [X] Reference Counting
- [X] Garbage Collection
- [X] Dynamic Vs Static Typing
- [X] Variable Re-Assignment
- [X] Object Mutability
- [X] Function Argument and Mutability
- [X] Shared Reference and Mutability
- [X] Variable Equality
- [X] Everytging is an Object
- [X] Python Optimization: Interning, String Interning, Peephole

## Numeric Types
- [X] Data Types
- [X] Operations
- [X] Constructors and Bases
- [X] Rational Numbers
- [X] Floats: Internal Representation
- [X] Equality Testing
- [X] Coercing to Integers
- [X] Rounding
- [X] Construtors and Contexts
- [X] Math Operation
- [X] Decimals
- [X] Complex Numbers
- [X] Booleans: Truth Values
- [X] Booleans: Precedence and Short-circuiting
- [X] Booleans: Boolean Operation
- [X] Comparison Operators

## Function Parameters
- [X] Argument VS Parameter
- [X] Positional and Keyword Arguments
- [X] Unpacking Iterables
- [X] Extended Unpacking
- [X] *args
- [X] **kwargs
- [X] Putting it all Together
- [X] Appplication: A simple Function Timer
- [X] Parameter Default

## First-Class Functions
- [X] Docstrings and Annotations
- [X] Lambda Expression
- [X] Lambda and Sorting
- [X] Randomize an Iterable using Sorted!! `Challenge`
- [X] Function Introspection
- [X] Callables
- [X] Map, Filter, Zip and List Comprehensions
- [X] Reducing Functions
- [X] Partial Functions
- [X] The operatir Module

## Scopes, Closures and Decorators
- [X] Gloabl and Local Scopes
- [X] Nonlocal Scopes
- [X] Closures
- [X] Closures - Applications 1
- [X] Closures - Applications 2
- [X] Decorators
- [X] Decorators Applications
    -   Timer
    -   Logger
    -   Stacked Decorators
    -   Memoization
- [X] Decorator Factories
- [X] Decorder Application: Dispatching

## Tuples as Data Structures and Named Tuples
- [X] Tuple as Data Struture
- [X] Named Tuples
- [X] Named Tuples: Modifying and Extending
- [X] Named Tuples: DocString and Default Values
- [X] Applications: 
    -   Returing Multipe Values
    -   Alternative to Dictionaries

## Modules, Packages and Namespaces
- [X] Modules
- [X] Imports and Importlib
- [X] Import Variants and Misconceptions
- [ ] Reloading Modules
- [X] Using __main__
- [X] Modules Recap
- [X] packages
- [X] Structing
- [X] Namespace Packges
- [ ] Importing from Zip Archives



# Content [Deep Dive OOPS](https://www.udemy.com/course/python-3-deep-dive-part-4/)

## Classes
- [ ] Objects and Classes
- [ ] Class Attributes
- [ ] Callable Class Attributes
- [ ] Classes are Callables
- [ ] Data Attributes
- [ ] Function Attributes
- [ ] Initializing Class Instances
- [ ] Creating Attributes at Run Time
- [ ] Properties
- [ ] Property Decorators
- [ ] Read-Only and Computed Properties
- [ ] Deleting Properties
- [ ] Some Questions on Property class
- [ ] Class and Static Methods
- [ ] Python Builtin and Standard Types
- [ ] Class Body Scope

## Project 1

## Polymorphism and Special Methods
- [ ] __str__ and __repr__ methods
- [ ] Arithmetic Operators
- [ ] Rich Comparisons
- [ ] Hashing and Equality
- [ ] Booleans
- [ ] Callables
- [ ] __del__ methods
- [ ] __format__ method

## Project 2

## Single Inheritance
- [ ] Single Inheritance
- [ ] Object Class
- [ ] Overriding
- [ ] Extending
- [ ] Delegating
- [ ] Slots
- [ ] Slots and Single Inheritance

## Project 3

## Descriptors
- [ ] Getters and Setters
- [ ] Using as Instance Properties
- [ ] Strong and Weak References
- [ ] Back to Instance Properties
- [ ] __set_name__ method
- [ ] Property Lookup Resolution
- [ ] Properties and Descriptors
- [ ] Application
- [ ] Functions and Descriptors

## Project 4

## Enumeratons
- [ ] Making the case for Enumerations
- [ ] Enumerations 
- [ ] Aliases
- [ ] Customizing/Extending Enums
- [ ] Automatic Values

## Project 5

## Exceptions ( Single Inheritance )
- [ ] Python Exceptions
- [ ] handling Exceptions
- [ ] Raising Exceptions
- [ ] Custom Exceptions

## Project 6

## Metaprogramming
- [ ] Decorators and Descriptors
- [ ] __new__ method
- [ ] How classes are Created
- [ ] Inheriting from type
- [ ] MetaClasses
- [ ] Class Decorators
- [ ] Decorator Classes
- [ ] Metaclass Vs Class Decorator
- [ ] Metaclass Parameters
- [ ] __prepare__ method
- [ ] classes, metaclasses and __call__
- [ ] Metaprogramming Applications
- [ ] Attribute Read Accessors
- [ ] Attribute Write Accessors
- [ ] Accessors



# Content [Pydantic](https://www.udemy.com/course/pydantic/)
## Basics
- [ ] Creating a Pydantic Model
- [ ] Deserialization
- [ ] Serialization
- [ ] Type coercion
- [ ] Required vs optional Fields
- [ ] Nullable Fields
- [ ] Combining Nullable and Optional
- [ ] Inspecting Fields
- [ ] JSON Schema Generation
- [ ] Project

## Model configuration
- [ ] Handling Extra Fields
- [ ] Strict vs Lax Type coercion
- [ ] Validating Default Values
- [ ] Validating Assingments
- [ ] Mutability
- [ ] Coercing Numbers to Strings
- [ ] Standarizing Strings
- [ ] Handling Python Enums
- [ ] Project

## Field Aliasing, Serialization and Deserialization
- [ ] Field Aliases and Default Values
- [ ] Alias Generator Functions
- [ ] Deserializing by Field Name or Alias
- [ ] Serialization Aliases
- [ ] Custom Serializers
- [ ] Project

## Specialized Pydantic Types
- [ ] PositiveInt
- [ ] Constrained Lists
- [ ] UUID
- [ ] Date Related Types
- [ ] Network Types
- [ ] Project

## Additional Field Features
- [ ] Numerical Constraints
- [ ] String Constraints
- [ ] Default Factories
- [ ] Additional Field Configurations
- [ ] Project

## Annotated Types
- [ ] Pydantic and Annotated Types
- [ ] Annotated Types and Type Variables
- [ ] String Constraints
- [ ] Project

## Custom Validators
- [ ] After Validators
- [ ] Before Validators
- [ ] Combining Before and After Validators
- [ ] Custom Validators using Annotated Types
- [ ] Dependent Field Validations
- [ ] Project

## Properties and Computed Fields
- [ ] Properties
- [ ] Computed Fields
- [ ] Project

## Custom Serializers using Annotated Types
- [ ] Custim Serializers with Annotated Types
- [ ] Project

## Complex Models
- [ ] Model Composition
- [ ] Model Inheritance
- [ ] Project

## Pydantic Applications
- [ ] Consuming REST API
- [ ] Ingesting a CSV File
- [ ] Validating Function Arguments
- [ ] Model Code Generators