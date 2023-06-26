import datetime

def clock():
    time = datetime.datetime.now() # obtedo a hora e a data local com a biblioteca datetime()

    hour = time.strftime("%H:%M:%S") # formatando a exibição da hora
    date = time.strftime("%d/%m/%Y") # formatando a exibição do dia

    clock_array = [hour, date]

    return clock_array # retorna uma lista com o hora e a data

def get_day():
    time = datetime.datetime.now() # obtedo a hora e a data local com a biblioteca datetime()

    # 'switch' para retornar o nome do dia em portugues
    match time.strftime("%A"):
        case "Sunday":
            day = "Domingo"
        case "Monday":
            day = "Segunda-feira"
        case "Tuesday":
            day = "Terça-feira"
        case "Wednesday":
            day = "Quarta-feira"
        case "Thursday":
            day = "Quinta-feira"
        case "Friday":
            day = "Sexta-feira"
        case "Saturday":
            day = "Sábado"
    
    return day # retornando o nome do dia em portugues
