from tkinter import *

choseong_list = [char for char in "ㄱㄲㄴㄷㄸㄹㅁㅂㅃㅅㅆㅇㅈㅉㅊㅋㅌㅍㅎ"]
jungseong_list = [char for char in "ㅏㅐㅑㅒㅓㅔㅕㅖㅗㅘㅙㅚㅛㅜㅝㅞㅟㅠㅡㅢㅣ"]
jongseong_list = [char for char in " ㄱㄲㄳㄴㄵㄶㄷㄹㄺㄻㄼㄽㄾㄿㅀㅁㅂㅄㅅㅆㅇㅈㅊㅋㅌㅍㅎ"]
ko_dict = {'q':'ㅂ', 'Q':'ㅃ', 'w':'ㅈ', 'W':'ㅉ', 'e':'ㄷ', 'E':'ㄸ', 'r':'ㄱ', 'R':'ㄲ', 't':'ㅅ', 'T':'ㅆ', 'y':'ㅛ', 'u':'ㅕ', 'i':'ㅑ', 'o':'ㅐ', 'p':'ㅔ', 'a':'ㅁ', 's':'ㄴ', 'd':'ㅇ', 'f':'ㄹ', 'g':'ㅎ', 'h':'ㅗ', 'j':'ㅓ', 'k':'ㅏ', 'l':'ㅣ', 'z':'ㅋ', 'x':'ㅌ', 'c':'ㅊ', 'v':'ㅍ', 'b':'ㅠ', 'n':'ㅜ', 'm':'ㅡ', 'O':'ㅒ', 'P':'ㅖ', 'Y':'ㅛ', 'U':'ㅕ', 'I':'ㅑ', 'H':'ㅗ', 'J':'ㅓ', 'K':'ㅏ', 'L':'ㅣ', 'B':'ㅠ', 'N':'ㅜ', 'M':'ㅡ' }

def main():
    
    tk = Tk()
    tk.title('한영 변환기')
    def click_btn():
        main_in = text1.get("1.0", END)
        text2.delete("1.0","end")
        text2.insert(END,en2ko(main_in))

    def return_btn(event):
        main_in = text1.get("1.0", END)
        text2.delete("1.0","end")
        text2.insert(END,en2ko(main_in))
    
    def clear():
        text1.delete("1.0",END)
        text2.delete("1.0",END)
    
    label1 = Label(tk,text='영어\n(입력)').grid(row=0, column=0,padx=10)
    label2 = Label(tk,text='한글\n(변환결과)').grid(row=1,column=0,padx=10)
    label3 = Label(tk,text='Made by j-mook').grid(row=2,column=1,padx=10, sticky='se')
    # 각 단위 입력받는 부분 만들기
    text1 = Text(tk)
    text2 = Text(tk)
    text1.grid(row=0,column=1,padx=5, pady=10, ipadx=20, ipady=0)
    text2.grid(row=1,column=1,padx=5, ipadx=20, ipady=0)

    btn1 = Button(tk,text='한/영 변환',command=click_btn).grid(row=2,column=1, pady=10)
    btn2 = Button(tk,text='초기화',command=clear).grid(row=2,column=0, pady=10)
    tk.bind("<Key>", return_btn)
    # tk.bind("<Shift-Return>", return_btn)
    tk.mainloop()

def en2ko(main_input):
    # convert en 2 ko
    ko_word = []
    for c in main_input:
        try:
            ko_word.append(ko_dict[c])
        except:
            ko_word.append(c)
    ko_word = list(''.join(ko_word)) + ['\n']
    print(ko_word)

    #combine each letter
    output_list = []
    charset=[]
    while(ko_word):
        charset.append(ko_word.pop(0))
        print(charset,ko_word)

        if charset[-1] in jungseong_list and ko_word[0] in jungseong_list:
            b = charset[-1]
            charset.append(make_jungseong_list(charset.pop(), ko_word[0]))
            if (b != charset[-1]):
                ko_word.pop(0)
        if charset[-1] in jongseong_list and ko_word[0] in jongseong_list:
            b = charset[-1]
            charset.append(make_jongseong_list(charset.pop(), ko_word.pop(0)))
            if (b != charset[-1]):
                ko_word.pop(0)

        jongseong_index = 0
        if ((len(ko_word) > 0 and ko_word[0] in choseong_list) and (len(ko_word) > 1 and ko_word[1] in jungseong_list)):
            choseong_index = choseong_list.index(charset[0])
            jungseong_index = jungseong_list.index(charset[1])
            if len(charset) > 2 and charset[2] in jongseong_list:
                jongseong_index = jongseong_list.index(charset[2])
                charset.pop(0)
            character_code = jongseong_index + 0xAC00 + (choseong_index * 21 * 28) + (jungseong_index * 28)
            output_list.append(chr(character_code))
            charset.pop(0)
            charset.pop(0)
        else:
            output_list.append(charset.pop(0))

    print("{}\t|    (변환)    |\n{}".format(main_input, ''.join(output_list)))
    return ''.join(output_list)

def make_jongseong_list(char1, char2):
    if char1 == 'ㄱ' and char2 == 'ㄱ':
        return "ㄲ"
    if char1 == 'ㄱ' and char2 == 'ㅅ':
        return "ㄳ"
    if char1 == 'ㄴ' and char2 == 'ㅈ':
        return "ㄵ"
    if char1 == 'ㄴ' and char2 == 'ㅎ':
        return "ㄶ"
    if char1 == 'ㄹ' and char2 == 'ㄱ':
        return "ㄺ"
    if char1 == 'ㄹ' and char2 == 'ㅁ':
        return "ㄻ"
    if char1 == 'ㄹ' and char2 == 'ㅂ':
        return "ㄼ"
    if char1 == 'ㄹ' and char2 == 'ㅅ':
        return "ㄽ"
    if char1 == 'ㄹ' and char2 == 'ㅌ':
        return "ㄾ"
    if char1 == 'ㄹ' and char2 == 'ㅍ':
        return "ㄿ"
    if char1 == 'ㄹ' and char2 == 'ㅎ':
        return "ㅀ"
    if char1 == 'ㅂ' and char2 == 'ㅅ':
        return "ㅄ"
    return char1

def make_jungseong_list(char1, char2):
    if char1=='ㅗ' and char2 == 'ㅏ':
        return "ㅘ"
    if char1=='ㅗ' and char2 == 'ㅐ':
        return "ㅙ"
    if char1=='ㅗ' and char2 == 'ㅣ':
        return "ㅚ"
    if char1=='ㅜ' and char2 == 'ㅓ':
        return "ㅝ"
    if char1=='ㅜ' and char2 == 'ㅔ':
        return "ㅞ"
    if char1=='ㅜ' and char2 == 'ㅣ':
        return "ㅟ"
    if char1=='ㅡ' and char2 == 'ㅣ':
        return "ㅢ"
    return char1


main()