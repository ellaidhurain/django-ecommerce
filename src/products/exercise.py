# # # list1 = [10, 21, 4, 45, 66, 93]

# # # # iterating each number in list
# # # print('even:')
# # # for num in list1:

# # #     # print(4%2)
# # #     #The % symbol in Python is called the Modulo Operator. It returns the remainder of dividing the left hand operand by right hand operand. It's used to get the remainder of a division problem.
# # #     if num % 2 == 0: # if remainder == 0
# # #         print(num )

# # # print("odd:")
# # # for num in list1:
# # #     if num % 2 != 0: # if remainder == 1 or if remainder !=0
# # #         print(num)

# # # list1 = [10, 21, 4, 45, 66, 93]

# # # # using list comprehension
# # # even_nos = [num for num in list1 if num % 2 == 0]
# # # odd_nos = [num for num in list1 if num % 2 != 0]


# # # # print("Even numbers in the list: ", even_nos)
# # # # print("Even numbers in the list: ", odd_nos)


# # marks = [89, 88, 79, 74, 74, 74, 74, 74, 64, 56, 56, 25, 24]
# # marks.append(100)
# # marks.sort(reverse=True)

# # current_rank = 0
# # class_rank = 0
# # current_mark = 25  # null(empty)

# # for mark in marks:
# #     class_rank += 1

# #     if mark == current_mark:
# #         current_mark = mark
# #         current_rank = class_rank

# # count = 1
# # # The while statement checks the condition. The condition must return a boolean value. Either True or False
# # while count <= 10:
# #     # print(count)
# #     count += 1


# # # value = None or 0 or '' or [] or () or {} # we can use this to check there is value or empty

# # # if value:
# # #     print('has value')
# # # else:
# # #     print('the value instance returns false')

# # # # check the array has value or not.
# # # value = [1,5]

# # # if value == []:
# # #     print('no value')
# # # else:
# # #     print(value)


# # # list = [1,2,3,4]

# # # # for num in list:
# # # #     # for num 1,2 there is no condition. so the value is printed by loop. for num 3 there is condition so the condition is applied. and break statement stops the loop.
# # # #     if num == 3:
# # # #         print('no 3 is there')
# # # #         continue
# # # #     print(num)

# # # list2 = [3]

# # # for num in list:
# # #     for letter in list2: # every num is list looped to every letter in 'abc'
# # #         print(num*letter)
# # #     # 1a ,1b, 1c, 2a, 2b, 2c

# # # for i in range(1,11):
# # #     print(i)

# # #     # 1 to 10 is printed

# # # x = 0
# # # while x < 10: # x is not greater than 10. so loop continues until the value of x is grater 10. ctrl+c stops infinite loop
# # #     if x == 5:
# # #         break
# # #     print(x)
# # #     x += 1


# # # month_days = [0,31,28,31,30,31,30,31,30,31,30,31,30]


# # # def is_leap(year):
# # #     """ return True for leap year False non leap year"""
# # #     return year % 4 == 0 and(year % 100 != 0 or year % 400 == 0 )

# # # print(is_leap(2012))

# # # def days_in_month(year,  month):
# # #     """ return no of days in month"""

# # #     # month should be between 1 and 12 else return error
# # #     if not 1 <= month <= 12:
# # #         return 'Invalid month'

# # #     # on leap year 29 days for feb or month 2
# # #     if month == 2 and is_leap(year):
# # #         return 29

# # #     # month_days - python build in function
# # #     return month_days[month]

# # # print(days_in_month(2012, 12))


# # import datetime
# # import pytz
# # # date = year, month ,day

# # d = datetime.date(2016,12,30)
# # tday = datetime.date.today()
# # tdelta = datetime.timedelta(days=248) # timedelta is used to add days with our date

# # # print(tday.day) # get current day
# # # print(tday.year) # get current year

# # # print(tday.weekday()) # it returns weekday number of our current day
# # # print(tday.isoweekday())

# # # 0-monday 1-tuesday 2-wednesday 3-thursday 4-friday 5-saturday 6-sunday
# # # for weekday monday is 0 sunday is 6
# # # for isoweekday monday is 1 sunday is 7
 
# # # print(tday + tdelta) # find the date 248 th day from current day

# # # bday = datetime.date(2023, 2, 11)
# # # til_bday = bday - tday
# # # print(til_bday.days)


# # # time = hours, minuets ,seconds , microseconds 
# # # t = datetime.time(9, 30, 50, 10000)
# # # print(t)


# # # dt = datetime.datetime(2023, 2, 11, 9, 30, 50, 100000)
# # # print(dt.time())
# # # print(dt.date())

# # # tdelta = datetime.timedelta(hours=12)
# # # print(dt + tdelta)


# # # dt_today = datetime.datetime.today()
# # dt_utc_now = datetime.datetime.now(tz=pytz.UTC) # timzone aware
# # # dt_utcnow = datetime.datetime.utcnow()

# # # print(dt_today,dt_now,dt_utcnow)
# # print(dt_utc_now)

