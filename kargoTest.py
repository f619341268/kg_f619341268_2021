if __name__ == '__main__':
    i = [3, 25, 209]
    j = [10, 300, 5]
    d = {1:"One", 2:"Two", 3:"Three", 4: "Four", 5:"Five", 6:"Six", 7:"Seven", 8:"Eight", 9:"Nine", 0:"Zero"}
    def convert(num):
        num = str(num)
        l = []
        while len(num)>0:
            l += [d[int(num[0])]]
            num=num[1:]
        return "".join(l)
    n = ",".join(list(map(convert, i)))
    n1 = ",".join(list(map(convert, j)))
    print(n)
    print(n1)
