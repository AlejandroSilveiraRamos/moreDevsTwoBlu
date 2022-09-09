#Challenge Boolean test



stuff = input("Digit your stuff to test: ")

spaceBtw = '' in stuff
#using fuction to releate if is true

print(" First stuff: \n Is numeric: {} \n is alpha: {} \n is num: {} \n is space: {} \n is any alfabetic: {} \n is any space betwean words: {} "
.format(
    stuff.isnumeric(),
    stuff.isalpha(),
    stuff.isalnum(),
    stuff.isspace(),
    stuff.isdigit(),
    spaceBtw
    ),
)

