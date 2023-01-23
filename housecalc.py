#Amount to borrow, Intrest Rate, Amount of years, calculate monthly rate, interest and principle
#500,000 over 30 years with additional
import  tkinter as tk

def run():
    interest_total = 0
    payed_total = 0
    loan_sum = loan_storage.get()
    unpayed_total = loan_sum
    payments = payments_storage.get()
    interest_rate = interest_storage.get()
    payment_price = loan_sum/payments
    calculated_interest = ((interest_rate/12) * .01)
    payment_with_interest = ((unpayed_total - payed_total) * calculated_interest) / (1 - pow((1 + calculated_interest), (-12*(payments/12))))
    result_text.configure(text = "Payment with interest per month would be $" + str(round(payment_with_interest, 2)))
    result_text.pack()

window = tk.Tk()
window.title("Loan Calculator")
window.geometry("400x200")
title_text = tk.Label(text = "Loan Calculator")
title_text.pack()
prompt_text = tk.Label(text = "Please enter amount of loan:")
prompt_text.pack()
loan_storage = tk.IntVar()
entry_bar = tk.Entry(textvariable = loan_storage)
entry_bar.pack()
prompt_text = tk.Label(text = "Please enter the amount of payments:")
prompt_text.pack()
payments_storage = tk.IntVar()
entry_bar = tk.Entry(textvariable = payments_storage)
entry_bar.pack()
prompt_text = tk.Label(text = "Please enter the yearly interest rate (For example, enter 8 for 8%):")
prompt_text.pack()
interest_storage = tk.IntVar()
entry_bar = tk.Entry(textvariable = interest_storage)
entry_bar.pack()
submit_button = tk.Button(text = "Submit", command = run)
submit_button.pack()
result_text = tk.Label(text = "")
result_text.pack()
window.mainloop()