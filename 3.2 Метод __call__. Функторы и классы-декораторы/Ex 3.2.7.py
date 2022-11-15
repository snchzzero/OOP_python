class RenderList:
    def __init__(self, type_list):
        self.type_list = type_list

    def __call__(self, *args, **kwargs):
        l1 = list()
        l1_final = list()

        for arg in args[0]:
             l1.append(f"<li>{arg}</li>\n")
        if self.type_list == "ul" or self.type_list == "ol":
            l1_final.append(f"<{self.type_list}>\n")
            l1_final.extend(l1)
            l1_final.append(f"</{self.type_list}>")
        else:
            l1_final.append(f"<ul>\n")
            l1_final.extend(l1)
            l1_final.append(f"</ul>")
        return ''.join(l1_final)




lst = ["Пункт меню 1", "Пункт меню 2", "Пункт меню 3"]
render = RenderList("o56l")
html = render(lst)
print(html)
