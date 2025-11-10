class Reportable:
    def __init__(self, obj):
        self.obj = obj

    def to_report_line(self):

        try:
            with open("file.txt", "a") as f:
                f.write(self.obj)

        except NotImplementedError:
            raise NotImplementedError
