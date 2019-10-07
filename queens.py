from tkinter import *
from PIL import Image,ImageTk

img = Image.open('黑皇后.png')

def init():
	root1 = Tk()
	root1.title('输入棋盘大小')
	wid = 245
	high = 120
	screenwidth = root1.winfo_screenwidth()
	screenheight = root1.winfo_screenheight()
	alignstr = '%dx%d+%d+%d' % (wid, high, (screenwidth - wid) / 2 + 10, (screenheight - high) / 2 + 10)
	root1.geometry(alignstr)
	l = Label(text='输入棋盘大小')
	l.pack()
	entry = Entry()
	entry.pack()
	button = Button(text='确认', command=lambda: operate(entry))
	button.pack()
	root1.mainloop()

def operate(entry):
	text = int(entry.get())
	show(cal_single(text), text)
	
	
def cal_single(k):
	# (i,j)在第i行第j列，左上到右下第(i-j)+7对角线，右上到左下第(i+j)条对角线上
	re = []
	row = [0]*k
	col = [0]*k
	# TLtoLR=top left to lower right/TRtoLL=top right to lower left
	TLtoLR = [0]*(2*k-1)
	TRtoLL = [0]*(2*k-1)
	now = 0
	j = 0
	while True:
		while j < k:
			if 0 == row[now] == col[j] == TLtoLR[now-j+k-1] == TRtoLL[now+j]:
				re.append((now, j))
				row[now] = col[j] = TLtoLR[now - j + k-1] = TRtoLL[now + j] = 1
				now += 1
				j = 0
				break
			while j == k - 1:
				if len(re) == 0:
					return []
				invalid = re.pop()
				j = invalid[1]
				now -= 1
				row[now] = col[j] = TLtoLR[now - j + k - 1] = TRtoLL[now + j] = 0
				if now < 0:
					return []
			j += 1
		if now == k:
			break
	return re


def show(re, k):
	if len(re) != 0:
		root=Toplevel()
		root.title(str(k)+'皇后问题')
		w,h = img.size
		im_resized = img.resize((40, 40), Image.ANTIALIAS)
		im = ImageTk.PhotoImage(im_resized)
		wid = 40*k
		high = 40*k
		screenwidth = root.winfo_screenwidth()
		screenheight = root.winfo_screenheight()
		alignstr = '%dx%d+%d+%d' % (wid, high, (screenwidth - wid) / 2 + 10, (screenheight - high) / 2 + 10)
		root.geometry(alignstr)
		can=Canvas(root,width=wid,height=high,bg='white')
		for r in re:
			can.create_image(20 + r[0]*40,20 + r[1]*40,image=im)
		for i in range(k + 1):
			can.create_line((0, 40*i),(wid, i*40),width=1)
			can.create_line((40*i, 0),(40*i, high),width=1)
		can.pack()
		root.mainloop()
	else:
		err = Label(text=str(k) + '皇后问题无解')
		err.pack()

	
if __name__ == '__main__':
	init()