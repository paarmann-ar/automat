from services.mail.core.base_email import BaseEMail
from services.mail.email.config.mail_config import MailConfig
from email.mime.multipart import MIMEMultipart
from email import encoders
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
import smtplib
import os
from typing import Any
from services.mail.template.template_manager import TemplateManager

# --
# ...
# --


class EMail(BaseEMail):
    def __init__(self) -> None:
        pass

    # --
    # ...
    # --

    @classmethod
    def get_config_dictionary(cls):
        return MailConfig().instance.dictionary

    # --
    # ...
    # --

    def __call__(self, **kwargs):
        self.set_email_attributs(**kwargs)
        self.__send()

    # --
    # ...
    # --

    def set_email_attributs(self, **kwargs):

        try:

            if sender_domains := kwargs.get("sender_domains"):
                self.from_object = self.config_dictionary["sender_domains"][
                    sender_domains
                ]
            else:
                self.from_object = kwargs.get("sender_object")

            if receiver_group := kwargs.get("receiver_group", []):
                self.receiver_list = self.config_dictionary["receiver_groups"][
                    receiver_group
                ]

            self.receiver_list = kwargs.get("receiver_list", [])
            self.cc_list = kwargs.get("cc_list", [])

            self.subject = kwargs.get("subject", "")

            self.attachments_object = kwargs.get("attachments_object", None)
            if not self.attachments_object:
                self.attachments_object = self.config_dictionary["attachment_default"]

            self.template_object = kwargs.get("template_object", None)

            if not self.template_object:
                template_object_from_config_file = self.config_dictionary[
                    "template_default"
                ]

                self.template_object = TemplateManager().instance

                self.template_object.set_template_attributs(
                    template_name=template_object_from_config_file.get("template_name"),
                    body=template_object_from_config_file.get("body"),
                )
                self.template_object = self.template_object.template_object

            template_name = kwargs.get("template_name", None)
            body = kwargs.get("body")

            if template_name and body:
                self.template_object = TemplateManager().instance

                self.template_object.set_template_attributs(
                    template_name=template_name,
                    body=body,
                )
                self.template_object = self.template_object.template_object

            return True

        except Exception as exp:
            print(repr(exp))
            return False

    # --
    # ...
    # --

    def __send(self) -> bool:

        try:

            message = MIMEMultipart("alternative")
            message["From"] = self.from_object["address"]
            message["subject"] = self.subject
            message["Cc"] = ",".join(self.cc_list)

            body = MIMEText(self.template_object["body"], "plain")
            html = MIMEText(self.template_object["mixed_html"], "html")

            message.attach(body)
            message.attach(html)

            if self.attachments_object is not None:
                for attached_file in self.attachment_manager(self.attachments_object):
                    message.attach(attached_file)

            server = smtplib.SMTP(self.from_object["smtp"])
            server.starttls()
            server.login(self.from_object["address"], self.from_object["password"])

            map(
                lambda receiver: server.sendmail(
                    self.from_object["address"], receiver, message.as_string()
                ),
                self.receiver_list,
            )

            server.quit()

            return True

        except Exception as exp:
            print(repr(exp))
            return False

    # --
    # ...
    # --

    def attachment_manager(self, attachments_object=None) -> Any:

        if attachments_object is None:
            return

        try:

            files = []
            attachments = []

            for item in attachments_object:
                item = attachments_object[item]
                is_attach = item["is_attach"]
                is_all_directory = item["is_all_directory"]
                directory = item["attachment_directory"]

                if is_attach:
                    if bool(os.listdir(directory)):

                        if is_all_directory:
                            for item in os.listdir(directory):
                                files.append(f"{directory}#{item}")
                        else:
                            files.append(f"{directory}#{item["file"]}")

            attachments = self.create_holder(files)

            return attachments

        except Exception as exp:
            # self.error(f"{__file__}--->{__name__}: {str(exp)}")
            print(repr(exp))
            return False

    # --
    # ...
    # --

    def create_holder(self, files):

        try:

            temp_attachments = []
            files = set(files)
            # f = list(dict.fromkeys(File))
            _ = 0

            for item in files:
                item = item.split("#")
                item = "/".join(item)
                attachment = open(item, "rb")

                temp_attachments.append(MIMEBase("application", "octet-stream"))
                temp_attachments[_].set_payload((attachment).read())
                encoders.encode_base64(temp_attachments[_])

                temp_attachments[_].add_header(
                    "Content-Disposition", "attachment; filename= %s" % item[1]
                )

                _ += 1

            return temp_attachments

        except Exception as exp:
            print(repr(exp))
            return False
