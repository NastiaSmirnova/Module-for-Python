import my_hash
#проверка свойства №1
a = "asdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnm"
b = "asdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnm"
hash_a = my_hash.hash(a)
hash_b = my_hash.hash(b)

print(hash_a)
print(hash_b)
print("Полиномиальные хэши равны?")
print(hash_a==hash_b)

#проверка свойства №2
c = "asdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnm"
d = "lkjhgfdsamnbvcxzpoiuytrewqlkjhgfdsamnbvcxzpoiuytrewqlkjhgfdsamnbvcxzpoiuytrewqlkjhgfdsamnbvcxzpoiuytrewq"
hash_c = my_hash.hash(c)
hash_d = my_hash.hash(d)

print(hash_c)
print(hash_d)
print("Полиномиальные хэши равны?")
print(hash_c==hash_d)

#проверка свойства №3
e = "asdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnm"
f = "asdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnmasdfghjklzxcvbnn"
hash_e = my_hash.hash(e)
hash_f = my_hash.hash(f)

print(hash_e)
print(hash_f)
print("Полиномиальные хэши равны?")
print(hash_e==hash_f)