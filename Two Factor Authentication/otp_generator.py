import pyotp


def otp():
    key = "SaddarKelashSandeepShahidTwoFactorAuthentication"
    totp = pyotp.TOTP(key, interval=60)
    return totp.now()