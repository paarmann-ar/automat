import importlib.util
import glob
import importlib
import inspect
import CONSTS

# --
# ...
# --


class GetAllClassInTestApplication:
    def __init__(self) -> None:
        self.classes = []
        self.module_sources = {}
        self.Objects_of_classes = []
        self.no_go_module = []

    # --
    # ...
    # --

    def get_list_of_object_from_all_classes_in_unit_testcases(self):
        self.get_list_of_all_classes_in_unit_testcases()

        self.Objects_of_classes = [class_() for class_ in self.classes]

    # --
    # ...
    # --

    def get_list_of_all_classes_in_unit_testcases(self):
        for file in glob.glob(
            f"{CONSTS.ROOT_DIR}/test_applications/d_365/chapters//**/*.py",
            recursive=True,
        ):
            name = file.split("\\")[-1][:-3]

            if name in self.no_go_module:
                continue

            spec = importlib.util.spec_from_file_location(name, file)
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            class_name = "".join([word.capitalize() for word in name.split("_")])

            class_ = getattr(module, class_name)
            self.classes.append(class_)

            self.module_sources.update(
                {
                    class_name: inspect.getsource(module),
                }
            )
