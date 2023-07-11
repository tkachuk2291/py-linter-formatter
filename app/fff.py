# errors_example = {
#     "errors":
#         [
#             {
#                 "line": 18,
#                 "column": 80,
#                 "message": "line too long (99 > 79 characters)",
#                 "name": "E501",
#                 "source": "flake8"
#             },
#             {
#                 "line": 18,
#                 "column": 100,
#                 "message": "no newline at end of file",
#                 "name": "W292",
#                 "source": "flake8"
#             }
#         ],
#     "path": "./source_code_2.py",
#     "status": "failed"
# }


errors = [
    {
        "code": "E501",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 80,
         "text": "line too long (99 > 79 characters)",
        "physical_line": '    return f"I like to filter, rounding, doubling, ' 
        "store and decorate numbers: {', '.join(items)}!\"",
    },
    {
        "code": "W292",
        "filename": "./source_code_2.py",
        "line_number": 18,
        "column_number": 100,
        "text": "no newline at end of file",
        "physical_line": '    return f"I like to filter, rounding, doubling, '
        "store and decorate numbers: {', '.join(items)}!\"",
    },
]


