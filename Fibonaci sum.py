from tkinter import*

root=Tk()
root.title("Fibonaci Sum")
root.geometry("400x400")

label_series=Label(root,text="Fabonaci Series :")
inputBox=Entry(root)
label_spiral=Label(root)

def Fibonaci():
    counter=0
    num=int(inputBox.get())
    num1=0
    num2=1
    sum=0
    sum2=0
    while (counter<=num):
        sum2=sum2+sum
        counter+=1
        num1=num2
        num2=sum
        sum=num1+num2
        label_series["text"]+=str(sum2)+ " "
        label_spiral["text"]="Fabonaci Series :"+str(sum2)
        
btn=Button(root,text="FIbonaci Series",command=Fibonaci,bg="white")
inputBox.pack()
btn.pack()
label_series.pack()
label_spiral.pack()

root.mainloop()