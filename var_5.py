import streamlit as st


def pas_save(data, name):
    y = []
    for line in data:
        lst = line.rstrip().split(',')
        fio = lst[3] + lst[4]
        fio1 = fio[1:len(name) + 1]
        if line.split(",")[0] == "PassengerId":
            continue
        if fio1 == name.capitalize() and int(lst[1]) == int(1) and int(len(name)) > int(0):
            y += [fio]
    return y


def var5(data):
    st.header("Вариант 5. Выполнила Бессонова А.А., группа 3-см")
    st.info("Вывести Класс, Имя, Возраст спасенных пассажиров с именами, начинающимися на введенный текст")
    st.subheader("Результат:")
    name = st.text_input("Введите первые буквы имени спасенного пассажира")
    st.table(pas_save(data, name))
