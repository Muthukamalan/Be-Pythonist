# namespace packages are package-like
#   - directories
#       - may contain modules
#       - may contain nested regular packages
#       - may contain nested namespace packages 
#       - but not have __init__.py
# 

'''
app/
    mod.py
    pack1/
        module1.py
        module2.py

        pack101/
            module101.py
'''