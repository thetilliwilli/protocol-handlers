import json

file1 = open("public/handlers.json")
my_handlers = map(lambda x: ('HKEY_CLASSES_ROOT\\' + x['key']).lower(), json.load(file1))
my_handlers_set = set(my_handlers)

#result of execution: Get-ChildItem -Recurse -Path Registry::HKEY_CLASSES_ROOT\ | Select-Object Name > all-keys-from-powershell.txt
file2 = open("public/all-keys-from-powershell.txt", encoding='utf-8').readlines()
their_handlers = map(
    lambda x: x.strip().lower(),
    filter(
        lambda x: x.lower().find(r"shell\open\command") != -1,
        file2
    )
)
their_handlers_set = set(their_handlers)

diff_set = my_handlers_set.symmetric_difference(their_handlers_set)
print(len(diff_set))

open("public/diff.txt", "w").write('\n'.join(sorted(diff_set)))
# print(diff_set)
