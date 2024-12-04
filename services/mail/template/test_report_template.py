from typing import Any
from toolboxs.decorators import singleton

# --
# ...
# --


@singleton
class test_report_template:
    def __init__(self) -> None:
        self.body = ""
        self.template = ""
        self.mixed_html = ""

    # --
    # ...
    # --

    def __call__(self, body="") -> Any:
        self.__set_template()
        self.__get_mixed_html_body(body)

    # --
    # ...
    # --

    def __set_template(self) -> str:

        self.template = """
                <html>
                    <head>
                        <style>
                            div.content { width: 15000px }
                            h1 {color:red;font-family: Arial;font-size: 80%;font-weight:lighter;}
                            h2 {color:green;font-family: Arial;font-size: 80%;}
                            h3 {color:black;font-family: Arial;font-size: 80%;font-weight:lighter;}
                            p {color:blue;font-family: Lucida Console;font-size: 80%;}
                        </style>
                    </head>
                      
                    <body>
                        <div class="content">
                        {}
                        </div>
                    </body>
                </html>
            """

    # --
    # ...
    # --

    def __get_mixed_html_body(self, body) -> str:
        self.mixed_html = (
            self.template if body == "" else self.template.replace("{}", body)
        )
