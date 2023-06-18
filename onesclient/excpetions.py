class OnesClientExpection(Exception):
    """
    Exception for OnesCleint related error
    """
    def __init__(self, msg =None):
        if msg is None:
            return "Somethiong went wrong in OnceClient."
        return msg
    
