#create blank dictionary
book = {} 
# book['name'] = "The Atomic habit"
# book['author'] = "James clear"
# book['price'] = 1000
book.update({'name':'The Atomic Habit'})
book.update({'author':'James clear'})
book.update({'price':'1000'})
book.update({'price':'999'}) #if key already exists, it will update key's value
print(book)

# #wrong way it create reference of book and do not copy book. so if you change dictionary using book or another_book, it will update both 
# another_book = book 
#correct way 
another_book = book.copy() 

another_book.clear() #delete all key value 
print(another_book)
print(book)

#print keys 
print(book.keys()) # name price author
print(book.values()) # the atomic habit, james clear 999
print(book.items()) # the atomic habit, james clear 999

student = ['name','dob','gender','weight']
print(student)

karan = dict.fromkeys(student)
karan['name'] = 'Karan kalotara'
karan['dob'] = '01-01-2004'
karan['gender'] = True 
karan['weight'] = 75.11
karan['secret'] = None
karan['pincode'] = 364001
print(karan)
#remove specific key 
karan.pop('secret')
#remove last item
karan.popitem()
print(karan)
print(karan.get('pincode','Not found'))
print('good bye')
