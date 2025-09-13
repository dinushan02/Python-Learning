#AND
has_high_income =True
has_good_credit =True

if has_high_income and has_good_credit:
    print("Eligible for loan")

#OR
has_high_income =False
has_good_credit =True

if has_high_income or has_good_credit:
    print("Eligible for loan")

#NOT
has_good_credit = True
has_criminal_record = False

if has_good_credit and not has_criminal_record: #False becomes True in not operator.
    print("Eligible for loan")
