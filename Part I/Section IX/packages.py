# packages
# packages are modules (but modules are not necessarily package)
# Thye can contain
#   - modules                       # pack1.mod1
#   - packages (sub-packages)       # pack1.pack11.mod1
# set __path__ value


# directory name became the package name and module code in the role of __init__.py
'''
app/
    mod.py
    pack1/
        __init__.py
        module1.py
        module2.py

        pack101/
            __init__.py
            module101.py


mod.py
-----
mod.__file__     = .../app/mod.py
mod.__path__     =  not set       #(module not have this property)
mod.__package__  = ''             #(current folder) 


pack1
-----
pack1.__file__    = .../app/pack1.__init__.py
pack1.__path__    = .../app/pack1
pack1.__package__ = 'pack1'


module1.py
----------------
pack1.module1.__file__    = .../app/pack1/module1.py
pack1.module1.__path__    =  not set
pack1.module1.__package__ =  'pack1'


pack101
-----
pack101.__file__    = .../app/pack1/pack101.__init__.py
pack101.__path__    = .../app/pack1/pack101
pack101.__package__ = 'pack1.pack101'


module101.py
----------------
pack1.pack101.module101.__file__    = .../app/pack1/pack101/module101.py
pack1.pack101.module101.__path__    =  not set
pack1.pack101.module101.__package__ =  'pack1.pack101'

'''

