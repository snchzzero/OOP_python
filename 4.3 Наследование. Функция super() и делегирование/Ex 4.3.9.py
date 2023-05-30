class SoftList(list):
    def __getitem__(self, index):
        if -len(self) <= index < len(self):
            return super().__getitem__(index)
        return False


sl = SoftList("python")
print(sl[0]) # 'p'
print(sl[-1]) # 'n'
print(sl[-6]) # 'n'
print(sl[-7]) # 'n'
print(sl[6]) # 'n'