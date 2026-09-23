from direct.showbase.ShowBase import ShowBase
class My3D(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)
app = My3D()
app.run()