# # dt_india = dt_utc_now.astimezone(pytz.timezone('Asia/Kolkata'))
# # print(dt_india)
# # print(dt_india.strftime('%B %d, %Y')) # Datetime to str formatting

# # dt_str = 'July 26, 2016'

# # dt = datetime.datetime.strptime(dt_str,'%B %d, %Y') # str to Datetime formatting
# # print(dt)



# # # (*args - star astrick parameter non-keyword, take more arguments
# # # (**kwargs - double star astrick parameter, takes keyword arguments

# # class car(): #defining car class
# #     def __init__(self,*args): #args receives unlimited no. of arguments as an array
# #         self.speed = args[0] #access args index like array does
# #         self.color=args[1]
                 
# # #creating objects of car class
         
# # audi=car(200,'red')
# # bmw=car(250,'black')
# # mb=car(190,'white')
    
# # # print(audi.color)
# # # print(bmw.speed)


# # class car(): #defining car class
# #     def __init__(self,**kwargs): #args receives unlimited no. of arguments as an array
# #         self.speed = kwargs['s'] #access args index like array does
# #         self.color = kwargs['c']
                 
# # #creating objects of car class
         
# # audi=car(s=200,c='red')
# # bmw=car(s=250,c='black')
# # mb=car(s=190,c='white')
    
# # # print(audi.color)
# # # print(bmw.speed)

# from datetime import datetime, timedelta

# start_date = datetime('2023 1, 1')
# end_date = datetime('2024 1, 31')


# def date_working_day_validation(date, class_data):
#     valid_date = start_date < date < end_date
#     if not valid_date:
#         return "Invalid date"
#     working_day = class_data.Calendar.Working_day
#     input_day = date.weekday()
#     saturday_list = []
#     first_day_of_month = datetime.date(date.year, date.month, 1)
#     no_of_days_in_month = monthrange(date.year, date.month)[1]
#     first_week_day = first_day_of_month.isoweekday()
#     if first_day_of_month.isoweekday() == 7:
#         first_week_day = 0
#     first_saturday_of_month = 7 - first_week_day
#     for i in range(first_saturday_of_month, no_of_days_in_month, 7):
#         saturday = datetime.date(date.year, date.month, i)
#         saturday_list.append(saturday)
#     fir_sat = class_data.Calendar.First_sat
#     sec_sat = class_data.Calendar.Sec_sat
#     third_sat = class_data.Calendar.Third_sat
#     fourth_sat = class_data.Calendar.Fourth_sat
#     fifth_sat = class_data.Calendar.Fifth_sat
#     weekend_sat_list = []
#     if not fir_sat:
#         weekend_sat_list.append(1)
#     if not sec_sat:
#         weekend_sat_list.append(2)
#     if not third_sat:
#         weekend_sat_list.append(3)
#     if not fourth_sat:
#         weekend_sat_list.append(4)
#     if not fifth_sat:
#         weekend_sat_list.append(5)
#     removable_sat_list = []
#     for i in weekend_sat_list:
#         if i == 5 and len(saturday_list) == 5:
#             removable_sat_list.append(saturday_list[4])
#         if i != 5:
#             removable_sat_list.append(saturday_list[i - 1])
#     for i in removable_sat_list:
#         saturday_list.remove(i)
        
