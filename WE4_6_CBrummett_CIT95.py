def computepay(hours, rate) :
    # print("In computepay", hours, rate)
    if fh > 40:
        reg = fr * fh
        otp = (fh - 40.0) * (fr * 0.5)
        xp = reg = otp
    else:
        xp = fh * fr
    # print("Returning",xp)
    return xp
xh = input("Enter Hours: ")
xr = input("Enter Rate: ")
try:
    fh = float(xh)
    fr = float(xr)
except:
    print("Error, please enter numeric input")
    quit()
xp = computepay(fh,fr)
print("Pay:",xp)