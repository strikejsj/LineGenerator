# 2022-03-31 JSJ


import tkinter
app = tkinter.Tk()

app.title("New Line Converter")
app.geometry('480x400')

# 텍스트필드 입력받기
def getTextInput():
    publicKey = txtField.get(1.0, tkinter.END + "-1c")
    
    # 마지막에 개행문자있으면 제거
    if publicKey[-2:] == r"\n":
        publicKey = publicKey[:-2]

    return publicKey

# 텍스트필드 출력하기
def setTextInput():
    publicKey = getTextInput()
    # \n > new line 변환
    formatted_publicKey = publicKey.replace('\\n', '\n').replace('\\t', '\t')

    # resultField.config(text = formatted_publicKey)
    # 버튼 클릭하면 내용 전부 지우고,
    resultField.delete(1.0, tkinter.END + "-1c")
    # 새 문구 삽입
    resultField.insert(tkinter.END + "-1c", formatted_publicKey)


# 변환할 텍스트필드 생성
txtField = tkinter.Text(app, height = 10)

# 버튼 생성 & 옵션 설정
btn = tkinter.Button(app,
    text = 'btn',
    background = 'white'
)

# 변환된 publicKey 필드 생성
resultField = tkinter.Text(app)

# 버튼 옵션 설정
btn.config(
    width = 10,
    height = 2,
    text = "Click Me :)",
    command = setTextInput)


# 버튼 배치
txtField.pack(fill="both")
btn.pack()
resultField.pack(fill="both")

app.mainloop()