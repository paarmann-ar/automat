from typing import Any
import os
from services.mail.template.config.template_config import TemplateConfig
import importlib
from services.mail.core.base_email import BaseEMail
# --
# ...
# --


class TemplateManager(BaseEMail):
    def __init__(self) -> None:
        pass

    # --
    # ...
    # --
    @classmethod
    def get_config_dictionary(cls):
        return TemplateConfig().instance.dictionary

    # --
    # ...
    # --

    def set_template_attributs(self, **kwargs):
        if body := kwargs.get("body", ""):
            body = self.clear_body(body)

        if template_name := kwargs.get("template_name"):
            template_class = self.get_template_class(template_name)
            template_instance = template_class()
            template_instance(body)

            self.instance.template_object = {
                "template": template_instance.template,
                "mixed_html": template_instance.mixed_html,
                "body": body,
            }

    # --
    # ...
    # --

    def clear_body(self, body="") -> str:
        if body != "":
            body = body.replace("\n", "<br>\n")
            body = body.replace(" ", "&nbsp;")

        return body

    # --
    # ...
    # --

    def __call__(self) -> str:
        return self.template_object

    # --
    # ...
    # --

    def get_template_class(self, template_name) -> str:
        template_directory = self.config_dictionary["template_directory"]
        template_namespace = self.config_dictionary["template_namespace"]

        files = os.listdir(template_directory)
        for file in files:
            if file == f"{template_name}.py":
                template_namespace = f"{template_namespace}.{template_name}"
                module = importlib.import_module(template_namespace)

                template_class = getattr(module, template_name)

                return template_class
