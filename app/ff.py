# услвоия вынес для себя что бы решить в отдельный файл
from pprint import pprint

error = {
    "code": "E501",
    "filename": "./source_code_2.py",
    "line_number": 18,
    "column_number": 80,
    "text": "line too long (99 > 79 characters)",
    "physical_line": '    return f"I like to filter, rounding, doubling, '
                     "store and decorate numbers: {', '.join(items)}!\"",
}
# тут то что я должен получить(закоментил для удобства)
# print(format_linter_error(error=error))
# # The output will be:
# {
#     "line": 18,
#     "column": 80,
#     "message": "line too long (99 > 79 characters)",
#     "name": "E501",
#     "source": "flake8"
# }

# #решения без одной строчки
# error["line"] = error.pop("line_number")
# error["line"] = error.pop("line_number")
#     a = {}
#     for num in error:
#         if num == "column_number":
#                 a["column"] = error[num]
#         if num == "text":
#                 a["message"] = error[num]
#         if num == "code":
#             a["name"] = error[num]
#         if num == "filename":
#             a["source"] = error[num]
#
#     print(error)

a = {"line": error.get("line_number")}
print(a)



# попытка решения в одну строку
# pprint(
#     {"line": error.get("line_number"), "column": error.get("column_number"), "message": error.get("text"),
#      "name": error.get("code"), "source": "flake8"}
# )
