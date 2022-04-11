from tkinter import *
from tkinter import ttk , messagebox
from tkinter.colorchooser import *  # เลือกสีจากจานสี ต้องเขียน Function เรียกก่อน

GUI = Tk()
GUI.title("โปรแกรมคำนวนราคาปลา รถพุ่มพวง")
GUI.geometry("700x800")

# สร้างข้อความหัวข้อเรื่อง
L = Label(GUI,text="กรุณากรอกข้อมูลการซื้อปลา",fg="green",bg="orange",font=(None,20))
L.pack()

#####################################
# ใส่รูปภาพลงบน GUI ต้องเป็นนามสกุล PNG
image = PhotoImage(file ="car.png")
#image = PhotoImage(file=r"E:\Python _ Class Python for Beginners from Zero by Uncle Engineer_start 12 Mar 22\basic python\car.png")
Image = Label(GUI,image=image)
Image.pack()

############ ราคาปลาวันนี้  ############
# ปลาช่อน กก ละ 80 บาท
# ปลาดุก กก ละ 50 บาท
# ปลาหมึก กก ละ 120 บาท
#####################################
# 1. ชื่อช่องกรอก
L1 = Label(GUI,text="กรุณากรอกน้ำหนักปลา (กิโลกรัม)",fg="green",bg="black",font=(None,20))
L1.pack(pady=10)
# 2. สร้างช่องกรอกน้ำหนักปลา เป็น กก.
v_quantity1 = StringVar() #สร้างตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
#v_quantity1 = IntVar() #สร้างตัวแปรที่ใช้เก็บข้อความเมื่อพิมพ์เสร็จแล้ว
E1 = ttk.Entry(GUI,textvariable = v_quantity1 , font=(None,20))
E1.pack(pady=10)
######################################
# 3. เลือกชนิดของปลา
fish_type = StringVar(value= "กรุณาเลือกชนิดของปลา") # เก็บชนิดปลา แบบ StringVar ไว้ในตัวแปร  fish_type
# สร้างช่องกรอก แบบ Combobox เพื่อให้มี  dropdown list เลือกชนิดปลาได้
list_type= ttk.Combobox(textvariable= fish_type,font =(None,20))
# 4. ชื่อชนิดของปลาที่มีขาย
list_type["values"] = ("ปลาช่อน","ปลาดุก","ปลาหมึก")
list_type.pack(pady=10)
######################################
# 1. ชื่อชช่องสำหรับผลการคำนวน
L2 = Label(GUI,text="รวมราคาทั้งหมด (บาท)",fg="orange",bg="black",font=(None,20))
L2.pack(pady=10)
# 2. สร้างช่องรับผลการคำนาณจากฟังชั่น Cal
E2 = ttk.Entry(font=(None,20))
E2.pack()
######################################
# สร้าง Function คำนวณราคาซื้อ 
def Cal():
    try:  # try / except เช็คว่าทำงานได้ไหม ถ้าไม่ได้มีข้อความแจ้งเติอน และให้ให้ทำใหม่
        quantity = float(v_quantity1.get())# get จำนวนน้ำหนักปลา
        fishtype = fish_type.get()# get ชนิดปลา
        
        if fishtype == "ปลาช่อน":
            E2.delete(0,END)  # ลบค่าเดิมออกก่อนคำนวนใหม่
            total1= (quantity * 80 )#ปลาช่อน กก ละ 80 บาท
            E2.insert(0,total1) 
            #messagebox.showinfo("ราคาทั้งหมด","ราคาปลาทั้งหมด {} บาท".format(total1)) 
            #v_quantity.set("1") # กรอกเป็นตัวเลขเท่านั้น ถ้ากรอกเป็นตัวอักษร try / except  ก็จะทำการแจ้งเตือน
            #E2.focus()
            
        elif fishtype == "ปลาดุก":
            E2.delete(0,END)  # ลบค่าเดิมออกก่อนคำนวนใหม่
            total2= (quantity * 50 )#ปลาช่อน กก ละ 80 บาท
            E2.insert(0,total2) 
            #messagebox.showinfo("ราคาทั้งหมด","ราคาปลาทั้งหมด {} บาท".format(total2)) 
            #v_quantity.set("1") # กรอกเป็นตัวเลขเท่านั้น ถ้ากรอกเป็นตัวอักษร try / except  ก็จะทำการแจ้งเตือน
            #E2.focus()
        elif fishtype == "ปลาหมึก":
            E2.delete(0,END)  # ลบค่าเดิมออกก่อนคำนวนใหม่
            total3= (quantity * 120 )#ปลาช่อน กก ละ 80 บาท
            E2.insert(0,total3) 
            #messagebox.showinfo("ราคาทั้งหมด","ราคาปลาทั้งหมด {} บาท".format(total2)) 
            #v_quantity.set("1") # กรอกเป็นตัวเลขเท่านั้น ถ้ากรอกเป็นตัวอักษร try / except  ก็จะทำการแจ้งเตือน
            #E2.focus()
        else :
            E2.delete(0,END)  # ลบค่าเดิมออกก่อนคำนวนใหม่
            total4= ("คุณยังไม่ได้เลือกชนิดปลา")#ปลาช่อน กก ละ 80 บาท
            E2.insert(0,total4)    
            #messagebox.showinfo("ราคาทั้งหมด","ราคาปลาทั้งหมด {} บาท".format(total3)) 
            #v_quantity.set("1") # กรอกเป็นตัวเลขเท่านั้น ถ้ากรอกเป็นตัวอักษร try / except  ก็จะทำการแจ้งเตือน
            #E2.focus()
    except:
        messagebox.showwarning("กรอกผิด", "คุณไม่ได้กรอกน้ำหนักปลาหรือไม่ได้เลือกชนิดปลา") # "กรอกผิด" = title Warnning  // "กรุณากรอกเฉพาะตัวเลข" = Message Warnning
        v_quantity1.set(" ")  # ถ้าใส่ตัวเลขไว้ จะแสดงตัวเลขน้ำหนักเริ่มต้นไว้ในช่องกรอก
        E2.focus() #
############################################
# สร้าง Function ลบข้อมูลที่กรอกเข้ามา เพื่อคำนวณรอบใหม่

def ClearData():
    E1.delete(0,END)
    E2.delete(0,END)
          
#  l สร้างปุ่มกดสำหรับ คำนวณ และเชื่อมคำสั่งคำสั่งให้ปุ่ม (command)

B2 = ttk.Button(GUI,text= "คำนวณ",command= Cal)
B2.pack(ipadx=30,ipady=20,pady = 10)

# 2.สร้างปุ่มกดสำหรับ Clear ข้อมูลที่กรอกมา และเชื่อมคำสั่งคำสั่งให้ปุ่ม (command)

B3 = ttk.Button(GUI,text= "Clear",command= ClearData)
B3.pack(ipadx=30,ipady=20,pady = 10)

################################################
  
GUI.mainloop()