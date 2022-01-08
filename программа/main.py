import encr_decr
import key

text = input("Message: ")

public, private = key.key()
print("Public key: ", public)
print("Private key: ", private)

res_ecrypted = encr_decr.encr_text(text, public[0], public[1])
print(res_ecrypted)

res_decrypted = encr_decr.decr_text(res_ecrypted, private[0], private[1])
print(res_decrypted)