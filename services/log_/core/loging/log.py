from typing import Any
from services.log_.config.log_config import LogConfig
from services.log_.core.base_log import BaseLog
from services.log_.templates.log_template_dictionary import LogTemplateDictionary

#--
#...
#--


class Log(BaseLog):
    def __init__(self, **kwargs) -> None:
        
        try:
            
            self.info_message = ['\n']
                                  
            #aliance for short writing
            self.info = self.error = self.set_information_for_log_file
            
            #create instance for file operation
            self.file_manager = kwargs.get('file_manager_class')

            #set template and config
            if template:= kwargs.get('template'):
                self.instance.log_template = self.instance.template_dictionary[template]
            else: 
                self.instance.log_template = ''
            
            if config:= kwargs.get('config'):
                self.instance.config_dictionary = self.instance.config_dictionary[__name__][config]
                self.log_file = self.config_dictionary['directory_address'] + self.config_dictionary['filename']
                self.number_of_log_in_batch = int(self.config_dictionary['number_of_log_in_batch'])
                self.is_show_in_consoule = self.config_dictionary['show_in_consoule']
            
        except Exception as exp:
            print(f"{__file__}--->{__name__} : + {str(exp)}")
        
#--
#...
#--

    @classmethod
    def get_template_dictionary(cls):
            return LogTemplateDictionary()()
        
#--
#...
#--

    @classmethod
    def get_config_dictionary(cls):
            return LogConfig().instance.dictionary

#--
#...
#--
    
    def set_information_for_log_file(self, message, is_force_write = False):

        try:
            
            #print message on screen
            if self.is_show_in_consoule:
                temp = f"import datetime\nprint({self.log_template})"
                exec(temp, {'message': message})

            #compile message and template
            temp = f"""import datetime;temp ={self.log_template}; f = open("temp.txt", "w"); f.write(str(temp[0] + temp[1]))"""
            exec(temp, {'message': message})
            
            #prepaire message
            message = self.file_manager.operation('r', 'temp.txt')
            
            #send message to write in file
            self.info_message.append(message)
            if len(self.info_message) > self.number_of_log_in_batch or is_force_write:
                self.__write_in_log_file()
                
        except Exception as exp:
            print(f"{__file__}--->{__name__} : + {str(exp)}")
#--
#...
#--

    def __write_in_log_file(self):
        
        try:
            
            self.file_manager.operation('a', self.log_file, '\n'.join(self.info_message))
            self.info_message.clear()
            self.info_message.append('\n')
            
        except Exception as exp:
            print(f"{__file__}--->{__name__} : + {str(exp)}")