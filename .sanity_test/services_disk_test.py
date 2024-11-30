from services.disk.json.json_manager import JSONManager
from services.disk.xml.xml_manager import XMLManager
from services.disk.service_disk_provider  import ServiceDiskProvider
from toolboxs.toolbox import Toolbox
import pprint
import CONSTS


json = ServiceDiskProvider().json
json_dicttionary = json.operation(CONSTS.CONFIG_JSON)

# --
# ...
# --

# json_dicttionary = """{
#         "db_dictionary":{
#             "Driver": "SQL Server",
#             "Host": "LocalHost\\JTLWAWI",
#             "Database": "master",
#             "UserName": "sa",
#             "Password" : "sa04jT14"
#         }
#     }"""

# json.operation(CONSTS.CONFIG_JSON, json_dicttionary) 

# --
# ...
# --

xml = ServiceDiskProvider().xml
xml_dicttionary = xml.operation(CONSTS.EXTERNAL_FILES + r'/sample_files/xml_test.xml', is_get_dictionary = True)
pprint.pprint(xml_dicttionary, indent=2)

# --
# ...
# --

xml_dicttionary = xml.operation(CONSTS.EXTERNAL_FILES + r'/sample_files/xml_test.xml', xml_dicttionary)

{
    "wawi.testcase.testcase_object.testcase_objects_dictionary":{
        "testcase_object_directory": "/wawi/testcase/testcase_object"
    },

    "wawi.testcase.sample_dictionary.testcase_sample_dictionary": {
        "testcase_sample_file_dictionary": "/wawi/testcase/sample_dictionary/sample_file.json"
    },

    "services.db.sqlserver.config.db_config":{
        "driver": "SQL SERVER",
        "host": "LocalHost/JTLWAWI",
        "database": "master",
        "username": "sa",
        "password" : "sa04jT14"
    },

    "AQC":{
        "CreateSessionTimeout": "1",
        "WitForAppLaunch": "1",
        "ProcessName": "JTL_WAWi",
        "TestMeDB" : "DefaultTestDB.bak",
        "TestMeDBFolder": "C:/OneDrive/Manager",
        "TestAppFolder" : "C:/Mad-Grb/Apps",
        "TestMeVersionFolder" : ""
    },

    "services.mail.config.mail_config" : {
        "jtl":{
            "smtp": "mail.jtl-software.de: 587",
            "tc":{
                "address": "tc@jtl-software.de",
                "password": "Gk%30lh7uZy!h919"
            },

            "tc_help":{
                "address": "tc-help@jtl-software.de",
                "password": "6Cwee$64xapH6!50"
            },

            "noreplay":{
                "address": "noreply@jtl-software.com",
                "password": "3MiFMdEHFETUzRw"
            },

            "tc_bugalert":{
                "address": "tc-bugalert@jtl-software.de",
                "password": "sGi609!nCal0x$31"
            },

            "tc_konfig":{
                "address": "tc-konfig@jtl-software.de",
                "password": "fZt0z4"
            },

            "mohammad.paarmann-ara":"mohammad.paarmann-ara@jtl-software.com"
        },

        "recipient_address": ["mohammad.paarmann-ara@jtl-software.com"],
        "admin_address": ["mohammad.paarmann-ara@jtl-software.com"],
        "dev_address": ["mohammad.paarmann-ara@jtl-software.com"]
    },

    "services.log_.config.log_config":
    {
        "services.log_.core.stack.stack_context":{
            "no_show_moduls" : ["TestUmgebung", "le_Datei", "mTestTools"],
            "no_show_methods" : ["StackOperation", "WaitForAvailablity", "__RunTest"]
        },

        "services.log_.core.loging.log":{
            "Pipeline":{
                "number_of_log_in_batch": "1",
                "Directory" : "C:\\OneDrive\\TC_Sample_Datei",
                "FileName": "\\Log_Pipeline.txt",
                "encoding" : "utf-8",
                "level":"Info",
                "show_in_consoule": "True"
            },

            "Error":{
                "number_of_log_in_batch": "1",
                "Directory" : "C:\\OneDrive\\TC_Sample_Datei",
                "FileName": "\\Log_Error.txt",
                "encoding" : "utf-8",
                "level":"Info",
                "show_in_consoule": "True"
            }
        }
    },

    "drivers":{}

}

file = ServiceDiskProvider().file
file.operation(address='', context='Terminal_API.element_package')