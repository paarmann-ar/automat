from services.log_.core.loging.log import Log
from services.disk.file.file_manager import FileManager
from services.log_.core.stack.stack_context import StackContext

# --
# ...
# --


class LogProvider:
    def __init__(self, **kwargs) -> None:
        template= kwargs.get('template','Pipeline')
        config=kwargs.get('config','Pipeline')

        file_manager_class = FileManager().instance
        
        self.info = Log(template=template, config=config, file_manager_class=file_manager_class).instance.info
        self.error = Log(template='Error', config='Error', file_manager_class=file_manager_class).instance.error
        self.stack = StackContext().StackOperation