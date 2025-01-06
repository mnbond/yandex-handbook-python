def month(number, lang="ru"):
    monthes = {
        "ru": ["Январь", "Февраль", "Март", "Апрель", 
               "Май", "Июнь", "Июль", "Август", 
               "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"],
        "en": ["January", "February", "March", "April", 
               "May", "June", "July", "August", 
               "September", "October", "November", "December"]
    }
    return monthes[lang][number - 1]
