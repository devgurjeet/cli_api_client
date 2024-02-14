# injector.py

from injector import Injector, Module, inject
from services.api_service import ApiService

class AppModule(Module):
    @inject
    def configure(self, binder):
        binder.bind(ApiService, to=ApiService)
        
def configure_injector():   
    injector = Injector(modules=[AppModule()])
    return injector
