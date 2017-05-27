
def error_handler(func):
    def error_wrapper():
        try:
            run = func()
            return run
        except TypeError as typo_err:
            print("Error with the query: \n %s" % typo_err)
        except AttributeError as attr_err:
            print("Not valid module: \n %s" % attr_err)
        except NameError as name_err:
            print("Not valid name: %s" % name_err)
        
    return error_wrapper
