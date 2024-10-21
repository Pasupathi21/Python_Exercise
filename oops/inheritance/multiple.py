# in multi level inheritance inherting method from super calss to sub and sub to another sub
# a -> b -> c -> d like this

class BaseApp:
    pass

class VersionOne(BaseApp):
    pass

class VersionTwo(VersionOne):
    pass

