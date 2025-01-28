import math
import random
from pathlib import Path
import sys

# --
# ...
# --


class Toolbox:

    @staticmethod
    def str_(input_):

        try:

            if isinstance(input_, str):
                return input_

            elif isinstance(input_, float) or isinstance(input_, int):
                return str(input_)

        except Exception as exp:
            print(repr(exp))

    # --
    # ...
    # --

    @staticmethod
    def get_random(start_string="RND ", type="string", limit=1000000):

        try:

            result = 0

            if start_string is tuple:
                start_string, _ = start_string

            if type == "string":
                rand_ = math.ceil(random.random() * limit)
                if rand_ < 10:
                    rand_ += 10
                result = start_string + str(rand_)

            elif type == "int":
                result = math.ceil(random.random() * limit)
                if result < 10:
                    result += 10
                    
            return result

        except Exception as exp:
            print(repr(exp))

    # --
    # ...
    # --

    @staticmethod
    def get_root_path() -> str:

        try:

            return str(Path(__file__).parent.parent)

        except Exception as exp:
            print(repr(exp))


    # --
    # ...
    # --

    @staticmethod
    def get_import_moduls() -> str:

        try:

            modules=[]
            sys_modules_keys = sys.modules.keys()
            for module in sys_modules_keys:
                if module[:48] == 'test_applications.d_365.chapters.finance_chapter':
                    modules.append(module)

            with open(f"{Toolbox().get_root_path().replace("\\", "/")}/.external_files/temp/temp_import_moluls.txt",'w') as temp_import_moluls:
                moduls_text=""
                for m in modules:
                    moduls_text = f"{moduls_text} {m} \n"

                print(moduls_text , file=temp_import_moluls)
            
            temp_import_moluls.close()

            return modules

        except Exception as exp:
            print(repr(exp))

    