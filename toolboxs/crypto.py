import CONSTS
import glob
from cryptography.fernet import Fernet
from services.disk.json.json_manager import JSONManager

def add_id_to_all_json_element():
    # key = Fernet.generate_key()
    # fernet = Fernet(key)
    # encMessage = fernet.encrypt(element.encode())
    # decMessage = fernet.decrypt(encMessage).decode()

    json_manager = JSONManager()

    for file in glob.glob(
        f"{CONSTS.ROOT_DIR}/test_applications/d_365/chapters/finance_chapter//**/*.json",
        recursive=True,
    ):
        if file[-10:] == "_aqua.json":
            continue

        json_dict = json_manager.operation(file)


        print(json_dict)

add_id_to_all_json_element()