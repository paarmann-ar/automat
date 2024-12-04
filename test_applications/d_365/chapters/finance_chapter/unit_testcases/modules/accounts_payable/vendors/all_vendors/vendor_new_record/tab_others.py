from typing import Any
from test_applications.d_365.core.object_provider import ObjectProvider
from test_applications.d_365.chapters.core.base_chapter import BaseChapter
from test_applications.d_365.abstrct_classes.tab.tab import Tab

# --
# ...
# --


class TabOthers(BaseChapter, Tab):
    def __init__(
        self,
        *args,
        **kwargs,
    ) -> None:
        super().__init__(*args, **kwargs)

        self.elements = self.get_elements()
        self.__prepare(**kwargs)
        self.__setup()

        print(__class__.__name__, id(__class__))

    # --
    # ... call
    # --

    def __call__(self, action="", **kwargs) -> Any:

        try:

            if super_result := super().__call__(action, **kwargs):
                return super_result

            match action:
                case "":
                    self.tab_others()

                case _:
                    raise Exception(
                        f"class {__class__.__name__} have no method {action}."
                    )

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ...
    # --

    def get_elements(self) -> str:
        return ObjectProvider()(__file__.replace(".py", ".json ", -1).replace("\\", "/").replace(" c", ""))

    # --
    # ... setup, teardown and prepare
    # --

    def __setup(self) -> bool:

        try:

            super().setup()
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    def __teardown(self) -> bool:

        try:

            super().teardown()

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    def __prepare(
        self,
        leadtime=("", True),
        delivery_time_external=("", True),
        external_processing_time=("", True),
        transit_time=("", True),
        processing_time_interna=("", True),
    ) -> bool:

        try:

            if super().prepare():
                return True

            self.leadtime = self.get_random(type="int"), (
                leadtime[1] if leadtime[0] == "" else leadtime[1]
            )
            self.delivery_time_external = (
                self.get_random(type="int"),
                (
                    delivery_time_external[1]
                    if delivery_time_external[0] == ""
                    else delivery_time_external[1]
                ),
            )
            self.external_processing_time = (
                self.get_random(type="int"),
                (
                    external_processing_time[1]
                    if external_processing_time[0] == ""
                    else external_processing_time[1]
                ),
            )
            self.transit_time = (
                self.get_random(type="int"),
                transit_time[1] if transit_time[0] == "" else transit_time[1],
            )
            self.processing_time_interna = (
                self.get_random(type="int"),
                (
                    processing_time_interna[1]
                    if processing_time_interna[0] == ""
                    else processing_time_interna[1]
                ),
            )
            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False

    # --
    # ... methods
    # --
    
    @Tab.expand_tab
    @BaseChapter.wait_for(element_for_waiting_until_visible="btn_tab")
    @BaseChapter.log
    def tab_others(self) -> bool:

        try:

            self.textbox(self.elements.txb_leadtime, self.leadtime, is_press_enter=True)
            self.textbox(
                self.elements.txb_delivery_time_external,
                self.delivery_time_external,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.txb_external_processing_time,
                self.external_processing_time,
                is_press_enter=True,
            )
            self.textbox(
                self.elements.txb_transit_time, self.transit_time, is_press_enter=True
            )
            self.textbox(
                self.elements.txb_processing_time_internal,
                self.processing_time_interna,
                is_press_enter=True,
            )

            self.delay(220)

            return True

        except Exception as exp:
            self.error(f"{repr(exp)},{str(exp)}\n{self.stack()}")
            return False
