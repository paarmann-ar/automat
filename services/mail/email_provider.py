from toolboxs.decorators import singleton
from services.mail.email.email import EMail
from services.mail.template.template_manager import TemplateManager
from services.log_.log_provider import LogProvider


# --
# ...
# --


@singleton
class EMailProvider:
    def __init__(self, **kwargs):
        self.email = EMail().instance
