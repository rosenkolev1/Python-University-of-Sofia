class PrettyPrint:
    def __init__(self):
        self.__border = '|'
        self.__content = ''
        self.__prefix = '***'
        self.__suffix = '***'

    def pretty_print(self):
        return f'{self.__border} {self.__prefix} {self.__content} {self.__suffix} {self.__border}'

    @property
    def border(self):
        return self.__border

    @border.setter
    def border(self, new_border):
        self.__border = new_border

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, new_content):
        self.__content = new_content

    @property
    def prefix(self):
        return self.__prefix

    @prefix.setter
    def prefix(self, new_prefix):
        self.__prefix = new_prefix

    @property
    def suffix(self):
        return self.__suffix

    @suffix.setter
    def suffix(self, new_suffix):
        self.__suffix = new_suffix


def pretty_print(content, border='|', prefix='666', suffix='666'):
    return f'{border} {prefix} {content} {suffix} {border}'

print(pretty_print('Hell world'))


# pretty_printer = PrettyPrint()

# pretty_printer.content = 'Hello world'
# print(pretty_printer.pretty_print())

# pretty_printer.prefix = '<<<'
# pretty_printer.suffix = '>>>'
# print(pretty_printer.pretty_print())