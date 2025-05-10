class ContextManager:
    def __enter__(self,*args,**kwargs):
        print('__enter__')
    
    def __exit__(self,*args):
        print('__exit__')
        
with ContextManager():
    print('Test')