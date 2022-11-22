# # FileNotFound
#
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["qwerasdf"])
#
# except FileNotFoundError: # 특정에러에서만 반응하게 설정 가능
#     file = open("a_file.txt", "w")
#     file.write("Something")
#
# except KeyError as error_message: # 에레 메세지가 아니라 어떤 것이 문제인지 출력가능
#     print(f"That key {error_message} dose not exist.")
#
# else: # try가 성공(except 문 작동 안함)해야지만 작동함
#     content = file.read()
#     print(content)
#
# finally: # 무조건 작동
#     raise KeyError("This is an error that I made up.") # 에러생성


height = float(input("Height: "))
weight = int(input("Weight: "))

if height > 3:
    raise ValueError("Human Height should not be over 3 meters.")

bmi = weight / height ** 2
print(bmi)