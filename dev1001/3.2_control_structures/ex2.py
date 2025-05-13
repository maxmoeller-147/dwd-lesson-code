correct_username = 'user123'
correct_password = 'password_abc'

entered_username = input('enter username:')
entered_password = input('enter password:')

if entered_username == correct_username and entered_password == correct_password:
    print('login succesful!')
else:
    print('username not found')