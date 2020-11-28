import aero

while True:
    text = input('aero > ')
    result, error = aero.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