#     cultural_hol_model = class_data.Calendar.Culture_event.all().filter(Is_holiday=True)
#     cultural_holiday = []
#     event_name = []
#     for i in cultural_hol_model:
#         inbetween_days = (i.End_date - i.Start_date).days + 1
#         for j in range(inbetween_days):
#             data = i.Start_date + datetime.timedelta(days=j)
#             cultural_holiday.append(data)
#             event_name.append(i.Event_name)
#     other_hol_model = class_data.Calendar.Other_holiday.all()
#     other_holiday = []
#     other_hol_name = []
#     for i in other_hol_model:
#         inbetween_days = (i.End_date - i.Start_date).days + 1
#         for j in range(inbetween_days):
#             data = i.Start_date + datetime.timedelta(days=j)
#             other_holiday.append(data)
#             other_hol_name.append(i.Holiday_name)
#     gov_hol_model = class_data.Calendar.Gov_holiday.all()
#     gov_hol = [i.Start_date for i in gov_hol_model]
#     gov_hol_name = [i.Holiday_name for i in gov_hol_model]
#     if str(input_day) not in working_day and date not in saturday_list:
#         if date in gov_hol and date in other_holiday and date in cultural_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "Regular weekly holiday + {} + {} + {}".format(
#                     gov_hol_name[gov_hol.index(date)], other_hol_name[other_holiday.index(date)],
#                     event_name[cultural_holiday.index(date)])}
#         elif date in gov_hol and date in other_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "Regular weekly holiday + {} + {}".format(
#                     gov_hol_name[gov_hol.index(date)], other_hol_name[other_holiday.index(date)])}
#         elif date in gov_hol and date in cultural_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "Regular weekly holiday + {}+ {}".format(
#                     gov_hol_name[gov_hol.index(date)], event_name[cultural_holiday.index(date)])}
#         elif date in other_holiday and date in cultural_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "Regular weekly holiday + {} + {}".format(other_hol_name[other_holiday.index(date)],
#                                                                     event_name[cultural_holiday.index(date)])}
#         elif date in gov_hol:
#             return {
#                 "Working_day": False,
#                 "Reason": "Regular weekly holiday + {}".format(gov_hol_name[gov_hol.index(date)])}
#         elif date in other_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "Regular weekly holiday + {}".format(other_hol_name[other_holiday.index(date)])}
#         elif date in cultural_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "Regular weekly holiday + {}".format(event_name[cultural_holiday.index(date)])}
#         else:
#             return {"Working_day": False, "Reason": "Regular weekly holiday "}
#     if str(input_day) in working_day or date in saturday_list:
#         if date in gov_hol and date in other_holiday and date in cultural_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "{} + {} + {}".format(
#                     gov_hol_name[gov_hol.index(date)], other_hol_name[other_holiday.index(date)],
#                     event_name[cultural_holiday.index(date)])}
#         elif date in gov_hol and date in other_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "{} + {}".format(
#                     gov_hol_name[gov_hol.index(date)], other_hol_name[other_holiday.index(date)])}
#         elif date in gov_hol and date in cultural_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "{}+ {}".format(
#                     gov_hol_name[gov_hol.index(date)], event_name[cultural_holiday.index(date)])}
#         elif date in other_holiday and date in cultural_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "{} + {}".format(other_hol_name[other_holiday.index(date)],
#                                            event_name[cultural_holiday.index(date)])}
#         elif date in gov_hol:
#             return {
#                 "Working_day": False,
#                 "Reason": "{}".format(gov_hol_name[gov_hol.index(date)])}
#         elif date in other_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "{}".format(other_hol_name[other_holiday.index(date)])}
#         elif date in cultural_holiday:
#             return {
#                 "Working_day": False,
#                 "Reason": "{}".format(event_name[cultural_holiday.index(date)])}
#         else:
#             return {"Working_day": True}


import datetime
import calendar

# balance = 75000
# interest_rate = 13 * .01
# monthly_payment = 5000

# date = datetime.date(2023,1,1)

# days_in_current_month = calendar.monthrange(date.year, date.month)[1]
# days_remaining_to_month_end = days_in_current_month - date.day
# payment_start_date_of_month = date + datetime.timedelta(days=days_remaining_to_month_end +1) # if monthly payment starts at 1 add 1 at last or 8 add 8
# #today_date + total days + 1 ==> 2 + 17 + 1 ==> 1-3-2023
# end_date = payment_start_date_of_month

# # calculate maximum month required to zero our balance
# while balance > 0:
#     # interest rate is added per year so calculate for 1 month
#     interest_charge = (interest_rate/12) * balance # interest charge for 1 month
#     balance += interest_charge # balance + interest
#     balance -= monthly_payment # 5400 - 400 ==> 5000
    
#     balance = round(balance, 2) # round with 2 decimal 
    
#     if balance < 0:
#         balance = 0
        
#     # print(end_date, balance)
#     days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
#     end_date = end_date + datetime.timedelta(days=days_in_current_month)

# # system env file
# import os
# db_user = os.environ.get('DB_PASS')
# print(db_user)


# from datetime import timedelta

# # exam dates
# start_date = '2022-1-1'.split('-')
# end_date = '2023-11-12'.split('-')
# input_date = datetime.date(int(start_date[0]),int(start_date[1]),int(start_date[2]))
# input_date2 = datetime.date(int(end_date[0]),int(end_date[1]),int(end_date[2]))


# # cal dates
# cal_start_date = datetime.date(2022, 1, 1) 
# cal_end_date = datetime.date(2023, 12, 31)

# # exam start date should greater than cal start date or less than cal end else error
# if (input_date < cal_start_date) or (input_date > cal_end_date):
#     print('not valid date')
    
# if not cal_start_date <= input_date <= cal_end_date:
#     print('invalid')
    

# inbetween_dates = (cal_end_date - cal_start_date).days + 1  
# # total inbetween days = 31+1
# # to remove end date delete +1
# # to remove the start date, insert a 1 argument to the beginning of the range function.

# scheduled_cal_days = []
# for i in range(inbetween_dates):
#     # print all days from cal_start_date to range(32)
#     day = cal_start_date + datetime.timedelta(days=i)     
#     scheduled_cal_days.append(day) 
 
# # check the date is present in cal_days list
# if input_date and input_date2 not in scheduled_cal_days:
#     print('Date must be present between cal year')



import pyscreenshot
  
# # To capture the screen
# image = pyscreenshot.grab()
  
# # To display the captured screenshot
# image.show()
  
# # To save the screenshot
# image.save("GeeksforGeeks.png")


  
# im=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
# image = pyscreenshot.grab(bbox=(10, 10, 1300, 700))
  
# # To view the screenshot
# image.show()
  
# # To save the screenshot
# image.save("GeeksforGeeks.png")


