from services.mail.email_provider import EMailProvider

email = EMailProvider().email

email(
    sender_domains="mohammad_Paarmann",
    receiver_group="dev_address",
    subject="Test_Subjekt",
    template_name="test_report_template",
    body="hahaha",
)

# attachments_object = {
#     'AttachItem_0' : {
#             'is_attach' : True,
#             'is_all_directory' : False,
#             'directory' : Simple_CSV_AnhangDatei.directory,
#             'file' : Simple_CSV_AnhangDatei.file
#         },

#     'AttachItem_1' : {
#             'is_attach' : True,
#             'is_all_directory' : False,
#             'directory' : xmlAuftrageDatei.directory,
#             'file' : xmlAuftrageDatei.file
#         },
#     }

# email.send(attachments_object=attachments_object)
