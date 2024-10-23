print(len([2343, True,  457]))


# variable access before declare
try:
    print(hello)

    hello = 'Hi'
except NameError as NE:
    print('NameError: Variable declaration issue')

print("set >>", len({
    1,
    "2",
    "21"
}))